### Library Import ###
import streamlit as st
import streamlit.components.v1 as components
import time
import pickle
import pandas as pd
import numpy
import plotly.express as px
import geopandas as gpd
import json
import plotly.io as pio

### Data Import ###
# Paths
precincts_geojson_path = r"C:\Users\cmphi\Documents\github\Capstone_911\data\Police Precincts\Police Precincts.geojson"
boroughs_geojson_path = r"C:\Users\cmphi\Documents\github\Capstone_911\data\Borough Boundaries\Borough Boundaries.geojson"
data_dict_path = r"C:\Users\cmphi\Documents\github\Capstone_911\data\forecast_3-31-2024.pkl"
# Imports
data_dict = pd.read_pickle(data_dict_path)
data_dict = {k: v for k, v in data_dict.items() if k != "scores"}
boroughs_geo = gpd.read_file(boroughs_geojson_path)
precincts_geo = gpd.read_file(precincts_geojson_path)

### Layout ###
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)
st.logo('../misc/brainstation_logo.png')

### Code Start ###
st.title("Data Visualization")
st.divider()

# Date selector
with st.form(key='select_form'):
    start_time = data_dict['total']['ds'].min()
    end_time = data_dict['total']['ds'].max()
    selected_date = st.date_input('Select the Date to Visualize:', 
                                   min_value=start_time, 
                                   max_value=end_time)
    submit_button = st.form_submit_button(label='Submit')

if submit_button:

    for key, df in data_dict.items():
            data_dict[key] = df.loc[df['ds'].dt.date == selected_date]

    ## Data_dict format manipulation for visualization ##
    boroughs_geo['boro_name'] = boroughs_geo['boro_name'].str.upper()
    # Exclude specific keys
    excluded_keys = ['total']
    # Filter and add a source column based on key type (numeric as strings) and excluding specific keys
    precinct_data = {key: df.assign(Source=key) for key, df in data_dict.items() if key.isdigit() and key not in excluded_keys}
    borough_data = {key: df.assign(Source=key) for key, df in data_dict.items() if not key.isdigit() and key not in excluded_keys}
    # Merge the DataFrames in each category if they are not empty
    merged_precinct_df = pd.concat(precinct_data.values(), ignore_index=True) if precinct_data else pd.DataFrame()
    merged_borough_df = pd.concat(borough_data.values(), ignore_index=True) if borough_data else pd.DataFrame()
    # JSON Conversion #
    # Convert  GeoPandas DataFrame to a GeoJSON string
    geojson_str_boroughs = boroughs_geo.to_json()
    geojson_str_precincts = precincts_geo.to_json()
    # Optionally, convert the GeoJSON string to a dictionary
    geojson_dict_boroughs = json.loads(geojson_str_boroughs)
    geojson_dict_precincts = json.loads(geojson_str_precincts)


    ## Starting with borough! ##
    st.subheader('Borough Timeseries Heatmap')
    with st.spinner('Wait for it...'):
        # Calculate the minimum and maximum values of 'yhat' across all time frames
        min_yhat = merged_borough_df['yhat'].min()
        max_yhat = merged_borough_df['yhat'].max()

        # Finally, The Plotting
        fig_borough = px.choropleth_mapbox(
            merged_borough_df,
            geojson=geojson_dict_boroughs,
            locations='Source',
            color='yhat',
            animation_frame=merged_borough_df['ds'],
            featureidkey='properties.boro_name',
            color_continuous_scale='Turbo', #Bluered
            range_color=[min_yhat, max_yhat],  # Set the range for the color scale
            mapbox_style='carto-darkmatter',  # Free style from OpenStreetMap
            zoom=9.5,  # Adjust the zoom level based on your map
            center={"lat": 40.730610, "lon": -73.935242}  # Center the map around New York City
        )

        fig_borough.update_geos(fitbounds="locations", visible=False)

        # Update layout with faster animation speed
        fig_borough.update_layout(
            width=1250,
            height=800,
            margin=dict(l=1, r=0, t=1, b=0),  # Adjust margins to accommodate buttons
            updatemenus=[{
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 250, "redraw": True}, "fromcurrent": True}],  # Adjust duration to make it faster
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top"
            }]
        )
        st.plotly_chart(fig_borough)
    st.divider()

    ## Next Precinct ##
    st.subheader('Precinct Timeseries Heatmap')
    with st.spinner('More waiting...'):
        # Calculate the minimum and maximum values of 'yhat' across all time frames
        min_yhat = merged_precinct_df['yhat'].min()
        max_yhat = merged_precinct_df['yhat'].max()

        # Finally, The Plotting
        fig_precinct = px.choropleth_mapbox(
            merged_precinct_df,
            geojson=geojson_dict_precincts,
            locations='Source',
            color='yhat',
            animation_frame=merged_precinct_df['ds'],
            featureidkey='properties.precinct',
            color_continuous_scale='Turbo',
            range_color=[min_yhat, max_yhat],  # Set the range for the color scale
            mapbox_style='carto-darkmatter',  # Free style from OpenStreetMap
            zoom=9.5,  # Adjust the zoom level based on your map
            center={"lat": 40.730610, "lon": -73.935242}  # Center the map around New York City
        )

        fig_precinct.update_geos(fitbounds="locations", visible=False)

        fig_precinct.update_layout(
            #autosize = True,
            width=1250,
            height=800,
            margin=dict(l=1, r=0, t=1, b=0),  # Adjust margins to accommodate buttons
        )

        # Update layout with faster animation speed
        fig_precinct.update_layout(
            width=1250,
            height=800,
            margin=dict(l=1, r=0, t=1, b=0),  # Adjust margins to accommodate buttons
            updatemenus=[{
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 250, "redraw": True}, "fromcurrent": True}],  # Adjust duration to make it faster
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top"
            }]
        )
        st.plotly_chart(fig_precinct)
