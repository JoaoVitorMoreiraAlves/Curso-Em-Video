#Aula sobre tratamento de erros

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print(f"ERRO!!!! O problema está no tipo do dado que você digitou")
except ZeroDivisionError:
    print("Não é possível dividir um valor por 0")
except KeyboardInterrupt:
    print("\nO usuário decidiu abortar o programa")
else:
    print(f"O resultado é {r:.2f}")
finally:
    print("Finalizando o Programa....\nVolte Sempre!!!")