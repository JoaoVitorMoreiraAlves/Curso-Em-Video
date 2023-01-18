#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print("-=-"*20)
print("Analisador de Triângulos")
print("-=-"*20)

reta1 = float(input("Digite a primeira reta: "))
reta2 = float(input("Digite a segunda reta: "))
reta3 = float(input("Digite a terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("É possível criar um Triângulo!!!")
else:
    print("Não é possível criar um Triângulo!!!")