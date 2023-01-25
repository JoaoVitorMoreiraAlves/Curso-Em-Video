def leiaInt(msg):
    from time import sleep
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO!! por favor, digite um número inteiro válido\033[m")
        except KeyboardInterrupt:
            print("\n\033[33mUsuário preferiu  não digitar nenhum valor.\033[m")
            print("Finalizando programa.....")
            sleep(2)
            exit()
        else:
            return n


def linha(tam = 42):
    return '=' * tam


def cabecalho (txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lst):
    cabecalho("MENU PRINCIPAL")
    cont = 1
    for item in lst:
        print(f"\033[34m{cont}\033[m - \033[34m{item}\033[m")
        cont +=1
    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc