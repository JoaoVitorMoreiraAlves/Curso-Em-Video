#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno1 = input("Digite o primeiro nome: ")
aluno2 = input("Digite o segundo nome: ")
aluno3 = input("Digite o terceiro nome: ")
aluno4 = input("Digite o quarto nome: ")

lista = [aluno1,aluno2,aluno3,aluno4]
print('-'*70)
print("A ordem de apresentações será de {}".format(random.sample(lista,4)))
print('-'*70)
print("Ou assim\n")

random.shuffle(lista)
print("A ordem será: ")
print(lista)
print('-'*70)