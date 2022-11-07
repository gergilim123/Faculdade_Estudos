'''
5) Faça um programa que lê uma string e imprime “Palíndromo” caso a string
seja um palíndromo e “Não é palíndromo” caso não seja.
Assuma que a entrada não tem acentos e que todas as letras são
minúsculas.

Obs: Um palíndromo é uma palavra ou frase, que é igual quando lida da
esquerda para a direita ou da direita para a esquerda (espaços em brancos
são descartados).
Exemplos de palíndromo: “ovo”, “reviver”, “mega bobagem”, “anotaram a data
da maratona”

'''

entrada = input("Digite uma palavra ou texto para saber se são palíndromo: ").replace(' ', '') # Replace para tirar o espaço, caso seja mais de uma palavra

print()

if (entrada[::-1] == entrada): # Inverter uma string 
    print("Sua palavra ou texto é um palíndromo.")
else:
    print("Sua palavra ou texto não é um palíndromo")


