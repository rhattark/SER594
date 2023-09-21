import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set(title='Universities by Innovation', 
       ylabel='Innovation', 
       xlabel='Years since Michael Crow became President')
ax.set(xlim=[0, 10], ylim=[0, 500])
asu_pts = np.arange(0, 10, 1)
plt.plot(asu_pts, 5 * asu_pts ** 2 + asu_pts + 25, 'maroon', label='ASU')
plt.plot(asu_pts, 2 * asu_pts, 'blue', label='UoA')
plt.plot(asu_pts, 0 * asu_pts, 'black', linestyle='--', label='1:1')
ax.legend()
plt.show()