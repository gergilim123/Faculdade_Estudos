'''
2) Faça um programa que leia n notas, mostre as notas e a média.

'''

quantidade_notas = int (input('Digite a quantidade de notas à ser digitadas: ')) # Recebendo a quantidade de notas a serem digitadas

while (quantidade_notas < 0):
    print ('Valor inválido.')
    quantidade_notas = int (input('Digite a quantidade de notas à ser digitadas: ')) # A nota não pode ser menor do que 0

n = [] # Lista de notas

for i in range (quantidade_notas):  # Input de valores para a lista (respeitando a quantidade de notas)
    notas = float (input ('Digite a sua nota: '))
    n.append(notas)

n.sort() # Ordenando a lista em ordem crescente

print ('\n')
print ('Suas notas: ', n)
print ('\n')

media = sum(n)/len(n)

print (f'A média é de: {media:,.1f}') # Formatação da média
































'''
notas = []

n = float (input('Digite n notas, para saber a média, (quando terminar digite (-1) para encerrar sua entrada): '))
notas.append(n)

while (n != -1):
    n = float (input('Digite n notas, para saber a média: '))
    notas.append(n)

notas.remove(-1)

media = sum(notas)/len(notas)

print ('Notas: ', notas)
print (f'A média é de: {media:,.2f}')
'''







