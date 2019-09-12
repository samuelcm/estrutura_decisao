#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
# mesma é uma data válida.

data = input("Digite uma data no formato 'dd/mm/aaaa'")

numeros = ['0','1','2','3','4','5','6','7','8','9']


dia = int(data[0] + data[1])
mes = int(data[3] + data[4])
ano = int(data[6]+ data[7]+ data[8]+ data[9])

mes1 = [1,3,5,7,8,10,12]
mes2 = [4,6,9,11]
mes3 = 2

if len(data) != 10:
    print ("Informe uma data no formato 'dd/mm/aaaa'")
else:
    if data[2] != "/" or data[5] != "/":
        print("A data não está no formato")
    else:
        if dia>31 or mes>12:
            print("Dia invalido")
        elif mes in mes2 and dia>30:
            print("Dia invalido")
        elif mes in mes2 and dia >28:
            print("Dia invalido")
            #funcao bissexto aqui
        else:
            print("Data válida")
