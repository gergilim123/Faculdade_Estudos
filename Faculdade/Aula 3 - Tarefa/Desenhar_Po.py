# Tipo de objeto

tipo_objeto = input ('Escolha o seu tipo de objeto para ser desenhado: ' '\n' '-> Q: Quadrado' '\n' '-> T: Triangulo' '\n' '-> L: Losango' '\n' 'Sua escolha: ')
tipo_objeto_1 = tipo_objeto.upper() # Transformando em Maisculo

# Tipo de caracter

tipo_de_caractere = input ('Escolha o tipo de caractere a ser desenhado: ')

# Verificar entrada

while (tipo_objeto_1 != 'Q') and (tipo_objeto_1 != 'T') and (tipo_objeto_1 != 'L'):
    print ('Indentificador de objeto invalido')
    break


# Quadrado

if (tipo_objeto_1 == 'Q'):
    valor_lado_quadrado = int (input ('Qual o tamanho do lado do seu quadrado: '))
    if (valor_lado_quadrado >= 3):
        print ('\n\n\n')
        for i in range(valor_lado_quadrado):
            print (tipo_de_caractere * valor_lado_quadrado)
    else:
        print ('Dimensão inválida')


# Função Triangulo e Losango

def gerar(altura, tipo):
    #if (tipo_objeto_1 == 'L'):
    #altura = int (input ('Qual a altura do seu losango: '))
    if (altura >= 3):
        print ('\n\n\n')
        y = 1 # Quantidade de vezes que vai imprimir o tipo de caractere --- tem que ser de 2 em 2
        x = 1 # Dentro do for x = x + 1 --- Até espaço for 0
        espaco = altura - x # Quantidade de espaços a serem dados (topo), até espaço ser 0
        for i in range (1, (altura + 1)):
            print (espaco * ' ', tipo_de_caractere * y)
            x = x + 1
            espaco = altura - x
            y = y + 2
        
        if (tipo == 'L'):
            w = ((altura * 2) - 1) - 2    # Quantidade de caractere inicial
            espaco_2 = 1                      # Tem que comçar com 1 e ir até (altura_los - 1), Acrescentar 1 
            for y in range (1, altura):
                print (espaco_2 * ' ', tipo_de_caractere * w)
                espaco_2 = espaco_2 + 1
                w = w - 2
    else:
        print ('Dimensão inválida')

# Triangulo
 
if (tipo_objeto_1 == 'T'):
    altura_tri = int (input ('Qual a altura do seu triangulo: '))

    gerar(altura_tri, 'T')
   
# Losango

if (tipo_objeto_1 == 'L'):
    altura_los = int (input ('Qual a altura do seu losango: '))

    gerar(altura_los, 'L')

    




        
        


    




        



        






    














