#Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o deicionário recberá também o ano de contratação e o slaário. Calcule e acrescente, além da idade com quantos anos a pessoas vai se aposentar.
#(se aposenta dps de 35 anos de trabalho)
import datetime
pessoa = dict()

pessoa["Nome"] = str(input("Digite o nome: "))
pessoa["Idade"] = datetime.date.today().year- int(input("Digite a data de nascimento: "))
pessoa["CTPS"] = int(input("Digite o número da carteira de trabalho (caso não tenha digite 0): "))

if pessoa["CTPS"] == 0:
    del pessoa["CTPS"]
else:
    pessoa["Contratação"] = int(input("Digite o ano de contratação: "))
    pessoa["Salário"] = float(input("Digite o salário: "))
    pessoa["Aposentarioa"] = pessoa["Idade"] + ((pessoa["Contratação"] + 35) - datetime.date.today().year)
for k,v in pessoa.items():
        print(f"{k} é igual a {v}")