def boneco(contador):
    if contador == 0:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                    |
                    |     """, animacao, "", 0.018)


        #Montando a palavra
        for i, v in enumerate(word):
            if v == letra:
                frase[i] = f"{letra.upper()} "

        #Mostrando a frase    
        for ele in frase:
            msgAnimada(ele, animacao, "")
            
            
        #2ª perte do desenho da forca 
        msgAnimada("""
                    |
                    |
                ========
        """, animacao, "\n", 0.018)
    elif contador == 1:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
                    |     """, animacao, "", 0.018)


        #Montando a palavra
        for i, v in enumerate(word):
            if v == letra:
                frase[i] = f"{letra.upper()} "

        #Mostrando a frase    
        for ele in frase:
            msgAnimada(ele, animacao, "")
            
            
        #2ª perte do desenho da forca 
        msgAnimada("""
                    |
                    |
                ========
        """, animacao, "\n", 0.018)
    elif contador == 2:
       #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
                |   |     """, animacao, "", 0.018)


        #Montando a palavra
        for i, v in enumerate(word):
            if v == letra:
                frase[i] = f"{letra.upper()} "

        #Mostrando a frase    
        for ele in frase:
            msgAnimada(ele, animacao, "")
            
            
        #2ª perte do desenho da forca 
        msgAnimada("""
                    |
                    |
                ========
        """, animacao, "\n", 0.018) 
    elif contador == 3:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|   |     """, animacao, "", 0.018)


        #Montando a palavra
        for i, v in enumerate(word):
            if v == letra:
                frase[i] = f"{letra.upper()} "

        #Mostrando a frase    
        for ele in frase:
            msgAnimada(ele, animacao, "")
            
            
        #2ª perte do desenho da forca 
        msgAnimada("""
                    |
                    |
                ========
        """, animacao, "\n", 0.018)
    elif contador == 4:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|\  |     """, animacao, "", 0.018)


        #Montando a palavra
        for i, v in enumerate(word):
            if v == letra:
                frase[i] = f"{letra.upper()} "

        #Mostrando a frase    
        for ele in frase:
            msgAnimada(ele, animacao, "")
            
            
        #2ª perte do desenho da forca 
        msgAnimada("""
                    |
                    |
                ========
        """, animacao, "\n", 0.018)
    elif contador == 5:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|\  |     """, animacao, "", 0.018)


        #Montando a palavra
        for i, v in enumerate(word):
            if v == letra:
                frase[i] = f"{letra.upper()} "

        #Mostrando a frase    
        for ele in frase:
            msgAnimada(ele, animacao, "")
            
            
        #2ª perte do desenho da forca 
        msgAnimada("""
               /    |
                    |
                ========
        """, animacao, "\n", 0.018)
    elif contador == 6:
        #1ª Parte do desenho da forca
        msgAnimada("""
                +---+
                |   |
                O   |
               /|\  |     """, animacao, "", 0.018)


        #Montando a palavra
        for i, v in enumerate(word):
            if v == letra:
                frase[i] = f"{letra.upper()} "

        #Mostrando a frase    
        for ele in frase:
            msgAnimada(ele, animacao, "")
            
            
        #2ª perte do desenho da forca 
        msgAnimada("""
               / \  |
                    |
                ========
        """, animacao, "\n", 0.018)

#Imports Gerais
from estilo import limpaTela, l, msgAnimada, valorInvalido
from random import choice

#Contantes
TAM = 40

#Variáveis globais
animacao = True

#Definindo as palavras 
palavras = [
    "amigo", "futuro", "coragem", "felicidade", "alegria", "esperança",
    "amizade", "sabedoria", "liberdade", "saudade", "aventura", "carinho",
    "honestidade", "solidariedade", "justiça", "confiança", "respeito", 
    "gentileza", "humildade", "empatia", "persistência", "gratidao", 
    "determinação", "integridade", "paciência", "resiliência", "criatividade",
    "inspiração", "equilíbrio", "tranquilidade", "sabedoria", "generosidade",
    "compaixão", "tolerância", "serenidade", "fidelidade", "otimismo", 
    "entusiasmo", "prudência", "temperança", "lealdade", "altruísmo", 
    "compromisso", "serenidade", "honra", "dignidade", "coragem", "valentia",
    "liderança", "vigilância", "disciplina", "versatilidade", "sabedoria",
    "imparcialidade", "decisão", "criatividade", "dedicação", "zelo",
    "firmeza", "confiança", "respeito", "sabedoria", "amizade", "esperança"
]


while True:
    #Escolhendo uma nova palavra 
    word = choice(palavras)

    #Espaço para preencher as palavras
    frase = ["_ "] * len(word)
    letrasUsadas = []

    #Resetando as letras
    letra = ""
    c=primeiraLetra=0

    while True:

        #Título
        if primeiraLetra == 0:
            limpaTela()
            msgAnimada("——" * (TAM // 2), animacao)
            msgAnimada(f"{'Jogo da Forca':^{TAM}}", animacao)
            msgAnimada("——" * (TAM // 2), animacao)
        else:
            limpaTela()
            if letra not in word: letrasUsadas.append(letra[0])
            msgAnimada("——" * TAM, animacao)
            
            #Mostrando as letras
            if letrasUsadas == []:
                msgAnimada(f"{'Tentativas aparecerão aqui':^{TAM*2}}", animacao)
            else:
                letrasJuntas = " ".join (ele.upper() for ele in letrasUsadas)
                print(f'{letrasJuntas:^{TAM*2}} ')


        #Definindo as palavras do jogo
        if frase == word: word = choice(palavras)

        # --------------------------------------------------------------------------- 

        #Adicionando tema
        if animacao:
            while True:
                if not animacao : msgAnimada("——" * (TAM // 2), animacao)
                msgAnimada("Escolha um tema abaixo:", animacao)
                msgAnimada("——" * (TAM // 2), animacao)
                msgAnimada("1 - Comida", animacao)
                msgAnimada("2 - Sentimentos", animacao)
                msgAnimada("3 - Games", animacao)
                msgAnimada("4 - Instrumenotos", animacao)
                msgAnimada("5 - Filmes", animacao)
                msgAnimada("——" * (TAM // 2), animacao)

                #Pegando o tema que o usuário escolheu
            
                msgAnimada("Sua escolha: ", animacao, "")
                try:
                    tema = str(input())
                    tema = int(tema)
                except ValueError:
                    valorInvalido("Digita apenas números", "——")
                    limpaTela()
                    animacao = False
                    continue

                if tema not in [1, 2, 3, 4, 5]:
                    valorInvalido("Valor fora intervalo", "——")
                    limpaTela()
                    animacao = False
                    continue
                else:
                    animacao = True
                    break

        # --------------------------------------------------------------------------- 

        #1ª Mostrando o boneco 
        if animacao : limpaTela()
        msgAnimada("——" * (TAM), animacao)
        boneco(c)

        # ---------------------------------------------------------------------------

        #Verificando a vitória ou derrota
        if "_ " not in frase: break

        #Pedindo as letra para o usuário
        animacao = False
        l("——", 40)
        letra = input("Insira uma letra: ").strip()
        try:
            if not letra[0].isalpha():
                #Bloco inválido 1
                valorInvalido("Números ou símbolos não são válidos", "——")
                continue

            else:
                #Bloco verdadeiro
                letra = letra[0]
                primeiraLetra += 1
                if letra not in word or letra.upper() + " " in frase: c += 1
                if c == 6 : break
                continue

        except IndexError:
            #Bloco inválido 2
            valorInvalido("Espaços não são válidos", "——")
            continue

    #Status
    limpaTela()
    l("——")
    print(f"{'Você morreu!':^{TAM}}") if c == 6 else print(f"{'Você sobreviveu!':^{TAM}}")
    l("——")

    #Perguntando se o jogador deseja jogar novamente
    sair = False
    while True:
        resp = str(input("Deseja jogar novamente [S/N]: "))
        if resp[0] in ["s", "S"]:
            animacao = True
            break
        elif resp[0] in ["n", "N"]:
            sair = True
            break
        else: 
            valorInvalido('Digite apenas "S" ou "N"', "——")
            continue

    if sair: break