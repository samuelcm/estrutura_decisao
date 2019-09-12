#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ["a", "e", "i", "o", "u"]

letra = input("digite uma letra: \n")

letra=[letra]

resposta = []

for i in letra:
    for v in vogal:
        if i == v:
            resposta.append(i)

if len(resposta) > 0:
    print("É uma vogal")
else:
    print("É uma consoante")
