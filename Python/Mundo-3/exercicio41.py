#Dentro do pacote utilidadeCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funciona como a função input(). mas com uma validação de dados para aceitar valores que sejam monetários.
from utilidadeCeV import dado, moeda2
print("-="*30)
num = dado.leiaDinheiro(("Digite o preço R$: "))
moeda2.resumo(num,35,22)

def leiaDinheiro(num):
    valido = False
    while not valido:
        entrada = str(input(num)).replace(',','.').strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[31mERRO!!! '{entrada}' é um preço invalido\033[m")
        else:
            valido = True
            return float(entrada)