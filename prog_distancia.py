# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km, e R$ 0,45 para viagens mais longas.

d = float(input('Digite a distância que deseja percorrer (km): '));

if(d <= 200):
	p = 0.5*d;
	print('O valor da viagem é: {}'.format(p));
else:
	t = 0.45*d;
	print('O valor da viagem é: {}'.format(t));

