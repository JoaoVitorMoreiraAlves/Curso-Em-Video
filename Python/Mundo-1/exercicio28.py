#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite o nome: "))

nome = nome.upper().strip()

print("Seu nome tem Silva?", "SILVA" in nome)