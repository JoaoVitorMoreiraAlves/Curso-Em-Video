#Faça um mini-sistema que utilize o Interactive Help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará.
#Obs use cores.
from time import sleep
def linha(txt,cor):
    print(cor)
    print("~"*(len(txt)+4))
    print(f"  {txt}")
    print("~"*(len(txt)+4))
    print("\033[m")


def ajuda(func):
    linha("Acessando a biblioteca {}".format(func),"\033[4;37;43m")
    sleep(2)
    print("\033[0;31;47m")
    help(func)
    print("\033[m")

func = ""
while func != "fim":
    sleep(1)
    linha("SISTEMA DE AJUDA PyHELP","\033[4;37;44m")
    func = str(input("Digite a Função ou Biblioteca: ")).lower()
    if func != "fim":
        ajuda(func)
print("Finalizando....")
sleep(1)