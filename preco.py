#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.
preco1 = float(input("digite o primeiro preco"))
preco2 = float(input("digite o segundo preco"))
preco3 = float(input("digite o terceiro preco"))

lista_precos = [preco1, preco2, preco3]

menor = None
for i in lista_precos:
    if menor is None:
        menor = i
    elif i < menor:
        menor = i


maior = None
for i in lista_precos:
    if maior is None:
        maior = i
    elif i > maior:
        maior = i

print("O maior preco é", maior)
print ("O menor preco é", menor)
