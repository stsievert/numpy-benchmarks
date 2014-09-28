
from __future__ import division
from pylab import *
from pandas import read_csv

x = read_csv('times.csv')

imac = ones(x.iMac.size)
air = asarray(x.Air) / imac
pro = asarray(x.Pro) / imac
names = x.Function

imac = hstack((imac, [1]))
air = hstack(([mean(air)], air))
pro = hstack(([mean(pro)], pro))
names = hstack((["\\textbf{Mean}"], names, [""]))

SIZE = (3*3, 2*3)
figure(figsize=SIZE)
ax = gca()
i = arange(1, imac.shape[0]+2)
plot(imac , 'go-' , label='2011 iMac')
plot(air  , 'bo'  , label='2012 Air')
plot( pro  , 'ro'  , label='2014 Pro')

grid()
legend(loc='best')

ylabel('Relative time (s/s)')
xlabel('Function')
title('Timing the Mac Pro')

#xticks(arange(9), names)
xticks(arange(pro.shape[0]+1), names)
STEP = 0.1
plt.yticks(arange(0.2, 1.6+STEP, step=STEP))
ax.set_ylim((0.2, 1.6))
ax.set_xlim(-1, pro.shape[0])

rect = matplotlib.patches.Rectangle((-0.2,0.2), 0.4, 1.6, color='yellow')
ax.add_patch(rect)

savefig('times.png', dpi=300)
show()
