# 📊 Netflix Data Analysis (Python | Pandas | Matplotlib)

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A **Python-based Data Analysis project** on a Netflix-style dataset containing 1500 entries.  
The project demonstrates **data cleaning, preprocessing, exploratory analysis (EDA), and visualization** using Python scripts.

---

## 🔹 Project Overview

This project analyzes Netflix-style content to uncover insights about:

- Movie vs TV Show distribution  
- Top genres and ratings  
- Country-wise content contributions  
- Release trends over the years  
- Movie duration patterns  
- Top directors  

All analysis is done through Python scripts, and visualizations are automatically saved into the `graphs/` folder.

---

## 📁 Dataset

- Synthetic dataset with **1500 Netflix entries**  
- Each row contains:
  - `show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`  

**Data location:** `data/netflix_sample_1500.csv`

---

## 🛠️ Technologies & Libraries

- **Python 3**  
- **Pandas** – data cleaning & preprocessing  
- **NumPy** – numerical operations  
- **Matplotlib** – visualizations  
- **Seaborn** – advanced charts  

---

## 📂 Repository Structure

```

netflix-analysis/
│
├── data/
│   └── netflix_sample_1500.csv
│
├── src/
│   ├── clean.py           # Data cleaning & preprocessing
│   └── analysis.py        # Exploratory analysis & visualization
│
├── graphs/                # Auto-generated visuals
│   ├── movies_vs_tv.png
│   ├── top_genres.png
│   ├── content_added_over_time.png
│   ├── ratings_distribution.png
│   ├── top_countries.png
│   ├── duration_distribution.png
│   └── top_directors.png
│
├── requirements.txt       # Python dependencies
└── README.md

````

---

## ▶️ How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/keerthana-m-19/netflix-analysis.git
cd netflix-analysis
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Clean the Data

```bash
python src/clean.py --input data/netflix_sample_1500.csv --output data/netflix_cleaned.csv
```

### 4. Run Analysis & Generate Visualizations

```bash
python src/analysis.py --input data/netflix_cleaned.csv --out graphs
```

Open the `graphs/` folder to view all generated charts.

---

## 📊 Visualizations Included

* Movies vs TV Shows count
* Top 10 genres
* Content added over the years
* Ratings distribution
* Top countries by content
* Movie duration distribution
* Top directors by number of titles

---

## 🧠 Insights

* Movies dominate compared to TV Shows
* **Drama**, **Comedy**, and **Action** are the most frequent genres
* Countries like **USA**, **India**, and **UK** produce most content
* Content production increased steadily over the years
* Ratings **TV-MA**, **TV-14**, and **PG-13** appear most often
* Most movies are between **80–120 minutes**

---

## 🚀 Future Enhancements

* Add an **interactive dashboard** (Streamlit / Tableau / PowerBI)
* Build a **movie recommendation system**
* Apply **ML models** to predict content ratings
* Perform **NLP topic modeling** on descriptions

---

## 👩‍💻 About the Creator

**Keerthana M**
AI & Data Science Student | Aspiring AI Engineer

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

```
