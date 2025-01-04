#DANIEL ALEXANDRE 20242014050028
#contador de números decrescentes
contador = 0
#inicio
numinicial = int(input("Digite o número inicial (deve ser >= 10): "))
numfinal = int(input("Digite o número final (deve ser <= 987631): "))

# Verificação do intervalo de entrada
while numinicial < 10:
    print("O número inicial deve ser maior ou igual a 10.")
    numinicial = int(input("Digite o número inicial (deve ser >= 10): "))

while numfinal > 987631:
    print("O número final deve ser menor ou igual a 987631.")
    numfinal = int(input("Digite o número final (deve ser <= 987631): "))

while numinicial > numfinal:
    print("O número inicial não pode ser maior que o número final.")
    numinicial = int(input("Digite o número inicial (deve ser >= 10): "))
    numfinal = int(input("Digite o número final (deve ser <= 987631): "))

# Intervalo de números de numinicial até numfinal
for numero in range(numinicial, numfinal + 1):
    # Guardando o número original
    anterior = numero % 10  # Último dígito
    
    valido = True
    
    # Enquanto o número tiver mais de um dígito
    while numero > 9:
        numero = numero // 10  # Remove o último dígito
        atual = numero % 10  # Novo último dígito
        
        if atual < anterior:  # Se o dígito atual for menor que o anterior
            anterior = atual  # Atualiza o "anterior" com o dígito atual
        else:
            valido = False  # Se a sequência não for decrescente, marca como inválido
            break  # Interrompe a verificação

    if valido:  # Se for decrescente
        contador += 1

# Exibindo o resultado
print("Existem", contador, "números decrescentes no intervalo de", numinicial, "até", numfinal, ".")
