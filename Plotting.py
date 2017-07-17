import numpy as n
import matplotlib.pyplot as p
fig = p.Figure()
ax=p.axes()

def plot_fig(hash_tags,count):

    labels = hash_tags     # Mentioning the labels(hash_tags) for pie-chart
    size = count           # Mentioning the sizes of the labels
    colors = ['r','g','b','m','y','c','w']   # Colours to be used
    explode = []
    for temp in labels:
        explode.append(0)  # Use to denote slicing
    p.pie(size,explode,labels,colors,startangle=120,shadow=False,radius=1.0,autopct = "%1.2f%%",pctdistance=.6,)   # Plotting the plot
    p.axis("equal")      # Shows the pie-chart in circle
    p.legend(labels)     # Legends displayed
    p.tight_layout()
    p.show()
