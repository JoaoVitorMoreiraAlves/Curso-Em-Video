#Faça um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artificios, indo de 10 até 0, com uma pausa de 1 segundo entre elas

import time

for i in range(10, -1, -1):
    print("{}".format(i))
    time.sleep(1)
print("BOOOOOOOOOOM! POOW! POWW!\nSÃO OS FOGOS")