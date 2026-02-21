import psycopg2
import os
import time
from src.data_generator import generate_saas_data


def connect_with_retry():
    for _ in range(10):
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST", "db"),
                database=os.getenv("DB_NAME", "saas_db"),
                user=os.getenv("DB_USER", "admin"),
                password=os.getenv("DB_PASSWORD", "admin123"),
                port=os.getenv("DB_PORT", 5432),
            )
            print("✅ Connected to database")
            return conn
        except psycopg2.OperationalError:
            print("⏳ Waiting for database...")
            time.sleep(3)

    raise Exception("Database connection failed.")


def load_to_db():
    customers, subscriptions, payments = generate_saas_data()

    print("Customers generated:", len(customers))
    print("Subscriptions generated:", len(subscriptions))
    print("Payments generated:", len(payments))

    conn = connect_with_retry()
    cursor = conn.cursor()

    # Insert Customers
    for _, row in customers.iterrows():
        cursor.execute("""
            INSERT INTO customers (customer_id, signup_date, country, acquisition_channel)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (customer_id) DO NOTHING;
        """, (
            row["customer_id"],
            row["signup_date"],
            row["country"],
            row["acquisition_channel"]
        ))

    # Insert Subscriptions
    for _, row in subscriptions.iterrows():
        cursor.execute("""
            INSERT INTO subscriptions (
                subscription_id,
                customer_id,
                plan_type,
                start_date,
                end_date,
                monthly_price,
                status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (subscription_id) DO NOTHING;
        """, (
            row["subscription_id"],
            row["customer_id"],
            row["plan_type"],
            row["start_date"],
            row["end_date"],
            row["monthly_price"],
            row["status"]
        ))

    # Insert Payments
    for _, row in payments.iterrows():
        cursor.execute("""
            INSERT INTO payments (subscription_id, amount, payment_date)
            VALUES (%s, %s, %s);
        """, (
            row["subscription_id"],
            row["amount"],
            row["payment_date"]
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("🚀 SaaS data generated and loaded successfully!")


if __name__ == "__main__":
    load_to_db()
