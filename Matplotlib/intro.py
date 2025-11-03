import matplotlib.pyplot as plt

# creating the lists
x = [1, 2, 3, 4, 5]  # horizontal axis
y = [10, 20, 25, 30, 40]  # vertical axis

plt.plot(x, y, marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
