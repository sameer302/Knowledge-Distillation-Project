# 1. Import the necessary libraries
import pandas as pd
import plotly.express as px
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# # 2. Define the path to your dataset
# file_path = 'ETTh1.csv'

# # 3. Load the data using pandas
# print("Loading the dataset...")
# df = pd.read_csv(file_path)
# df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y %H:%M')


# # 4. Create the interactive line plot
# print("Generating interactive plot object...")
# fig = px.line(
#     df,
#     x='date',
#     y='OT',
#     labels={'OT': 'Oil Temperature'} # This sets the name that appears in the legend
# )

# # 5. Customize the plot to match your image
# fig.update_layout(
#     xaxis_title='Month',
#     yaxis_title='Oil Temperature',
#     legend_title_text='', # Hides the legend title
#     title='ETTh1 - Oil Temperature Over Time' # Optional: Adds a title
# )

# # This part formats the x-axis to show monthly ticks like '2016/07'
# fig.update_xaxes(
#     dtick="M1", # Sets the tick interval to one month
#     tickformat="%Y/%m", # Sets the format of the tick label
#     tickangle=-45 # Rotates the labels for better readability
# )


# # 6. Define the output path and save the file
# # output_dir = 'user: if you want to save somewhere else'
# # os.makedirs(output_dir, exist_ok=True)
# output_filename = 'monthly_view_plot.html'
# # full_path = os.path.join(output_dir, output_filename)

# fig.write_html(output_filename)

# # print(f"✅ Plot saved successfully to: '{full_path}'")
# print(f"✅ Plot saved successfully ")

# import pandas as pd
# import matplotlib.pyplot as plt

# Read your CSV, with correct date conversion
df = pd.read_csv('ETTh1.csv')
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y %H:%M')

plt.figure(figsize=(14,6))
plt.plot(df['date'], df['OT'], color='blue', linewidth=2, label='Oil Temperature')
plt.xlabel('Month')
plt.ylabel('Oil Temperature')
plt.title('ETTh1 - Oil Temperature Over Time')
plt.legend()

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m'))

plt.xticks(rotation=45)
plt.tight_layout()

# Save as PNG (best for GitHub preview)
plt.savefig('monthly_view_plot.png', dpi=150)
