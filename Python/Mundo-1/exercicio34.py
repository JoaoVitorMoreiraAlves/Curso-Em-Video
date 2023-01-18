#Desenvolva um programa que pergunta a distância de uma viagem em KM, Calcule o preço da passagem, cobrando 0,50 centavos por KM para viagens com até 200KM, a 0,45 centavos para viagens mais longas.

km = float(input("Digite a quantidade de KM da viagem: "))
if km > 200:
    print("O valor da viagem é de R${:.2f} reais".format(km * 0.45))
else:
    print("O valor da viagem é de R${:.2f} reais".format(km * 0.5))