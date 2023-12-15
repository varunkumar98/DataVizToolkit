import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import Normalize

class ChartBuilder:
    class BarChart:
        def create_bar_chart(self, data, x_axis, y_axis):
            """
            Create Bar Chart.

            Parameters:
                - data: Dictionary or DataFrame containing the data
                - x_axis: Name of the column for the x-axis.
                - y_axis: Name of the column for the y-axis.
            """
            #Check if the data is dictionary or dataframe, otherwise raise valueerror
            if not isinstance(data, (dict, pd.DataFrame)):
                raise ValueError("Invalid Data Format. Use a Dictionary or DataFrame")
            #convert dictionary to dataframe if necessary
            if isinstance(data, dict):
                df = pd.DataFrame(data)
            else:
                df = data
            #Extract x and Y values from the dataset
            x_values = df[x_axis].values
            y_values = df[y_axis].values

            #Plot the Bar Chart
            plt.bar(x_values, y_values, color=self.custom_colors(len(x_values)))
            plt.xlabel(x_axis)
            plt.ylabel(y_axis)
            plt.title("Bar Chart")
            plt.show()

        def custom_colors(self, num_colors):
            """
            Customize colors based on the provided palette

            Parameters:
                - color_palette: String representing the color palette

            Returns:
                - List of colors
            """
            num_colors_str = input("Enter the number of colors: ")
            try:
                num_colors = int(num_colors_str)
            except ValueError:
                print("Invalid input. Please enter an integer.")
            #Normalize the color range based on the number of colors
            norm = Normalize(vmin=0, vmax=num_colors - 1)
            color_map = plt.get_cmap("viridis")
            
            #Return the list of colors
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