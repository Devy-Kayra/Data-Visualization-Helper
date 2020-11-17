import matplotlib as mp # we import matplotlib
from matplotlib import pyplot as plt # we import pyplot from matplotlib
from matplotlib import style

newGraphic = plt.figure("New Graphic");

x = [1 , 2 , 3 , 4] # we create list for X axis
y = [10 , 20 , 30 , 40] # we create list for Y axis

newY = [20 , 30 , 40 , 50] # we create list for new lines.

plt.plot(x , y , label = 'First Line') # We create new graphic with x axis and y axis
plt.plot(x , newY , label = 'Second Line') # We create new plots with x also newY axis.

plt.xlabel("X AXIS") # We add label for x axis.
plt.ylabel("Y AXIS") # We add label for y axis.

plt.title("Graphic Title") # We create graphic title

plt.legend() # we use for show label
plt.show()