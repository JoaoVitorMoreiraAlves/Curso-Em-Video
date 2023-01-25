#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação de aceitar apenas um valor número.

def leiaInt(num):
    n = str(input(num))
    while True:
        if n.isnumeric():
            n = int(n)
            break
        else:
            print("\033[0;31mVocê digitou errado!!!!\033[m")
            n = str(input(num))
    return n



print("-="*20)
num = leiaInt("Digite o número: ")
print(f"Você acabou de digitar o número {num}")