#Interactive HELP
#help(input)
def soma(a=0,b=0):
    #DoctStrings abaixo
    """
    A Funcao soma possui dois parametros
    A = inteiro
    B = inteiro
    return = sem retorno
    """
    #Função
    s = a+b
    print(f"A soma entre {a} e {b} é {s}")

#help(soma)
soma(3,9)
soma()
soma(3)

print("-="*30)
#Escopo de Variáveis - caso seja criada uma váriavel dentro da função, após o uso a váriavel deixara de existir.
def teste(b):
    a = 8
    b += 4
    c = 2
    print(f"Na função teste, A vale {a}")
    print(f"Na função teste, B vale {b}")
    print(f"Na função teste, C vale {c}")


a = 5
teste(a)
print(f"No programa principal o A vale {a}")


print("-="*30)

def teste(b):
    global a #Declaria que a variavel A se tornou  global portanto quando terminar o uso da função o valor que for decedido para A, irá ser modificado no programa principal
    a = 8
    b += 4
    c = 2
    print(f"Na função teste, A vale {a}")
    print(f"Na função teste, B vale {b}")
    print(f"Na função teste, C vale {c}")


a = 5
teste(a)
print(f"No programa principal o A vale {a}")

print("-="*30)

#Retornando valores em função
def somar(a=0,b=0,c=0):
    s = a+b+c
    return s


print(f"As soma valem {somar(3,2,5)}, {somar(3,2,)}, {somar(2,5)}")