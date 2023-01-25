def metade(num,show):
    if show:
        return moeda(num/2)
    return num/2


def dobro(num, show):
    if show:
        return moeda(num*2)
    return num*2


def aumenta(num,porcent,show):
    if show:
        return moeda(num+(num*porcent/100))
    return num+(num*porcent/100)


def diminui(num,porcent,show):
    if show:
        return moeda(num-(num*porcent/100))
    return num-(num*porcent/100)


def moeda(num):
    return (f"R${num}")


def porcent(num):
    return (f"{num}%")


def resumo(n,aumento,reduc):
    print("-"*30)
    print("{:^30}".format("RESUMO DO VALOR"))
    print("-"*30)
    print("Preço analisado: \t{}".format(moeda(n)))
    print("Dobro do Preço: \t{}".format(dobro(n,True)))
    print("Metade do Preço: \t{}".format(metade(n,True)))
    print("{} de aumento: \t{}".format(porcent(aumento),aumenta(n,aumento,True)))
    print("{} de redução: \t{}".format(porcent(reduc),diminui(n,reduc,True)))