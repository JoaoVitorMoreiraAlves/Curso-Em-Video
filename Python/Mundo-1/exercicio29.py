#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparace a primera vez.
#Em que posição ela aparece a ultima vez.

frase = str(input("Digite uma frase: ")).upper().strip()
print("-"*40)
print("Quantidade de A:",frase.count("A"))
print("-"*40)
print("Posição do primeiro A:",frase.find("A")+1)
print("-"*40)
print("A ultima posição do A:",frase.rfind("A")+1)
print("-"*40)