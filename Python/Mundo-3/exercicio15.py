#Crie um programa que crie uma matriz de dimensão 3X3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela com a formatação correta.
#Exemplo de Matriz:
# 1 2 3
# 4 5 6
# 7 8 9

matriz = [[],[],[],
          [],[],[],
          [],[],[]]
for i in range(0,9):
    matriz[i].append(int(input("Digite o valor: ")))

print("-="*15)
print("MATRIZ 3X3")
print("-="*15)
for i in range(0,9):
    if i == 0:
        print("|  ",end="")
    if i == 3 or i == 6:
        print("|\n|  ", end="")
    print(f"{matriz[i][0]} ",end="")
print("|")


print("-="*15)
print("JEITO DO GUANABARA")
print("-="*15)

lista = [[0,0,0],
        [0,0,0],
        [0,0,0]]

for linha in range(0,3):
    for coluna in  range(0,3):
        lista[linha][coluna] = int(input(f"Digite um valor na matriz [{linha},{coluna}]: "))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{lista[linha][coluna]:^5}]",end="")
    print()