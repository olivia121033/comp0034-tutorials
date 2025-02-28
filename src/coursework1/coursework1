# Imports
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc


# Define meta tags and external stylesheets
meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Initialize Dash app
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Load the dataset
file_path = Path(__file__).parent.joinpath('London_diffusiondata_2022.xlsx')
air_quality = pd.read_excel(file_path)

# Normalize column names to lowercase
air_quality.columns = air_quality.columns.str.lower()

# Ensure required columns exist
required_columns = ['borough', 'exceeding legal limit (40ugm-3)', 'exceeding who guideline (10 ugm-3)', 
                    'average concentration roadside*', 'average concentration background**', '% exceeding legal limit', '% exceeding who guideline']
missing_columns = [col for col in required_columns if col not in air_quality.columns]
if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

# Normalize column names to lowercase
air_quality.columns = air_quality.columns.str.lower()

# Convert relevant columns to numeric types
numeric_columns = [
    'average concentration roadside*', 
    'average concentration background**', 
    '% exceeding legal limit',
    'exceeding legal limit (40ugm-3)', 
    'exceeding who guideline (10 ugm-3)', 
    'average concentration roadside*', 
    'average concentration background**'
]

for col in numeric_columns:
    air_quality[col] = pd.to_numeric(air_quality[col], errors='coerce')  # Coerce errors to NaN

air_quality = air_quality.dropna(subset=numeric_columns)

# Check for missing values (if needed)
if air_quality[numeric_columns].isnull().any().any():
    print("Warning: There are missing values in the numeric columns.")

# Function to create bar chart
def bar_roadside(event_type):
    """
    Creates a bar chart showing the concentration variations with light blue bars.
    """
    try:
        df_filtered = air_quality[['borough', event_type]]

        if df_filtered.empty:
            raise ValueError(f"No data available for {event_type}")

        # Create bar chart with light blue color
        fig = px.bar(
            df_filtered,
            x='borough',
            y=event_type,
            title='Concentration Variation Throughout the UK in 2022',
            labels={'borough': 'Borough', 'value': 'Concentration', 'variable': 'Type'},
            template="simple_white"
        )
        
        # Change all bars to light blue
        fig.update_traces(marker_color='#ADD8E6')

        fig.update_xaxes(ticklen=0)
        return fig

    except Exception as e:
        fig = px.bar(title="Error Loading Data")
        fig.add_annotation(text=str(e), x=0.5, y=0.5, showarrow=False, font=dict(size=16))
        return fig
    
# Function to create line chart
def line_chart(feature):
    """
    Creates a line chart showing the correlation between exceeding legal limits/WHO guidelines and average concentration.
    Colors changed to pink and blue.
    """
    try:
        concentration_col = feature.lower()  # Matches lowercase column names
        exceedance_cols = ['exceeding legal limit (40ugm-3)', 'exceeding who guideline (10 ugm-3)']

        df_filtered = air_quality[['borough', concentration_col] + exceedance_cols]

        # Melt dataframe to plot two lines (legal limit vs WHO guideline)
        df_melted = df_filtered.melt(id_vars=['borough', concentration_col], 
                                     value_vars=exceedance_cols, 
                                     var_name='exceedance type', 
                                     value_name='exceeding level')

        # Create line chart with pink and blue colors
        fig = px.line(df_melted, 
                      x='exceeding level', 
                      y=concentration_col, 
                      color='exceedance type', 
                      markers=True,
                      title=f"Correlation: {feature} vs Exceeding Limits",
                      labels={'exceeding level': 'Exceeding Limits / WHO Guidelines',
                              concentration_col: 'Average Concentration',
                              'exceedance type': 'Type of Exceedance'},
                      template="simple_white",
                      color_discrete_sequence=['#FF69B4', '#ADD8E6']  # Pink and Blue
                     )

        return fig

    except Exception as e:
        fig = px.line(title="Error Loading Data")
        fig.add_annotation(text=str(e), x=0.5, y=0.5, showarrow=False, font=dict(size=16))
        return fig
    
# Function to create pie chart
def pie_sites():
    """
    Creates a pie chart showing the distribution of monitoring sites across boroughs.
    """
    try:
        df_filtered = air_quality[['borough', 'number of sites']].copy()

        if df_filtered.empty:
            raise ValueError("No data available for 'Number of sites'")

        # Create pie chart
        fig = px.pie(
            df_filtered,
            names='borough',
            values='number of sites',
            title='Composition of Monitoring Sites Throughout the UK (2022)',
            template="simple_white",
            hole=0.3  # Creates a donut-style chart
        )

        return fig

    except Exception as e:
        fig = px.pie(title="Error Loading Data")
        fig.add_annotation(text=str(e), x=0.5, y=0.5, showarrow=False, font=dict(size=16))
        return fig

# Function to create bar chart for exceedance percentages
def exceedance_bar_chart(exceedance_type):
    """
    Creates a bar chart showing the percentage of sites exceeding legal limits or WHO guidelines.
    """
    try:
        df_filtered = air_quality[['borough', exceedance_type]].copy()

        if df_filtered.empty:
            raise ValueError(f"No data available for {exceedance_type}")

        # Create bar chart
        fig = px.bar(
            df_filtered,
            x='borough',
            y=exceedance_type,
            title=f'Percentage of Sites Exceeding: {exceedance_type}',
            labels={'borough': 'Borough', exceedance_type: 'Percentage Exceeding (%)'},
            template="simple_white"
        )

        # Change bar color to red
        fig.update_traces(marker_color='#FF0000')  # Red color

        return fig

    except Exception as e:
        fig = px.bar(title="Error Loading Data")
        fig.add_annotation(text=str(e), x=0.5, y=0.5, showarrow=False, font=dict(size=16))
        return fig
    
def bubble_chart():
    """
    Creates a bubble chart showing the relationship between roadside and background concentrations,
    with bubble size representing the percentage exceeding legal limits.
    """
    try:
        # Ensure there are no missing values and access the columns
        df_filtered = air_quality[['average concentration roadside*', 
                                    'average concentration background**', 
                                    '% exceeding legal limit', 
                                    'borough']].copy()

        # Drop rows with any missing values in the required columns
        df_filtered = df_filtered.dropna()

        # Debugging line to check the DataFrame structure
        print(df_filtered.head())  # Make sure this is placed before the plotting

        # Create bubble chart
        fig = px.scatter(
            df_filtered,
            x='average concentration background**',
            y='average concentration roadside*',
            size='% exceeding legal limit',
            color='borough',  # Differentiate bubbles by borough
            hover_name='borough',
            title='Displays average concentration roadside and average concentration background depending on the % exceeding legal limit',
            labels={
                'average concentration background**': 'Average Concentration Background',
                'average concentration roadside*': 'Average Concentration Roadside',
                '% exceeding legal limit': 'Percentage Exceeding Legal Limit'
            },
            template="simple_white"

        )

        fig.update_layout(
            title={
                'text': 'Displays average concentration roadside and average concentration background depending on the % exceeding legal limit',
                'font': {
                    'size': 16, 
                    'color': 'black'
                            }
                        }
        )
        return fig

    except Exception as e:
        # Improved error message for better debugging
        fig = px.scatter(title="Error Loading Data")
        fig.add_annotation(text=str(e), x=0.5, y=0.5, showarrow=False, font=dict(size=16))
        return fig

# Dashboard layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
            html.H1("UK Diffusion Tube Data Dashboard"),
            html.P("This dashboard provides data about air quality in the UK in 2022.")
        ]), width=8),
        dbc.Col(
            dbc.Select(
                options=[
                    {"label": "Roadside", "value": "average concentration roadside*"},
                    {"label": "Background", "value": "average concentration background**"},
                ],
                value="average concentration roadside*",
                id="event-type-selector",
            ),
            width=4, className="d-flex align-items-center justify-content-end"
        ),
    ], align="center", className="mb-4"),  # Added margin below the row for spacing

    # New title above the bar chart
    html.H2("What area has the highest average concentration roadside and background in 2022?", 
            className="text-center mt-3"),  

    dbc.Row([
        dbc.Col(dcc.Graph(id="bar-chart"))
    ], className="mt-3"),  # Added top margin for spacing

    # Title above the line chart
    html.H2("To what extent does exceeding legal limit / WHO guidelines affect the average concentrations?", 
            className="text-center mt-4"),

    dcc.RadioItems(
        options=[
            {'label': 'Average Concentration Roadside', 'value': 'average concentration roadside*'},
            {'label': 'Average Concentration Background', 'value': 'average concentration background**'}
        ],
        value='average concentration roadside*',  # Default selection
        id='feature-selector',
        inline=True
    ),
    
    dcc.Graph(id='line-chart')
])

app.layout.children.extend([
    html.H2("What is the composition of sites throughout the UK?", className="text-center mt-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id="pie-chart"))
    ], className="mt-3")
])

app.layout.children.extend([
    html.H2("Proportions of cities exceeding legal limits / WHO guidelines?", className="text-center mt-4"),

    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
    options=[
        {"label": "% Exceeding Legal Limit", "value": "% exceeding legal limit"},
        {"label": "% exceeding who guideline", "value": "% exceeding who guideline"},
    ],
    value="% exceeding legal limit",
    id="exceedance-selector",
    clearable=False
), width=6
        )
    ], className="mt-3 mb-3"),

    dbc.Row([
        dbc.Col(dcc.Graph(id="exceedance-bar-chart"))
    ], className="mt-3")
])

app.layout.children.extend([
    html.H2("Air Quality in the UK", className="text-center mt-4"),
    dbc.Row([
        dbc.Col(dcc.Graph(id="bubble-chart"))
    ], className="mt-3")
])

# Callback to update bar chart
@callback(
    Output("bar-chart", "figure"),
    Input("event-type-selector", "value")
)
def update_bar_chart(event_type):
    return bar_roadside(event_type)

# Callback to update line chart
@callback(
    Output("line-chart", "figure"),
    Input("feature-selector", "value")
)
def update_line_chart(feature):
    return line_chart(feature)

@callback(
    Output("pie-chart", "figure"),
    Input("feature-selector", "value")  # You can remove this input if filtering isn't needed
)
def update_pie_chart(_):
    return pie_sites()

@callback(
    Output("exceedance-bar-chart", "figure"),
    Input("exceedance-selector", "value")
)
def update_exceedance_chart(exceedance_type):
    return exceedance_bar_chart(exceedance_type)

@callback(
    Output("bubble-chart", "figure"),
    Input("event-type-selector", "value")  # Optional: add more inputs if needed
)
def update_bubble_chart(_):
    return bubble_chart()

# Run the app
if __name__ == "__main__":
    app.run(debug=True)