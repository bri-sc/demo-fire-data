import pandas as pd
import folium
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize, to_hex

def generate_map(df, center=[30, 14], zoom=1):
    """
    
    Generates a simple folium map with markers for each point. 

    Parameters:
    df (pd.DataFrame): dataframe containing FIRMS data.
    centre (list): Coordinates [latitude, longitude] for map centering. 
    zoom (int): Initial zoom value for the map. 

    Returns:
    fmap: A folium map with red markers. 

    """


    fmap = folium.Map(location=center, zoom_start=zoom)

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=0.5,
            color='red',
            fill=True,
            fill_opacity=0.7,
            fill_colour='red',
            popup=f"FRP: {row['frp']:.1f}"
        ).add_to(fmap)

    return fmap


def generate_frp_map(df, center=[30, 14], zoom=1):

    """
    
    Generates a folium map with coloured markers by FRP for each point using a linear colour scale. 

    Parameters:
    df (pd.DataFrame): dataframe containing FIRMS data.
    centre (list): Coordinates [latitude, longitude] for map centering. 
    zoom (int): Initial zoom value for the map. 

    Returns:
    fmap: A folium map with frp based colour coded markers. 

    """
    
    fmap = folium.Map(location=center, zoom_start=zoom)


    norm = Normalize(vmin=df['frp'].min(), vmax=df['frp'].max()) # normalises the frp values between 0 and 1 for colourmap.
    colormap = cm.get_cmap('YlOrRd')

    for _, row in df.iterrows():
        color = to_hex(colormap(norm(row['frp'])))
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=0.5,
            color=color,
            fill=True,
            fill_opacity=0.7,
            popup=f"FRP: {row['frp']:.1f}"
        ).add_to(fmap)

    return fmap



def generate_frp_map_log(df, center=[30, 14], zoom=1):

    """
    
    Generates a folium map with coloured markers by log-transformed FRP values for each point. 

    Parameters:
    df (pd.DataFrame): dataframe containing FIRMS data.
    centre (list): Coordinates [latitude, longitude] for map centering. 
    zoom (int): Initial zoom value for the map. 

    Returns:
    fmap: A folium map with log frp based colour coded markers. 

    """
    
    fmap = folium.Map(location=center, zoom_start=zoom)

    norm = Normalize(vmin=df['frp_log'].min(), vmax=df['frp_log'].max())
    colormap = cm.get_cmap('YlOrRd')

    for _, row in df.iterrows():
        color = to_hex(colormap(norm(row['frp_log'])))
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=0.5,
            color=color,
            fill=True,
            fill_opacity=0.7,
            popup=f"FRP: {row['frp']:.1f}"
        ).add_to(fmap)

    return fmap