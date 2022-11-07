tempo_caracol = [] # Com o valor -1 
nivel_0 = []
nivel_1 = []
nivel_2 = []
velocidade = []

entrada_segundos = int(input("Informe o tempo em segundos de cada um dos caracóis, (quando terminar digite (-1) para encerrar sua entrada): "))
tempo_caracol.append(entrada_segundos)

while (entrada_segundos != (-1)):
    entrada_segundos = int(input("Informe o tempo em segundos de cada um dos caracóis: "))
    tempo_caracol.append(entrada_segundos)

for i in (tempo_caracol):
    if (i < 180) and (i > 0): #Nível 0
        nivel_0.append(i)
    if (i >= 180) and (i < 240): #Nível 1
        nivel_1.append(i)
    if (i >= 240): #Nível 2
        nivel_2.append(i)
    if (i != (-1)):
        velocidade.append(i)
        

        
print ('\n')
print ('Caracois no nível 0:', len(nivel_0))
print ('Caracois no nível 1:', len(nivel_1))
print ('Caracois no nível 2:', len(nivel_2))

tempo_medio = (sum(nivel_0) + sum(nivel_1) + sum(nivel_2))/ (len(nivel_0) + len(nivel_1) + len(nivel_2)) # Tempo Médio

print (f'Tempo medio: {tempo_medio:,.1f} s')

# Velocidade

velocidade_max = min(velocidade)
velocidade_min = max(velocidade)

# Velocidades transformadas

velocidade_max_1 = 33/ (velocidade_max/60)
velocidade_min_1 = 33/ (velocidade_min/60)

print(f'Velocidade máxima: {velocidade_max_1:,.1f} cm/min')
print(f'Velocidade mínima: {velocidade_min_1:,.1f} cm/min')




