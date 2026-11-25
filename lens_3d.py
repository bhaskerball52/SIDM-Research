import numpy as np
import matplotlib.pyplot as plt

# settings for the rays and the lens
Δt = 0.5
steps = 400
GM = 0.01          # try 0.25 later for strong lensing
offset = 1

# background galaxy (ellipse) in the plane x = 100
a_src = 3
b_src = 1.5
cy = 3
cz = 0

def light_ray(y0, z0):
    x, y, z = -100, y0, z0
    vx, vy, vz = 1, 0, 0
    xs = [x]
    ys = [y]
    zs = [z]
    for i in range(steps):
        r = np.sqrt(x**2 + y**2 + z**2) + offset
        pull = 2 * GM / r**2
        ax = pull * (-x / r)
        ay = pull * (-y / r)
        az = pull * (-z / r)
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

phi = np.linspace(0, 2*np.pi, 100)
y_start = cy + a_src * np.cos(phi)
z_start = cz + b_src * np.sin(phi)

y_end = []
z_end = []
for i in range(len(y_start)):
    xs, ys, zs = light_ray(y_start[i], z_start[i])
    y_end.append(ys[-1])
    z_end.append(zs[-1])

plt.figure()
plt.scatter(y_start, z_start, color='blue', s=10, label='start')
plt.scatter(y_end, z_end, color='red', s=10, label='final')
plt.plot(0, 0, 'o', color='black')
plt.axis('equal')
plt.legend()
plt.xlabel('y')
plt.ylabel('z')
plt.show()