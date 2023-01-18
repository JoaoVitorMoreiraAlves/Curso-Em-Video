#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite o nome: ")).strip()

nome = nome.split()
num = len(nome)
print("-"*40)
print("Primeiro:",nome[0])
print("-"*40)
print("Último:",nome[num-1])