#Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
#Dica: utilize o operador módulo (resto da divisão).

numero =float(input("Digite um numero"))

if numero == 0:
    print("Zero nao é par ou impar")
elif numero%2 == 0:
    print("O número é par")
else:
    print("O número é impar")
