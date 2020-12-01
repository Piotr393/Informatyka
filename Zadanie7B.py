from random import randint


lista1 = []

for x in range(10000):
    x = randint(1,20000)
    while x in (lista1):
          x = randint(1,20000)
    while x not in (lista1):
          lista1.insert(1, x)

        
lista1.sort()    
print(lista1)
y = sum(lista1)
y1 = y / 10000
print("suma = ", y)   
print("średnia =" ,y1)
    
z = lista1[5000]
z1 =lista1[5001]
z2 = (z + z1) / 2
print("mediana =", z2)
