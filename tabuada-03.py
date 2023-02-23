# Escreva programa que exiba uma lista de opções
# (menu): adição, subtração, divisão, multipli-
# cação e sair. Imprima a tabuada da operação
# escolhida, para um número informado pelo
# usuário. Repita até que a opção de saída
# seja escolhida
#
print ('1. Adicao')
print ('2. Subtracao')
print ('3. Multiplicacao')
print ('4. Divisao')
print ('5. Sair')
opcao = input ('Opcao: ')

while opcao != '5' :
    tabuada = int( input ('Numero: '))
    
    i = 1
    while i <= 10 :
        if opcao == '1' :
           n = tabuada + i
           print ('{0:2d} + {1:2d} = {2:3d}'.format(tabuada,i,n))
        elif opcao == '2':
           n = tabuada - i
           print ('{0:2d} - {1:2d} = {2:3d}'.format(tabuada,i,n))
        elif opcao == '3':
           n = tabuada * i
           print ('{0:2d} * {1:2d} = {2:3d}'.format(tabuada,i,n))
        elif opcao == '4':
           n = tabuada / i
           print ('{0:2d} / {1:2d} = {2:.3f}'.format(tabuada,i,n))
        i = i + 1

    print ('1. Adicao')
    print ('2. Subtracao')
    print ('3. Multiplicacao')
    print ('4. Divisao')
    print ('5. Sair')
    opcao = input ('Opcao: ')

print ('**** FIM *****')

    