import numpy as np
import matplotlib.pyplot as plt
import colorsys

Δt = 1
GM = 1
x_0 = -100
y_0= -5
v_x0 = 1
v_y0 = 0
ax_0 = 0
ay_0 = 0

fig_1 = plt.figure()

def light_ray(x_0, y_0, v_x0, v_y0):
    x = []
    y = []
    t = []

    for i in range(200): 
        r = np.sqrt(x_0**2 + y_0**2)
        a = (GM)/r**2
        ax_0 = a * (-x_0/r)
        ay_0 = a * (-y_0/r)
        x_1 = x_0 + v_x0 * Δt
        y_1 = y_0 + v_y0 * Δt 
        vx_1 = v_x0 + Δt * ax_0
        vy_1 = v_y0 + Δt * ay_0
        x.append(x_0)
        y.append(y_0)
        t.append(i * Δt)
        x_0, y_0, v_x0, v_y0 = x_1, y_1, vx_1, vy_1
    
    for i in range(len(x)-1):
        hue = i / (len(x) - 1)
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)
        plt.plot([x[i], x[i+1]], [y[i], y[i+1]], color=rgb)
    
    print(x)
    print(y)
    print(t)





light_ray(x_0, y_0, v_x0, v_y0)
light_ray(-100, 5,1, 0)

plt.xlim(-100, 100)
plt.ylim(-30, 100)
plt.plot(0,0, 'o', color='black')
plt.show()