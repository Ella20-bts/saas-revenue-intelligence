import streamlit as st
import pandas as pd
import psycopg2
import os
import plotly.express as px
from datetime import datetime

from src.analytics.metrics import (
    calculate_mrr,
    calculate_total_revenue,
    calculate_churn_rate,
    calculate_arpu,
    calculate_ltv,
    calculate_arr,
    calculate_ltv_cac_ratio,
    calculate_retention_matrix,
    calculate_survival_curve
)


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="SaaS Revenue Intelligence",
    layout="wide"
)

st.title("SaaS Revenue Intelligence Platform")
st.caption("Customer Analytics • Revenue Metrics • Cohort Intelligence")


# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------
def get_data():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "saas-postgres"),
            database=os.getenv("DB_NAME", "saas_db"),
            user=os.getenv("DB_USER", "admin"),
            password=os.getenv("DB_PASSWORD", "admin123"),
            port=os.getenv("DB_PORT", 5432),
        )

        customers = pd.read_sql("SELECT * FROM customers;", conn)
        subscriptions = pd.read_sql("SELECT * FROM subscriptions;", conn)
        payments = pd.read_sql("SELECT * FROM payments;", conn)

        conn.close()

        return customers, subscriptions, payments

    except Exception as e:
        st.error(f"Database Error: {e}")
        return None, None, None


customers, subscriptions, payments = get_data()

if customers is None or customers.empty:
    st.warning("No data available. Run ETL pipeline first.")
    st.stop()


# --------------------------------------------------
# EXECUTIVE KPI PANEL
# --------------------------------------------------

mrr = calculate_mrr(subscriptions)
total_revenue = calculate_total_revenue(payments)
churn_rate = calculate_churn_rate(subscriptions)
arpu = calculate_arpu(payments, customers)
ltv = calculate_ltv(arpu, churn_rate)
arr = calculate_arr(mrr)

simulated_cac = 1200
ltv_cac_ratio = calculate_ltv_cac_ratio(ltv, simulated_cac)

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("MRR", f"${mrr:,.0f}")
col2.metric("ARR", f"${arr:,.0f}")
col3.metric("Total Revenue", f"${total_revenue:,.0f}")
col4.metric("Churn Rate", f"{churn_rate:.2f}%")
col5.metric("ARPU", f"${arpu:,.2f}")
col6.metric("LTV / CAC", f"{ltv_cac_ratio:.2f}x")

st.divider()


# --------------------------------------------------
# MONTHLY REVENUE TREND
# --------------------------------------------------
st.subheader("Monthly Revenue Trend")

payments["payment_date"] = pd.to_datetime(payments["payment_date"])
payments["month"] = payments["payment_date"].dt.strftime("%Y-%m")

monthly = (
    payments.groupby("month")["amount"]
    .sum()
    .reset_index()
)

fig_revenue = px.line(
    monthly,
    x="month",
    y="amount",
    markers=True
)

st.plotly_chart(fig_revenue, use_container_width=True)


# --------------------------------------------------
# RETENTION HEATMAP
# --------------------------------------------------
st.subheader("Retention Heatmap")

retention_matrix = calculate_retention_matrix(subscriptions)

fig_heatmap = px.imshow(
    retention_matrix,
    aspect="auto",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig_heatmap, use_container_width=True)


# --------------------------------------------------
# SURVIVAL CURVE
# --------------------------------------------------
st.subheader("Cohort Survival Curve")

survival = calculate_survival_curve(subscriptions)

fig_survival = px.line(
    survival,
    x="months_active",
    y="survival_rate",
    markers=True
)

st.plotly_chart(fig_survival, use_container_width=True)


# --------------------------------------------------
# PLAN DISTRIBUTION
# --------------------------------------------------
st.subheader("Subscription Plan Distribution")

plan_dist = subscriptions["plan_type"].value_counts().reset_index()
plan_dist.columns = ["plan_type", "count"]

fig_plan = px.pie(
    plan_dist,
    values="count",
    names="plan_type",
    hole=0.4
)

st.plotly_chart(fig_plan, use_container_width=True)


# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------
st.subheader("Recent Payments")
st.dataframe(payments.head(50))

st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
