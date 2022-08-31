import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure ( )
ax = fig.add_subplot ( 111, projection='3d' )

x1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
y2 = np.random.randint ( 50, size=10 )
z1 = np.random.randint ( 30, size=10 )

x2 = [ -1, -2, -3, -4, -5, -6, -7, -8, -9, -10 ]
y2 = np.random.randint ( -10, 0, size=10 )
z2 = np.random.randint ( 10, size=10 )

ax.scatter ( x1, y2, z1, c='b', marker='o', label='blue' )
ax.scatter ( x2, y2, z2, c='g', marker='D', label='green' )

ax.set_xlabel ( 'x axis' )
ax.set_ylabel ( 'y axis' )
ax.set_zlabel ( 'z axis' )
plt.title ( "3D Design" )
plt.legend ( )
plt.tight_layout ( )
plt.show ( )


