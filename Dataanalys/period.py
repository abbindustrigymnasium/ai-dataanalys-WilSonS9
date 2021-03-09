from math import *
import matplotlib.pyplot as plt
import numpy as np

f = open("rawdata119870.csv", "r")
a = f.read()
li = a.split('\n')
del li[len(li)-1]

f.close()

i = []
x = []
y = []
z = []
it = []
xt = []
yt = []
zt = []
xtt = []
ytt = []
ztt = []
maxes = []
fi = 6

for value in li:
    n = value.split(',')
    i.append(float(n[0])-1567068324355)
    x.append(float(n[1]))
    y.append(float(n[2]))
    z.append(float(n[3]))
def smooth(start, stop, yout, yin):
    sy = 0
    c = start
    while c <= stop:
        sy += yin[c]
        c += 1
    yout.append(sy / (2 * fi + 1))

def do(steps):
    step = 1
    old = y
    new = []
    while step <= steps:
        summing = 0
        while summing < len(old):
            if summing - fi >= 0 and summing + fi <= len(old) - step:
                smooth(summing - fi, summing + fi, new, old)
            else:
                new.append(old[summing])
            summing += 1
        old = new
        new = []
        step += 1
    return old

yt = do(1)
ytt = do(2)
s3 = 1
while s3 < len(ytt) - 2 :
    if ytt[s3] > ytt[s3-1] and ytt[s3] > ytt[s3+1]:
        maxes.append(s3 * 20)
    s3 += 1
print(maxes)

s5 = 0
sum1 = 0
an1 = 0
av1 = 0
sum2 = 0
an2 = 0
av2 = 0
while s5 < len(maxes):
    val = maxes[s5]
    if val >= 2000 and val <= 21000:
        sum1 += val - maxes[s5 - 1]
        an1 += 1
    elif val > 21000 and val <= 50000:
        sum2 += val - maxes[s5 - 1]
        an2 += 1
    s5 += 1
av1 = sum1/an1
av2 = sum2/an2
print('First average: ' + str(60000/av1), 'steps per minute')
print('Second average: ' + str(60000/av2), 'steps per minute')

def plot():
    t = np.arange(0, round(i[len(i)-1]), 20.1)
    fig, ax = plt.subplots()
    # kx = ax.plot(t, xtt, label='xtt')
    ky = ax.plot(t, yt, label='yt')
    ky2 = ax.plot(t, ytt, label='ytt')
    # ky3 = ax.plot(t, yfinal, label='ySmoothed')
    # kz = ax.plot(t, ztt, label='ztt')
    # kx2 = ax.plot(t, x, label='x')
    ky2 = ax.plot(t, y, label='y')
    # kz2 = ax.plot(t, z, label='z')
    ax.legend(loc='lower right', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)
    ax.set(xlabel='t (ms)', ylabel='a (m/s^2)',
    title='periods')
    ax.grid(alpha=0.3)

    # if area<0:
    #     area *= -1
  #  ax.text(0, 0, 'Area = ' + str(round(area, 4)), horizontalalignment='left', verticalalignment='top')
    fig.savefig("cycleDoubleBruv.png")
    plt.show()
plot()