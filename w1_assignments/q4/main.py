# 4)Temperature Line Chart
# Topics: Line Plot, Markers, Grid, Pyplot
# Problem:
# Given temperatures recorded over 7 days: [28, 30, 29, 31, 32, 33, 34]
# Plot a line graph showing the temperature trend with:
# Circular markers
# Line width 2
# Title: “Weekly Temperature Trend”
# Labeled axes
# Grid enabled

tempRecord = [28, 30, 29, 31, 32, 33, 34]
days = [1, 2, 3, 4, 5, 6, 7]

import numpy as np
days = np.array(days)
tempRecord = np.array(tempRecord)

import matplotlib.pyplot as plt
plt.plot(days, tempRecord, 'or', linewidth=2)
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.grid(color='green', linestyle='-', linewidth=0.5, alpha=0.5)
plt.title('Weekly Temperature Trend')

plt.show()

plt.bar(days, tempRecord)
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.grid(color='green', linestyle='-', linewidth=0.5, alpha=0.5)
plt.title('Weekly Temperature Trend')
plt.show()