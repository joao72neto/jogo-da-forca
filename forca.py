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
tempo = 0.02

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

#opções de temas
temasPossiveis = ["Comida", "Sentimentos", "Games", "Instrumentos", "Filmes"]

#Mostranso menus
temas=mainTitle=True

while True:
    #Escolhendo uma nova palavra 
    word = choice(palavras)

    #Espaço para preencher as palavras
    frase = ["_ "] * len(word)
    letrasUsadas = []

    #Resetando as letras
    letra = ""
    c=primeiroErro=0
    
    while True:
   
        #Definindo as palavras do jogo
        if frase == word: word = choice(palavras)

        # --------------------------------------------------------------------------- 

        #Adicionando tema
        if temas:
            while True:
            
                #Título de apresentação
                if mainTitle:
                    limpaTela()
                    l("——")
                    msgAnimada(f"{'Jogo da Forca':^{TAM}}", animacao)
                    l("——")
                    msgAnimada("Escolha um tema abaixo:", animacao)
                    l("——")
                else:
                    limpaTela()
                    l("——")
                    msgAnimada("Escolha um outro tema abaixo:", animacao)
                    l("——")
                
                #Escolhendo as categorias
                msgAnimada("1 - Comida", animacao)
                msgAnimada("2 - Sentimentos", animacao)
                msgAnimada("3 - Games", animacao)
                msgAnimada("4 - Instrumentos", animacao)
                msgAnimada("5 - Filmes", animacao)
                l("——")

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

        #Título para mostrar letras inválidas
        limpaTela()
        if primeiroErro != 0:
            
            if letra not in word and not letra.isnumeric() and letra not in letrasUsadas:
                letrasUsadas.append(letra[0])
            
            #Mostrando as letras inválidas
            print()
            if len(letrasUsadas) == 1:
                letrasJuntas ="Letra Usada: " + " ".join (ele.upper() for ele in letrasUsadas)
            else:
                letrasJuntas ="Letras Usadas: " + " ".join (ele.upper() for ele in letrasUsadas)
            print(f'{letrasJuntas:^{TAM*2}} ')
            print()

        #Mostrando o tema selecionado
        l("——", TAM)
        temaEscolhido = "Tema Escolhido: " + "".join(temasPossiveis[tema-1])
        msgAnimada(f"{temaEscolhido:^{TAM*2}}", animacao)
     

        #1ª Mostrando o boneco 
        l("——", TAM)
        boneco(c)

        # ---------------------------------------------------------------------------

        #Verificando a vitória ou derrota
        if "_ " not in frase: break

        #Pedindo as letra para o usuário
        temas = False
        animacao=True
        l("——", 40)
        msgAnimada("Insira uma letra: ", animacao, "")
        animacao=False
        letra = input().strip()
        try:
            if not letra[0].isalpha():
                #Bloco inválido 1
                valorInvalido("Números ou símbolos não são válidos", "——", 80)
                limpaTela()
                continue

            else:
                #Bloco verdadeiro
                letra = letra[0]
                
                if letra not in word or letra.upper() + " " in frase: 
                    c += 1
                    primeiroErro += 1
                    
                if c == 6 : break
                continue

        except IndexError:
            #Bloco inválido 2
            valorInvalido("Espaços não são válidos", "——", 80)
            limpaTela()
            continue

    #Status
    animacao=True
    limpaTela()
    l("——")
    msgAnimada(f"{'Você morreu!':^{TAM}}", animacao) if c == 6 else msgAnimada(f"{'Você sobreviveu!':^{TAM}}", animacao)
    l("——")

    #Perguntando se o jogador deseja jogar novamente
    sair = False
    while True:
        msgAnimada("Deseja jogar novamente [S/N]: ", animacao, "")
        resp = str(input())
        if resp[0] in ["s", "S"]:
            temas = True
            mainTitle=False
            break
        elif resp[0] in ["n", "N"]:
            sair = True
            break
        else: 
            valorInvalido('Digite apenas "S" ou "N"', "——")
            continue

    if sair: break