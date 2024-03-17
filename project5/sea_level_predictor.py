import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,8))
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    plt.scatter(x, y)

    # Create first line of best fit
    line1 = linregress(x, y)
    #ext_x = np.arange(min(x),max(x) + (2050 - max(x)))
    pred_y = line1.intercept + line1.slope * range(min(x),2051)
    plt.plot(range(min(x),2051), pred_y, color = "red")

    # Create second line of best fit
    line2 = linregress(df[df["Year"]>= 2000]["Year"], df[df["Year"]>= 2000]["CSIRO Adjusted Sea Level"])
    pred_y = line2.intercept + line2.slope * range(2000, 2051)
    plt.plot(range(2000, 2051), pred_y, color = "red")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()