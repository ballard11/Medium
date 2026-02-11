#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


import pandas as pd
import plotly.express as px
import time

df = pd.read_csv('data/Maryland_Statewide_Vehicle_Crashes.csv')
df = df[['YEAR', 'LIGHT_DESC', 'COUNTY_DESC', 'REPORT_TYPE', 'WEATHER_DESC', 'ACC_DATE', 'ACC_TIME', 'LATITUDE', 'LONGITUDE', 'JUNCTION_DESC']]


# In[33]:


# Identify the top ten counties by crash count
top_five_counties = df['COUNTY_DESC'].value_counts().head(5).index.tolist()

# Filter the dataframe to include only the top ten counties
df_top_five = df[df['COUNTY_DESC'].isin(top_five_counties)]


# In[5]:


# Create a pivot table with REPORT_TYPE as rows and COUNTY_DESC as columns, 
# then compute the counts of each REPORT_TYPE for each county
pivot_table = df_top_five.pivot_table(index='REPORT_TYPE', columns='COUNTY_DESC', 
                                     values='YEAR', aggfunc='count')

# Convert the counts to percentages
pivot_percentage = pivot_table.div(pivot_table.sum(axis=0), axis=1)*100

# Display the resulting pivot table with percentages
pivot_table.T


# In[6]:


pivot_percentage.T


# ## TimeSeries Trend

# In[16]:


# Convert ACC_DATE to datetime format
df['ACC_DATE'] = pd.to_datetime(df['ACC_DATE'], format='%y-%m-%d')

# Combine ACC_DATE and ACC_TIME into a single datetime column
df['ACC_DATETIME'] = pd.to_datetime(df['ACC_DATE'].astype(str) + ' ' + df['ACC_TIME'].astype(str).str[-8:])

# Extract hour and month from ACC_DATETIME
df['HOUR'] = df['ACC_DATETIME'].dt.hour
df['MONTH'] = df['ACC_DATETIME'].dt.month

# Create a new DataFrame with daily accident counts for each county
daily_counts = df.groupby(['ACC_DATE', 'COUNTY_DESC']).size().reset_index()
daily_counts.columns = ['ACC_DATE', 'COUNTY_DESC', 'COUNT']

# Apply a 30-day rolling average to the COUNT column for each county
daily_counts['SMOOTHED_COUNT'] = daily_counts.groupby('COUNTY_DESC')['COUNT'].transform(lambda x: x.rolling(30, min_periods=1).mean())

# Create the line plot using the smoothed data
fig = px.line(daily_counts[daily_counts['COUNTY_DESC'].isin(top_five_counties)], x='ACC_DATE', y='SMOOTHED_COUNT', color='COUNTY_DESC', title='30-Day Smoothed Trend in Crashes')

# Show the plot
fig.show()


# In[18]:


# Filter the data to include only rows from the top_five_counties
filtered_counts = daily_counts[daily_counts['COUNTY_DESC'].isin(top_five_counties)]

# Split the data into two subsets: before and after March 1, 2020
before_covid = filtered_counts[filtered_counts['ACC_DATE'] < '2020-03-01']
after_covid = filtered_counts[filtered_counts['ACC_DATE'] >= '2020-03-01']

# Calculate the average crashes per day for each county for the two time periods
avg_before_covid = before_covid.groupby('COUNTY_DESC')['COUNT'].mean().reset_index()
avg_after_covid = after_covid.groupby('COUNTY_DESC')['COUNT'].mean().reset_index()

# Merge the results to create a combined DataFrame
merged = avg_before_covid.merge(avg_after_covid, on='COUNTY_DESC', suffixes=('_PRE', '_POST'))

# Calculate the percent difference
merged['PERCENT_DIFF'] = ((merged['COUNT_POST'] - merged['COUNT_PRE']) / merged['COUNT_PRE']) * 100

# Rename the columns for clarity
merged.columns = ['COUNTY_DESC', 'Avg Crashes/Day (Pre-Covid)', 'Avg Crashes/Day (Post-Covid)', 'Percent Difference']

merged


# ## Fatal Crashes

# In[28]:


# Filter the data for fatal crashes
df_Fatal = df[df['REPORT_TYPE'] == 'Fatal Crash']

# Extract year from ACC_DATETIME for monthly aggregation
df_Fatal['YEAR'] = df_Fatal['ACC_DATETIME'].dt.year

# Create a new DataFrame with monthly fatal accident counts for each county
monthly_fatal_counts = df_Fatal.groupby(['YEAR', 'MONTH', 'COUNTY_DESC']).size().reset_index()
monthly_fatal_counts.columns = ['YEAR', 'MONTH', 'COUNTY_DESC', 'COUNT']

# Apply a 3-month rolling average to the COUNT column for each county
monthly_fatal_counts['SMOOTHED_COUNT'] = monthly_fatal_counts.groupby('COUNTY_DESC')['COUNT'].transform(lambda x: x.rolling(3, min_periods=1).mean())

# Create a new column for plotting purposes: "YEAR-MONTH"
monthly_fatal_counts['YEAR_MONTH'] = monthly_fatal_counts['YEAR'].astype(str) + '-' + monthly_fatal_counts['MONTH'].astype(str).str.zfill(2)

# Create the line plot using the smoothed data
fig = px.line(monthly_fatal_counts[monthly_fatal_counts['COUNTY_DESC'].isin(top_five_counties)], x='YEAR_MONTH', y='SMOOTHED_COUNT', color='COUNTY_DESC', title='3-Month Smoothed Trend in Fatal Crashes')

# Show the plot
fig.show()


# In[31]:


# Filter the data to include only rows from the top_five_counties
filtered_fatal_counts = monthly_fatal_counts[monthly_fatal_counts['COUNTY_DESC'].isin(top_five_counties)]

# Create a 'MONTH_YEAR' column for easier filtering
filtered_fatal_counts['MONTH_YEAR'] = pd.to_datetime(filtered_fatal_counts['YEAR'].astype(str) + '-' + filtered_fatal_counts['MONTH'].astype(str) + '-01')

# Split the data into two subsets: before and after March 1, 2020
before_covid_fatal = filtered_fatal_counts[filtered_fatal_counts['MONTH_YEAR'] < '2020-03-01']
after_covid_fatal = filtered_fatal_counts[filtered_fatal_counts['MONTH_YEAR'] >= '2020-03-01']

# Calculate the average fatal crashes per month for each county for the two time periods
avg_before_covid_fatal = before_covid_fatal.groupby('COUNTY_DESC')['COUNT'].mean().reset_index()
avg_after_covid_fatal = after_covid_fatal.groupby('COUNTY_DESC')['COUNT'].mean().reset_index()

# Merge the results to create a combined DataFrame
merged_fatal = avg_before_covid_fatal.merge(avg_after_covid_fatal, on='COUNTY_DESC', suffixes=('_PRE', '_POST'))

# Calculate the percent difference
merged_fatal['PERCENT_DIFF'] = ((merged_fatal['COUNT_POST'] - merged_fatal['COUNT_PRE']) / merged_fatal['COUNT_PRE']) * 100

# Rename the columns for clarity
merged_fatal.columns = ['COUNTY_DESC', 'Avg Fatal Crashes/Month (Pre-Covid)', 'Avg Fatal Crashes/Month (Post-Covid)', 'Percent Difference']

merged_fatal


# In[ ]:




