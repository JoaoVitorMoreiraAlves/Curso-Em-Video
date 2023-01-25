#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também a função leiaFloat() com a mesma funcionalidade.
def leiaInt(inteiro):
    validacao = False
    while not validacao:
        try:
            entrada = int(input(inteiro))
        except (ValueError, TypeError):
            print("\033[31mERRO!!! O Problema está reacionado ao dado informado. Por favor informe um valor inteiro\033[m")
        except KeyboardInterrupt:
            print("\n\033[33mO usuário desistiu de informar o valor INTEIRO\033[m")
            return 0
        else:
            return entrada


def leiaFloat(real):
    validacao = False
    while not validacao:
        try:
            a = float(input(real))
        except (ValueError, TypeError):
            print("\033[31mERRO!!! O Problema está reacionado ao dado informado. Por favor informe um valor real\033[m")
        except KeyboardInterrupt:
            print("\n\033[33mO usuário desistiu de informar o valor REAL\033[m")
            return 0
        else:
            return a


inteiro = leiaInt("Digite um numero inteiro: ")
real = leiaFloat("Digite um valor real: ")
print(f"O valor inteiro digitado foi {inteiro} e o real foi {real}")