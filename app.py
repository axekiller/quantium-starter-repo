import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the output data
df = pd.read_csv("data/output.csv")

# Sort by date
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Group by date, summing sales across all regions
df_grouped = df.groupby("date", as_index=False)["sales"].sum()

# Create the line chart
fig = px.line(df_grouped, x="date", y="sales",
              labels={"date": "Date", "sales": "Total Sales ($)"},
              title="Pink Morsel Sales Over Time")

# Build the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods - Pink Morsel Sales Visualiser",
            style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)