#Crie um programa que leia o nome de uma cidade e diga se ela
#Começa ou não começa com o nome "SANTO"

cidade = str(input("Digite o nome da cidade: "))
print(cidade)
cidade = cidade.upper().strip().split()

print("SANTO" in cidade[0])
print(cidade)