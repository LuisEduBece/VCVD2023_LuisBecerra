# Calculating v(t) and x(t) in a breaking car
# Final project - Vehicle Components and Driving Dynamics
# By Luis E. Becerra

from math import *
from numpy import *
import matplotlib.pyplot as plt 

# Define gravity constant
g = 9.8

# Define friction coefficients
friction_coefficients = {
    "sand": 0.3,
    "gravel": 0.35,
    "water": 0.05,
    "concrete": {"dry": 0.5, "wet": 0.35},
    "ice": {"dry": 0.15, "wet": 0.08}
}

# Taking user inputs to assign to variables
wet_dry = ""
mass = float(input("Enter the mass of the car in kg: "))
initial_velocity = float(input("Enter the velocity of the car in m/s: "))
road_type = input("Enter the road type (concrete/ice/gravel/water/sand): ")
if road_type == 'concrete' or road_type == 'ice': # alt: if road_type in ['concrete', 'ice']
    wet_dry += input("Enter the road condition (wet/dry): ")
inclination = float(input("Enter the inclination of the road in degrees: "))

# set friction coefficient based on road type and condition
mu = 0.0
if road_type in friction_coefficients:
    if wet_dry != "": # if wet_dry was input (concrete/ice)
        mu = friction_coefficients[road_type][wet_dry]
    else:
        mu = friction_coefficients[road_type]

# Calculate friction, deceleration
deceleration = cos(radians(inclination)) * g
breaking_distance = initial_velocity + (initial_velocity**2) / (2 * deceleration)
stopping_time = (initial_velocity / deceleration)

# Time array
times = linspace(0, stopping_time, 10)  # start, stop, number of values

# Initialize an empty array for velocities, positions
velocities = zeros_like(times)
positions = zeros_like(times)

# Calculate position and velocities for each time using a loop
for index, time in enumerate(times):
    velocities[index] = initial_velocity - deceleration * time
    positions[index] = (initial_velocity * time) - (0.5 * deceleration * time**2)

# PLOTTING ##############################

# data to be plotted
x = times
y = positions

# plotting https://www.geeksforgeeks.org/plot-line-graph-from-numpy-array/
plt.title("Distance & Time") 
plt.xlabel("Time (s)") 
plt.ylabel("Distance (m)") 
plt.plot(x, y, color ="blue") 
plt.show()

# data to be plotted
x1 = times
y1 = velocities

# plotting https://www.geeksforgeeks.org/plot-line-graph-from-numpy-array/
plt.title("Speed & Time") 
plt.xlabel("Time (s)") 
plt.ylabel("Speed (m/s)") 
plt.plot(x1, y1, color ="red") 
plt.show()