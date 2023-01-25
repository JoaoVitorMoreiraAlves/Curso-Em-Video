#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

frase = str(input("Digite a frase: ")).strip().upper().split()
frase = "".join(frase)

inverso = ""
for i in range(len(frase) -1, -1, -1):
    inverso += (frase[i])

print("A frase inicial {} de forma inversa {}".format(frase,inverso),end="")
if inverso == frase:
    print("\nÉ um Palindromo")
else:
    print("\nNão é um Palindromo")