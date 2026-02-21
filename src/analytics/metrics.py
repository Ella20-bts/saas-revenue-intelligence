import pandas as pd


# --------------------------------------------------
# CORE SAAS METRICS
# --------------------------------------------------

def calculate_mrr(subscriptions: pd.DataFrame) -> float:
    active = subscriptions[subscriptions["status"] == "active"]
    return active["monthly_price"].sum()


def calculate_total_revenue(payments: pd.DataFrame) -> float:
    return payments["amount"].sum()


def calculate_churn_rate(subscriptions: pd.DataFrame) -> float:
    if len(subscriptions) == 0:
        return 0.0

    cancelled = subscriptions[subscriptions["status"] == "cancelled"]
    return (len(cancelled) / len(subscriptions)) * 100


def calculate_arpu(payments: pd.DataFrame, customers: pd.DataFrame) -> float:
    total_customers = customers["customer_id"].nunique()
    if total_customers == 0:
        return 0.0

    return payments["amount"].sum() / total_customers


def calculate_ltv(arpu: float, churn_rate: float) -> float:
    if churn_rate == 0:
        return 0.0

    return arpu / (churn_rate / 100)


def calculate_arr(mrr: float) -> float:
    return mrr * 12


def calculate_ltv_cac_ratio(ltv: float, cac: float) -> float:
    if cac == 0:
        return 0.0
    return ltv / cac


# --------------------------------------------------
# ADVANCED ANALYTICS
# --------------------------------------------------

def calculate_retention_matrix(subscriptions: pd.DataFrame) -> pd.DataFrame:
    df = subscriptions.copy()

    df["start_date"] = pd.to_datetime(df["start_date"])
    df["end_date"] = pd.to_datetime(df["end_date"], errors="coerce")

    df["cohort"] = df["start_date"].dt.strftime("%Y-%m")

    df["months_active"] = (
        (df["end_date"].fillna(pd.Timestamp.today()) - df["start_date"])
        .dt.days // 30
    )

    retention = (
        df.groupby(["cohort", "months_active"])
        .size()
        .reset_index(name="count")
    )

    pivot = retention.pivot(
        index="cohort",
        columns="months_active",
        values="count"
    ).fillna(0)

    return pivot


def calculate_survival_curve(subscriptions: pd.DataFrame) -> pd.DataFrame:
    df = subscriptions.copy()

    df["start_date"] = pd.to_datetime(df["start_date"])
    df["end_date"] = pd.to_datetime(df["end_date"], errors="coerce")

    df["months_active"] = (
        (df["end_date"].fillna(pd.Timestamp.today()) - df["start_date"])
        .dt.days // 30
    )

    survival = (
        df.groupby("months_active")
        .size()
        .reset_index(name="count")
    )

    survival["survival_rate"] = (
        survival["count"] / survival["count"].iloc[0]
    )

    return survival
