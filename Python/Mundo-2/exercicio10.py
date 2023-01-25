#Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
import time
lista = choice(["Pedra", "Papel", "Tesoura"])

print("Vamos jogar jokenkô? então:")
jogador = str(input("Digite pedra, papel ou tesoura para jogar: ")).upper()
print("Jo")
time.sleep(1)
print("ken")
time.sleep(1)
print("pô")

if (lista == "Pedra" and jogador == "PAPEL"):
    print("\033[32mPARABÉNS você venceu a máquina jogou Pedra\033[m")
elif (lista == "Papel" and jogador == "TESOURA"):
    print("\033[32mPARABÉNS você venceu a máquina escolheu Papel\033[m")
elif (lista == "Tesoura" and jogador == "PEDRA"):
    print("\033[32mPARABÉNS você venceu a máquina escolheu Tesoura\033[m")
elif (lista.upper() == jogador):
    print("\033[33mDeu empate ambos jogaram {}\033[m".format(lista))
else:
    print("\033[31mVocê perdeu a máquina jogou {}\033[m".format(lista))