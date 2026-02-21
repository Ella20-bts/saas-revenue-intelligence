-- Customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    signup_date DATE NOT NULL,
    country VARCHAR(50),
    acquisition_channel VARCHAR(50)
);

-- Subscriptions table
CREATE TABLE subscriptions (
    subscription_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    plan_type VARCHAR(20),
    start_date DATE,
    end_date DATE,
    monthly_price NUMERIC(10,2),
    status VARCHAR(20)
);

-- Payments table
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    subscription_id INT REFERENCES subscriptions(subscription_id),
    payment_date DATE,
    amount NUMERIC(10,2)
);
CREATE TABLE IF NOT EXISTS saas_revenue (
    id SERIAL PRIMARY KEY,
    customer_id VARCHAR(50),
    plan_type VARCHAR(50),
    monthly_revenue FLOAT,
    churn_probability FLOAT,
    signup_date DATE,
    extracted_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS saas_revenue_current (
    customer_id VARCHAR(50) PRIMARY KEY,
    plan_type VARCHAR(50),
    monthly_revenue FLOAT,
    churn_probability FLOAT,
    signup_date DATE,
    extracted_at TIMESTAMP
);

