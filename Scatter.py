import matplotlib as mp # we import matplotlib
from matplotlib import pyplot as plt # we import pyplot from matplotlib
from matplotlib import style # we get to the style this library

style.use("ggplot") # We changed default style to ggplot style
plt.figure("New Scatter")

x = [0 , 1 ,2 , 3 , 4, 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13] # X axis
y = [2 ,3 , 4 , 5, 7 , 6 , 7 , 3 , 7 , 8 , 10 , 3 , 11 , 5] # Y axis

plt.scatter(x , y , s = 60 , color= 'B' , marker = "X" , edgecolors= "black")
# s = size , marker = pointer to show
plt.show()