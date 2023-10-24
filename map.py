import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from statistics import mean
import os

my_dir = os.path.dirname(__file__)
json_file_path = os.path.join(my_dir, 'data.json')
df = pd.read_json(json_file_path)

def map():
    fig = px.scatter_mapbox(
        df, 
        lat='lat', 
        lon='lon',
        center=dict(lat=48, lon=-96),
        zoom=3.3,
        color_discrete_sequence=['#00ff8d'],
        hover_name='time',
        hover_data=['activity', 'lat', 'lon', 'elevation']
    )

    fig.update_layout(
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
