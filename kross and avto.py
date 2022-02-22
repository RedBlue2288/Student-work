import numpy as np
import matplotlib.pyplot as plt

def kross_kor(x,y,T,N):
    Cross_xy = np.zeros(T)
    Cross_yx = np.zeros(T)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    sig_x = np.var(x)
    sig_y = np.var(y)
    for tau in range(T):
        for i in range(0,N-tau):
            xy = (x[i]-x_mean)*(y[i+tau]-y_mean)
            yx = (y[i]-y_mean)*(x[i+tau]-x_mean)
            Cross_xy[tau]+= 1/(N-tau) * xy /np.sqrt(sig_x*sig_y)
            Cross_yx[tau]+= 1/(N-tau) * yx /np.sqrt(sig_x*sig_y)
    return Cross_xy, Cross_yx

def avto_kor(x,T,N):
    avto_x = np.zeros(T)
    x_mean = np.mean(x)
    sig_x = np.var(x)
    for tau in range(T):
        for i in range(0,N-tau-1):
            avto_x[tau]+= 1/(N-tau) * (x[i]-x_mean) * (x[i+tau]-x_mean)/sig_x
    return avto_x

N = 10**4
T = 10**3
t = np.arange(0,T,0.01)
x = np.sin(2*np.pi/6*t)
y = np.cos(2*np.pi*t)
##tau = np.arange(0,T)

xy, yx = kross_kor(x,y,T,N)
a_x = avto_kor(x,T,N)
tau = np.arange(-T+1,T)
H = list(xy[::-1])
H.extend(yx[1:])

fig1 = plt.figure()
fig2 = plt.figure()

ax0 = fig1.add_subplot(3,1,1)
ax0.plot(t[:N],x[:N], label = "sin", color = 'blue')
ax1 = fig1.add_subplot(3,1,2)
ax1.plot(t[:N],y[:N], label = "cos", color = 'green')
ax2 = fig1.add_subplot(3,1,3)
ax2.plot(tau, H, label = "kross: sin-cos", color = 'orange')
##ax2.plot(xy, label = "kross: sin-cos", color = 'orange')
##ax3 = fig1.add_subplot(4,1,4)
##ax3.plot(yx, label = "kross: cos-sin", color = 'green')
fig1.legend()

ax0 = fig2.add_subplot(2,1,1)
ax0.plot(t[:N],x[:N], label = "sin", color = 'black')
ax1 = fig2.add_subplot(2,1,2)
ax1.plot(a_x, label = "avtokor-sin", color = 'green')
fig2.legend()

plt.show()
