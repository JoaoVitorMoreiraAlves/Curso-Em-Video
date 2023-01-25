#Faça um programa que tenha uma função chamada contador(). que receba três parâmetros: inicio, fim e passo e realiza a contagem.
#Seu programa tem que realizar três contagens através da função criada:
#De 1 até 10, de 1 em 1
#De 10 até 0, de 2 em 2
#Uma contagem personalizada.
from time import sleep
def contador(inicio,fim,passo):
    if passo < 0:
            passo = passo*-1
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f"{cont} ",end="", flush=True)
            sleep(0.5)
            cont += passo
        print("FIM!!")
        print("-="*30)
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ",end="", flush= True)
            sleep(0.5)
            cont -= passo
        print("FIM!!")
        print("-="*30)


contador(1,10,1)
contador(10,0,1)

print("Contagem Personalizada")
print("-="*30)
inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite o passo: "))
contador(inicio,fim,passo)