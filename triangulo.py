#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
#se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
#se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que
#o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;


lado1 = float(input("Digite o primeiro lado do triangulo"))
lado2 = float(input("Digite o segundo lado do triangulo"))
lado3 = float(input("Digite o terceiro lado do triangulo"))



if lado1 > lado2 + lado3 or lado2 > lado1+lado3 or lado3 > lado2+lado1:
        print("As medidas não podem formar um triangulo")
else:
    if lado1 == lado2 and lado1 == lado3:
        print("O triangulo é equilatero. Possui todos lados iguais")
    elif lado1 == lado2 and lado1 != lado3:
        print("O triangulo é isósceles. Possui 2 lados iguais")
    elif lado2 == lado3 and lado1 != lado3:
        print("O triangulo é isósceles. Possui 2 lados iguais")
    elif lado1 == lado3 and lado1 != lado2:
        print("O triangulo é isósceles. Possui 2 lados iguais")
    else:
        print("O triangulo é escaleno. Não possui nenhum lado igual")
