#Faça um programa que tenha a função chamada escreva() que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptavél.
def escreva(txt):
    print("~"*(len(txt)+4))
    print(f"  {txt}")
    print("~"*(len(txt)+4))


#Programa Principal
escreva("Gustavo Guanabara")
escreva("Curso de Python no Youtube")
escreva("CeV")