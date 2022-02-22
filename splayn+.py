from numpy import *
import mymodule
import matplotlib.pyplot as plt         


def Func (t,tn,a,b,c,d):
    S = a + b*(t - tn) + (c/2)*((t - tn)**2) + (d/6)*((t - tn)**3)
    return S

def Splayn(x,t,tau,N,h):
##    h = zeros(N-1)
##    for i in range(len(h)):
####        h[i] = t[i+1] - t[i]
##        h[i] = random.uniform(0.1,0.4)
####    print(h)    
    mat_c = zeros((N-2,N-2))
    mat_b  = zeros(N-2)
    c  = zeros(N-1)
    d = zeros(N-1)
    b = zeros(N-1)
    
    for i in range(len(h)-1):
        for j in range(len(h)-1):
            if i == j: mat_c[i,j] = 2*(h[i] + h[i+1])
            if i+1 == j: mat_c[i,j] = h[i+1]
            if i == j+1: mat_c[i,j] = h[j+1]

    for i in range(N-2):
        mat_b[i] = 6*(((x[i+2] - x[i+1])/h[i+1]) - ((x[i+1]-x[i])/h[i]))
        
    c_1 = mymodule.Progonka(mat_c, mat_b)
    for i in range(1,len(c)):
        c[i] = c_1[i-1]
    for i in range(N-2):
        d[i] = (c[i+1] - c[i])/h[i]
        b[i] = ((x[i+1]-x[i])/h[i]) - h[i]*(c[i]/3 + c[i+1]/6)
    d[N-2] = c[N-2]/h[N-2]
    b[N-2] = (x[N-1]-x[N-2])/h[N-2] - h[N-2]*(c[N-2]/3)
    
    f = zeros(len(tau))
    n = 0
    for i in range(1,len(tau)):
        while t[n] < tau[i]:
            n+=1    
        f[i] = Func (tau[i],t[n-1],x[n-1],b[n-1],c[n-1],d[n-1])
    return f


N = 50
h = zeros(N-1)
for i in range(len(h)):
    h[i] = random.uniform(0.1,2.1)
        
t = [0]
for i in range(len(h)):
    t.append(t[i] + h[i])  

tau = linspace(0,t[-1], N*3)
x = sin(t)

plt.xlabel('time')
plt.ylabel('x(t)')
plt.plot(t,x, 'o',c = 'w',mec = 'r', mew = '2')
plt.plot(tau,Splayn(x,t,tau,N,h),'.',c = 'black')
plt.legend(('Source function','Splayn'),loc = 1)
plt.show()
