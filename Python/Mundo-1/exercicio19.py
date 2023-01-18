#Faça um programa que leia o comprimento do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
#O teorema de Pitágoras diz que a soma do quadrado dos catetos é sempre igual ao quadrado da hipotenusa.
from math import hypot,pow,sqrt

oposto = float(input("Digite o cateto oposto: "))
adjacente = float(input("Digite o cateto adjacente: "))
print('-'*60)
print("Como o valor do Cateto oposto é de {} e do cateto adjacente é de {} \nO valor da hipotenusa é de {:.2f}".format(oposto,adjacente,sqrt((pow(oposto,2)+pow(adjacente,2)))))
print('-'*60)
print("Ou assim {:.2f}".format(hypot(oposto,adjacente)))