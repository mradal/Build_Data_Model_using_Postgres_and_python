import random
from faker import Faker
import pandas as pd

# Initialize Faker with a seed for controlled randomization
fake = Faker(seed=12345)

# Function to generate sample customer data
def generate_customer_data(num_records, fake):
    customers = []
    for _ in range(num_records):
        customers.append({
            'customer_id': _ + 1,
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'address': fake.address(),
            'product_id': random.randint(1, num_records),  # Adding product_id here
        })
    return customers

# Function to generate sample product data
def generate_product_data(num_records, fake):
    products = []
    for _ in range(num_records):
        products.append({
            'product_id': _ + 1,
            'product_name': fake.word().capitalize(),
            'description': fake.sentence(),
            'price': round(random.uniform(10, 200), 2),
            'category': fake.word(),
        })
    return products

# Function to generate sample sales data
def generate_sales_data(num_records, customer_ids, product_ids, fake):
    sales = []
    for _ in range(num_records):
        sale = {
            'sale_id': _ + 1,
            'customer_id': random.choice(customer_ids),
            'product_id': random.choice(product_ids),
            'sale_date': fake.date_time_between(start_date='-1y', end_date='now'),
            'quantity': random.randint(1, 5),
        }
        # Calculate total_amount based on product price
        product_price = random.uniform(10, 200)
        sale['total_amount'] = sale['quantity'] * product_price
        sales.append(sale)
    return sales

# Number of records to generate
num_records = 1000

# Generate customer data
customer_data = generate_customer_data(num_records, fake)
customers_df = pd.DataFrame(customer_data)

# Generate product data
product_data = generate_product_data(num_records, fake)
products_df = pd.DataFrame(product_data)

# Generate sales data
customer_ids = customers_df['customer_id'].tolist()
product_ids = products_df['product_id'].tolist()
sales_data = generate_sales_data(num_records, customer_ids, product_ids, fake)
sales_df = pd.DataFrame(sales_data)

# Save data to CSV files
customers_df.to_csv('customers.csv', index=False)
products_df.to_csv('products.csv', index=False)
sales_df.to_csv('sales.csv', index=False)

print(f"Generated and saved {num_records} records to CSV files.")
