# 911 Hotspot Predictor
Author: Connell Phillipps <br><br>


## 1 - **Project Overview**
The goal of this project is to highlight and demonstrate the skills learned through BratinStations Data Science bootcamp. In this project, I aim to use data provided by NYC Open Data to create a predictive algorithm to show 911 call hot spots. The goal is to create a tool that could be used to station NYC service units in the most ideal locations to reduce response time and maximize unit placement efficiency. Broken down by NYC police precinct and providing a general overview of the entire NYC region, this project will be able to create a heat map to demonstrate 911 call hot spots.

### 1.1 - Problem Area
When 911 calls come in, they can vary in importance and urgency. However, when a serious call is made, it is the goal of 911 operators to efficiently assign the closest responder to the situation. It can sometimes be a challenge to coordinate and ensure assets are allocated in the appropriate region to assure minimum response time. By using a trained algorithm, this project could cut down on response time and alleviate stress on already overworked 911 responders by ensuring the correct unit is always in the most optimal area for any given hour of any given day.

### 1.2 - Those affected
The directly affected parties are those who would use this every day to assign service vehicle locations. However, the greater community would see the effect of this algorithm through increased response time, potentially leading to saved lives in cases where urgency is the top priority.

### 1.3 - Data Science Solution
I'm not 100% sure on the models to use here. My main idea is to create a grid of latitude and longitude within NYC bounds (excluding rivers or waterways) and calculate the probability of a call originating from that location at any given day and time. The second model could be used as a broader scale allocation tool to try to predict the number of calls within each NYC precinct region to assess at what day and time resources should be more efficiently assigned.

### 1.4 - Impact of Solution
According to this [article](https://patch.com/new-york/new-york-city/nypds-slow-response-times-keep-growing-longer-data-shows) by Matt Troutman on 2/2/2024, NYC response times have been increasing, with an average police response time of 16 minutes. Even if this tool could help reduce this amount of time by a fraction, the impact could lead to saved lives. For me, the cost of a life is immeasurable and thus gives me great motivation to create a successful predictive model.


### 1.5 - Dataset
For access to the dataset used in this project visit:<br> 
https://data.cityofnewyork.us/Public-Safety/NYPD-Calls-for-Service-Year-to-Date-/n2zq-pubd/about_data<br><br>
If you would like to follow along with this project you will need to be careful to change the path when initializing the dataframe at the begining of each notebook. <br><br>
<img src=".\misc\initdf1.png" height="400">
<img src=".\misc\initdf2.png" height="400"><br>
This data set was provided from NYC Open Data, a relatively clean data set that is up to date and large enough to create an insightful resources.
A future iteration could pull the latest dataset from NYC Open Data's website so the infroming dataset is alwasy populated with the most recent call entries.


## 2 - Project Organization
This project will be broken down in 2 main ways. First, this project was created during the course of the BrainStation DataScience Bootcamp, we had 3 sprint to finish the project and I want to preserve the stage of each sprint. For that reason the folder will be broken down into sprint 1-3, and a final finish project folder. If you wish to skip to the completed work look no further then the finish project folder, however, if you would like to see the process of how this project was created over the span of the bootcamp you can compare each sprint to one another.
Secondly, As to avoid creating one massive notebook that contains all the work done I have broken the processing into smaller notebooks.
1. `api_requesting` - This notebook starts the project off and walks through how to collect all the data needed for this project. This will also be helpful for returning back to and re-pulling the data off NYC open data's website when the update the information to help create more accurate predictions for the future.
2. `basic_EDA` / `EDA` - This notebook acts as the first look and data exploration stage. In this notebook first we clean the data and currently at the time of writing this readme reduce the working file size from ~12GB to ~1.5GB. Along with smarter datatype picking it also removes redundant information and null values. In the data exploration stages it looks at the distribution of 911 calls by different metrics within the data as well as looking at the deviation from the mean to start the timeseries modeling and exploration of this project.
3. `modeling` - This note is the notebook for modeling. Here the project will set up a summarize hourly timeseries database broken into different locational granularities (Burrow, Precinct and lat/lon). The end product of this model will be a function that allows us to pass in a locational timeseries database populated with number of calls per of and output a forecast of how many calls each location will receive per hour. This will then be feed into a visualization tool to create a heatmap of the forecasted number of calls by location.
