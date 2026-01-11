import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

M1 = np.array([
    [-0.5, 0], 
    [0, 0.5]
])

M2 = np.array([
    [0, -0.5],
    [-0.5,  0]
])


SCALE = 1 

parts = {
    'body': np.array([[2,2], [24,2], [24,3], [22,3], [24,4], [24,5], [23,6], [22,6], [23,8], [23,11], [20,15], [20,17], [18,19], [15,19], [14,17], [14,16], [12,16], [12,17], [11,19], [8,19], [6,17], [6,15], [3,11], [3,8],[4,6],[3,6],[2,5],[2,4],[4,3],[2,3]]) * SCALE,
    'belly': np.array([[10,2], [16,2], [18,4], [18,8], [16,9], [10,9], [8,8], [8,4], [10,2]]) * SCALE,
    'eye_l': np.array([[7,15], [8,14], [10,14], [11,15], [11,17], [10,18], [8,18], [7,17]]) * SCALE,
    'eye_r': np.array([[15,15], [16,14], [18,14], [19,15], [19,17], [18,18], [16,18], [15,17]]) * SCALE,
    'mouth': np.array([[6,13], [7,12], [19,12], [20,13]]) * SCALE
}

def draw_frog(ax, M, label):
    # Transformation: [x', y'] = [x, y] * M^T
    def transform(pts):
        return pts @ M.T

    ax.add_patch(patches.Polygon(transform(parts['body']), facecolor='#a4c3a2', edgecolor='black', linewidth=1, label=label))
    ax.add_patch(patches.Polygon(transform(parts['belly']), facecolor='#cfe05e', edgecolor='black', linewidth=1))
    ax.add_patch(patches.Polygon(transform(parts['eye_l']), facecolor='black'))
    ax.add_patch(patches.Polygon(transform(parts['eye_r']), facecolor='black'))
    

    m = transform(parts['mouth'])
    ax.plot(m[:,0], m[:,1], color='black', linewidth=1)

fig, ax = plt.subplots(figsize=(20, 10))


draw_frog(ax, np.eye(2), "Original")
draw_frog(ax, M1, "Transformed 1")
draw_frog(ax, M2, "Transformed 2")


plt.xticks(np.arange(-14, 25, 2))
plt.yticks(np.arange(-14, 21, 2))
ax.axhline(0, color='black', linewidth=1.2) # X-axis
ax.axvline(0, color='black', linewidth=1.2) # Y-axis
ax.set_xlim(-14, 24)
ax.set_ylim(-14, 20)
ax.grid(True, linestyle='-', alpha=0.7)
ax.set_aspect('equal')
ax.legend(loc='upper left')
ax.set_title("Frog Transformation on One Cartesian Axis")

plt.show()
