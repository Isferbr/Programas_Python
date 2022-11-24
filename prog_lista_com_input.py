# Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

loop = True
list = []

while(loop):
    numero = float(input('Digite um número diferente de zero, ou zero para encerrar\n'))
    if numero != 0:
        lista.append(numero)
    else:
        loop = False

    print('A quantidade de valores inseridos é de', len(lista))
    print('A soma dos valores inseridos é de', sum(lista))
    print('A média dos valores inseridos é de', round(sum(list)/len(lista), 2))
