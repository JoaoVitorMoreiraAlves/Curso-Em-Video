frase = "Curso em Vídeo Python"

print(frase)
print(frase[9]) #[9] Ele mostra o valor na posição 9 do vetor
print(frase[9:21]) #[9:21] Ele mostra o valor da posição 9 até a 20
print(frase[9:21:2]) #[9:21:2] Ele mostra o valor da posição 9 até a 20 pulando de 2 em 2

print(frase[:5]) #[:5] Ele mostra o valor da posição 0 até 5 por ele considera que existe um "0" antes do ":"

print(frase[15:]) #[15:] Ele mostra o valor da posição 15 até o final do vetor

print(frase[9::3]) #[9::3] Ele mostra o valor da posição 9 até o final pulando de 3 em 3

print(len(frase)) #len, le a quantidade de posições 
print(frase.count("o")) #.count, lê quantas vezes a letra "o" repete
print(frase.count("o",0,14)) #lê quantas vezes a letra "o" repete da posição 0 ao 13

print(frase.find("deo")) #lê em qual posição inicia a palavra "deo"

print(frase.find("Android")) #retorna -1 pois a palavra "Android" não existe na String

print("Curso" in frase) # Diz se a frase "curso" está na frase e retorna verdadeiro ou falso

print(frase.replace("Python", "Android")) # Troca a palavra "Python" por "Android", o próprio python aumenta o tamanho do vetor

print(frase.upper()) # tudo maiusculo
print(frase.lower()) # tudo minusculo

print(frase.capitalize()) #Primeira letra Maiscula e todo o restante Minuscula

print(frase.title()) #Primeira letra Miauscula de CADA palavra

frase = "   Aprenda Python   "

print(frase.strip()) #Tira os espaços inuteis que ficam antes e depois da String

print(frase.rstrip()) #Tira os ultimos espaços inuteis da String por conta do "r" de right

print(frase.lstrip()) #Tira os primeiros espaços inuteis da String por conta do "l" de left

frase = "Curso em Vídeo Python"
frase = frase.split()
print(frase) #Cria um vetor e divide a frase dentro

print(" ".join(frase)) #Separa a String por "-"

print(frase[0]) #Pega a posição 0 do vetor frase
print(frase[2] [3]) #Pega a posição 3 do vetor 2 da frase