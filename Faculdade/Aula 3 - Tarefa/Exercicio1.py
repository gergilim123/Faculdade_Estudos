'''
1) Faça um programa que leia um número n e imprima n linhas na tela com o
seguinte formato (exemplo se n = 5):

'''

n = int (input ("Digite um número: "))
x = 0

for i in range(1, (n + 1)):
    x = i + (x * 10)
    print (x)
    