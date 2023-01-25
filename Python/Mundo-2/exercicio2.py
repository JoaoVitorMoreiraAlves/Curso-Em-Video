#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input("Digite o número inteiro: "))
opinador = int(input("""
Digite [  1  ] para converter em binário
Digite [  2  ] para converter em Octal
Digite [  3  ] para converter em Hexadecimal
Digite a sua opção: """))

if (opinador == 1):
    print("O número {} em binário é {}".format(num,bin(num)[2:]))
elif (opinador == 2):
    print("O número {} em Octal é {}".format(num,oct(num)[2:]))
elif (opinador == 3):
    print("O número {} em Hexadecimal é {}".format(num,hex(num)[2:]))
else:
    print("Escolha errada o programa será finalizado")