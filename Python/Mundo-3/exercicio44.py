#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema só vai ter 2 opções: 
#Cadastrar uma nova pessoas 
#Listar todas as pessoas cadastradas.
from utilidadeCeV.interface import *
from utilidadeCeV.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoExite(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas","Cadastrar Pessoa","Sair do Programa"])
    if resposta == 1:
        #Opção de Ver pessoas cadastradas
        lerArquivo(arq)

    elif resposta == 2:
        #Opção para Cadastrar Pessoa
        cabecalho("Novo Cadastro")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabecalho("\033[33mFinalizando o programa...\033[m ")
        sleep(2)
        break
    else:
        print("\033[31mERRO!! Digite uma opção válida!\033[m")
    sleep(2)