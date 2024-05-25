# 911 Hotspot Predictor
Author: Connell Phillipps <br><br>


## Project Overview
The goal of this project is to highlight and demonstrate the skills learned through BratinStations Data Science bootcamp. In this project, I aim to use data provided by NYC Open Data to create a predictive algorithm to show 911 call hot spots. The goal is to create a tool that could be used to station NYC service units in the most ideal locations to reduce response time and maximize unit placement efficiency. Broken down by NYC police precinct and providing a general overview of the entire NYC region, this project will be able to create a heat map to demonstrate 911 call hot spots.

### Problem Area
When 911 calls come in, they can vary in importance and urgency. However, when a serious call is made, it is the goal of 911 operators to efficiently assign the closest responder to the situation. It can sometimes be a challenge to coordinate and ensure assets are allocated in the appropriate region to assure minimum response time. By using a trained algorithm, this project could cut down on response time and alleviate stress on already overworked 911 responders by ensuring the correct unit is always in the most optimal area for any given hour of any given day.

### Those affected
The directly affected parties are those who would use this every day to assign service vehicle locations. However, the greater community would see the effect of this algorithm through increased response time, potentially leading to saved lives in cases where urgency is the top priority.

### Data Science Solution
I'm not 100% sure on the models to use here. My main idea is to create a grid of latitude and longitude within NYC bounds (excluding rivers or waterways) and calculate the probability of a call originating from that location at any given day and time. The second model could be used as a broader scale allocation tool to try to predict the number of calls within each NYC precinct region to assess at what day and time resources should be more efficiently assigned.

### Impact of Solution
According to this [article](https://patch.com/new-york/new-york-city/nypds-slow-response-times-keep-growing-longer-data-shows) by Matt Troutman on 2/2/2024, NYC response times have been increasing, with an average police response time of 16 minutes. Even if this tool could help reduce this amount of time by a fraction, the impact could lead to saved lives. For me, the cost of a life is immeasurable and thus gives me great motivation to create a successful predictive model.


### Dataset
For acess to the dataset used in this project visit:<br> 
https://data.cityofnewyork.us/Public-Safety/NYPD-Calls-for-Service-Year-to-Date-/n2zq-pubd/about_data<br><br>
If you would like to follow along with this project you will need to be careful to change the path when initilizing the dataframe at the begining of each notebook. <br><br>
<img src=".\misc\initdf1.png" height="400">
<img src=".\misc\initdf2.png" height="400"><br>
This data set was provied from NYC Open Data, a realatively clean data set that is up to date and large enough to create an insightful resoureces.
A future iteration could pull the latest dataset from NYC Open Datas website so the infroming dataset is alwasy populated with the most recent call entries.