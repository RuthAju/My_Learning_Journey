import matplotlib.pyplot as plt
import matplotlib.animation as an
import numpy as np
import pandas as pd

# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
# plt.plot(x, y)
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.show()

# x = np.array([1, 8])
# y = np.array([3, 10])
# plt.plot(x, y, "*")
# plt.show()

# x = np.array([1, 2, 6, 8])
# y = np.array([3, 8, 1, 10])
# plt.plot(x, y)
# plt.show()

# y = np.array([3, 8, 1, 10])
# plt.plot(y, marker = "o")
# plt.show()

# y = np.array([3,8,1,10])
# plt.plot(y, "o:r")
# plt.show()

# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# font1 = {'family':'serif','color':'k','size':20}
# font2 = {'family':'serif','color':'b','size':15}

# plt.title("Sports Watch Data", fontdict = font1, loc = 'left')
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)

# plt.plot(x, y)
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

# plt.show()



# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)

# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x, y)
# plt.show()

#day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)

#day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)

# plt.show()

# # Question 1
# Range = np.arange(70, 150, 15)

# M = np.random.randint(70, 150, 15)
# F = np.random.randint(70, 150, 15)

# plt.hist([M, F], color=("g", "r"), bins= Range, rwidth=0.98, label= ["Men", "Women"])
# plt.title("BLOOD SUGAR LEVEL ANALYSIS")
# plt.xlabel("Blood Sugar Levels(mg/dL)")
# plt.ylabel("Number of Patients")
# plt.legend()
# plt.show()

# Question 2
# data = np.random.randint(70, 150, 15)
# Range = np.arange(70, 150, 10)
# colors = ["r", "y", "b"]
# plt.hist([data, data, data], bins = Range, label= ["80-100mg/dL","100-125mg/dL", "125-150mg/dL"], color= (["r", "y", "b"]), rwidth=0.98)
# plt.title("DISTRIBUTION OF BLOOD SUGAR LEVELS")
# plt.xlabel("Blood Sugar Levels(mg/dL)")
# plt.ylabel("Number of Patients")
# plt.legend()
# plt.show()


# # Question 3
# # Set up the figure and axis
# fig, ax = plt.subplots()

# # Generate initial random data
# data = np.random.randint(70, 150, 15)
# Range = np.arange(70, 150, 10)


# # Creates an initial histogram plot
# ax.hist(data, bins= Range, color="teal", rwidth=0.98)

# # Labels and title
# ax.set(xlim=[70, 150], xlabel = "Data Values", ylabel = "Frequency", title= "REAL-TIME UPDATING HISTOGRAM")
# ax.legend()

# # Function to update the histogram for each frame
# def update(frame):

#     # Simulate incoming new data by generating a new random value
#     n_data = np.random.randint(70, 150, 15)

#     # Append new data to the existing data
#     global data
#     data =np.append(data, n_data)
# # Clear the histogram and replot with updated data
#     # Clears axis to refresh plot
#     ax.cla()
#     ax.set(xlim=[70, 150], xlabel = "Data Values", ylabel = "Frequency", title= "REAL-TIME UPDATING HISTOGRAM")

#     # Plots updated histogram
#     ax.hist(data, bins= Range, color="teal", rwidth=0.98)

# plt.xlabel("Data Values")
# plt.ylabel("Frequency")
# plt.title("REAL_TIME UPDATING HISTOGRAM")

# # Creates an animation
# Animation = an.FuncAnimation(fig= fig, func= update, frames=50, interval= 200)
# plt.show()

# # Question 4
# data = np.random.randint(70, 150, 15)

# # Vectorized timestamp conversion using pandas
# timestamps = pd.to_datetime(data, unit="D", origin="unix" )

# # Color list for each bar, excluding red
# colors = ["darkgoldenrod", "palevioletred", "cadetblue", "yellowgreen", "dimgray", "aquamarine", "chocolate", "teal", "gold", "indigo"]

# # Set up the plot
# fig, ax = plt.subplots()

# # Create the histogram with specified color for each bin
# n, bins, patches = ax.hist(timestamps, bins=10, edgecolor="red", linewidth = 1)

# # Apply custom colors to each bar through iteration
# for i, patch in enumerate(patches):
#     patch.set_facecolor(colors[i % len(colors)])

# ax.set_title("My Histogram\nCheck it out")

# # Axis labels
# ax.set_xlabel("Value Range")
# ax.set_ylabel("Frequency")

# # Show plot
# plt.show()

# # Question 5
# fig = plt.figure()

# # Separate slices from the center
# slice_space = [0, 0.1, 0.1, 0.2, 0.1]

# exp_labels = ["House rent", "Food", "Internet", "Car", "Others"]
# exp_vals = [1400, 600, 300, 410, 250]
# color = ["indigo", "teal", "salmon", "navy", "burlywood"]
# # Creates the piechart
# plt.pie(exp_vals, labels = exp_labels, explode= slice_space, colors= color, autopct='%1.2f%%', shadow=True)
# plt.title("Expense Distribution")
# plt.show()


# z = np.array([1,2,3], ndmin= 2)
# print(z)


a = np.arange(9)
print(a)

result = np.split(a,3)
# print(result)
for i in result:
    print(i)