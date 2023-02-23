# Calculo de todos os numeros primos entre 2 ate 100
n = 100
primos = []

for i in range(2,n):
    cont = 0
    for j in range(1,i+1):
        if i % j == 0:
            cont += 1
    if cont <=2:
        primos.append(i)
print(primos)
    



        
