

import numpy as np
import matplotlib.pyplot as plt
import colorsys

# the integral is equal to 4 * np.pi * G * rho_0 * r_c**3 * (r/r_c - np.arctan(r/r_c))
Δt = 1
G = 0.03
rho_0 =1
r_c =5
x_0 = -100
y_0= -5
z_0=-40
v_x0 = 1
v_y0 = 0
v_z0 = 0
ax_0 = 0
ay_0 = 0
az_0 = 0

def halo_pull(r):
    M = 4 * np.pi * G * rho_0 * r_c**3 * (r/r_c - np.arctan(r/r_c))
    return (G * M)/(r**2)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
def light_ray(x_0, y_0, z_0, v_x0, v_y0, v_z0):
    x = []
    y = []
    z = []
    t = []
    

    for i in range(200): 
        r = np.sqrt(x_0**2 + y_0**2 + z_0**2)
        a = halo_pull(r)
        ax_0 = a * (-x_0/r)
        ay_0 = a * (-y_0/r)
        az_0 = a * (-z_0/r)
        x_1 = x_0 + v_x0 * Δt
        y_1 = y_0 + v_y0 * Δt 
        z_1 = z_0 + v_z0 * Δt
        vx_1 = v_x0 + Δt * ax_0
        vy_1 = v_y0 + Δt * ay_0
        vz_1 = v_z0 + Δt * az_0
        x.append(x_0)
        y.append(y_0)
        z.append(z_0)
        t.append(i * Δt)
        x_0, y_0, z_0, v_x0, v_y0, v_z0 = x_1, y_1, z_1, vx_1, vy_1, vz_1
    
    for i in range(len(x)-1):
        hue = i / (len(x) - 1)
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)
        ax.plot([x[i], x[i+1]], [y[i], y[i+1]], [z[i], z[i+1]], color=rgb)
    
    print(x)
    print(y)
    print(t)





light_ray(x_0, y_0, z_0, v_x0, v_y0, v_z0)
light_ray(-100, 5, -40,1, 0, 0)

ax.set_xlim(-100, 100)
ax.set_ylim(-30, 100)
ax.set_zlim(-100, 100)
ax.plot(0,0,0, 'o', color='black')
plt.show()


