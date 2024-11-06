import matplotlib.pyplot as plt
overs=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
runs=[7,10,3,9,5,2,35,45,25,30,60,12,16,19,13,2,8,1,11,23]
plt.plot(overs,runs,marker='x',markerfacecolor='blue',markersize=8,linestyle='dashed',linewidth=2,color='red')
plt.xlabel("overs",color='purple')
plt.ylabel("runs",color='green')
plt.title("Megha")
plt.show()
