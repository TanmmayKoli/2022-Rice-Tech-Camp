import numpy as np
import matplotlib.pyplot as plt

p = np.loadtxt('pressure.csv',delimiter=',')  # Read in the fluid pressure
u = np.loadtxt('u_velocity.csv',delimiter=',')  # Read in the horizontal velocity of the fluid
v = np.loadtxt('v_velocity.csv',delimiter=',') # Read in the vertical velocity of the fluid
xnodes = np.loadtxt('xnodes.csv',delimiter=',')  # Read in the x (horizontal) nodes
ynodes = np.loadtxt('ynodes.csv',delimiter=',')  # Read in the y (vertical) nodes

# Generate contour plot
plt.figure()  # Create a new figure in the memory
plt.contour(xnodes, ynodes, u)  # Initial plot command
plt.savefig('u_velocity0.png')

# Generate contour plot
plt.figure()  # Create a new figure in the memory
plt.contour(xnodes, ynodes, u)  # Initial plot command
plt.pcolormesh(xnodes, ynodes, v,cmap = plt.get_cmap('rainbow'))  # Modify color map
plt.colorbar() # Display color bar

plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.title('Horizontal Velocity Around a Car')

xcar = np.loadtxt('x_car.csv',delimiter=',')
ycar = np.loadtxt('y_car.csv',delimiter=',')
plt.scatter(xcar, ycar)

# This line of code will ensure that the image has the correct x-to-y dimensions.
plt.axes().set_aspect(1)

# Save figure
plt.savefig('u_velocity.png')

plt.figure()  # Create a new figure in the memory


plt.contour(xnodes, ynodes, p)  # Generate a contour plot of fluid pressure.
plt.pcolormesh(xnodes, ynodes, v,cmap = plt.get_cmap('rainbow'))  # Modify color map on the contour plot

plt.streamplot(xnodes,ynodes,u,v,density=1.5)  # Add a streamline plot of the flow velocity.
plt.scatter(xcar, ycar)  # Add a plot that shows the car silhouette.

# Add x and y labels, and a title to this plot.
plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.title('Streamlines Around a Car')

# This line of code will ensure that the image has the correct x-to-y dimensions.
plt.axes().set_aspect(1)

plt.savefig('streamlines.png')