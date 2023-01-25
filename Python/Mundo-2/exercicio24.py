#Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar:
# [2] multiplicar:
# [3] maior:
# [4] novos números:
# [5] sair do programa
# Seu programa deverá realizar a operção solicitada em cada caso.
import time

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
opinador = 0

while opinador != 5:
    opinador = int(input("""    [  1  ] Somar
    [  2  ] Multiplicar
    [  3  ] Maior
    [  4  ] Novos números
    [  5  ] Sair do Programa
    Escolha sua opção: """))
    print("=="*20)
    if opinador == 1:
        print("A soma entre {} e {} é de {}".format(num1,num2,num1+num2))
    elif opinador == 2:
        print("A multiplicação entre {} e {} é de {}".format(num1,num2,num1*num2))
    elif opinador == 3:
        if num1 > num2:
            print("O número {} é maior que o {}".format(num1,num2))
        elif num2 > num1:
            print("O número {} é maior que o {}".format(num2,num1))
        else:
            print("Os valores são iguais")
    elif opinador == 4:
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))
    elif opinador == 5:
        print("Finalizando....")
        time.sleep(3)
    else:
        print("Opção inválida, escolha outra")
print("Programa finalizado com sucesso!! Volte sempre")