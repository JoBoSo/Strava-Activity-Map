from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from statistics import mean
from map import map

### App ###

app = Dash(__name__)

app.layout = html.Div(
    children=[

        html.H1("Strava Activity Map"),

        dcc.Graph(figure=map()),

    ],

    className='MyStyle'
)


if __name__ == '__main__':
    app.run(debug=True)
