#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input("Digite o salário: R$"))
print('-'*90)
print("O salário era de R${} e depois do aumento de 15% passou a ganhar R${:.2f} Reais".format(salario,(salario*0.15)+salario))