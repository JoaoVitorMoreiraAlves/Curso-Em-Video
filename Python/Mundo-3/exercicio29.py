#Faça um programa que tenha uma lista chamada número e duas funções, sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anteior.
from random import randint
from time import sleep
def sorteia(lst):
    i = 0
    while i < 5:
        lst.append(randint(1,10))
        i += 1
    print(f"Sorteando 5 valores da lista: ",end="")
    for n in lst:
        sleep(0.5)
        print(f"{n}, ",end="",flush=True)
    print("PRONTO!")
    


def somaPar(lst):
    par = 0
    for i in lst:
        if i%2 == 0:
            par += i
    print(f"A soma dos valores pares de {lst}, temos {par}")


num = []
sorteia(num)
somaPar(num)