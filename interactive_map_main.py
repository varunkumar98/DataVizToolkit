"""
Main file of Interactive Map module
"""

import pandas as pd
from dataviztoolkit.interactive_map import InteractiveMap

from google.colab import files
uploaded = files.upload()

# Load your dataset
df = pd.read_csv('Netflix TV Shows and Movies.csv')

# Aggregate data by release year
average_scores_by_year = df.groupby('release_year')['imdb_score'].mean().reset_index()

# Create an instance of TimeSeriesChart
time_series_chart = InteractiveMap.TimeSeriesChart()

# Plot the time series data
time_series_chart.plot_time_series(
    data=average_scores_by_year, 
    x_axis='release_year', 
    y_axis='imdb_score', 
    title='Average IMDb Score of Netflix Shows and Movies Over Time'
)
          
# Create an instance of PieChart
pie_chart = InteractiveMap.PieChart()

# Assuming you have a column 'type' in your dataset with values like 'Movie' and 'TV Show'
pie_chart.plot_pie_chart(data=df, names_column='type', values_column='imdb_score', title='Distribution of Content Types on Netflix')

#Creating an Area Chart
#Aggregating data by release year from dataset
yearly_count = df.groupby('release_year').size().reset_index(name='count')
#calculating the cummulative sum
yearly_count['cummulative_count']=yearly_count['count'].cumsum()

#Creating an instance of AreaChart
area_chart = InteractiveMap.AreaChart()

#Creating an area chart
area_chart.plot_area_chart(data=yearly_count, x_axis='release_year', y_axis='cummulative_count', title = 'Cummulative Content on Netflix over Time')
