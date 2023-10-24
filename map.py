import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from statistics import mean
import os

my_dir = os.path.dirname(__file__)
json_file_path = os.path.join(my_dir, 'data.json')
df = pd.read_json(json_file_path)

# zoom - can adjust the subtraction factor (10 - 12)
# lat_num = [float(i) for i in lat]
# lon_num = [float(i) for i in lon]
# max_bound = max(abs(max(lat_num)-min(lat_num)), abs(max(lon_num)-min(lon_num))) * 111
# zoom = 11.5 - np.log(max_bound)

def map():
    fig = px.density_mapbox(
        df, 
        lat='lat', 
        lon='lon',
        # center=dict(lat=mean(lat_num), lon=mean(lon_num)),
        # zoom=zoom,
        center=dict(lat=48, lon=-96),
        zoom=3.3,
        # mapbox_style="carto-positron",
        opacity = 0.3,
        radius = 2.5,
        range_color = [0,250000],
        color_continuous_scale='inferno'
    )

    fig.add_trace(
        go.Scattermapbox(
            lat=df["lat"],
            lon=df["lon"],
            mode="markers",
            showlegend=False,
            hoverinfo="skip",
        )
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
