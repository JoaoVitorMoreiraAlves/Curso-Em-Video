#Escreva um programa que aprova o empréstimo bancário para a compra de uma casa.O Programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salaário ou então o empréstimo será negado.

casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite em quantos anos será pago o empréstimo: "))

if ((casa/(anos *12)) > (salario*0.3)):
    print("ERRO! Não foi possível realizar o empréstimo bancário pois o empréstimo ultrapassa os 30""%"" do salário\nEmpréstimo {:.2f}\n30""%"" do salário {}".format((casa/(anos *12)),salario*0.3))
else:
    print("O empréstimo foi realizado com sucesso!!!\nA prestação mensal será de {:.2f} e a quitação acontecerá em {} meses".format((casa/(anos*12)), anos*12))