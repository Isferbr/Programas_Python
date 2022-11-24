from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'sistema_menu.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
#if arquivoExiste(arq):
#    print('Arquivo encontrado com sucesso!')
#else:
#     print('Arquivo não encontrado!')

while True:
    cabeçalho('SISTEMA ARQUIVO v1.0')
    resposta = menu(['Criar Arquivo','Cadastrar Pessoas','Listar Pessoas','Sair do Sistema'])
    if resposta == 1:
        #cabeçalho('Opção 1')
        cabeçalho('ARQUIVO NOVO')
        nome = str(input('Digite o nome do novo arquivo (nome.txt): '))
        if not arquivoExiste(nome):
            criarArquivo(nome)
        else:
            print('Arquivo já existe!')
    elif resposta == 2:
        #cabeçalho('Opção 2')
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #cabeçalho('Opção 3')
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 4:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)
    
