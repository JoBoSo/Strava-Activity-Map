import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sqlite3

conn = sqlite3.connect('database.sqlite3')
sql_query = "SELECT * FROM strava_gpx_data"
df = pd.read_sql_query(sql_query, conn)
conn.close()

df['elevation'] = pd.to_numeric(df['elevation'], errors='coerce')

def map():
    fig = go.Figure(go.Scattermapbox(
        lat=df['lat'], 
        lon=df['lon'],
        marker=go.scattermapbox.Marker(
            color=df['elevation'],
            colorscale=[[0, '#00ff8d'],  [0.25, '#ef40ff'], [0.75, '#FF006D'], [1, '#FF0004']],
            colorbar=dict(
                title=dict(
                    text='Elev. (m)',
                    font=dict(
                        color='white',
                        size=12,
                        family='Arial',
                    ),
                ),
                bgcolor='#02bd94',
                thickness=50,
                ticklabelposition='inside',
                tickfont=dict(
                    color='white',
                    size=12,
                    family='quicksand',
                ),
                xref='container',
                xpad=1,
                ypad=0,
            ),
            opacity=0.3,
            size=2.5,
            sizemin=2.5,
        )
        # hover_name='time',
        # hover_data=['activity', 'lat', 'lon', 'elevation']
    ))

    fig.update_layout(
        mapbox=dict(
            center=dict(lat=50, lon=-100),
            zoom=2.9,
        ),
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "sourceattribution": "United States Geological Survey",
                "source": [
                    "https://server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}" 
                ]
            },
            {
                "sourcetype": "raster",
                "sourceattribution": "Government of Canada",
                "source": ["https://geo.weather.gc.ca/geomet/?"
                        "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
                        "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
            }
        ]
    )

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

# fig = map()
# fig.show()
