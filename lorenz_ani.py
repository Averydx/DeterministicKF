from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

fig1 = plt.figure()
fig2 = plt.figure()

ax = fig1.add_subplot(projection='3d')
ax1 = fig2.add_subplot()


def lorenz(xyz, *, s=10, r=28, b=2.667):
   """
   Parameters
   ----------
   xyz : array-like, shape (3,)
      Point of interest in three-dimensional space.
   s, r, b : float
      Parameters defining the Lorenz attractor.

   Returns
   -------
   xyz_dot : array, shape (3,)
      Values of the Lorenz attractor's partial derivatives at *xyz*.
   """
   x, y, z = xyz
   x_dot = s*(y - x)
   y_dot = r*x - y - x*z
   z_dot = x*y - b*z
   return np.array([x_dot, y_dot, z_dot])

dt = 0.01
N = 10_000

xyzs = np.empty((N, 3))  # Need one more for the initial values
xyzs[0] = (0., 1., 1.05)  # Set initial values
# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(N-1):
   xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

xyzs = xyzs.T

def update_3D(num, data, line):
    line.set_data(xyzs[:2, :num])
    line.set_3d_properties(xyzs[2, :num])

def update_X(num, data, line):
    line.set_xdata(t[:num])
    line.set_ydata(xyzs[0,num])

N = 10000
t = np.arange(0,10000)
line, = ax.plot(xyzs[0, 0:1], xyzs[1, 0:1], xyzs[2, 0:1],lw = 0.6)
line2, = ax1.plot(t[0],xyzs[0,0:1],lw = 0.6)

# Setting the axes properties
ax.set_xlim3d([-50.0, 50.0])
ax.set_xlabel('X')

ax.set_ylim3d([-50.0, 50.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 50.0])
ax.set_zlabel('Z')

#ax.view_init(elev=90, azim=45, roll=0)

ani1 = animation.FuncAnimation(fig1, update_3D, N, fargs=(xyzs, line), interval=10000/N, blit=False)
ani2 = animation.FuncAnimation(fig2, update_X, N, fargs=(xyzs, line2), interval=10000/N, blit=False)
#ani.save('matplot003.gif', writer='imagemagick')
plt.show()


