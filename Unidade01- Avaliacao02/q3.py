#DANIEL ALEXANDRE 20242014050028
limite = int(input("digite o limite: ")) #limite desejado
primos = [] #começa com uma lista vazia

# Verificar se um número é primo
for numero in range(3, limite, 2):  # Começa de 3 e só verifica números ímpares
    primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):  # Teste até a raiz quadrada de 'numero'
        if numero % divisor == 0:
            primo = False
            break
    if primo:
        primos.append(numero) #guarda em primos os numeros calculados

# Contar os pares consecutivos de primos ímpares
contador = 0
for i in range(1, len(primos)):
    if primos[i] == primos[i - 1] + 2:
        contador += 1

print(contador)
