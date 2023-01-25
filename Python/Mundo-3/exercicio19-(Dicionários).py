#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

pessoa = dict()
pessoa["Nome"] = str(input("Digite o nome: "))
pessoa["Media"] = float(input("Digite a média: "))
print("-="*30)

if pessoa["Media"] >= 7:
    pessoa["Situacao"] = "Aprovado"
elif pessoa["Media"] >= 5:
    pessoa["Situacao"] = "Recuperação"
else:
    pessoa["Situacao"] = "Reprovado"

for keys, value in pessoa.items():
    print(f"{keys} é igual a {value}")