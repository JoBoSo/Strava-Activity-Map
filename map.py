import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

my_dir = os.path.dirname(__file__)
json_file_path = os.path.join(my_dir, 'data.json')
df = pd.read_json(json_file_path)

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
                        color='black',
                        size=12,
                        family='Arial',
                    )
                ),
                thickness=50,
                ticklabelposition='inside',
                tickfont=dict(
                    color='white',
                    size=12,
                    family='Arial',
                ),
                xref='container',
                xpad=1,
                ypad=3,
            ),
            opacity=0.2,
            size=2.5,
        )
        # hover_name='time',
        # hover_data=['activity', 'lat', 'lon', 'elevation']
    ))

    fig.update_layout(
        mapbox=dict(
            center=dict(lat=48, lon=-96),
            zoom=3.3,
        ),
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "sourceattribution": "United States Geological Survey",
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
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
