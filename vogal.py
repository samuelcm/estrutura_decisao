#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ["a", "e", "i", "o", "u"]

letra = input("digite uma letra: \n")

if letra in vogal:
    print("é uma vogal")
else:
    print("é uma consoante")

for letra in vogal:
    if letra == vogal:
        print("é uma vogal")
    else:
        print("é uma consoante")
