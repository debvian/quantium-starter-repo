import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the sales data
df = pd.read_csv("data/final_sales.csv")

# Convert 'date' column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Create a Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div(children=[

    # Header
    html.H1("Pink Morsel Sales Dashboard", style={'textAlign': 'center', 'color': '#ff4c4c', 'margin-bottom': '20px'}),

    # Region Selection Radio Button
    html.Label("Select Region:", style={'font-size': '18px', 'font-weight': 'bold'}),
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',  # Default selection
        inline=True,
        style={'margin-bottom': '20px'}
    ),

    # Line Chart
    dcc.Graph(id='sales-line-chart'),

    # Note about price increase
    html.P("🔺 Price Increase on January 15, 2021",
           style={'textAlign': 'center', 'font-weight': 'bold', 'color': '#ff0000'})

], style={'width': '80%', 'margin': 'auto', 'font-family': 'Arial'})


# Define callback to update chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    filtered_df = df if selected_region == 'all' else df[df['region'].str.lower() == selected_region.lower()]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        title="Sales Over Time",
        labels={"date": "Date", "sales": "Total Sales", "region": "Region"},
        markers=True
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        plot_bgcolor="#f9f9f9",
        paper_bgcolor="#ffffff",
        font=dict(family="Arial", size=14),
    )

    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
