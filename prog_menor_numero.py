# Escreva um programa que leia três números e que imprima o maior.

n1 = float(input('Digite o 1º número: '));
n2 = float(input('Digite o 2º número: '));
n3 = float(input('Digite o 3º numero: '));

menor = n1;

if(n2 < menor):
        menor = n2;
if(n3 < menor):
        menor = n3;
        
print('O número menor é: ',menor);
