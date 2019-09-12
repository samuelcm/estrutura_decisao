#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.
preco1 = float(input("digite o primeiro preco"))
preco2 = float(input("digite o segundo preco"))
preco3 = float(input("digite o terceiro preco"))

def melhor_preco(a, b, c):
    if a< b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c
        
melhor = melhor_preco(preco1,preco2,preco3)

print("O melhor preço é {}.".format(melhor))
