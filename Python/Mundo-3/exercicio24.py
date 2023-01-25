#Aprimore o Desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aprovietamento de cada jogador.

time = []
jogador = {}
opinador = ""
gols = []
while True:
    jogador["Nome"] = str(input("Digite o nome do jogador: "))
    jogador["QntJogos"] = int(input(f"Qual a quantidade de jogos do jogador {jogador['Nome']}: "))
    for i in range(0,jogador["QntJogos"]):
        gols.append(int(input(f"Quantos gols na {i+1}º partida: ")))
    jogador["Gols"] = gols[:]
    jogador["tot"] = 0
    for i in gols:
        jogador["tot"] += i
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    while opinador != "N" and opinador != "S":
        opinador = str(input("Deseja continuar? [S/N]: ")).upper()[0]
    if opinador == "N":
        opinador = ""
        break
    opinador = ""

print("-="*30)
print("Cod  Nome                Gols              Total")
print("-"*60)

for i in range(0,len(time)):
    print(f"{i+1:<2} {time[i]['Nome']:<20} {time[i]['Gols']} {time[i]['tot']:>13}")

print("-"*60)

while True:
    while opinador != "N" and opinador != "S":
        opinador = str(input("Deseja Ver os dados de algum jogador em especifico? [S/N]: ")).upper()[0]
    if opinador == "N":
        break
    aux = int(input("Digite o número do jogador: "))
    if aux > len(time):
        print("Valor digitado errado")
    else:   
        aux = aux - 1
        print("-"*60)
        print(f"DADOS DO JOGADOR {time[aux]['Nome']}")
        print("-"*60)
        for k in range(0,len(time[aux]["Gols"])):
            print(f"No jogo {k+1} fez {time[aux]['Gols'][k]} gols")
        print("-"*60)
    opinador = ""
print("FINALIZANDO....")