#Aprimore o desafio anterior mostrando no final:
#A) a soma de todos os valores pares digitados
#B) a soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[],[],[],
          [],[],[],
          [],[],[]]
par = coluna3 = maior = 0
for i in range(0,9):
    matriz[i].append(int(input("Digite o valor: ")))
    if matriz[i][0] % 2 == 0:
        par += matriz[i][0]
    if i == 2 or i == 5 or i == 8:
        coluna3 += matriz[i][0]
    if i == 3:
        maior = matriz[i][0]
    elif i == 4 or i == 5:
        if matriz[i][0] > maior:
            maior = matriz[i][0]

print("-="*15)
print("MATRIZ 3X3")
print("-="*15)
for i in range(0,9):
    if i == 0:
        print("|  ",end="")
    if i == 3 or i == 6:
        print("|\n|  ", end="")
    print(f"{matriz[i][0]:>2}  ",end="")
print("|")

print(f"A soma dos valores pares é igual a : {par}")
print(f"A soma da terceira coluna é de: {coluna3}")
print(f"O maior da segunda linha é {maior}")



print("-="*15)
print("Jeito do GUANABARA")
print("-="*15)
lista = [[0,0,0],
        [0,0,0],
        [0,0,0]]
pares = mai = colunaa =0
for linha in range(0,3):
    for coluna in  range(0,3):
        lista[linha][coluna] = int(input(f"Digite um valor na matriz [{linha},{coluna}]: "))
        if lista[linha][coluna] % 2 == 0:
            pares += lista[linha][coluna]
        if lista[linha][2]:
            colunaa += lista[linha][2]
for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{lista[linha][coluna]:^5}]",end="")
    print()

for c in range(0,3):
    if c == 0:
        mai = lista[1][c]
    elif lista[1][c] > mai:
        mai = lista[1][c]
print(f"O maior valor da segunda linha é {mai}")
print(f"A soma dos pares é {pares}")
print(f"A soma da terceira coluna é {colunaa}")
