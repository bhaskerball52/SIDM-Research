import numpy as np
import matplotlib.pyplot as plt

Δt = 0.5
steps = 400
GM = 0.25
eps = 1          # softening so r never hits 0

# galaxy (oval) in the plane x = 100
cy, cz = 3, 0
a_src = 3
b_src = 1.5      # axis ratio b/a = 0.5

def light_ray(y0, z0):
    x, y, z = -100, y0, z0
    vx, vy, vz = 1, 0, 0
    xs = [x]
    ys = [y]
    zs = [z]
    for i in range(steps):
        r = np.sqrt(x**2 + y**2 + z**2 + eps**2)
        a = 2 * GM / r**2
        ax = a * (-x / r)
        ay = a * (-y / r)
        az = a * (-z / r)
        x = x + vx * Δt
        y = y + vy * Δt
        z = z + vz * Δt
        vx = vx + ax * Δt
        vy = vy + ay * Δt
        vz = vz + az * Δt
        xs.append(x)
        ys.append(y)
        zs.append(z)
    return xs, ys, zs

fig = plt.figure()
axes3d = fig.add_subplot(projection='3d')

phi = np.linspace(0, 2*np.pi, 100)
axes3d.plot(np.full(100, 100), cy + a_src*np.cos(phi), cz + b_src*np.sin(phi), color='blue', linewidth=3)

grid = np.linspace(-15, 15, 15)
for y0 in grid:
    for z0 in grid:
        xs, ys, zs = light_ray(y0, z0)
        inside = ((ys[-1] - cy)/a_src)**2 + ((zs[-1] - cz)/b_src)**2 <= 1
        if inside:
            axes3d.plot(xs, ys, zs, color='red')
        else:
            axes3d.plot(xs, ys, zs, color='lightgray', linewidth=0.5)

axes3d.scatter(0, 0, 0, color='black', s=60)
axes3d.set_xlim(-100, 100)
axes3d.set_ylim(-20, 20)
axes3d.set_zlim(-20, 20)
axes3d.set_box_aspect((5, 1, 1))
plt.show()