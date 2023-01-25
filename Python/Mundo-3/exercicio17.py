#Faça um programa que ajuda um jogar da MEGA SENA a cria PALPITES. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 número entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random
import time

a = "Jogos da Mega-Sena"
print("-="*15)
print(f"{a:^30}")
print("-="*15)
qntjogos = int(input("Quantos jogos irá sortear?: "))
jogos = []

print("-="*15)
print("Imprimindo Jogos:")
for i in range(0,qntjogos):
    for numero in range(0,6):  
        num = random.randint(1,60)
        if num not in jogos:
            jogos.append(num)
        else:
            while num in jogos:
                num = random.randint(1,60)
                if num not in jogos:
                    break
            jogos.append(num)
    time.sleep(1)
    jogos.sort()
    print("Jogo {}: {}".format(i+1,jogos))
    jogos.clear()