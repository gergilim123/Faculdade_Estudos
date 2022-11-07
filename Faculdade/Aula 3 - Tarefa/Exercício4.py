'''
4) Faça um programa que conta o número de palavras em um texto.

'''

texto = input ('Digite um texto: ')

texto_separado = texto.split() # Cria uma lista com as str separadas pro espaço

print ('Quantidade de palavras no seu texto: ', len(texto_separado)) # len() é a quantidade de elementos em uma lista

