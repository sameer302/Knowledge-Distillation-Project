# 1. Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read your CSV, with correct date conversion
df = pd.read_csv('ETTm1.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

plt.figure(figsize=(14,6))
plt.plot(df['date'], df['OT'], color='blue', linewidth=2, label='Oil Temperature')
plt.xlabel('Month')
plt.ylabel('Oil Temperature')
plt.title('ETTm1 - Oil Temperature Over Time')
plt.legend()

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m'))

plt.xticks(rotation=45)
plt.tight_layout()

# Save as PNG (best for GitHub preview)
plt.savefig('monthly_view_plot.png', dpi=150)
