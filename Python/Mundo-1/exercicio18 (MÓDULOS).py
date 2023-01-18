#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Exemplo : Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

from math import floor,trunc

num1 = float(input("Digite um número: "))
print('-'*50)
print("A porção inteira do número {} é {}".format(num1,floor(num1)))
print('-'*50)
print("Também é possivel utilizar assim {}".format(trunc(num1)))
print('-'*50)
print("Assim tambem {}".format(int(num1)))