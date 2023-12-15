# DataVizToolkit
In the package, there are 3 modules. They are Chart Builder, Interactive Map, and Custom Themes.
I have created a main directory - dataviztoolkit. Then, in the subdirectory, I added Project code directory to include the main files for visualizations.

#__init__.py
# Import the ChartBuilder class from the dataviztoolkit.chart_builder module.
from dataviztoolkit.chart_builder import ChartBuilder

# Import the InteractiveMap class from the dataviztoolkit.interactive_map module.
from dataviztoolkit.interactive_map import InteractiveMap

# Import the CustomThemes class from the dataviztoolkit.custom_themes module.
from dataviztoolkit.custom_themes import CustomThemes

#chart_builder.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import Normalize

# Define a class named ChartBuilder for creating different types of charts.
class ChartBuilder:
    # Define a nested class named BarChart for creating bar charts.
    class BarChart:
        # Define a method to create a bar chart.
        def create_bar_chart(self, data, x_axis, y_axis):
            """
            Create a Bar Chart.

            Parameters:
                - data: Dictionary or DataFrame containing the data.
                - x_axis: Name of the column for the x-axis.
                - y_axis: Name of the column for the y-axis.
            """
            # Check if the input data is a valid type (dictionary or DataFrame).
            if not isinstance(data, (dict, pd.DataFrame)):
                raise ValueError("Invalid Data Format. Use a Dictionary or DataFrame.")

            # Convert dictionary to a DataFrame if the input is a dictionary.
            if isinstance(data, dict):
                df = pd.DataFrame(data)
            else:
                df = data

            # Extract x and y values from the DataFrame.
            x_values = df[x_axis].values
            y_values = df[y_axis].values

            plt.bar(x_values, y_values, color=self.custom_colors(len(x_values)))
            plt.xlabel(x_axis)
            plt.ylabel(y_axis)
            plt.title("Bar Chart")
            plt.show()

        # Define a method to generate custom colors.
        def custom_colors(self, num_colors):
            """
            Customize colors based on the provided palette.

            Parameters:
                - num_colors: Number of colors to generate.

            Returns:
                - List of colors.
            """
            num_colors_str = input("Enter the number of colors: ")
            try:
                num_colors = int(num_colors_str)
            except ValueError:
                print("Invalid input. Please enter an integer.")

            # Generate a list of colors using a colormap.
            norm = Normalize(vmin=0, vmax=num_colors - 1)
            color_map = plt.get_cmap("viridis")

            return [color_map(norm(i)) for i in range(num_colors)]

    # Define a nested class named HeatMap for creating heat maps.
    class HeatMap:
        # Define a method to create a heat map.
        def create_heat_map(self, data, title):
            """
            Create a Heat Map.

            Parameters:
                - data: DataFrame containing the data for the heat map.
                - title: Title of the heat map.
            """
            # Check if the input data is a pandas DataFrame.
            if not isinstance(data, pd.DataFrame):
                raise ValueError("Data must be a pandas DataFrame.")

            plt.figure(figsize=(10, 8))
            sns.heatmap(data.corr(), annot=True, cmap='viridis')
            plt.title(title)
            plt.show()

    # Define a nested class named BoxPlot for creating box plots.
    class BoxPlot:
        # Define a method to create a box plot.
        def create_box_plot(self, data, column, title):
            """
            Create a Box Plot.

            Parameters:
                - data: DataFrame containing the data.
                - column: Name of the column for which to create the box plot.
                - title: Title of the box plot.
            """
            # Check if the input data is a pandas DataFrame.
            if not isinstance(data, pd.DataFrame):
                raise ValueError("Data must be a pandas DataFrame.")
            
            plt.figure(figsize=(10, 6))
            plt.boxplot(data[column].dropna())  # Drop NA values for plotting
            plt.title(title)
            plt.ylabel(column)
            plt.show()

#chart_builder_main.py
from dataviztoolkit import ChartBuilder
import pandas as pd

from google.colab import files
uploaded = files.upload()

# Importing the dataset
df_chart = pd.read_csv('Netflix TV Shows and Movies.csv')

# Create an instance of the BarChart class from the ChartBuilder.
chart = ChartBuilder.BarChart()

# Generate a bar chart using imdb_score and imdb_votes
chart.create_bar_chart(df_chart.head(10), x_axis='imdb_score', y_axis='imdb_votes')

# Generate custom colors for the bar chart.
chart.custom_colors('viridis')

# Create an instance of the HeatMap class from the ChartBuilder.
heat_map = ChartBuilder.HeatMap()

# Generate a heat map using the DataFrame
heat_map.create_heat_map(df_chart, title='Correlation Heat Map of Netflix Dataset')

# Create an instance of the BoxPlot class from the ChartBuilder.
box_plot = ChartBuilder.BoxPlot()

# Generate a box plot for 'imdb_score'
box_plot.create_box_plot(df_chart, column='imdb_score', title='IMDb Score Distribution on Netflix')
<img width="603" alt="Screenshot 2023-12-09 at 10 49 33 PM" src="https://github.com/varunkumar98/DataVizToolkit/assets/45570174/b8afd4fe-2ac5-4d37-b8c5-15f4ae5858e8">

<img width="751" alt="Screenshot 2023-12-09 at 10 45 53 PM" src="https://github.com/varunkumar98/DataVizToolkit/assets/45570174/9ce41fcc-6d71-4fe1-8e85-54ba2ce56c84">
<img width="766" alt="Screenshot 2023-12-09 at 10 48 36 PM" src="https://github.com/varunkumar98/DataVizToolkit/assets/45570174/017c7a50-0ba6-4f4c-8b35-00d5a01aa1d0">

##interactive_map.py
import pandas as pd
import plotly.express as px

# Define a class named InteractiveMap for creating different types of interactive charts.
class InteractiveMap:
    # Define a nested class named TimeSeriesChart for creating time series charts.
    class TimeSeriesChart:
        # Define a method to plot time series data.
        def plot_time_series(self, data, x_axis, y_axis, title):
            """
            Plot time series data.

            Parameters:
              - data: DataFrame containing the time series data.
              - x_axis: Name of the column for the x-axis (time).
              - y_axis: Name of the column for the y-axis (values).
              - title: Title of the chart.
            """
            # Check if the input data is a DataFrame.
            if not isinstance(data, pd.DataFrame):
                raise ValueError("Invalid data format. Use a DataFrame.")

            # Create a line chart using Plotly Express with the specified parameters.
            fig = px.line(data, x=x_axis, y=y_axis, title=title)

            # Display the chart.
            fig.show()

    # Define a nested class named PieChart for creating pie charts.
    class PieChart:
        # Define a method to plot a pie chart.
        def plot_pie_chart(self, data, names_column, values_column, title):
            """
            Create a pie chart.

            Parameters:
              - data: DataFrame containing the data.
              - names_column: Name of the column to be used as labels.
              - values_column: Name of the column to be used for values.
              - title: Title of the pie chart.
            """
            # Check if the input data is a DataFrame.
            if not isinstance(data, pd.DataFrame):
                raise ValueError("Invalid data format. Use a DataFrame.")

            # Create a pie chart using Plotly Express with the specified parameters.
            fig = px.pie(data, names=names_column, values=values_column, title=title)

            # Display the chart.
            fig.show()

    # Define a nested class named AreaChart for creating area charts.
    class AreaChart:
        # Define a method to plot an area chart.
        def plot_area_chart(self, data, x_axis, y_axis, title):
            """
            Plotting an Area Chart

            Parameters:
              - data: DataFrame containing the data.
              - x_axis: Name of the column for the x-axis.
              - y_axis: Name of the column for the y-axis.
              - title: Title of the Area Chart.
            """
            # Check if the input data is a DataFrame.
            if not isinstance(data, pd.DataFrame):
                raise ValueError("Invalid data format. Use a DataFrame.")
            
            # Create an area chart using Plotly Express with the specified parameters.
            fig = px.area(data, x=x_axis, y=y_axis, title=title)

            # Display the chart.
            fig.show()

##interactive_map_main.py
import pandas as pd
import seaborn as sns
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

#Creating an Area Chart
#Aggregating data by release year from dataset
yearly_count = df.groupby('release_year').size().reset_index(name='count')
#calculating the cummulative sum
yearly_count['cummulative_count']=yearly_count['count'].cumsum()

#Creating an instance of AreaChart
area_chart = InteractiveMap.AreaChart()

#Creating an area chart
area_chart.plot_area_chart(data=yearly_count, x_axis='release_year', y_axis='cummulative_count', title = 'Cummulative Content on Netflix over Time')

# Create an instance of PieChart
pie_chart = InteractiveMap.PieChart()

# Assuming you have a column 'type' in your dataset with values like 'Movie' and 'TV Show'
pie_chart.plot_pie_chart(df, names_column='type', values_column='imdb_score', title='Distribution of Movies and shows on Netflix')
<img width="678" alt="Screenshot 2023-12-09 at 10 44 26 PM" src="https://github.com/varunkumar98/DataVizToolkit/assets/45570174/647c27c1-b7c9-4170-9a33-72ed5451b931">

<img width="691" alt="Screenshot 2023-12-09 at 10 44 48 PM" src="https://github.com/varunkumar98/DataVizToolkit/assets/45570174/d2cafa15-649a-4f2d-aeb0-65f5e35e403d">

<img width="724" alt="Screenshot 2023-12-09 at 10 45 15 PM" src="https://github.com/varunkumar98/DataVizToolkit/assets/45570174/89cb8d35-30c8-4cd7-ae71-cd3da4dbbaa4">

##custom_themes.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define a class named CustomThemes for managing custom themes.
class CustomThemes:
    # Define an inner class ThemeBuilder for creating custom themes.
    class ThemeBuilder:
        # Define a method create_theme for creating a custom theme.
        def create_theme(self, theme_name, color_scheme, font_style):
            """
            Create a custom theme for visualizations.

            Parameters:
                - theme_name: Name of the custom theme.
                - color_scheme: String representing the color scheme (e.g., 'light', 'dark').
                - font_style: String representing the font style (e.g., 'sans-serif', 'serif').

            Returns:
                - Dictionary containing theme properties.
            """

            # Initialize a dictionary to store theme properties.
            theme_properties = {
                'name': theme_name,  # Set the theme name.
                'color_scheme': color_scheme,  # Set the color scheme.
                'font_style': font_style,  # Set the font style.
                'font_size': 12,  # Default font size.
                'font_family': 'sans-serif' if font_style == 'sans-serif' else 'Times New Roman',  # Choose font family based on font_style.
                'background_color': '#f2f2f2' if color_scheme == 'light' else '#333333',  # Set background color based on color_scheme.
                'plot_color_palette': 'deep'  # Default plot color palette.
            }

            # Return the dictionary containing theme properties.
            return theme_properties

##custom_themes_main.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataviztoolkit.custom_themes import CustomThemes

from google.colab import files
uploaded = files.upload()

# Load your dataset
df = pd.read_csv('Netflix TV Shows and Movies.csv')

# Filter to include only movies and group by 'release_year'
movies_per_year = df[df['type'] == 'MOVIE'].groupby('release_year').size()

# Sort the count in decreasing order
movies_per_year_sorted = movies_per_year.sort_values(ascending=False)

# Create an instance of ThemeBuilder and create a theme
theme_builder = CustomThemes.ThemeBuilder()
my_theme = theme_builder.create_theme('MyCustomTheme', 'light', 'sans-serif')

# Apply the custom theme to a plot
plt.rcParams['font.size'] = my_theme['font_size']
plt.rcParams['font.family'] = my_theme['font_family']
plt.rcParams['figure.facecolor'] = my_theme['background_color']

# Create a figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# Histogram of 'imdb_score'
ax1.hist(df['imdb_score'], color='#007bff', bins=20, edgecolor='black')
ax1.set_title('Distribution of IMDb Scores')
ax1.set_xlabel('IMDb Score')
ax1.set_ylabel('Frequency')

# Scatter plot of 'imdb_score' vs 'imdb_votes'
ax2.scatter(df['imdb_score'], df['imdb_votes'], color='#ff7f0e', edgecolor='black')
ax2.set_title('IMDb Score vs. Votes on Netflix Content')
ax2.set_xlabel('IMDb Score')
ax2.set_ylabel('Number of IMDb Votes')
ax2.grid(True)

# Bar plot 
if not movies_per_year_sorted.empty:
    bar_color = sns.color_palette('deep', len(movies_per_year_sorted)) 

    # Plotting the bar plot
    ax3.bar(movies_per_year_sorted.index, movies_per_year_sorted.values, color=bar_color)
    ax3.set_title('Number of Movies Released Each Year on Netflix')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Number of Movies')
    ax3.tick_params(axis='x', rotation=45)
else:
    print("No data available for bar plot")

# Adjust layout
plt.tight_layout()
plt.show()

<img width="1041" alt="Screenshot 2023-12-09 at 10 17 40 PM" src="https://github.com/varunkumar98/DataVizToolkit/assets/45570174/056b6d77-8646-4a19-b46f-5ef30bd6b799">
