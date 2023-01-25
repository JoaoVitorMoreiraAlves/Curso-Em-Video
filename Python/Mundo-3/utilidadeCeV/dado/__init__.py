def leiaDinheiro(num):
    valido = False
    while not valido:
        entrada = str(input(num)).replace(',','.').strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[31mERRO!!! '{entrada}' é um preço invalido\033[m")
        else:
            valido = True
            return float(entrada)