'''

Sua tarefa será escrever a versão inicial de um programa em Python para auxiliar o
pesquisador a filtrar os textos. Adotaremos as seguintes regras simplificadas para a
classificação dos elementos:
    
     Palavra: sequência de letras (sem acento).
    Exemplos: UNIP estrutura de dados

     Número: sequência de dígitos precedidos ou não do sinal negativo (-).
    Identificaremos números inteiros, não tratando números racionais, reais, complexos
    ou com pontos indicando a separação em grupos de três dígitos.
    Exemplos: 2020 -100000
    
     Hashtag: caractere # seguido de letras.
    Exemplos: #python #unip #amoviajar
    
     Emoticon: sequência de um ou mais caracteres que não se enquadra nas descrições
    anteriores. Emoticons são compostos principalmente por caracteres de pontuação,
    mas podem conter letras, números ou serem precedidos por #.
    Exemplos: :-) #:-) :D <3


'''

list_palavra = []
list_numero = []
list_emoticon = []

texto = (input('Digite o seu texto aqui: '))

list_hashtag = texto.split('#') # Lista Hashtag



















