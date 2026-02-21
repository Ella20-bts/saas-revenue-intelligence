# 📊 SaaS Revenue Intelligence Platform

Enterprise-grade SaaS revenue analytics system built with Python, PostgreSQL, Docker, and Streamlit.

This project simulates a real-world subscription-based SaaS company and delivers executive-level revenue intelligence including retention analytics, cohort analysis, CAC modeling, and lifetime value computation.

---

## 🚀 Overview

This platform models the analytics layer of a modern SaaS company by implementing:

- End-to-end ETL pipeline
- Synthetic subscription + payment data generation
- PostgreSQL data warehouse
- Modular analytics computation engine
- Executive KPI dashboard
- Retention heatmap and survival analysis
- Fully containerized architecture

---

## 🏗 System Architecture


Data Generator
↓
ETL Pipeline (Python)
↓
PostgreSQL Database
↓
Analytics Layer (Metrics Engine)
↓
Streamlit Executive Dashboard


All components are Dockerized and designed with modular separation of concerns.

---

## 📈 SaaS Metrics Implemented

### Revenue Metrics
- MRR (Monthly Recurring Revenue)
- ARR (Annual Recurring Revenue)
- Total Revenue
- ARPU (Average Revenue Per User)
- LTV (Customer Lifetime Value)

### Efficiency Metrics
- Churn Rate
- Simulated CAC (Customer Acquisition Cost)
- LTV / CAC Ratio

### Retention Analytics
- Cohort Retention Analysis
- Retention Heatmap
- Survival Curve
- LTV by Plan
- Revenue by Country

---

## 🧠 Executive KPI Scorecard

The dashboard includes an executive SaaS panel displaying:

- ARR
- LTV
- Simulated CAC
- LTV / CAC Ratio

Designed to mirror investor-level reporting standards.

---

## 🛠 Tech Stack

| Layer | Technology |
|--------|------------|
| Language | Python 3.11 |
| Database | PostgreSQL 15 |
| Analytics | Pandas, NumPy |
| Visualization | Plotly, Streamlit |
| Containerization | Docker, Docker Compose |
| Architecture | Modular Service-Oriented Design |

---

## 📂 Project Structure


saas-revenue-intelligence/
│
├── init/
│ └── init.sql
│
├── src/
│ ├── analytics/
│ │ └── metrics.py
│ │
│ ├── etl/
│ │ └── load.py
│ │
│ ├── services/
│ │ └── db.py
│ │
│ └── data_generator.py
│
├── dashboard.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md


---

## ▶️ Running the Project

### 1️⃣ Clone Repository


git clone https://github.com/Ella20-bts/saas-revenue-intelligence.git

cd saas-revenue-intelligence


### 2️⃣ Build Containers


docker-compose build


### 3️⃣ Run the System


docker-compose up


### 4️⃣ Open Dashboard


http://localhost:8502


---

## 📊 What This Project Demonstrates

✔ Revenue modeling for subscription businesses  
✔ Cohort retention analytics implementation  
✔ SaaS KPI engineering  
✔ Modular Python architecture  
✔ PostgreSQL integration  
✔ Dockerized data infrastructure  
✔ Executive-level dashboard design  

---

## 🔮 Future Enhancements

- FastAPI backend for metrics API layer
- Automated ETL scheduler
- Cloud deployment (AWS/GCP)
- CI/CD pipeline
- Predictive churn modeling
- Data warehouse optimization

---

## 👩‍💻 Author

Louella Respuesto  
Aspiring Data & Analytics Engineer  

Focused on building production-style data systems and revenue intelligence platforms.

---

## ⭐ If You Found This Useful

Star the repository and connect on GitHub.
