#Refaça o Desafio 051, lendo o primeiro termo e razão de uma PA, mostrando os 10 primeiro termos da progressão usando a estrutura while.

primeiro_termo = int(input("Digite o primeiro Termo: "))
razao = int(input("Digite a razao: "))
cont = 0
num = 10
while cont != num:
    print("{} -> ".format(primeiro_termo), end="")
    cont += 1
    primeiro_termo += razao

print("Acabou")