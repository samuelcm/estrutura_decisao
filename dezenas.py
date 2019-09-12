#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
#dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305,
#301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


numero = int(input("Digite um numero inteiro menor que 1000\n"))

centena = numero//100
dezena = (numero%100)//10
unidade = (numero%100)%10

def centenas (a):
    if centena == 1:
        return "centena"
    else:
        return "centenas"

def dezenas (a):
    if dezena == 1:
        return "dezena"
    elif dezena > 1:
        return "dezenas"


def unidades (a):
    if unidade == 1:
        return "unidade"
    elif unidade > 1:
        return "unidades"

num1 = centenas(numero)
num2 = dezenas(numero)
num3 = unidades(numero)

if (numero%100) == 0 and numero>=100:
    print (numero, "=", centena, num1)
elif numero <10:
    print(numero, "=", unidade, num3)
elif numero <100:
    if numero%10 == 0:
        print (numero, "=", dezena, num2)
    else:
        print (numero, "=", dezena, num2, "e", unidade, num3)
else:
    if (numero%100) >= 10:
        if (numero%100)%10 == 0:
            print (numero, "=", centena, num1, "e ", dezena, num2)
        else:
            print (numero, "=", centena, num1, "," , dezena, num2, "e", unidade, num3 )
    else:
        print (numero, "=", centena, num1, "e", unidade, num3 )
