# Task 2: A Line Plot with Pandas
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step1: Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# Step2: SQL query to get order totals
query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price FROM orders o 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY o.order_id
ORDER BY o.order_id;
"""

# Step3: Load into a DataFrame
df = pd.read_sql_query(query, conn)

# Step4: Add cumulative revenue column
# Using cumsum
df['cumulative'] = df['total_price'].cumsum()

# Step5: Plot cumulative revenue vs order_id
df.plot(
    kind="line",
    x="order_id",
    y="cumulative",
    color="purple",
    legend=False
)

# Step6: Titles and Labels
plt.title("Cumulative Revenue Over Orders")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")

# Step7: Show the plot
plt.show()

# Step8: Close connection
conn.close()