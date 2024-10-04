import matplotlib.pyplot as plt

delta_t = 0.05
t = 0
h = 1
v = 10
a = -9.81

times = [t]
heights = [h]
velocities = [v]

while h>=0:
    t += delta_t
    h += v*delta_t
    v += a*delta_t
    
    times.append(t)
    heights.append(h)
    velocities.append(v)

    print('time=',str(t),' height=',str(h),' velocity=',str(v))
    
print('The ball hits the ground after ',str(t),'seconds.')

plt.figrue(0)
plt.plot(times,heights)
plt.savefig('height.png')

plt.figure(1)
plt.plot(times,heights)
plt.title('Ball Height vs. Time')
plt.xlabel('Time [s]')
plt.ylabel('Height [m]')
plt.savefig('height_with_axes_labels.png')

plt.plot(times,velocities)
plt.title('Ball Velocity vs. Time')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.savefig('velocity_with_axes_labels.png')