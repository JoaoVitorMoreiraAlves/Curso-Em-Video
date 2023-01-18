#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0.15 por KM Rodado.

km=float(input("Digite a quantidade de Km rodados: "))
dias=int(input("Digite os dias alugados: "))
print('-'*80)
print("Como o carro rodou {}Km durante {} dias o preço a se pagar é de R${:.2f} Reais".format(km,dias,(dias*60)+(km*0.15)))