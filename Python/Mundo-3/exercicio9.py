#Crie um programa onde o usuario possa digitar cinco valores númericos e cadastre-os em uma lista já na posição correta de inserção (SEM USAR O SORTE())
#No final mostre a lista ordenada na tela.

num = []
aux = 0
troca = 1
for i in range(0,5):
    num.append(int(input("Digite um valor: ")))

print("Deixando a lista em crescente com Bubble Sort")
print("Lista normal: {}".format(num))
while (troca == 1):
    troca = 0
    for i in range(0,4):
        if (num[i] > num[i+1]):
            troca = 1
            aux = num[i]
            num[i] = num[i+1]
            num[i+1] = aux
print(f'Lista Arrumada: {num}')

print("-="*30)
print("Deixando a lista em crescente sem sort(), de forma simples")

lista = []

for c in range(0,5):
    n = int(input("Digite um valor: "))

    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("Adicionado no final da lista")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f"Adicionado na posição {pos}")
                break
            pos += 1
print("-=" *30)
print("A lista crescente é {}".format(lista))