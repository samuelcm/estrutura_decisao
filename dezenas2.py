#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
#dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305,
#301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


numero = input("Digite um numero inteiro menor que 1000\n")


#pede tamanho do numero
#verifica se algum é zero

num_list = list(numero)

resultado = []
nomes = []

for idx,val in enumerate(num_list):

    if int(val) >1:
        plural = 's'
    else:
        plural = ''

    if val !=0:
        if idx == 0:
            resultado.append(f"{val} centena{plural}")
        elif idx == 1:
            resultado.append(f"{val} dezena{plural}")
        elif idx == 2:
            resultado.append(f"{val} unidade{plural}")

print(resultado)
print(nomes)
