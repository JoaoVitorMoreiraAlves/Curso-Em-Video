#Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA (Progreção Aritimética). No final, mostra os 10 primeiros termos dessa progressão.

print("--*--" * 5)
print("10 Termos de uma PA")
print("--*--" * 5)
termo = int(input("Digite o PRIMEIRO TERMO da PA: "))
razao = int(input("Digite a RAZÃO da PA: "))

for c in range(termo, (termo + (10-1) * razao) + razao,razao):
    print(c, "-> ", end="")
print("Acabou")