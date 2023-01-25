#Crie um programa onde o usuário digite uma EXPRESSÃO qualquer que use PARÊNTESES. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = []
pilha = []

calculo = str(input("Digite a expressão: "))
for letra in calculo:
    expressao.append(letra)
for simb in expressao:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Sua expressão está válida!!")
else:
    print("Sua expressão está invalida!!!")