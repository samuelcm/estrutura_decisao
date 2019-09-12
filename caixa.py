#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e
#depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50
#e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a
# quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
# uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
#quatro notas de 10, uma nota de 5 e quatro notas de 1.


numero = int(input("Digite um numero inteiro até R$ 600,00.\n"))

centena = numero//100
dezena = (numero%100)//10
unidade = (numero%100)%10


nota_cem = centena

if dezena==5:
    nota_cinq = 1
elif dezena >5:
    nota_cinq =1
    nota_dez = dezena - 5
elif dezena<5:
    nota_dez = dezena


if unidade == 5:
    nota_cinco = 1
    nota_um = unidade

print(nota_cem, "notas de cem", nota_cinq, "notas de 50", nota_dez, "nota de 10", nota_cinco, "nota de cinco", nota_um, "nota de um")
