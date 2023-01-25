#Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de zero até vinte
#Seu programa deverá ler um número pelo teclado (de 0 a 20) e mostrá-lo por extenso.

tupla = ("Zero","Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezesete", "Dezoito", "Dezenove", "Vinte")

num = int(input("Digite um número entre 0 e 20: "))
opcao = ""
while True:
    while num < 0 or num > 20:
        num = int(input("Valor errado!!! Por favor digite um número entre 0 e 20: "))
    print("O numero {} por extenso é {}".format(num,tupla[num]))

    opcao = str(input("""
    [  S  ] Para continuar
    [  N  ] Para parar
    Digite sua opção: """)).upper()[0]

    while opcao != "N" and opcao != "S":
        opcao = str(input("""
    [  S  ] Para continuar
    [  N  ] Para parar
    Digite sua opção: """)).upper()[0]
    if opcao == "N":
        break
    if opcao == "S":
        num = -1