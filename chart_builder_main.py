"""
Main file of Chart Builder
"""

from dataviztoolkit import ChartBuilder
import pandas as pd

from google.colab import files
uploaded = files.upload()

# Create a bar chart
df_chart = pd.read_csv('Netflix TV Shows and Movies.csv') 
chart = ChartBuilder.BarChart()
chart.create_bar_chart(df_chart.head(10), x_axis='imdb_score', y_axis='imdb_votes')
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
