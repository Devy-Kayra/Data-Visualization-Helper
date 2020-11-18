import matplotlib as mp # we import matplotlib
from matplotlib import pyplot as plt # we import pyplot from matplotlib
from matplotlib import style # we get to the style this library

style.use("ggplot") # We changed default style to ggplot style
plt.figure("New Histogram")

ages = [18 , 23 , 18 , 42 , 30 , 45 , 63 , 24 , 56 , 100] # We have ages
bins = 10 # Range of values for every part

plt.xlabel("Ages")
plt.ylabel("Age Count")

plt.hist(ages , bins , edgecolor = "black") # We create histogram with black edges
plt.show()