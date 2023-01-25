#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O Programa deverá ser capas de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='Desconhecido',gols=0):
    print(f"O jogador {nome} fez {gols} gols no campeonato")


n = str(input("Digite o nome do jogador: "))
g = str(input("Digite quantos gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(gols=g)
else:
    ficha(n,g)