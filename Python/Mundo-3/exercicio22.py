#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato.

jogador = dict()
i = 0
jogador["Nome"] = str(input("Digite o nome do jogador: "))
gols = []
qntjogos = int(input(f"Quantos jogos o jogador {jogador['Nome']} jogou?: "))
for cont in range(0,qntjogos):
    gols.append(int(input(f"Quantos gols na partida {cont+1}: ")))
    i += gols[cont]
jogador["Gols"] = gols[:]
jogador["Total"] = i

print("-="*30)
print("Resultados")
print("-="*30)
print(jogador)
print("-="*30)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("-="*30)
print(f"O jogador {jogador['Nome']} jogou {qntjogos} partidas.")

for i in range(0,qntjogos):
    print(f"   ==> Na partida {i+1}, fez {jogador['Gols'][i]} gols.")
print(f"Foi um total de {jogador['Total']} gols.")