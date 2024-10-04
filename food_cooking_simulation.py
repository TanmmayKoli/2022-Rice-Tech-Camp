import os
import numpy as np
import matplotlib.pyplot as plt
import pdb

L = 0.05
H = 0.05
Nx = 30
Ny = 30
deltax = L/Nx
deltay = H/Ny

rho = 840
k = 0.418
cp = 3810

Tboundary = 100
Tinitial = 20

Ntime = 1000

alpha = k/(rho*cp)

tfinal= 1800
deltat=tfinal/Ntime

T_old = Tinitial*np.ones((Nx,Ny))

for i in range(0, Nx):
  T_old[0][j] = Tboundary
  T_old[i][Ny-1] = Tboundary

for j in range(0, Ny):
  T_old[0][j] = Tboundary
  T_old[Ny-1] [j] = Tboundary

T_new=np.copy(T_old)
time_array = np.arange(0.,tfinal,deltat)

x_array=np.linspace(0, L, num=Nx)
y_array=np.linspace(0, H, num=Ny)

print("The thermal diffusivity is {} m^2/s.".format(alpha))
print("The final time is {} seconds.".format(tfinal))
print("The step size is {} seconds.".format(step_size))
print("The simulation will loop through {} time steps.".format(len(time_array)))


for n,time in enumerate(time_array):
  for i in range(1,Nx-1):
    T_new[i,j]=T_old[i,j] + alpha*deltat*(T_old[i-1,j] - 2*T_old[i+1,j]/deltax* 2 + (T_old[i,j-1] ))
    if n%(Ntime/10)==0:
      X, Y = np.meshgrid(x_array,y_array)
      fig,ax = plt.subplots(1,1)
      plt.contourf(Y,X,T_new,cmap=plt.cm.jet)
      plt.colorbar()
      time_min = time/60.
      plt.xlabel('x[m]')
      plt.ylabel('y[m')
      ax.set_title('Time = %.2f min'%time_min)
      n_string = str(n).zfill(3)
      plt.savefig('plot'+n_string+' png')
      plt.close()
    T_old = np.copy(T_new)
    sim_centerpoint_times.appen(time/60.0)
    sim_centerpoint_temps.append(T_new[i_midpoint][j_midpoint])

print("The final time is {} minutes.".format(tfinal/60))
print("The final temperature at center is {} celcius".format(T_old[int(Nx/2)][int(Ny/2)]))

plt.figure()
pt.plot(sim_centerpoint_times, sim_centerpoint_temps, label="Simulation")
plt.plot(experimental_times, experimental_temps, label="Experiment")
plt.xlabel('Time[min]')
plt.ylabel('Temp[C]')
plt.legend(loc='upper left')
plt.savefig('experimental_simulation_comparison.png')
