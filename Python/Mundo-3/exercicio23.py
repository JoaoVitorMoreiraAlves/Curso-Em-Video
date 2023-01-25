#Crie um programa que leia NOME,SEXO,IDADE de varias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B)A média de idade do grupo.
#C) Uma lista com todos as mulheres.
#D) Uma lista com todas as pessoas com idade acima da média.

turma = []
pessoa = dict()
opinador = ""
media = 0
while True:
    pessoa["Nome"] = str(input("Digite o nome: "))
    pessoa["Sexo"] = str(input("Digite o sexo [M/F]: ")).upper()[0]
    while pessoa["Sexo"] != "M" and pessoa["Sexo"] != "F":
        print("Erro!! Por favor digite apenas M ou F")
        pessoa["Sexo"] = str(input("Digite o sexo [M/F]: ")).upper()[0]
    pessoa["Idade"] = int(input("Digite a idade: "))
    while opinador != "S" and opinador != "N":
        opinador = str(input("Deseja continuar? [S/N]: ")).upper()[0]
    turma.append(pessoa.copy())
    if opinador == "N":
        break
    opinador = ""
for i in range(0,len(turma)):
    media += turma[i]["Idade"]

media = media / len(turma)
print("-="*30)
print("RESULTADOS")
print("-="*30)

print(f"Foram cadastradas um total de {len(turma)} pessoas")
print(f"A média de idade do grupo é de {media:.2f} anos")
print("As mulheres do grupo são: ",end="")
for i in range(0,len(turma)):
    if turma[i]["Sexo"] == "F":
        print(f"{turma[i]['Nome']}, ",end="")
print("\nAs pessoas com a idade acima da média são: ")
for i in range(0,len(turma)):
    if turma[i]["Idade"] > (media):
        print(f"{turma[i]['Nome']}, do sexo {turma[i]['Sexo']} com {turma[i]['Idade']} anos \n",end="")