#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão 20% de juros

preco = float(input("Digite o preço do produto: "))
opinador = int(input("""
Escolha a opção de pagamento
Digite [  1  ] para pagar à vista
Digite [  2  ] para pagar no cartão à vista
Digite [  3  ] para pagar no cartão em até 2x
Digite [  4  ] para pagar no cartão 3x ou mais
Qual sua opção?: """))

if (opinador == 1):
    print("Você selecionou pagar à vista no dinheiro/cheque e ganha um desconto de 10% portanto o valor final do produto será de {} reais".format(preco - (preco * 0.1)))
elif (opinador == 2):
    print("Você selecionou pagar à vista no cartão e ganhou um desconto de 5% portanto o valor final do produto será de {} reais".format(preco - (preco * 0.05)))
elif (opinador == 3):
    print("Você selecionou pagar em até 2x no cartão e o preço do produto não sofrerá desconto nem juros ficando em {} reais".format(preco))
elif (opinador == 4):
    print("Você selecionou pagar em 3x ou mais no cartão e receberá um juros de 20% portanto o valor final do produto será de {} reais".format(preco + (preco * 0.2)))
else:
    print("\033[31mComo não foi selecionado a forma de pagamento corretamente a compra será cancelada\033[m")