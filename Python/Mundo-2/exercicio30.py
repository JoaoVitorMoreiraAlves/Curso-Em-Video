
opinador = total = menor = maior = cont = 0


while opinador != "N":
    num = int(input("Digite um número: "))
    cont += 1
    total += num
    if cont == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opinador = str(input("Quer Cotinuar? [S/N]: ")).upper().strip()[0]

print("Você digitou {} números e a média foi de {:.2f}".format(cont,total/cont))
print("O maior valor foi {} e o menor foi {}".format(maior,menor))