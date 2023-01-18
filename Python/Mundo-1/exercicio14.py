#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

num = float(input("Digite o preço: R$"))

print("O preço {} com 5% de desconto fica no valor de {:.2f}".format(num,num - num*0.05))