### Libraries ###
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from datetime import datetime, timedelta
import plotly.express as px

### Layout ###
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)
st.logo('../misc/brainstation_logo.png')

### Data Imports ###
dataframes_dict = pd.read_pickle(r"C:\Users\cmphi\Documents\github\Capstone_911\data\forecast_3-31-2024.pkl")
dataframes_dict = {k: v for k, v in dataframes_dict.items() if k != "scores"}

### Functions ###
def create_traces(selected_dataframes, start_date, end_date):
    colors = px.colors.qualitative.Plotly
    traces = []
    
    for index, df_name in enumerate(selected_dataframes):
        df = dataframes_dict[df_name]
        df = df[(df['ds'] >= pd.to_datetime(start_date)) & (df['ds'] <= pd.to_datetime(end_date))]
        
        if 'quality' in df.columns:
            color_scale = px.colors.sequential.Blues[::-1] if index % 3 == 0 else \
                          px.colors.sequential.Greens[::-1] if index % 3 == 1 else \
                          px.colors.sequential.Reds[::-1]
            for quality in sorted(df['quality'].unique(), reverse=True):
                filtered_df = df[df['quality'] == quality]
                trace = go.Scatter(
                    x=filtered_df['ds'],
                    y=filtered_df['yhat'],
                    mode='lines',
                    name=f"{df_name} (Quality {quality})",
                    line=dict(color=color_scale[quality + 2])  # Adjusting indexing for dark to light
                )
                traces.append(trace)
        else:
            st.warning(f"DataFrame {df_name} does not contain 'quality' column.")
    return traces

### - CODE START - ###
st.title("Deep Dive - Specific Investigation")
st.divider()

with st.form(key='select_form'):
    selected_dataframes = st.multiselect("Select the Precincts/Boroughs to Investigate:",
                                         options=list(dataframes_dict.keys()),
                                         default=['total'])
    start_time = dataframes_dict['total']['ds'].min()
    end_time = dataframes_dict['total']['ds'].max()
    pred_start = dataframes_dict['total'][dataframes_dict['total']['quality'] == 1]['ds'].min()

    selected_dates = st.date_input('Select the Dates to Investigate:', 
                                   value=(pred_start, end_time), 
                                   min_value=start_time, 
                                   max_value=end_time)

    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    traces = create_traces(selected_dataframes, selected_dates[0], selected_dates[1])
    
    fig = go.Figure(data=traces)
    fig.update_layout(
        title="NYC 911 Calls Over Time",
        xaxis_title="Date",
        yaxis_title="Number of Calls",
        legend_title="Quality",
        template="plotly_white",
        showlegend=True,
        xaxis=dict(rangeslider=dict(visible=True), type="date", range=[selected_dates[0].isoformat(), selected_dates[1].isoformat()])
    )

    st.plotly_chart(fig)

    st.divider()
    for df in selected_dataframes:
        range_df = dataframes_dict[df][(dataframes_dict[df]['ds'] >= pd.to_datetime(selected_dates[0])) & (dataframes_dict[df]['ds'] <= pd.to_datetime(selected_dates[1]))]
        st.subheader(f'Location: {df} - Dataframe')
        st.write(range_df)
        st.divider()