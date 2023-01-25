#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideia
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
from math import pow

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (pow(altura,2))

if (imc < 18.5):
    print("O seu IMC indica que você está Abaixo do Peso ideal")
elif (imc <= 25):
    print("O seu IMC indica que você está no Peso Ideal")
elif (imc <= 30):
    print("O seu IMC indica que você está Sobrepeso")
elif (imc <= 40):
    print("O seu IMC indica que você está com Obesidade")
else:
    print("O seu IMC indica que você está com Obesidade mórbida")