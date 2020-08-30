"""
a=1.5
n=10
nome="Marcelo"
nome2="Jorge"
#print(" a =",a,"\n n =",n,"\n nome =",nome)
lista=[a,n,nome,nome2]
print(len(lista))
for i in range(len(lista)):
    print(lista[i])
"""
import math 
import matplotlib.pyplot as plt
N=10
X=[]
Y=[]
Z=[]
for i in range(1,N+1):
    x=i
    y=math.log(x)
    z=math.sqrt(x)
    X.append(x)
    Y.append(y)
    Z.append(z)
plt.plot(X,Y,"o-",label='estação 1')
plt.plot(X,Z,"^-",label='estação 2')
plt.xlabel('tempo')
plt.ylabel('temperatura')
plt.grid()
plt.legend()
plt.show()

