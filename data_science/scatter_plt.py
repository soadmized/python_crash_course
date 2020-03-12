import matplotlib.pyplot as plt

x_values = []
y_values = []

for num in range(100):
    x_values.append(num)
    y_values.append(num * num)

plt.scatter(x_values, y_values, s=40)

plt.title('Square of value', fontsize=24)
plt.xlabel('Value', fontsize=16)
plt.ylabel('Square', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=24)

plt.show()
