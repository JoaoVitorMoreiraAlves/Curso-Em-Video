#Crie um programa que tenha uma TUPLA única com NOMES DE PRODUTOS e seus respectivos PREÇOS na sequência.
#No final, mostre uma listagem de preços, organizndo os dados em forma tabular.

tupla = ("Pao", 5, 
        "Leite", 8,
        "Frango", 15.50,
        "Danone", 3)
num = 1

print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)
for c in range(0,len(tupla)):
    if c % 2 == 0:
        print(f"Preço: {tupla[c]:.<30}", end="")
    else:
        print(f"Preço R$: {tupla[c]:>6.2f}")
print("="*50)