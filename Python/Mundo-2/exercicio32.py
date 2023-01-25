#Faça um programa que mostra a tabuada de vários número, um de cada vez, para cada valor digitado pelo usuário. O Programa será interrompido quando o número solicitado for negativo.

while True:
    valor = int(input("Digite o valor para ver a tabuada ou um valor negativo para parar: "))
    if (valor < 0):
        break

    print("=-=" * 6)
    for i in range (1,11):
        print("{} X {} = {}".format(i,valor,valor*i))
    print("=-=" * 6)
    print("Proximo valor")
print("Programa finalizado")