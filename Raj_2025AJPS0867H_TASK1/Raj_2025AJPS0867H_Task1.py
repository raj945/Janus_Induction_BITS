#importing Useful Library

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

#reading data from File

df=pd.read_csv('Flight_Data.csv')

#calling each row , and giving them a Variable
Time = df['Time']
Velocity = df['Velocity']
Height = df['Height(m)']

#this is basiclly line already defined by founder here fig means full Canvas , and axis means the plotting Area or 1 graph
#there can be one fig , but multiple axis
#next inside subplot (1,2) here means( now of Row , now of Column)

fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(12,4), dpi=150)

#Graph of Velocity/time
axis1.set_xlim(min(Time),max(Time))
axis1.set_ylim(min(Velocity) - 5,max(Velocity) + 5)
axis1.grid()
axis1.set_xlabel("Time (s)")
axis1.set_ylabel("Velocity (m/s)")
axis1.set_title("Velocity per Second Data" , fontsize=14, fontweight="bold")

#Graph of Height /Time

axis2.set_xlim(min(Time),max(Time))
axis2.set_ylim(min(Height) - 5,max(Height) + 5)
axis2.grid()
axis2.set_xlabel("Time (s)")
axis2.set_ylabel("Height (m)")
axis2.set_title("Height per Second Data",fontsize=14, fontweight="bold")

#here we are defining , that in starting graph will be blank [] 

ani_plot, = axis1.plot([],[] , 'r-' , lw=3 , label = "velocity")
ani_plot2, = axis2.plot([], [], 'b-', lw=3 , label = " Height")

axis1.legend(frameon=True, facecolor="white", edgecolor="black")
axis2.legend(frameon=True, facecolor="white", edgecolor="black")


#updating data frames by frame , like frame start from 0,1,2.. like this

def update_data(frame):
    ani_plot.set_data(Time[:frame],Velocity[:frame])
    ani_plot2.set_data(Time[:frame], Height[:frame])

    return ani_plot,ani_plot2

#here everytime it call , update_data function it has new point so it draw it after 1second
animation = FuncAnimation(fig,update_data,interval = 1000,repeat=False , frames= len(Velocity))



plt.tight_layout()
plt.style.use("seaborn-v0_8")   # clean, modern look

plt.show()