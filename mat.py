import matplotlib.pyplot as plt


vals = [20000, 15000, 40000]
labels = ['x', '0', 'None']

plt.pie(vals, labels=labels,  autopct='%1.1f%%')
plt.title('проценты побед в крестиках и ноликах')
plt.show()