import pandas as pd
import psycopg2

# Database connection details
DB_HOST = "localhost"
DB_NAME = "digitalxc_db"
DB_USER = "your_user"
DB_PASS = "your_password"

# Load the dataset
df = pd.read_csv("Sample Data file for Analysis_Jan'25.xlsx")

# Connect to the database
conn = psycopg2.connect(
    host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
)
cur = conn.cursor()

# Insert data
for _, row in df.iterrows():
    cur.execute(
        """
        INSERT INTO tickets (ticket_id, category, sub_category, priority, 
                             created_date, resolved_date, status, 
                             assigned_group, technician, resolution_time_hours, customer_impact) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        tuple(row),
    )

conn.commit()
cur.close()
conn.close()
print("Data Loaded Successfully!")
