#Faça um programa que tenha uma função chamada área que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg,comp):
    print(f"A área de um terreno {larg}X{comp} é de {larg*comp:.2f}m².")


#Programa Principal
print("Controle de Terrenos")
print("-="*30)
larg = float(input("Largura em metros: "))
comp = float(input("Comprimento em metros: "))
area(larg,comp)