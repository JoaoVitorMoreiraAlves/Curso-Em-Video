#Escreva um programa que leia a velocidde de um carro
#Se ele ultrapassar 80Km/H, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar 7 reais por cada Km acim do limite.

km = int(input("Digite a velocidade do carro em KM: "))

if km <= 80:
    print("Muito bem!!! Você está dirigindo respeitando as leis")
else:
    a = km - 80
    print("Que feio!!! Você está dirigindo {} km/h acima do limite de velocidade e será punido no valor de {} reais".format(a,a * 7))