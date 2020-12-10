__author__ = "Nihal Yadalam Murali Kumar"
__matriculation_number__ = "6873339"
__email_id__ = "nihal.yadalammurali@gmail.com"

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 150
myArr = []
x = []
y = []
z = []
u = []
v = []
w = []

f = open("field2.irreg.txt", "r")

myArr = f.readlines()

# header data
Header = myArr[0:6]
print(Header)

# discard header data
del myArr[0:6]

# adding individual fields of a record to vector lists
for elements in myArr:
    element = elements.split()
    x.append(float(element[0]))
    y.append(float(element[1]))
    z.append(float(element[2]))
    u.append(float(element[3]))
    v.append(float(element[4]))
    w.append(float(element[5]))


speed = np.hypot(u, v)
q = plt.quiver(x, y, u, v, speed, width=0.0015, scale=1.5, scale_units='inches', cmap='jet')
plt.xlabel('X-Axis - width of the particle vector', fontsize=7)
plt.ylabel('Y-Axis - length of the particle vector', fontsize=7)
color_bar = plt.colorbar()
color_bar.set_ticks([0, 1])
color_bar.set_ticklabels(["low", "high"])
color_bar.ax.set_ylabel('Larger the magnitude higher the speed of the particle', fontsize=7)
plt.savefig('FlowData.png')
plt.show()
