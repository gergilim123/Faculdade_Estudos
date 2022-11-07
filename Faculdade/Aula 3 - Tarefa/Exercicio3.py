'''
3) Faça um programa que:
Lê duas listas com 5 inteiros cada.
Checa quais elementos da segunda lista são iguais a algum elemento da
primeira lista.
Se não houver elementos em comum, o programa deve informar isso.

'''


lista_1 = []
lista_2 = []
lista_igual = []

# Input primeira lista

x = 0

while (x < 5):
    numero = float(input('Digite 5 valores para a sua primeira lista: '))
    lista_1.append(numero)
    x = x + 1

print ('\n')

y = 0

while (y < 5):
    numero_2 = float(input('Digite 5 valores para a sua segunda lista: '))
    lista_2.append(numero_2)
    y = y + 1

for i in lista_1:
    for j in lista_2:
        if (i == j):
            lista_igual.append(i)
            break

print ('\n')
print ('Os valores iguais são: ', lista_igual)

