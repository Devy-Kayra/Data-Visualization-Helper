#Important this project just example.
#This data is not true.
import matplotlib as mp
from matplotlib import pyplot as plt
from matplotlib import style

newGraphic = plt.figure("Car Selling Graphic");

x = ["January" , "February" , "March" , "April" , "May"]
y = [100.000 , 200.000 , 300.000 , 400.000 , 500.000]

BMV = [100.000 , 125.000 , 20.000 , 39.000 , 10.000]
Ford = [120.000 , 145.000 , 220.000 , 239.000 , 310.000]
Toyota = [300.000 , 425.000 , 500.000 , 339.000 , 410.000]
Tesla = [100.000 , 25.000 , 30.000 , 49.000 , 70.000]
Mercedes = [300.000 , 425.000 , 540.000 , 339.000 , 210.000]

plt.plot(x , BMV , label = "BMV")
plt.plot(x , Ford , label = "Ford")
plt.plot(x , Toyota , label = "Toyota")
plt.plot(x , Tesla , label = "Tesla")
plt.plot(x , Mercedes , label = "Mercedes")

plt.xlabel("\nMonths")
plt.ylabel("Selling Count (thousand)")

plt.title("Car Selling Graphic")

plt.legend()
plt.show()