"""
Main file of Chart Builder - This module is mainly used to create charts and along with its customization features makes it ease of use to 
non-technical users. 
"""

from dataviztoolkit import ChartBuilder
import pandas as pd

from google.colab import files
uploaded = files.upload()

# Create a bar chart
df_chart = pd.read_csv('Netflix TV Shows and Movies.csv') 

#create bar chart object using a ChartBuilder class
chart = ChartBuilder.BarChart()

#creating a bar chart
chart.create_bar_chart(df_chart.head(10), x_axis='imdb_score', y_axis='imdb_votes')

#customizing the colors of the map with the help of 'viridis' color scheme
chart.custom_colors('viridis')

# Create an instance of BoxPlot
box_plot = ChartBuilder.BoxPlot()

# Generate a box plot for a specific column
# Replace 'imdb_score' with the column you wish to visualize
box_plot.create_box_plot(df_chart, column='imdb_score', title='IMDb Score Distribution on Netflix')

# Create an instance of HeatMap
heat_map = ChartBuilder.HeatMap()

# Generate a heat map
heat_map.create_heat_map(df_chart, title='Correlation Heat Map of Netflix Dataset')
