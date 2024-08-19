"""Programa que simula um jogo da forca"""

# Imports Gerais
from random import choice
from estilo import limpaTela, l, msgAnimada, valorInvalido


def boneco(contador):

    """Função que Monta um boneco na Tela"""

    if contador == 0:
        # 1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                    |
                    |     """, ANIMACAO, "", 0.018)


        # Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        # Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")

        # 2ª perte do desenho da forca
        msgAnimada("""
                    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 1:
        # 1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
                    |     """, ANIMACAO, "", 0.018)

        # Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        # Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")

        # 2ª perte do desenho da forca
        msgAnimada("""
                    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 2:
        # 1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
                |   |     """, ANIMACAO, "", 0.018)

        # Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        # Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")

        # 2ª perte do desenho da forca
        msgAnimada("""
                    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 3:
        # 1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|   |     """, ANIMACAO, "", 0.018)

        # Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        # Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")

        # 2ª perte do desenho da forca
        msgAnimada("""
                    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 4:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|\  |     """, ANIMACAO, "", 0.018)

        #Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        #Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")

        #2ª perte do desenho da forca
        msgAnimada("""
                    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 5:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|\  |     """, ANIMACAO, "", 0.018)


        #Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        #Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")


        #2ª perte do desenho da forca
        msgAnimada("""
               /    |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)
    elif contador == 6:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|\\  |     """, ANIMACAO, "", 0.018)


        #Montando a palavra
        for i, v in enumerate(word):
            if v == LETRA:
                frase[i] = f"{LETRA.upper()} "

        #Mostrando a frase
        for ele in frase:
            msgAnimada(ele, ANIMACAO, "")


        #2ª perte do desenho da forca
        msgAnimada("""
               / \  |
                    |
                ========
        """, ANIMACAO, "\n", 0.018)


# Contantes
TAM = 40

# Variáveis globais
ANIMACAO = True
TEMPO = 0.02

# Definindo as palavras
palavras = [
    "amigo", "futuro", "coragem", "felicidade", "alegria", "esperança",
    "amizade", "sabedoria", "liberdade", "saudade", "aventura", "carinho",
    "honestidade", "solidariedade", "justiça", "confiança", "RESPeito",
    "gentileza", "humildade", "empatia", "persistência", "gratidao",
    "determinação", "integridade", "paciência", "resiliência", "criatividade",
    "inspiração", "equilíbrio", "tranquilidade", "sabedoria", "generosidade",
    "compaixão", "tolerância", "serenidade", "fidelidade", "otimismo",
    "entusiasmo", "prudência", "temperança", "lealdade", "altruísmo",
    "compromisso", "serenidade", "honra", "dignidade", "coragem", "valentia",
    "liderança", "vigilância", "disciplina", "versatilidade", "sabedoria",
    "imparcialidade", "decisão", "criatividade", "dedicação", "zelo",
    "firmeza", "confiança", "RESPeito", "sabedoria", "amizade", "esperança"
]


# opções de TEMAS
TEMASPossiveis = ["Comida", "Sentimentos", "Games", "Instrumentos", "Filmes"]

# Mostranso menus
TEMAS = MAINTITLE = True

while True:
    # Escolhendo uma nova palavra
    word = choice(palavras)

    # Espaço para preencher as palavras
    frase = ["_ "] * len(word)
    letrasUsadas = []

    # Resetando as letras
    LETRA = ""
    C = PRIMEIROERRO = 0

    while True:

        # Definindo as palavras do jogo
        if frase == word:
            word = choice(palavras)

        # ---------------------------------------------------------------------------

        # Adicionando tema
        if TEMAS:
            while True:

                # Título de apresentação
                if MAINTITLE:
                    limpaTela()
                    l("——")
                    msgAnimada(f"{'Jogo da Forca':^{TAM}}", ANIMACAO)
                    l("——")
                    msgAnimada("Escolha um tema abaixo:", ANIMACAO)
                    l("——")
                else:
                    limpaTela()
                    l("——")
                    msgAnimada("Escolha um outro tema abaixo:", ANIMACAO)
                    l("——")

                # Escolhendo as categorias
                msgAnimada("1 - Comida", ANIMACAO)
                msgAnimada("2 - Sentimentos", ANIMACAO)
                msgAnimada("3 - Games", ANIMACAO)
                msgAnimada("4 - Instrumentos", ANIMACAO)
                msgAnimada("5 - Filmes", ANIMACAO)
                l("——")

                # Pegando o tema que o usuário escolheu
                msgAnimada("Sua escolha: ", ANIMACAO, "")

                try:
                    TEMA = str(input())
                    TEMA = int(TEMA)

                except ValueError:
                    valorInvalido("Digita apenas números", "——")
                    limpaTela()
                    ANIMACAO = False
                    continue

                if TEMA not in [1, 2, 3, 4, 5]:
                    valorInvalido("Valor fora intervalo", "——")
                    limpaTela()
                    ANIMACAO = False
                    continue

                ANIMACAO = True
                break

        # ---------------------------------------------------------------------------

        # Título para mostrar letras inválidas
        limpaTela()
        if PRIMEIROERRO != 0:

            if LETRA not in word and not LETRA.isnumeric():
                if LETRA not in letrasUsadas:
                    letrasUsadas.append(LETRA[0])

            # Mostrando as letras inválidas
            print()
            if len(letrasUsadas) == 1:
                LETRASJUNTAS = "Letra Usada: "
                LETRASJUNTAS += " ".join(v.upper() for v in letrasUsadas)
            else:
                LETRASJUNTAS = "Letras Usadas: "
                LETRASJUNTAS += " ".join(v.upper() for v in letrasUsadas)

            print(f'{LETRASJUNTAS:^{TAM*2}} ')
            print()

        # Mostrando o tema selecionado
        l("——", TAM)
        TEMAESCOLHIDO = "Tema Escolhido: " + "".join(TEMASPossiveis[TEMA-1])
        msgAnimada(f"{TEMAESCOLHIDO:^{TAM*2}}", ANIMACAO)

        # 1ª Mostrando o boneco
        l("——", TAM)
        boneco(C)

        # ---------------------------------------------------------------------------

        # Verificando a vitória ou derrota
        if "_ " not in frase:
            break

        # Pedindo as letra para o usuário
        TEMAS = False
        ANIMACAO = True
        l("——", 40)
        msgAnimada("Insira uma letra: ", ANIMACAO, "")
        ANIMACAO = False
        LETRA = input().strip()
        try:
            if not LETRA[0].isalpha():
                # Bloco inválido 1
                valorInvalido("Números ou símbolos não são válidos", "——", 80)
                limpaTela()
                continue

            # Bloco verdadeiro
            LETRA = LETRA[0]

            if LETRA not in word or LETRA.upper() + " " in frase:
                C += 1
                PRIMEIROERRO += 1

            if C == 6:
                break

            continue

        except IndexError:
            # Bloco inválido 2
            valorInvalido("Espaços não são válidos", "——", 80)
            limpaTela()
            continue

    # Status
    ANIMACAO = True
    limpaTela()
    l("——")

    if C == 6:
        msgAnimada(f"{'Você morreu!':^{TAM}}", ANIMACAO)
        l("——")
        print(f"A palavra era: {word}")
        l("——")

    else:
        msgAnimada(f"{'Você sobreviveu!':^{TAM}}", ANIMACAO)
        l("——")

    # Perguntando se o jogador deseja jogar novamente
    SAIR = False
    while True:

        msgAnimada("Deseja jogar novamente [S/N]: ", ANIMACAO, "")
        RESP = str(input())

        if RESP[0] in ["s", "S"]:
            TEMAS = True
            MAINTITLE = False
            break

        if RESP[0] in ["n", "N"]:
            SAIR = True
            break

        valorInvalido('Digite apenas "S" ou "N"', "——")
        continue

    if SAIR:
        break
