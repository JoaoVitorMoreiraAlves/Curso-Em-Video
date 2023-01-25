#Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergute ao usuário qual será o valor a ser sacado (número inteiro) e o prograa vai informar quantas cédulas de cada valor serão entregue.
# OBS considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("="*30)
print("{:^30}".format("Banco dos Devs"))
print("="*30)

valor = int(input("Qual valor você deseja sacar?: "))
total = valor
totalcedula = 0
cedula = 50
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        print("Total de {} cédulas de R$ {}".format(totalcedula,cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break