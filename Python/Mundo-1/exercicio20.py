#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin,cos,tan,radians

angulo = float(input("Digite o valor do ângulo: "))

seno = sin(radians(angulo))
cose = cos(radians(angulo))
tang = tan(radians(angulo))
print('-'*40)
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo,seno))
print('-'*40)
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo,cose))
print('-'*40)
print("O ângulo de {} tem a TÂNGENTE de {:.2f}".format(angulo,tang))
print('-'*40)