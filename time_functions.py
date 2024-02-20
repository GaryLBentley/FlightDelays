import pandas as pd
import numpy as np
import datetime

# Time functions reused under Apache 2.0 License
# https://www.kaggle.com/code/fabiendaniel/predicting-flight-delays-tutorial
# Original author: FABIENDANIEL 
# Some code has been refactored to account for deprecations in Pandas

# Function that convert the 'HHMM' string to datetime.time
def format_hour(date_string):
    if pd.isnull(date_string):
        return np.nan
    else:
        if date_string == 2400: date_string = 0
        date_string = "{0:04d}".format(int(date_string))
        hour = datetime.time(int(date_string[0:2]), int(date_string[2:4]))
        return hour
#_____________________________________________________________________
# Function that combines a date and time to produce a datetime.datetime
def date_hour(x):
    if pd.isnull(x.iloc[0]) or pd.isnull(x.iloc[1]):
        return np.nan
    else:
        return datetime.datetime.combine(x.iloc[0],x.iloc[1])
#_______________________________________________________________________________
# Function that combine two columns of the dataframe to create a datetime format
def flight_time(df, col):    
    time_list = []
    for index, cols in df[['DATE', col]].iterrows():    
        if pd.isnull(cols.iloc[1]):
            time_list.append(np.nan)
        elif float(cols.iloc[1]) == 2400:
            cols.iloc[0] += datetime.timedelta(days=1)
            cols.iloc[1] = datetime.time(0,0)
            time_list.append(date_hour(cols))
        else:
            cols.iloc[1] = format_hour(cols.iloc[1])
            time_list.append(date_hour(cols))
    return pd.Series(time_list)