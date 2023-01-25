def fat(num,show=False):
    fat = 1
    for i in range(num,0,-1):
        fat *= i
    if show:
        for i in range(num,0,-1):
            if i == 1:
                print(f"{i} = ",end="")
            else:
                print(f"{i} X ",end="")
        print(f"{fat}")
    else:
        print(f"O fatorial de {num} é {fat}")

    

num = int(input("Digite o valor para ver o fatorial: "))
show = False
opcao = ""
while opcao != "N" and opcao != "S":
    opcao = str(input("Deseja ver o processo de calculo? [S/N]: ")).upper()[0]
    if opcao == "S":
        show = True
fat(num,show)