# 1. Import the necessary libraries
import pandas as pd
import plotly.express as px
import os

# 2. Define the path to your dataset
file_path = r'user: enter path of file' 

# 3. Load the data using pandas
print("Loading the dataset...")
df = pd.read_csv(file_path, parse_dates=['date'])

# 4. Create the interactive line plot
print("Generating interactive plot object...")
fig = px.line(
    df,
    x='date',
    y='whatever quantity you are measuring',
    labels={'user: enter legend labels'} # This sets the name that appears in the legend
)

# 5. Customize the plot to match your image
fig.update_layout(
    xaxis_title='user: enter',
    yaxis_title='user: enter',
    legend_title_text='', # Hides the legend title
    title='user; enter' # Optional: Adds a title
)

# This part formats the x-axis to show monthly ticks like '2016/07'
fig.update_xaxes(
    dtick="M1", # Sets the tick interval to one month
    tickformat="%Y/%m", # Sets the format of the tick label
    tickangle=-45 # Rotates the labels for better readability
)


# 6. Define the output path and save the file
output_dir = 'user: if you want to save somewhere else'
os.makedirs(output_dir, exist_ok=True)
output_filename = 'monthly_view_plot.html'
# full_path = os.path.join(output_dir, output_filename)

fig.write_html(output_filename)

# print(f"✅ Plot saved successfully to: '{full_path}'")
print(f"✅ Plot saved successfully to")