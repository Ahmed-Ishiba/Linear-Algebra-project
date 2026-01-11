import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

#Original image matrix of x and y coordinates
original_shape = np.array([
    [0, 1, 1, 5, 5, 6,4.5,4.5,4,4, 3],
    [3, 3, 1, 1, 3, 3, 4, 4.5,4.5,4.3, 5]
])

# Transformation Matrix
trans_matrix = np.array([
    [0.25,  0],
    [0,    -2]
])

# Translation Vector
sliding_vector = np.array([[5], [0]])

# Apply transformation
transformed_shape = (trans_matrix @ original_shape)+ sliding_vector


def complete_shape(S): #function to close the shape by adding the first point at the end
    return np.hstack([S, S[:, [0]]])

#close shapes
orig  = complete_shape(original_shape)
trans = complete_shape(transformed_shape)

###############################################

plt.figure(figsize=(20, 6)) #create a figure

###############################################

#orignal shape
#        x coord  y coord color  line width  label to display
plt.plot(orig[0], orig[1], 'k-', linewidth=2, label="Original Shape")
plt.scatter(orig[0], orig[1], color='k')

# Transformed shape
#        x coord   y coord   color  line width  label to display
plt.plot(trans[0], trans[1], 'r-', linewidth=2, label="Transformed Shape")
plt.scatter(trans[0], trans[1], color='r')

plt.axhline(0, color='gray', linewidth=0.7)
plt.axvline(0, color='gray', linewidth=0.7)

plt.grid(True)

plt.gca().set_xlim(0,8)#.set_aspect('equal', adjustable='box')
plt.gca().set_xlim(0,10)


plt.xlabel("X")
plt.ylabel("Y")
plt.title("Original Shape and Linear Transformation")
plt.legend()

plt.show()
