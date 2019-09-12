#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
#ajeitar
letra = None

while True:
    letra = input("Digite M ou F")
    try:
        letra =='M' or letra == 'F'
        break
    except:
        print("Invalid input")
        continue

    if letra == 'M':
        sexo = 'Masculino'
    else:
        sexo = 'Feminino'


print('O sexo é ', sexo)
