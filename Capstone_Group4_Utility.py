"""
<Project Title>


Copyright (c) 2021
Licensed
Written by <>
"""

import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def genre_countplot(a,b,data):
    # Plot the genres and their count respectively
    ax1=sns.barplot(x = a,y = b, data = data)
    plt.xticks(rotation=90)
    plt.ylabel(b, fontweight='bold')
    plt.xlabel(a, fontweight='bold')
    plt.title('The number of '+ a, fontweight='bold')
    for p1 in ax1.patches:
        ax1.annotate('{:.0f}'.format(p1.get_height()), (p1.get_x()-0.1, p1.get_height()+30))
    plt.show()


def pieplot(data, colname):
    # Create an axis object
    fig, ax = plt.subplots(1, 1, figsize = (15, 8))

    # Get the data in the right format
    labels = list(data.keys())
    sizes  = list(data.values())

    # Plot the pie chart
    ax.pie(sizes, labels = labels, shadow = False, startangle = 0, autopct = "%1.2f%%")
    ax.axis('equal')
    ax.set_title(f"Pie chart for {colname} feature.")
    plt.show()
    
def clean_tags(df, col_ind):
    unique_tags = []
    for i in range(len(df)):
        for string in df.iloc[i,col_ind].split(', '):
            if string not in unique_tags:
                unique_tags.append(string)

    for tagg in unique_tags:
        pdseries_temp = []
        for i in range(len(df)):
            temp = tagg in str(df.iloc[i,col_ind])
            pdseries_temp.append(temp)
        df[tagg] = pdseries_temp
    
    
    
    
    
    
    
    
    
    