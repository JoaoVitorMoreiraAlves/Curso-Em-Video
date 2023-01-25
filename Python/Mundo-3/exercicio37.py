# Adpte o código do desafio 107, criado uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

from utilidadeCeV import moeda

n = 1000
aumento = 15
diminui = 20

print("-="*30)
print(f"A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}")
print("-="*30)
print(f"O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}")
print("-="*30)
print(f"Aumentando {aumento}%, temos {moeda.moeda(moeda.aumenta(n,aumento))}")
print("-="*30)
print(f"Reduzindo {diminui}%, temos {moeda.moeda(moeda.diminui(n,diminui))}")