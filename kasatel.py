from math import *
#уравнение
def equation(x):
    return 2*x*x-2
#производная
def F1(x):
    return  4*x
 

def Method_cas(a,b):
    try:
        x0=(a+b)/2
        xn=equation(x0)
        xn1=xn-equation(xn)/F1(xn)
        while abs(xn1-xn)>eps:
            xn=xn1
            xn1=xn-equation(xn)/F1(xn)
        return xn1
    except ValueError:
        print ('Value not invalidate')

#для проверки необходимо ввести 'a' и 'b'
#необходимое условие: (a<b)

a = float(input('a ='))
b = float(input('b ='))
d = Method_cas(a,b)
print(d)
