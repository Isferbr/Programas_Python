
# Entrada do nome
nome = input('Digite o seu nome: ')
# Entrada do peso
peso = float(input('Digite seu peso: '))
# Entrada da altura
altura = float(input('Digite sua altura: '))
# Calculo do IMC
imc = peso/(altura*altura)
# Mostra o resultado do IMC
print(f'O resultado do seu IMC é: {imc:,.2f}')
