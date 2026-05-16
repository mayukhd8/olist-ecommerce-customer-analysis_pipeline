# 🛒 E-commerce Revenue Analysis Pipeline

## 📌 Overview
This project builds an end-to-end data pipeline using the Brazilian Olist E-commerce dataset.

The pipeline processes raw data and generates business insights such as:
- Monthly revenue trends
- Top performing cities
- Customer behavior patterns
- Consistent high-performing locations

---

## ⚙️ Tech Stack
- Python
- Pandas

---

## 🧠 Pipeline Architecture
  LOAD → CLEAN → TRANSFORM → ANALYZE


---

## 📊 Key Insights Generated

### 1. Monthly Revenue
Identifies revenue trends across time.

### 2. Top Cities by Revenue
Finds highest performing geographic regions.

### 3. Top Cities per Month
Tracks city-level performance over time.

### 4. City Consistency
Identifies cities that consistently rank in top 3.

---

## 📁 Project Structure
src/
├── data_loader.py
├── data_cleaning.py
├── data_transform.py
├── analysis.py

---

## Example Output
### Monthly revenue table
### Top cities ranking
### Consistency analysis

---

# Future Improvements
### Add visualization (Matplotlib / Seaborn)
### Build dashboard (Streamlit)
### Automate pipeline (Airflow)

## ▶️ How to Run

```bash
python main.py
