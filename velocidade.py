# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h.

v = float(input("Digite a velocidade do carro (km/h): "));
m = 5*(v-80);

if(v > 80):
	print("Multado");
	print('O valor a ser pago pela multa é de: {}'.format(m));
else:
	print('Não Multado');


