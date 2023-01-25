#Crie um programa que vai ler vários números e colocar em uma lista, depois disso, mostre:
#A) Quantos números foram digitados
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

num = []
opinador = ""
while True:
    num.append(int(input("Digite o valor: ")))

    while opinador != "N" and opinador != "S":
        opinador = str(input("Deseja continuar? [S/N]: ")).upper()[0]
    
    if opinador == "N":
        break
    else:
        opinador = ""

print(f"Lista: {num}")
print("O total de elementos da lista: {}".format(len(num)))
num.sort(reverse=True)
print("A lista Decrescente é: {}".format(num))
if 5 in num:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")