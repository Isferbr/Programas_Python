# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%, para os inferiores ou iguais, um aumento de 15%.

s = float(input('Digite seu salario: '));

if(s > 1250):
	a = s*(1.10);
	print('O valor é: {}'.format(a));
else:
	m = s*(1.15);
	print('O valor é: {}'.format(m));
	
