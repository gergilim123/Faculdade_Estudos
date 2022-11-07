'''
6) Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do
usuário e imprima a data com o nome do mês por extenso.

'''
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'semtembro', 'outubro', 'novembro', 'dezembro']

def data(mes):
    return meses[mes-1]


print('Informe a sua data de nascimento: ')
dia = (input('Dia: ')) 
mes = int ((input('Mês: '))) 
ano = (input('Dia: '))

mes = data(mes)

print (dia, 'de', mes, 'de', ano)












        








