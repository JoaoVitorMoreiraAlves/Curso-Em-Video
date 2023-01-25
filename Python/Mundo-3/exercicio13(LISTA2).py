#Faça um programa que leia NOME E PESO de várias pessoas. guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas
#C) Uma listagem com as pessoas mais leves

pessoa = []
turma = []
cont = 0
opinador = ""
pesada = []
leve = []
while True:
    pessoa = (str(input("Digite o nome: ")),
        float(input("Digite o peso: ")))
    turma.append(pessoa[:])
    if cont == 0:
        pesada.append(pessoa)
        leve.append(pessoa)
    else:
        if pesada[0][1] == pessoa[1]:
            pesada.append(pessoa)
        elif pesada[0][1] < pessoa[1]:
            pesada.clear()
            pesada.append(pessoa)
        elif leve[0][1] > pessoa[1]:
            leve.clear()
            leve.append(pessoa)
    cont += 1
    while opinador != "N" and opinador != "S":
        opinador = str(input("Deseja continuar? [S/N]: ")).upper()[0]
    if opinador == "N":
        break
    else:
        opinador = ""

print("-=-"*30)
print(f"Foram cadastrada {cont} pessoas")
print("-=-"*30)
print(f"Total de pessoas {turma}")
print("-=-"*30)
print(f"Os mais pesados possuem {pesada[0][1]} KG e são as seguintes pessoas que possuem esse peso: ",end="")
for p in turma:
    if p[1] == pesada[0][1]:
        print(f"{p[0]} -> ",end="")
print("FIM")
print("-=-"*30)
print(f"Os mais leves possuem {leve[0][1]} KG e são as seguintes pessoas que possuem esse peso: ", end="")
for p in turma:
    if p[1] == leve[0][1]:
        print(f"{p[0]} -> ",end="")
print("FIM")