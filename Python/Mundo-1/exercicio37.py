#Escreve um programa que pergunta o salário de um funcionário e calcula o valor do seu aumento.
#Para salários superiores a 1.250 reais calcule um aumento de 10%
#Para os inferiores ou iguals, o aumento é de 15%

salario = float(input("Digite seu salário: "))

if salario > 1250.00:
    print("Você recebeu um aumento de 10%")
    print("Salário atual: {} reais".format(salario + salario*0.10))
else:
    print("Você recebeu um aumento de 15%")
    print('Salário atual: {} reais'.format(salario + salario * 0.15))