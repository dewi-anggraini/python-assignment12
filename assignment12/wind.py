# Task 3: Interactive Visualizations with Plotly
import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Step1: Load the wind dataset
df = pldata.wind(return_type='pandas')

# Step2: Print first and last 10 rows
print("First 10 rows")
print(df.head(10))
print("Last 10 rows")
print(df.tail(10))

# Step3: Clean the "Strenght" Column into a float (exmpl: 10.0)
df['strength'] = df['strength'].str.replace(r'[^0-9.]', '', regex=True).astype(float)

# Step4: Create interactive scatter plot
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs Frequency by Direction"
)

# Step5: Save plot as html
fig.write_html("wind.html")

# Step6: Show the plot
fig.show()
