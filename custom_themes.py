# dataviztoolkit/custom_themes.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class CustomThemes:
    class ThemeBuilder:
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
            theme_properties = {
                'name': theme_name,
                'color_scheme': color_scheme,
                'font_style': font_style,
                'font_size': 12,
                'font_family': 'sans-serif' if font_style == 'sans-serif' else 'Times New Roman',
                'background_color': '#f2f2f2' if color_scheme == 'light' else '#333333',
                'plot_color_palette': 'deep'
            }

            return theme_properties