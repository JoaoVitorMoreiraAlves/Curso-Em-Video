#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrado.

num1 = float(input("Digite a largura da parede: "))
num2 = float(input("Digite a altura da parede: "))

print("A sua parede tem a dimensão de {}X{} e a sua área é de {}m² \nPortanto será necessário {} litros de tinta".format(num1,num2,num1*num2,(num1*num2)/2))