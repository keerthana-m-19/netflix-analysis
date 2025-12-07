"""
clean.py
Load raw Netflix CSV, perform cleaning & normalization, and export cleaned CSV.
Usage:
    python src/clean.py --input data/netflix_sample_1500.csv --output data/netflix_cleaned.csv
"""

import argparse
import pandas as pd
import numpy as np
from dateutil import parser

def load_csv(path):
    return pd.read_csv(path)

def safe_parse_date(val):
    try:
        return parser.parse(val)
    except Exception:
        return pd.NaT

def normalize_duration(df):
    # Create numeric duration column: movie minutes or average seasons * 45 minutes (approx) if needed
    def duration_to_minutes(x):
        if pd.isna(x):
            return np.nan
        s = str(x).strip()
        if "min" in s:
            try:
                return int(s.replace(" min","").strip())
            except:
                return np.nan
        # Seasons -> convert to approximate minutes: seasons * avg episodes * 30
        # Here we'll extract the first number and multiply by 6 episodes * 30 minutes ~ 180 per season
        import re
        m = re.search(r"(\d+)", s)
        if m:
            seasons = int(m.group(1))
            # approx minutes per season (coarse): 6 eps * 30 min = 180
            return seasons * 180
        return np.nan

    df['duration_minutes'] = df['duration'].apply(duration_to_minutes)
    return df

def explode_genres(df):
    # create a cleaned 'genre' exploded column for per-row single-genre analyses
    df['listed_in'] = df['listed_in'].fillna("Unknown")
    df['genre_list'] = df['listed_in'].str.split(',')
    df['genre_list'] = df['genre_list'].apply(lambda gl: [g.strip() for g in gl] if isinstance(gl, list) else ["Unknown"])
    df = df.explode('genre_list').rename(columns={'genre_list':'genre'})
    return df

def clean_dataframe(df):
    # Basic imputations
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    df['rating'] = df['rating'].fillna('NR')

    # date parsing
    if 'date_added' in df.columns:
        df['date_added_parsed'] = df['date_added'].apply(safe_parse_date)
        # fallback: if date_added_parsed is NaT, fill with Jan 1 of release_year if available
        if 'release_year' in df.columns:
            mask = df['date_added_parsed'].isna() & df['release_year'].notna()
            df.loc[mask, 'date_added_parsed'] = pd.to_datetime(df.loc[mask, 'release_year'].astype(int).astype(str) + "-01-01")
    else:
        df['date_added_parsed'] = pd.NaT

    # normalize durations to numeric minutes
    df = normalize_duration(df)

    # explode genres for analysis
    df = explode_genres(df)

    # unified column names lower-case (optional)
    df.columns = [c.lower() for c in df.columns]

    return df

def main(args):
    df = load_csv(args.input)
    cleaned = clean_dataframe(df)
    cleaned.to_csv(args.output, index=False)
    print(f"Cleaned CSV saved to {args.output}")
    # Save a small sample for quick preview
    cleaned.head(20).to_csv(args.preview, index=False)
    print(f"Preview (20 rows) saved to {args.preview}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to raw csv")
    parser.add_argument("--output", default="data/netflix_cleaned.csv", help="path to save cleaned csv")
    parser.add_argument("--preview", default="data/netflix_cleaned_preview.csv", help="save preview CSV")
    args = parser.parse_args()
    main(args)
