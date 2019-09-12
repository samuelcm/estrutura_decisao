#Faça um programa que calcule as raízes de uma equação do segundo grau,
#na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
#consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
#e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais.
#Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
#informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais;
#informe-as ao usuário;

#x = (-b +- raiz (delta))/2*a
#delta = b**2 - 4*a*c

a = float(input("Digite o valor de 'a'"))
if a != 0:
    b = float(input("Digite o valor de 'b'"))
    c = float(input("Digite o valor de 'c'"))
else:
    print("O valor de 'a' é zero. A equacao nao é de segundo grau")


delta = b**2 - 4*a*c
x1 = (-b + (delta**0.5))/2*a
x2 = (-b - (delta**0.5))/2*a


if delta <0:
    print ("A equacao nao possui raizes reais")
elif delta == 0:
    print(x1)
else:
    print("Raiz1: ", x1)
    print("Raiz2: ",x2)
