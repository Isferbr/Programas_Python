# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), multiplicação(*) e divisão(/). Exiba o resultado da operação solicitada.

n1 = float(input('Digite o 1º número: '));
n2 = float(input('Digite o 2º número: '));

operacao = input('''Digite a opearação matemática que deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

if(operacao == '+'):
	print('{} + {} = '.format(n1,n2));
	print(n1 + n2);

elif(operacao == '-'):
	print('{} - {} = '.format(n1,n2));
	print(n1 - n2);

elif(operacao == '*'):
	print('{} * {} = '.format(n1,n2));
	print(n1 * n2);

elif(operacao == '/'):
	print('{} / {} = '.format(n1,n2));
	print(n1 / n2);

else:
	print('Você não digitou um operador válido, execute o programa novamente.');

