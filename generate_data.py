import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Connect to your PostgreSQL DB
conn = psycopg2.connect(
    dbname="rag_demo",
    user="postgres",         # change if needed
    password="1234",  # change to your actual password
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Drop existing tables if rerunning
cur.execute("""
DROP TABLE IF EXISTS order_items, orders, reviews, products, customers, employees, suppliers CASCADE;
""")

# Create tables
cur.execute("""
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(50),
    address TEXT,
    join_date DATE
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10, 2),
    stock INT,
    description TEXT
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    order_date DATE,
    total_amount NUMERIC(10, 2),
    status VARCHAR(50)
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id),
    product_id INT REFERENCES products(id),
    quantity INT,
    unit_price NUMERIC(10, 2)
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(50),
    department VARCHAR(50),
    hire_date DATE,
    salary NUMERIC(10, 2)
);

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    contact_name VARCHAR(100),
    phone VARCHAR(50),
    address TEXT,
    created_at DATE
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    customer_id INT REFERENCES customers(id),
    rating INT,
    comment TEXT,
    created_at DATE
);
""")

# Populate Customers
for _ in range(1000):
    cur.execute("""
        INSERT INTO customers (name, email, phone, address, join_date)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        fake.name(),
        fake.email(),
        fake.phone_number(),
        fake.address(),
        fake.date_between(start_date='-3y', end_date='today')
    ))

# Populate Products
categories = ['Food', 'Beauty', 'Health', 'Beverage', 'Spices', 'Wellness']
for _ in range(1000):
    cur.execute("""
        INSERT INTO products (name, category, price, stock, description)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        fake.word().capitalize() + " " + fake.word().capitalize(),
        random.choice(categories),
        round(random.uniform(10, 200), 2),
        random.randint(10, 200),
        fake.sentence()
    ))

# Populate Employees
departments = ['Sales', 'Support', 'IT', 'Logistics', 'Inventory', 'Finance']
roles = ['Manager', 'Officer', 'Assistant', 'Engineer', 'Specialist']
for _ in range(1000):
    cur.execute("""
        INSERT INTO employees (name, role, department, hire_date, salary)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        fake.name(),
        random.choice(roles),
        random.choice(departments),
        fake.date_between(start_date='-5y', end_date='today'),
        round(random.uniform(5000, 20000), 2)
    ))

# Populate Suppliers
for _ in range(1000):
    cur.execute("""
        INSERT INTO suppliers (name, contact_name, phone, address, created_at)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        fake.company(),
        fake.name(),
        fake.phone_number(),
        fake.address(),
        fake.date_between(start_date='-5y', end_date='today')
    ))

# Populate Orders
for _ in range(1000):
    customer_id = random.randint(1, 1000)
    date = fake.date_between(start_date='-2y', end_date='today')
    status = random.choice(['Shipped', 'Delivered', 'Processing', 'Cancelled'])
    total = round(random.uniform(50, 500), 2)
    cur.execute("""
        INSERT INTO orders (customer_id, order_date, total_amount, status)
        VALUES (%s, %s, %s, %s)
    """, (customer_id, date, total, status))

# Populate Order Items
for _ in range(3000):
    cur.execute("""
        INSERT INTO order_items (order_id, product_id, quantity, unit_price)
        VALUES (%s, %s, %s, %s)
    """, (
        random.randint(1, 1000),
        random.randint(1, 1000),
        random.randint(1, 5),
        round(random.uniform(10, 200), 2)
    ))

# Populate Reviews
for _ in range(1000):
    cur.execute("""
        INSERT INTO reviews (product_id, customer_id, rating, comment, created_at)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        random.randint(1, 1000),
        random.randint(1, 1000),
        random.randint(1, 5),
        fake.sentence(),
        fake.date_between(start_date='-2y', end_date='today')
    ))

# Add indexes
cur.execute("""
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
CREATE INDEX idx_products_category ON products(category);
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_reviews_product_id ON reviews(product_id);
CREATE INDEX idx_reviews_customer_id ON reviews(customer_id);
""")

# Done
conn.commit()
cur.close()
conn.close()
print("✅ Data generation complete with indexes!")
