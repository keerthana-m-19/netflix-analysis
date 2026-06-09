# Netflix Data Analysis

## Overview

This project performs Exploratory Data Analysis (EDA) on Netflix's dataset to uncover insights about movies and TV shows available on the platform. Using Python and data analysis libraries, the project explores content distribution, release trends, ratings, genres, and country-wise contributions.

## Objectives

* Analyze Netflix movies and TV shows.
* Identify content trends and patterns.
* Visualize key insights using charts and graphs.
* Perform data cleaning and preprocessing for analysis.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

## Dataset

The dataset contains information about Netflix content, including:

* Title
* Type (Movie/TV Show)
* Director
* Cast
* Country
* Release Year
* Rating
* Duration
* Genre

## Project Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Data Visualization
5. Insight Generation

## Key Analysis Performed

* Movies vs TV Shows Distribution
* Content Released by Year
* Top Content-Producing Countries
* Most Common Ratings
* Genre Analysis
* Duration Analysis of Movies
* Trend Visualization

## Key Findings

* Movies make up the majority of Netflix content.
* The number of releases increased significantly after 2015.
* The United States contributes the largest share of content.
* Drama and Comedy are among the most popular genres.
* TV-MA is one of the most frequently assigned ratings.

## Project Structure

## Project Structure

```text
Netflix-Analysis/
│
├── data/
│   ├── netflix_cleaned.csv
│   ├── netflix_cleaned_preview.csv
│   └── netflix_sample_1500.csv
│
├── src/
│   ├── clean.py
│   └── analysis.py
│
├── visuals/
│   ├── content_added_over_time.png
│   ├── duration_distribution.png
│   ├── movies_vs_tv.png
│   ├── rating_distribution.png
│   ├── top_countries.png
│   ├── top_directors.png
│   ├── top_genres.png
│   ├── genre_counts.csv
│   └── top_titles.csv
│
├── README.md
└── requirements.txt
```


## How to Run

1. Clone the repository.
2. Install required libraries:

   ```
   pip install pandas numpy matplotlib seaborn
   ```
3. Open the Jupyter Notebook.
4. Run all cells to reproduce the analysis.

## Future Improvements

* Interactive dashboard using Power BI or Tableau.
* Recommendation system using Machine Learning.
* Advanced statistical analysis and predictive modeling.

## Author

Keerthana M
B.Tech Artificial Intelligence & Data Science
Aspiring Machine Learning Engineer
