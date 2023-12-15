# -*- coding: utf-8 -*-
"""Final_Project_ITP-DS.py

The primary purpose of this Python file is to run every module included in the dataviztoolkit package. 
We used the pip command to install the plotly and matplotlib libraries. I have arranged all of my project's main files into a subdirectory 
called "Project Code". We can run the InteractiveMap, ChartBuilder, and CustomThemes modules to see the results of the several visualizations 
that we have worked on for this project by using the %run command. 

Original file is located at
    https://colab.research.google.com/drive/1Ddoe_vUfFhuyBAtQYTckpOOzagosUunC
"""

# Install the matplotlib library using pip.
pip install matplotlib

#install the plotly library using pip
pip install plotly

#create a directory - dataviztoolkit
!mkdir dataviztoolkit

# Create an empty __init__.py file in the dataviztoolkit directory
!touch dataviztoolkit/__init__.py

# Create a Python script file named chart_builder.py in the dataviztoolkit directory
!touch dataviztoolkit/chart_builder.py

# Create a Python script file named interactive_map.py in the dataviztoolkit directory
!touch dataviztoolkit/interactive_map.py

# Create a Python script file named custom_themes.py in the dataviztoolkit directory
!touch dataviztoolkit/custom_themes.py

# Create a subdirectory named Project_code inside the dataviztoolkit directory
!mkdir dataviztoolkit/Project_code

# Create a Python script file named chart_builder_main.py inside the Project_code subdirectory
!touch dataviztoolkit/Project_code/chart_builder_main.py

# Create a Python script file named interactive_map_main.py inside the Project_code subdirectory
!touch dataviztoolkit/Project_code/interactive_map_main.py

# Create a Python script file named custom_themes_main.py inside the Project_code subdirectory
!touch dataviztoolkit/Project_code/custom_themes_main.py

# Execute the chart_builder_main.py script located in the Project_code subdirectory
 %run dataviztoolkit/Project_code/chart_builder_main.py

# Execute the interactive_map_main.py script located in the Project_code subdirectory
 %run dataviztoolkit/Project_code/interactive_map_main.py

# Execute the custom_themes_main.py script located in the Project_code subdirectory
 %run dataviztoolkit/Project_code/custom_themes_main.py

