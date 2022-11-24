# Escreva um programa que recebe duas notas de um aluno, calcula a média dessas notas e diz qual a situação do aluno: Aprovado (se nota a maior ou igual a 7.0), Reprovado (se nota menor que 4.0) ou de Prova Final (se maior ou igual a 4.0 e menor que 7.0).

n1 = float(input('Digite a 1ª nota: '));
n2 = float(input('Digite a 2ª nota: '));

m = (n1 + n2)/2;

if(m >= 7):
	print('Aprovado');
elif(m >= 4):
	print('Prova Final');
else:
	print('Reprovado');
