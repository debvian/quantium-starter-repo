import pandas
from dash import Dash, html, dcc, Input, Output
from plotly.express import line

# Path to the formatted data file
DATA_PATH = "./formatted_data.csv"

# Colors for theme
COLORS = {
    "primary": "#FCE4EC",  # Light pink background
    "secondary": "#AD1457",  # Dark pink/maroon
    "font": "#311B92",  # Dark purple text
    "accent": "#FF4081"  # Vibrant pink accent
}

# Load in data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# Initialize Dash app
dash_app = Dash(__name__)


# Create the visualization
def generate_figure(chart_data):
    line_chart = line(chart_data, x="date", y="sales", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=COLORS["primary"],
        paper_bgcolor=COLORS["secondary"],
        font_color=COLORS["font"],
        title_x=0.5,  # Center title
        xaxis_title="Date",
        yaxis_title="Sales",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#FFC1E3"),  # Soft grid color
    )
    return line_chart


visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(data),
    style={"border-radius": "15px", "padding": "10px", "background-color": COLORS["primary"]}
)

# Create the header
header = html.H1(
    "Pink Morsel Sales Dashboard",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": "white",
        "border-radius": "15px",
        "padding": "15px",
        "margin-bottom": "20px",
        "box-shadow": "0px 4px 8px rgba(0, 0, 0, 0.2)"
    }
)

# Region picker
region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "all",
    id="region_picker",
    inline=True,
    style={
        "color": COLORS["font"],
        "font-size": "18px",
        "font-weight": "bold",
        "margin-bottom": "15px"
    }
)

region_picker_wrapper = html.Div(
    [html.Label("Select Region:", style={"font-size": "20px", "color": COLORS["font"], "font-weight": "bold"}),
     region_picker],
    style={"padding": "10px", "border-radius": "10px", "background-color": COLORS["primary"]}
)


# Define the region picker callback
@dash_app.callback(
    Output("visualization", "figure"),
    Input("region_picker", "value")
)
def update_graph(region):
    # Filter the dataset
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]

    # Generate a new line chart with the filtered data
    figure = generate_figure(trimmed_data)
    return figure


# Define the app layout
dash_app.layout = html.Div(
    [
        header,
        region_picker_wrapper,
        visualization
    ],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "20px",
        "padding": "20px",
        "max-width": "800px",
        "margin": "auto",
        "box-shadow": "0px 4px 10px rgba(0, 0, 0, 0.2)"
    }
)

# Run the app
if __name__ == '__main__':
    dash_app.run()
