# Escreva um programa que leia 10 números digitados pelo usuário e mostre como resultado pro usuário a soma dos 10 números digitados. OBS: utilize uma estrutura de repetição (for ou while) na sua resposta.
soma = 0
for x in range(1,11):
    n = float(input('Digite um número: '))
    soma += n

print(soma)
  
   
