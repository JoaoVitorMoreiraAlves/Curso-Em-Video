#Crie um Programa que leia o nome da pessoa completo e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo sem consierar espaços
#Quantas letras tem o primeiro nome

nome = str(input("Digite o nome: ")).strip()

print('-'*50)
print("Seu nome em maiúsculas é:",nome.upper())
print('-'*50)
print("Seu nome em minpusculas é:",nome.lower())
print('-'*50)

print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print('-'*50)
nome = nome.split()
print("O primeiro nome {} possui {} letras".format(nome[0], len(nome[0])))
print('-'*50)