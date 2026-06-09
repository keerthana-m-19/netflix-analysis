"""
analysis.py
Produce analytics and save visualizations to visuals/.
Usage:
    python src/analysis.py --input data/netflix_cleaned.csv --out visuals/
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def load_data(path):
    return pd.read_csv(path, parse_dates=['date_added_parsed'], low_memory=False)

def movies_vs_tv(df, out_dir):
    counts = df['type'].value_counts()
    plt.figure(figsize=(6,4))
    counts.plot(kind='bar')
    plt.title("Movies vs TV Shows")
    plt.ylabel("Count")
    plt.tight_layout()
    fname = os.path.join(out_dir, "movies_vs_tv.png")
    plt.savefig(fname)
    plt.close()
    return fname

def top_genres(df, out_dir, top_n=12):
    genre_counts = df['genre'].value_counts().head(top_n)
    plt.figure(figsize=(10,6))
    genre_counts.plot(kind='bar')
    plt.title(f"Top {top_n} Genres")
    plt.ylabel("Count")
    plt.tight_layout()
    fname = os.path.join(out_dir, "top_genres.png")
    plt.savefig(fname)
    plt.close()
    return fname

def content_added_over_time(df, out_dir):
    # use date_added_parsed if present else use release_year
    if 'date_added_parsed' in df.columns and df['date_added_parsed'].notna().sum() > 0:
        df['year_added'] = pd.DatetimeIndex(df['date_added_parsed']).year
    else:
        df['year_added'] = df['release_year']
    series = df['year_added'].value_counts().sort_index()
    plt.figure(figsize=(12,5))
    series.plot(kind='line', marker='o')
    plt.title("Content Added by Year")
    plt.xlabel("Year")
    plt.ylabel("Titles Added")
    plt.tight_layout()
    fname = os.path.join(out_dir, "content_added_over_time.png")
    plt.savefig(fname)
    plt.close()
    return fname

def top_countries(df, out_dir, top_n=12):
    c = df['country'].value_counts().head(top_n)
    plt.figure(figsize=(10,6))
    c.plot(kind='bar')
    plt.title(f"Top {top_n} Countries")
    plt.ylabel("Count")
    plt.tight_layout()
    fname = os.path.join(out_dir, "top_countries.png")
    plt.savefig(fname)
    plt.close()
    return fname

def duration_distribution(df, out_dir):
    movies = df[df['type'].str.lower() == 'movie']
    # drop NAs and unrealistic durations
    data = movies['duration_minutes'].dropna()
    plt.figure(figsize=(10,5))
    sns.histplot(data, bins=30)
    plt.title("Movie Duration Distribution")
    plt.xlabel("Duration (minutes)")
    plt.tight_layout()
    fname = os.path.join(out_dir, "duration_distribution.png")
    plt.savefig(fname)
    plt.close()
    return fname

def top_directors(df, out_dir, top_n=15):
    d = df['director'].value_counts().head(top_n)
    plt.figure(figsize=(10,6))
    d.plot(kind='barh')
    plt.title(f"Top {top_n} Directors by Count")
    plt.xlabel("Number of Titles")
    plt.tight_layout()
    fname = os.path.join(out_dir, "top_directors.png")
    plt.savefig(fname)
    plt.close()
    return fname

def ratings_distribution(df, out_dir):
    r = df['rating'].value_counts().head(20)
    plt.figure(figsize=(8,5))
    r.plot(kind='bar')
    plt.title("Rating Distribution")
    plt.tight_layout()
    fname = os.path.join(out_dir, "rating_distribution.png")
    plt.savefig(fname)
    plt.close()
    return fname

def save_summary_tables(df, out_dir):
    # Save CSVs for top-10 lists (for direct embedding in README)
    df['title'] = df['title'].astype(str)
    top_titles = df['title'].value_counts().head(50).reset_index()
    top_titles.columns = ['title', 'count']
    top_titles.to_csv(os.path.join(out_dir, "top_titles.csv"), index=False)

    df['genre'] = df['genre'].astype(str)
    df.groupby('genre').size().sort_values(ascending=False).head(50).reset_index(name='count')\
      .to_csv(os.path.join(out_dir, "genre_counts.csv"), index=False)

def main(args):
    ensure_dir(args.out)
    df = load_data(args.input)

    print("Generating plots...")
    movies_vs_tv(df, args.out)
    top_genres(df, args.out)
    content_added_over_time(df, args.out)
    top_countries(df, args.out)
    duration_distribution(df, args.out)
    top_directors(df, args.out)
    ratings_distribution(df, args.out)
    save_summary_tables(df, args.out)
    print(f"All visuals saved to {args.out}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to cleaned csv (output of clean.py)")
    parser.add_argument("--out", default="visuals", help="directory to save visuals")
    args = parser.parse_args()
    main(args)
