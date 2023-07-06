import random

import matplotlib.pyplot as plt

def draw_binary_tree(node, x, y, x_shift, y_shift):

    print(node.value)

    # Draw the current node
    plt.text(x, y, node.value, color='k', ha='center', va='center',
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

    # Draw the left child and its edge
    if node.left:
        plt.plot([x, x - x_shift], [y, y - y_shift], 'k')  # Edge
        draw_binary_tree(node.left, x - x_shift, y - y_shift, x_shift / 2, y_shift)  # Left child

    # Draw the right child and its edge
    if node.right:
        plt.plot([x, x + x_shift], [y, y - y_shift], 'k')  # Edge
        draw_binary_tree(node.right, x + x_shift, y - y_shift, x_shift / 2, y_shift)  # Right child

class Node:

    def __init__(self, size=16):
        self.value = 1
        self.left = None
        self.right = None
        self.max_size = size


    def append(self, value):
        pass


def rx0():
    s = ""
    for i in range(9):

        if i % 3 == 0 and i > 0:
            s += '\n'

        if random.random() > 0.5:
            s+='X'
        else:
            s += '0'
    return s


# Create a binary tree

root = Node(size=20)

# for i in range(20):
#     root.append(rx0())

root = Node()
root.left = Node()
root.right = Node()
root.left.left = Node()
root.left.right = Node()
root.right.left = Node()
root.right.right = Node()




plt.figure(figsize=(8, 8))
plt.axis('off')
print(root)
draw_binary_tree(root, 0, 0, 0.5, 1)
plt.show()