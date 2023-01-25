#Faça um programa que calcula a soma entre todos os número impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
contador = 0
for i in range(1,501,2):
    if i%3 == 0 :
        contador += 1
        s += i
print("A somatória dos {} multiplos de 3 entre 1 e 500 é {}".format(contador, s))