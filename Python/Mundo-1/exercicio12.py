#Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# 1 DOLAR TA 3.27 reais
num = float(input("Digite quanto de dinheiro a pessoa tem: R$"))

print("A pessoa consegue trocar R${:.2f} Reais por US${:.2f} Dólares".format(num,num/3.27))