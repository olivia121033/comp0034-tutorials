# Imports for Dash, html, and Bootstrap components
from dash import Dash, html
import dash_bootstrap_components as dbc

# Variable that defines the meta tag for the viewport
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Define the rows and columns
row_one = dbc.Row([
    dbc.Col(html.Div([
        html.H1("Paralympics Data Analytics"),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida.")
    ]))
])

row_two = dbc.Row([
    dbc.Col(html.Div([
        dbc.Select(
            options=[
                {"label": "Events", "value": "events"},
                {"label": "Sports", "value": "sports"},
                {"label": "Countries", "value": "countries"},
                {"label": "Athletes", "value": "participants"},
            ],
            value="events",
            id="dropdown-input",
        )
    ]), width=4),
    dbc.Col(html.Div([
        dbc.Label("Select the Paralympic Games type"),
        dbc.Checklist(
            options=[
                {"label": "Summer", "value": "summer"},
                {"label": "Winter", "value": "winter"},
            ],
            value=["summer"],
            id="checklist-input",
        ),
    ]), width={"size": 4, "offset": 2}),
])

row_three = dbc.Row([
    dbc.Col(html.Div([
        html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
    ])),
    dbc.Card([
        dbc.CardImg(src=app.get_asset_url("logos/2022_Beijing.jpg"), top=True),
        dbc.CardBody([
            html.H4("Beijing 2022", className="card-title"),
            html.P("Number of athletes: XX", className="card-text"),
            html.P("Number of events: XX", className="card-text"),
            html.P("Number of countries: XX", className="card-text"),
            html.P("Number of sports: XX", className="card-text"),
        ]),
    ], style={"width": "18rem"})
])

row_four = dbc.Row([
    dbc.Col(html.Div([
        html.Img()
    ])),
    dbc.Col(html.Div([
        html.Div()
    ]))
])

# Wrap the layout in a Bootstrap container
app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
    row_four,
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

#newnew

row_one = dbc.Row([
    dbc.Col(html.Div([
        html.H1("UK Diffusion Tube Data Dashboard"),
        html.P("This dashboard provides data about air quality in the UK in 2022.")
    ]))
])

# Function to create bar chart
def bar_roadside(event_type):
    """
    Creates a stacked bar chart showing the ratio of roadside average concentrations in the UK.
    """
    try:
        df_filtered = air_quality[['borough', event_type]]

        if df_filtered.empty:
            raise ValueError(f"No data available for {event_type}")

        # Create bar chart
        fig = px.bar(
            df_filtered,
            x='borough',
            y=event_type,
            title='Concentration Variation Throughout the UK in 2022',
            labels={'borough': 'Borough', 'value': 'Concentration', 'variable': 'Type'},
            template="simple_white"
        )
        fig.update_xaxes(ticklen=0)
        return fig

    except Exception as e:
        fig = px.bar(title="Error Loading Data")
        fig.add_annotation(text=str(e), x=0.5, y=0.5, showarrow=False, font=dict(size=16))
        return fig

row_two = dbc.Row([
    dbc.Col(html.Div([
        dbc.Select(
            options=[
                {"label": "Roadside", "value": "average concentration roadside*"},
                {"label": "Background", "value": "average concentration background**"},
            ],
            value="average concentration roadside*",
            id="event-type-selector",
        )
    ]), width=4),
]),
dbc.Row([
    dbc.Col(dcc.Graph(id="bar-chart"))
])

# Callback to update bar chart
@callback(
    Output("bar-chart", "figure"),
    Input("event-type-selector", "value")
)
def update_bar_chart(event_type):
    return bar_roadside(event_type)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
