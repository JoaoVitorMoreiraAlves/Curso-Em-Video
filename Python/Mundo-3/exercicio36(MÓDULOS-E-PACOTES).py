#Crie um módulo chamada moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), metade().
# Faça também um programa que importe esses módulos e use algumas dessas funções.
from utilidadeCeV import moeda

n = float(input("Digite o preço R$: "))
aumento = int(input("Quantos % vai aumentar?: "))
diminui = int(input("Quantos % vai diminuir?: "))

print("-="*30)
print(f"A metade de {n} é {moeda.metade(n)}")
print("-="*30)
print(f"O dobro de {n} é {moeda.dobro(n)}")
print("-="*30)
print(f"Aumentando {aumento}%, temos {moeda.aumenta(n,aumento)}")
print("-="*30)
print(f"Reduzindo {diminui}%, temos {moeda.diminui(n,diminui)}")