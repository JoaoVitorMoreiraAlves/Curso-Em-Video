#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(*num):
    maior = 0
    if len(num) == 0:
        print("Nenhum valor")
    else:
        print("A lista é ",end="")
        for i in num:
            print(f"{i} ",end="")
        print("e o maior valor é o ", end="")
        for i in range(0,len(num)):
            if i == 0:
                maior = num[i]
            if num[i] > maior:
                maior = num[i]
        print(f"{maior}")


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()