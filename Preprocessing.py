
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


data=pd.read_csv("traffic.csv")
data.head()


data['DateTime'] = pd.to_datetime(data['DateTime'])

# Extract and assign components of the datetime to new columns
data['Year'] = data['DateTime'].dt.year
data['Month'] = data['DateTime'].dt.month
data['DayOfMonth'] = data['DateTime'].dt.day
data['Hour'] = data['DateTime'].dt.hour
data['Minute'] = data['DateTime'].dt.minute
data['Second'] = data['DateTime'].dt.second

data['WeekDay'] = data['DateTime'].dt.weekday + 1
#Monday is assigned 1, Tue 2 and so on..

data = data.drop(['ID', 'DateTime'], axis=1)
#dropped ID cause its ID and Datetime as we split Date, day, hr, second into different columns

# Display the first few rows of the dataframe to verify the changes
data.head()
