import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the sales data
df = pd.read_csv("data/final_sales.csv")

# Convert 'date' column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Sort the data by date
df = df.sort_values("date")

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Data", style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            df,
            x="date",
            y="sales",
            color="region",
            title="Sales Over Time",
            labels={"date": "Date", "sales": "Total Sales", "region": "Region"},
            markers=True
        )
    ),

    html.P("The price of Pink Morsels increased on January 15, 2021.", style={'textAlign': 'center', 'fontWeight': 'bold'})
])

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)
