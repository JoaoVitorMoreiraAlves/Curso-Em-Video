#Crie um programa que tenha uma TUPLA com várias palavras (não usar acentos). Depois disso você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ("Programador", "Aprender", "Programar", "Linguagem", "Python", "Curso")

for p in tupla:
    print(f"\nNa palavra {p} temos: ",end="")
    for letra in p:
        if letra.lower() in ("aeiou"):
            print("{}  ".format(letra),end="")