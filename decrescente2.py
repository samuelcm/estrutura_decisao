a = float(input("digite o primeiro numero"))
b = float(input("digite o segundo numero"))
c = float(input("digite o terceiro numero"))

lista = []

#achando o maior e colocando primeiro na lista
if a< b and a<c:
    lista.append(a)
elif b<a and b<c:
    lista.append(b)
else:
    lista.append(c)

#achando o menor e colocando na lista
if a> b and a>c:
    lista.append(a)
elif b>a and b>c:
    lista.append(b)
else:
    lista.append(c)

#colocando na lista o que sobrou (que sempre será o numero do meio. nem maior nem menor)
if a not in lista:
    lista.append(a)
elif b not in lista:
    lista.append(b)
else:
    lista.append(c)

#colocando em ordem decrescente.
lista_desc = [lista[1], lista[2], lista[0]]

print(lista_desc)
