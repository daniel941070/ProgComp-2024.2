#DANIEL ALEXANDRE 20242014050028
#contador de números palíndromos
contador = 0

#inicio
for numero in range(10, 100001):
    original = numero  # Guardamos o número original
    invertido = 0  # Variável para armazenar o número invertido

    # Inverter o número
    while numero > 0:
        digito = numero % 10  # Pega o último dígito
        invertido = invertido * 10 + digito  # Constrói o número invertido
        numero = numero // 10  # Remove o último dígito do número original

    # Verifica se o número original é igual ao invertido
    if original == invertido:
        contador += 1  # adiciona 1 ao contador se for palíndromo

# Exibe o resultado
print("Existem", contador, "números palíndromos entre 10 e 100000.")
