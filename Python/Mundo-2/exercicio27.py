

print("Gerador de PA")
print("-=" * 12)

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao da PA: "))
contador = 0
i = 0
while contador < 10:
    print("{} -> ".format(termo), end="")
    i += 1
    contador += 1
    termo += razao
    if contador == 10:
        print("Pausa")
        contador -= int(input("Quantos termos você quer mostrar mais?: "))
print("Progressão finalizada com {} termos mostrados".format(i))