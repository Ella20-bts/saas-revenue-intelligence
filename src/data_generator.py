import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generate_saas_data(num_customers=5000):
    today = datetime.today()

    countries = ["USA", "UK", "Canada", "Germany", "Australia"]
    channels = ["Organic", "Paid Ads", "Referral", "LinkedIn", "Cold Email"]
    plans = {
        "Basic": 29,
        "Pro": 79,
        "Enterprise": 199
    }

    customers = []
    subscriptions = []
    payments = []

    for i in range(1, num_customers + 1):
        signup_date = today - timedelta(days=random.randint(30, 900))
        customers.append([
            i,
            signup_date.date(),
            random.choice(countries),
            random.choice(channels)
        ])

        plan = random.choice(list(plans.keys()))
        price = plans[plan]

        churn_probability = 0.25
        is_churned = random.random() < churn_probability

        start_date = signup_date
        if is_churned:
            end_date = start_date + timedelta(days=random.randint(30, 365))
            status = "churned"
        else:
            end_date = None
            status = "active"

        subscriptions.append([
            i,
            i,
            plan,
            start_date.date(),
            end_date.date() if end_date else None,
            price,
            status
        ])

        # Generate payments (monthly recurring)
        current_date = start_date
        last_date = end_date if end_date else today

        while current_date < last_date:
            payments.append([
                i,
                i,
                current_date.date(),
                price
            ])
            current_date += timedelta(days=30)

    customers_df = pd.DataFrame(customers, columns=[
        "customer_id", "signup_date", "country", "acquisition_channel"
    ])

    subscriptions_df = pd.DataFrame(subscriptions, columns=[
        "subscription_id", "customer_id", "plan_type",
        "start_date", "end_date", "monthly_price", "status"
    ])

    payments_df = pd.DataFrame(payments, columns=[
        "payment_id", "subscription_id", "payment_date", "amount"
    ])

    return customers_df, subscriptions_df, payments_df
