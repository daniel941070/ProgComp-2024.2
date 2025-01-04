#DANIEL ALEXANDRE 20242014050028
import random

# Lista de palavras
palavras = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ", "ASILO", "ASTRO", "BAILE", 
    "BAIXA", "BALAO", "BALSA", "BARCO", "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", 
    "BREJO", "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO", "CESTA", "CLIMA", 
    "COBRA", "COLAR", "COQUE", "COURO", "CRAVO", "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", 
    "FESTA", "FLUOR", "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO", "GESSO", 
    "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA", "HEROI", "HOTEL", "ICONE", "IMPAR", 
    "IMUNE", "INDIO", "JUNTA", "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO", 
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE", "MORRO", "MURAL", "MOVEL", 
    "NACAO", "NINHO", "NOBRE", "NORMA", "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", 
    "PEDRA", "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO", "PRATO", "PRECO", 
    "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO", "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", 
    "ROUPA", "SABAO", "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO", "TARDE", 
    "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO", "TORRE", "TRAJE", "TREVO", "TROCO", 
    "TRONO", "TURMA", "URUBU", "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)

# Escolher duas palavras aleatórias
palavra1 = random.choice(palavras)
palavra2 = random.choice(palavras)

# Mensagens iniciais
print("Tente adivinhar as duas palavras!")

print(palavras)# pra o usuario saber quais palavras existem
print("Você tem 7 tentativas.")
tentativas = 0
maxTentativas = 7

# Loop principal do jogo
while tentativas < maxTentativas:
    # Exibe o número da tentativa
    print("Tentativa",(tentativas + 1),"de", maxTentativas)

    # Recebe o input da primeira palavra
    tentativa1 = input("Digite a primeira palavra (5 letras): ")
    while len(tentativa1) != 5 or tentativa1 not in palavras:
        print("Palavra inválida! A palavra deve ter 5 letras e ser digitada em caixa alta")
        tentativa1 = input("Digite a primeira palavra (5 letras): ")

    # Recebe o input da segunda palavra, só se a primeira for válida
    tentativa2 = input("Digite a segunda palavra (5 letras): ")
    while len(tentativa2) != 5 or tentativa2 not in palavras:
        print("Palavra inválida! A palavra deve ter 5 letras  e ser digitada em caixa alta")
        tentativa2 = input("Digite a segunda palavra (5 letras): ")

    # Listas para armazenar os resultados das palavras
    resultado1 = []
    resultado2 = []

    # Verificando a primeira palavra
    for i in range(5):
        if tentativa1[i] == palavra1[i]:
            resultado1.append("\033[1;32m" + tentativa1[i] + "\033[0m")  # Verde
        elif tentativa1[i] in palavra1:
            resultado1.append("\033[1;33m" + tentativa1[i] + "\033[0m")  # Amarelo
        else:
            resultado1.append("\033[1;30m" + tentativa1[i] + "\033[0m")  # Cinza

    # Verificando a segunda palavra
    for i in range(5):
        if tentativa2[i] == palavra2[i]:
            resultado2.append("\033[1;32m" + tentativa2[i] + "\033[0m")  # Verde
        elif tentativa2[i] in palavra2:
            resultado2.append("\033[1;33m" + tentativa2[i] + "\033[0m")  # Amarelo
        else:
            resultado2.append("\033[1;30m" + tentativa2[i] + "\033[0m")  # Cinza

    # Exibe as palavras com cores
    print("Primeira palavra:", *resultado1)
    print("Segunda palavra:", *resultado2)

    # Verifica se o jogador acertou ambas as palavras
    if tentativa1 == palavra1 and tentativa2 == palavra2:
        print("Parabéns! Você adivinhou as duas palavras corretamente!")
        break  # Sai do loop caso o jogador tenha acertado

    # Incrementa o número de tentativas
    tentativas += 1

# Caso o número de tentativas chegue ao máximo
if tentativas == maxTentativas and (tentativa1 != palavra1 or tentativa2 != palavra2):
    print(f"Você não conseguiu adivinhar as palavras em {maxTentativas} tentativas.")
    print("As palavras eram:", palavra1, "e", palavra2)
