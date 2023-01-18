#Dissecando uma variável

palavra = input("Digite algo: ")

print("O tipo primitivo da palavra é ", type(palavra))
print("É número? ", palavra.isnumeric())
print("É alfabético? ", palavra.isalpha())
print("É alfanúmerico? ", palavra.isalnum())
print("É maisculo? ",palavra.isupper())
print("É minusculo? ",palavra.islower())
print("É somente espaços? ",palavra.isspace())