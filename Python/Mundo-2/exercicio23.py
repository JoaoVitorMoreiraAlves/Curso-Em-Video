#Melhore o jogo do Desafio 028 aonde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
from time import sleep
num = int(input("Digite um valor entre 0 e 10: "))
cont = 1
aleatorio = random.randint(0,10)

while num != aleatorio:
    if num < aleatorio:
        print("Mais....", end="")
    elif num > aleatorio:
        print("Menos....", end="")
    num = int(input("Você errou!!! Digite outro valor: "))
    cont += 1
print("\033[34mParabéns você acertou o número é {} e você utilizou {} tentativas\033[m".format(aleatorio,cont))