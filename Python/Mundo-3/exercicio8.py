#Crie um programa onde o usuário possa digitar vários valores número e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.

num = []
aux = 0
opinador = ""
while True:
    aux = int(input("Digite um número: "))

    if aux in num:
        print("Esse número ja existe na lista então não será adicionado")
    else:
        print("Valor adicionado com sucesso")
        num.append(aux)
    
    while opinador != "S" and opinador != "N":
        opinador = str(input("Deseja Continuar? [S/N]: ")).upper()[0]
    if opinador == "S":
        opinador = ""
    elif opinador == "N":
        break

print(f"A lista digitada foi {num}")
num.sort()
print(f"E a lista ordenada é {num}")