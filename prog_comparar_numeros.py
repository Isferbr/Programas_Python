# Escreva um programa que leia dois números e que imprima o menor.

n1 = float(input('Digite o 1º número: '));
n2 = float(input('Digite o 2º número: '));

if(n1 > n2):
	print('O {} é o menor'.format(n2));
else:
	print('O {} é o menor'.format(n1));

