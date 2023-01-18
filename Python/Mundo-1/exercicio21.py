#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

lista = [aluno1,aluno2,aluno3,aluno4]
print('-'*50)
print("O Aluno que deverá limpar o quadro será o(a) {}".format(choice(lista)))