#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
#são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
#3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
#(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
#dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

hr = int(input("Quantas horas de trabalho neste mês?"))
pgto_hr = float(input("Quanto é sua hora de trabalho?"))

salario_bruto = hr*pgto_hr

if salario_bruto <=900:
    aliquota = 0
elif salario_bruto >900 and salario_bruto <=1500:
    aliquota= 0.05
elif salario_bruto>1500 and salario_bruto<= 2500:
    aliquota= 0.1
else:
    aliquota= 0.2
pgto_ir= salario_bruto *aliquota
aliq_porc = aliquota*100
INSS = (hr*pgto_hr)*0.1
FGTS = (hr*pgto_hr)*0.11
sind= (hr*pgto_hr)*0.03

descontos = pgto_ir + INSS + sind

print("Salário bruto:","(", hr, "*", pgto_hr, "): R$", salario_bruto)
print("(-) IR (", aliq_porc,"%): R$", pgto_ir)
print("(-) INSS (10%):R$", INSS)
print ("FGTS (11%):R$", FGTS)
print ("(-)Sindicato (3%) : R$",sind)
print ("Total de descontos: R$",descontos)
print ("Salário líquido: R$ {total}".format(total=salario_bruto-descontos))
