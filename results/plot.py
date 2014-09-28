
from __future__ import division
from pylab import *
from pandas import read_csv

x = read_csv('times.csv')

imac = ones(x.iMac.size)
air = asarray(x.Air) / imac
pro = asarray(x.Pro) / imac
names = x.Function

imac = hstack((imac, [1]))
air = hstack((air, [mean(air)]))
pro = hstack((pro, [mean(pro)]))
names = hstack((names, ["\\textbf{Mean}", ""]))

SIZE = (3*3, 2*3)
figure(figsize=SIZE)
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
gca().set_ylim((0.2, 1.6))
gca().set_xlim(-1, pro.shape[0])

savefig('times.png', dpi=300)
show()
