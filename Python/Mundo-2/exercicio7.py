#Refaça o Desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero todos os lados iguais
#Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

print("-=-"*20)
print("Triângulos")
print("-=-"*20)

reta1 = float(input("Digite a primeira reta: "))
reta2 = float(input("Digite a segunda reta: "))
reta3 = float(input("Digite a terceira reta: "))

if (reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2):
    if (reta1 == reta2 == reta3):
        print("É um triângulo Equilátero, pois todos os seus lados possuem o mesmo valor")
    elif (reta1 != reta2 and reta1 != reta3 and reta2 != reta3):
        print("É um triângulo Escaleno, pois todos os seus lados são diferentes")
    else:
        print("É um triangulo isósceles, pois dois dos seus lados são iguais")
else:
    print("Não é possível criar um Triângulo!!!1")