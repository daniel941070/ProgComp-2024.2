#DANIEL ALEXANDRE 20242014050028
import datetime

# Data de referência: 27/04/1968 (sabado)
dataReferencia = datetime.datetime(1968, 4, 27)

# Obter a data de hoje
hoje = datetime.datetime.today()

# Calcular a quantidade de dias passados entre 27/04/1968 e hoje
diasPassados = (hoje - dataReferencia).days

# Contador de sábados
contadorSabados = 0

# A data 27/04/1968 foi um sábado
# Vamos calcular quantos sábados ocorreram desde essa data
for i in range(diasPassados + 1):  # +1 para incluir o próprio dia 27/04/1968
    # Cada 7 dias a partir de 27/04/1968 é um sábado
    if i % 7 == 0:
        contadorSabados += 1

# Exibir os resultados
print("Já se passaram ", diasPassados, " dias desde 27/04/1968 até hoje.")
print("Já ocorreram ", contadorSabados, " sábados desde 27/04/1968 até hoje.")
