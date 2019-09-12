#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("digite o primeiro preco"))
num2 = float(input("digite o segundo preco"))
num3 = float(input("digite o terceiro preco"))

lista = [num1, num2, num3]

print(sorted(lista, reverse = True))
