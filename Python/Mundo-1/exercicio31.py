# Crie um programa que faça um computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
#O progrmador deverá escrever na tela se o usuário perdeu ou vendeu.
import random
import time
print("-=-"*20)
print("Vou pensar em um número entre 0 e 5 tente adivinhar")
print("-=-"*20)

num = int(input("Digite o número entre 0 e 5: "))

print("PROCESSANDO...")
time.sleep(1)
num2 = random.randint(0,5)

if num == num2:
    print("\033[4;32;47mO número são iguais! Você Venceu\033[m")
else:
    print("\033[4;31;47mO número está diferente!VOCÊ PERDEU\033[m")
print("O número escolhido pelo computador foi {}".format(num2))