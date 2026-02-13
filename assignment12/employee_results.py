# Task 1: Plotting with Pandas
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step1: Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# Step2: Write the sql query
query = """
SELECT last_name, SUM(price * quantity) AS revenue FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id;
"""

# Step3: Load the query results into a Pandas DataFrame
employee_results = pd.read_sql_query(query, conn)

# Step4: Plot the result as a bar chart
employee_results.plot(
    kind="bar",
    x="last_name",
    y="revenue",
    color="orange",
    legend=False
)

# Step5: Titles and Labels
plt.title("Employee Revenue")
plt.xlabel("Employee Last Name")
plt.ylabel("Revenue")

# Step6: Show the plot
plt.show()

# Step7: Close the connection
conn.close()