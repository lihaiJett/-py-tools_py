# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pylab import *

a = np.arange(10, 50, 0.1)
h = 11.5
la = 48
bh = 3.8
bookSizeH = 17

x = [26.1, 30.69,32,  36.6, 37.8, 42.48, ]
y = [51, 68, 62, 39, 40, 46, ]

rh = h + (bh * sin(radians(a)))
Lc = rh / tan(radians(90 - a))
Dc = rh / sin(radians(90 - a))
Lnc = (Dc * sin(radians(0.5 * la))) / sin(radians(90 + a - (0.5 * la)))
Lcf = (Dc * sin(radians(0.5 * la))) / sin(radians(90 - a - (0.5 * la)))
Lnf = abs(Lnc) + abs(Lcf)
Ln = Lc - Lnc

Lf = rh / tan(radians(90 - a - (0.5 * la)))

# 书本高度占捕捉区域比例
sizeYPercentage = bookSizeH / Lnf * 100
# 书本一半捕捉到的可移动范围
hRange = Lnf - 17

plt.figure(figsize=(12, 6))

plt.subplot(111)
plt.title("h=" + str(h) + "", loc='center')

# plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.6f'))
plt.xticks(np.arange(0, 50, 1))
# plt.yticks(np.arange(10, 100, 5))


# p0, = plt.plot(a, Dc)
#
# p1, = plt.plot(a, Lnf, "y")
#
# p2, = plt.plot(a, Ln, "b")
#
# p3, = plt.plot(a, sizeYPercentage, "r")

p4, = plt.plot(x, y, "g")

# plt.plot([10, 50], [32, 32], 'k--')
#
# plt.annotate(r'book percent = 32%', xy=(10, 32), xycoords='data', xytext=(+30, +30),
#              textcoords='offset points', fontsize=10,
#              arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
#
# plt.plot([10, 50], [100, 100], 'k--')
#
# plt.annotate(r'book percent = 100%', xy=(10, 100), xycoords='data', xytext=(+30, +30),
#              textcoords='offset points', fontsize=10,
#              arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
#
# plt.legend([p0, p1, p2, p3], ["Dc", "Lnf", "Ln", "bookPercentage"], loc="upper right")

plt.savefig("xxx.jpg")
