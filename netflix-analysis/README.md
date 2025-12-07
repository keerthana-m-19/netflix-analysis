# 📊 Netflix Data Analysis (Python | Pandas | Matplotlib)

This project performs an in-depth **Data Analysis (DA)** on a Netflix-style dataset containing 1500 entries. Using Python scripts, Pandas, Matplotlib, and Seaborn, the project uncovers insights about movies, TV shows, genres, ratings, and content trends over the years.

---

## 📁 Dataset Overview

The dataset contains **1500 synthetic Netflix entries** generated for analysis purposes.  
Each row represents a Movie or TV Show with fields like:

- `show_id`  
- `type` (Movie/TV Show)  
- `title`  
- `director`  
- `cast`  
- `country`  
- `date_added`  
- `release_year`  
- `rating`  
- `duration`  
- `listed_in` (genre)  
- `description`  

---

## 🛠️ Technologies Used

- **Python 3**  
- **Pandas** – data cleaning & preprocessing  
- **Matplotlib** – visualizations  
- **Seaborn** – advanced charts  
- **NumPy** – numerical operations  

---

## ✨ Key Features

### ✔️ Data Cleaning  
- Handled missing values  
- Converted date formats  
- Standardized duration into numeric format  
- Cleaned and exploded genre list  

### ✔️ Exploratory Data Analysis (EDA)
Includes:

- Movie vs TV Show comparison  
- Top genres  
- Top countries producing content  
- Most frequent directors  
- Ratings distribution  
- Content release trends  
- Movie duration analysis  

---

## 📊 Visualizations

The project generates multiple charts automatically saved into the `graphs/` folder:

- **Count of Movies vs TV Shows**  
- **Top 10 Genres**  
- **Content Added Over the Years**  
- **Rating Distribution**  
- **Top Countries by Content**  
- **Movie Duration Analysis**  
- **Top Directors by Number of Titles**  

---

## 🧠 Insights

- Movies dominate the dataset compared to TV Shows  
- Genres like **Drama**, **Comedy**, and **Action** are most frequent  
- Countries like **USA**, **India**, and **UK** produce the most content  
- Content production increased steadily over the years  
- Ratings **TV-MA**, **TV-14**, and **PG-13** are most common  
- Most movies fall between **80–120 minutes**  

---

## 📂 Project Structure



Netflix-Data-Analysis/
│
├── data/
│   └── netflix_sample_1500.csv
│
├── src/
│   ├── clean.py
│   └── analysis.py
│
├── graphs/               # Auto-created by analysis.py
│   ├── movies_vs_tv.png
│   ├── top_genres.png
│   ├── content_added_over_time.png
│   ├── ratings_distribution.png
│   ├── top_countries.png
│   ├── duration_distribution.png
│   └── top_directors.png
│
├── requirements.txt
└── README.md




## ▶️ How to Run the Project

### **1. Clone the Repository**
```bash
git clone https://github.com/keerthana-m-19/netflix-analysis.git
cd netflix-analysis
````

### **2. Install Requirements**

```bash
pip install -r requirements.txt
```

### **3. Clean the Data**

```bash
python src/clean.py --input data/netflix_sample_1500.csv --output data/netflix_cleaned.csv
```

### **4. Run Analysis & Generate Visuals**

```bash
python src/analysis.py --input data/netflix_cleaned.csv --out graphs
```

Open the `graphs/` folder to see the generated PNGs.

---

## 🚀 Future Enhancements

* Add **interactive dashboard** (Streamlit / Tableau / PowerBI)
* Build a **movie recommendation system**
* Add **ML models** to predict rating category
* Perform **NLP topic modeling** on descriptions

---

## 👩‍💻 About the Creator

**Keerthana M**
AI & Data Science Student | Aspiring AI Engineer

---

 

Do you want me to do that next?
```
