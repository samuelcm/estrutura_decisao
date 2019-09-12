#Faça um Programa que leia três números e mostre o maior e o menor deles.

contador = 0
num = []
while contador<3:
    numero = int(input("digite um numero"))
    num.append(numero)
    contador += 1

menor = None
for i in num:
    if menor is None:
        menor = i
    elif i < menor:
        menor = i


maior = None
for i in num:
    if maior is None:
        maior = i
    elif i > maior:
        maior = i

print(maior)
