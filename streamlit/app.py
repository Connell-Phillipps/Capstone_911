### Libraries ###
import streamlit as st
from st_pages import Page, show_pages, add_page_title
import pandas as pd
import numpy as np
import plotly.express as px

### Layout ###
st.set_page_config(
    layout="centered",
    initial_sidebar_state="expanded",
)
st.logo('../misc/brainstation_logo.png')

### Data Imports ###
response_df = pd.read_csv("../data/NYPD_Response_Times_for_Crimes_in_Progress.csv")


### Page Start ###
# Logo
col1, col2, col3 = st.columns(3)
with col2:
    st.image('../misc/nypd_logo.png', use_column_width="auto")

# Title
st.title("911 Call Volume Forecasting")
st.divider()

# Problem Statement
st.subheader('Problem Statement:')
st.write('Is there any way to reduce 911 call response time by prediction call volume by location?')
st.divider()

# Average Response Time
st.subheader('Average Response Time')
st.caption('[nyc.gov](https://www.nyc.gov/site/911reporting/reports/response-time-trends.page)')
# Create a Plotly Express plot
fig = px.line(response_df, x="Date Week", y=["Critical", "Serious", "Non-Critical"],
              labels={"value": "Average Response Time (min)", "Date Week": "Year"})

# Update the trace colors
fig.for_each_trace(
    lambda trace: trace.update(line=dict(color="red")) if trace.name == "Critical" else
                  trace.update(line=dict(color="orange")) if trace.name == "Serious" else
                  trace.update(line=dict(color="#66BB66"))
)

# Display the plot in Streamlit
st.plotly_chart(fig)
st.markdown('''
#### **Insights:**
* Reducing response time leads to increased public opinion of police
    * Increasing public opinion of police builds a stronger community by increasing trust and outlook of police
    * When people trust and have a better opinion of the police they are more likely to report incidents
    * When police respond faster they have a greater change to defuse situations and decrease threats
* Reducing response times wouldn't really reduce response times for critical crime in progress calls, police already respond as fast as possible to those calls.
* There is a chance that using this model to more strategic place officers might reduce response time for a critical call and save lives.
* [READ MORE](https://www.policinginstitute.org/wp-content/uploads/2015/07/Pate-1976-Police-Response-Time.pdf)

            ''')



show_pages(
    [
        Page("app.py", "Home", "🏠"),
        #Page("pages/Data_info.py", "Data Information", "📊"),
        Page("pages/Visualization.py", "Visualizations", "📈"),
        Page("pages/Deep_Dive.py", "Deep Dive", "🔍"),
        Page("pages/About_Me.py", "About Me", "👤")
    ]
)

