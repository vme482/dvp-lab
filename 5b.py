import matplotlib.pyplot as plt
CARS=('Duster','Rangeover','kia','benz','BMW',"TATA")
data=[30,60,20,90,75,50]
plt.figure(figsize=(10,7))
plt.pie(data,labels=CARS)
plt.title("Megha-Diploma")
plt.show()
