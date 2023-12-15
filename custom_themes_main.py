"""
Main file of Custom Themes module - The functionality of this module is to personalize the look and feel of the graphs along with its extensive
customization features makes it flexible and user-friendly.
"""

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

# Histogram of 'imdb_score' in the first subplot
ax1.hist(df['imdb_score'], color='#007bff', bins=20)
ax1.set_title('Distribution of IMDb Scores')
ax1.set_xlabel('IMDb Score')
ax1.set_ylabel('Frequency')

# Scatter plot of 'imdb_score' vs 'imdb_votes' in the second subplot
ax2.scatter(df['imdb_score'], df['imdb_votes'], color='#ff7f0e')
ax2.set_title('IMDb Score vs. Votes on Netflix Content')
ax2.set_xlabel('IMDb Score')
ax2.set_ylabel('Number of IMDb Votes')
ax2.grid(True)

# Bar plot 
# Checking if movies_per_year_sorted is not empty
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
