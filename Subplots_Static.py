import matplotlib.pyplot as plt
categories=['Mon','Tue','Wed','Thu','Fri']
sales=[10,22,50,25,30]

y1=[10,20,25,35,45]
y2=[20,30,35,45,55]

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.bar(categories,sales)
plt.title("Daily Sales")
plt.xlabel("Week Days")
plt.ylabel("Sales")
plt.show()