"""
Classes and functions of InteractiveMap modules is provided in this python files. 
"""

import pandas as pd
import plotly.express as px

class InteractiveMap:
    class TimeSeriesChart:
        def plot_time_series(self, data, x_axis, y_axis, title):
            """
            Plot time series data.

            Parameters:
              - data: DataFrame containing the time series data.
              - x_axis: Name of the column for the x-axis (time).
              - y_axis: Name of the column for the y-axis (values).
              - title: Title of the chart.
            """
            #Check if the data is a DataFrame, raise an error if not
            if not isinstance(data, pd.DataFrame):
                raise ValueError("Invalid data format. Use a DataFrame.")

            #create line plot
            fig = px.line(data, x=x_axis, y=y_axis, title=title)
            fig.show()
    class PieChart:
        def plot_pie_chart(self, data, names_column, values_column, title):
            """
            Create a pie chart.

            Parameters:
              - data: DataFrame containing the data.
              - names_column: Name of the column to be used as labels.
              - values_column: Name of the column to be used for values.
              - title: Title of the pie chart.
            """
            #check if the data is a dataframe, raise an error if not
            if not isinstance(data, pd.DataFrame):
                raise ValueError("Invalid data format. Use a DataFrame.")
            
            #create a pie chart
            fig = px.pie(data, names=names_column, values=values_column, title=title)
            fig.show()
    class AreaChart:
      def plot_area_chart(self, data, x_axis, y_axis, title):
            """
            Plotting a Area Chart

            Parameters:
              - data: DataFrame containing the data.
              - x_axis: Name of the column for the x-axis
              - y_axis: Name of the column for the y_axis
              - title: Title of the Area Chart
            """
            #validate that the data is a dataframe, raise an error if not
            if not isinstance(data, pd.DataFrame):
              raise ValueError("Invalid data format. Use a DataFrame.")
            #create a area plot
            fig = px.area(data, x=x_axis, y=y_axis, title=title)
            fig.show()
