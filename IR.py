#calcular IR
#De 1.903,99 até 2.826,65	7,5 142,80
#De 2.826,66 até 3.751,05	15	354,80
#De 3.751,06 até 4.664,68	22,50	636,13
#Acima de 4.664,68	27,50	869,36

#ENTRADAS DE SALARIO
vencimento = float(input("Vencimento:\n"))
funcao = float(input("Função:\n"))
aux_transp = float(input("Auxilio Transporte:\n"))
aux_alim = float(input("Auxílio Alimentação:\n"))
aux_saude = float(input("Auxílio Saúde:\n"))

#DESCONTOS
desc_sindicato = vencimento * 0.009
desc_transp = 62.63
desc_funafin = vencimento * 0.135


#BASE DE CALCULO DO IR
salario = vencimento + funcao

#LIMITES DE CADA BASE DE CALCULO
bc2 = 1903.99
bc21 = 2826.65

bc3= 2826.66
bc31 = 3751.05

bc4 = 3751.06
bc41 = 4664.68

bc5 = 4664.68

#ALIQUOTAS QUE EXITEM NO IR

aliq1 = 0
aliq2 = 0.075
aliq3 = 0.15
aliq4 = 0.225
aliq5 = 0.275

#DEFINIR LOGO O VALOR DE ISENCAO E O QUANTO DO SALARIO É TRIBUTÁVEL.

salario_isento =1903.98
salario_trib = salario - salario_isento

#CASO O SALARIO ULTRAPASSE ALGUMA ALIQUOTA JA DEFINE O QUANTO VAI PAGAR

pgto_aliq1 = 0
pgto_aliq2= 0.075* (bc21 - bc2)
pgto_aliq3 = 0.15* (bc31- bc3)
pgto_aliq4 = 0.225 *(bc41 - bc4)


#PGTO_IR = DIVIDIR O PGTO A PARTIR DO SALARIO TRIBUTAVEL. SE O SALARIO ULTRAPASSA UMA FAIXA
# JÁ DEFINE O QUANTO VAI PAGAR DAQUELA FAIXA. O RESTANTE (SAL TRIB - LIMITE DA FAIXA QUE PASSOU)* ALIQUOTA
if salario <bc2:
    pgto_IR= 0
elif salario>= bc2 and salario < bc3:
    pgto_IR = salario_trib*aliq2
elif salario>= bc3 and salario < bc4:
    pgto_IR =  pgto_aliq2 + ((salario_trib-bc3)*aliq3)
elif salario>= bc4 and salario < bc5:
    pgto_IR = pgto_aliq2+pgto_aliq3 + ((salario_trib-bc4)*aliq4)
elif salario> bc5:
    pgto_IR = pgto_aliq2+pgto_aliq3 + pgto_aliq4 + ((salario_trib-bc5)*aliq5)


#SOMANDO TODOS DESCONTOS
desconto_total = desc_transp + desc_funafin + desc_sindicato + pgto_IR
#SALARIO BRUTO
salario_bruto = vencimento+funcao+ aux_alim + aux_saude + aux_transp
salario_liquido = salario_bruto-desconto_total

print(f"Seu salário bruto é: R$ {round(salario_bruto,2)}")
print(f"O total de descontos: {round(desconto_total,2)}")
print(f"Você pagará de Funafin: R$ {round(desc_funafin,2)}")
print(f"Seu Pagamento de IR é: R$ {round(pgto_IR,2)}")
print(f"Seu salário líquido é de: R$ {round(salario_liquido,2)}")
