#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses Resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
print("-="*30)
print("JOGADO DADOS")
print("-="*30)

pessoas = {"Nome":["","","",""],"Dado":[randint(1,6),randint(1,6),randint(1,6),randint(1,6)]}


for i in range(0,4):
    pessoas["Nome"][i]=str(input("Digite o nome: "))
print(pessoas)

print("-="*30)
print("CARREGANDO RESULTADOS")
print("-="*30)
sleep(1)
for i in range(0,4):
    sleep(0.5)
    print(f"O jogador: {pessoas['Nome'][i]} rodou o dado e ganhou o número: {pessoas['Dado'][i]}")

print("-="*30)
print("CARREGANDO RESULTADOS EM ORDEM DO VENCEDOR AO PERDEDOR")
print("-="*30)
sleep(1)

#Bubble Sort em Dicionário
for i in range(len(pessoas["Dado"])):
    for j in range(len(pessoas["Dado"])-1):
        if pessoas["Dado"][j] > pessoas["Dado"][j+1]:
            aux = pessoas["Dado"][j+1]
            pessoas["Dado"][j+1] = pessoas["Dado"][j]
            pessoas["Dado"][j] = aux

            aux = pessoas["Nome"][j+1]
            pessoas["Nome"][j+1] = pessoas["Nome"][j]
            pessoas["Nome"][j] = aux
auxiliar = 1
for i in range(len(pessoas["Dado"])-1,-1,-1):
    print(f"{auxiliar} lugar: {pessoas['Nome'][i]} rodou o dado e ganhou o número: {pessoas['Dado'][i]}")
    auxiliar += 1
