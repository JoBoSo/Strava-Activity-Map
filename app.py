from dash import Dash, html, dcc
from map import map

### App ###

app = Dash(__name__)

app.layout = html.Div(
    children=[

        html.Div("Strava Activity Map", className='header'),

        dcc.Graph(figure=map(), className='map'),

    ],

    className='map-container'
)


if __name__ == '__main__':
    app.run(debug=True)
