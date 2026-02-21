# SaaS Revenue Intelligence Platform

**Enterprise-style SaaS Revenue Analytics System**  
Built with Python, PostgreSQL, Docker, and Streamlit to model revenue, retention, and customer lifetime value for subscription-based businesses.

---

## 🧠 Overview

This project simulates a real SaaS analytics backend, with clean architecture and modular design:

- Containerized ETL pipeline for synthetic SaaS data
- PostgreSQL data warehouse
- Business metric analytics layer
- Interactive executive dashboard
- Advanced retention and survival modeling

It demonstrates techniques and practices used in **enterprise data engineering workflows**.

---

## 🛠 Core Features

### 📊 Revenue & KPI Analytics
- Monthly Recurring Revenue (MRR)
- Annual Recurring Revenue (ARR)
- Total Revenue
- Average Revenue Per User (ARPU)
- Customer Lifetime Value (LTV)
- LTV / CAC Ratio

---

### 📈 Cohort & Retention Modeling
- Cohort retention bar chart
- Retention heatmap
- Customer survival curve

---

### 📦 CAC & Plan Analytics
- Customer Acquisition Cost (simulated)
- Plan-level lifetime value
- Revenue by plan type
- Subscription status breakdown
- Revenue by country

---

## 📁 Architecture


saas-revenue-intelligence/
│
├── init/ # Database init scripts
│ └── init.sql
│
├── src/
│ ├── analytics/ # Business metrics logic
│ │ └── metrics.py
│ │
│ ├── etl/ # ETL data pipeline
│ │ └── load.py
│ │
│ ├── services/ # Database connection layer
│ │ └── db.py
│ │
│ └── data_generator.py # Synthetic SaaS data generator
│
├── dashboard.py # Streamlit BI layer
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md


---

## 💻 Tech Stack

| Area | Technology |
|------|------------|
| Language | Python |
| Database | PostgreSQL |
| Containerization | Docker & Docker Compose |
| Visualization | Plotly & Streamlit |
| Data Modeling | Cohort retention, survival rate |
| Analytics | ARPU, MRR, LTV, CAC |

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Ella20-bts/saas-revenue-intelligence.git
cd saas-revenue-intelligence
2. Build containers
docker-compose build
3. Start services
docker-compose up -d
4. Load ETL data
docker-compose run etl
5. Open Dashboard

Visit:

http://localhost:8502
📌 Why This Matters

This repository demonstrates full end-to-end data engineering workflows that enterprise teams care about:

✔ Modular code
✔ Separation of concerns
✔ Production-like ETL pattern
✔ Metrics layer reusable in backend APIs
✔ Containerized stack
✔ Clean analytics architecture

📎 Recommended Viewing

⭐ Start with: /dashboard.py
📊 Second: src/analytics/metrics.py
🔁 Third: src/etl/load.py

🧠 Next Upgrade Opportunities

This project could be extended to:

Incremental ETL with CDC logic

Deployment to AWS ECS/RDS

API backend with FastAPI / Flask

CI/CD pipeline with GitHub Actions

Data quality and monitoring layer

👩‍💻 Author

Louella Respuesto
Data Engineering | SaaS Analytics | Remote-Ready