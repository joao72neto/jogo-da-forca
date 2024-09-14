"""Programa que simula um jogo da forca"""


# pylint: disable=c0103, r0912

# Imports Gerais
from random import choice, randint
from estilo import limpaTela, l, msgAnimada
from tratarErros import valorInvalido, pegarCaracteres, removerAcentos
from jogoElementos import temas, boneco, menu


#Definindo um tamanho para a centralização
TAM = 40

#Definindo se o usuário quer mudar de modo ou não
MUDARMODO = True

#Animações
ANIMACAO = True
TEMPO = 0.02

#Saindo do programa
SAIR = [False]

# Definindo as palavras do jogo
palavras = temas()

# Temas disponíveis
temasPossiveis = list(palavras.keys())

#Qtd de vezes que o jogador jogou
vezesJogadas = 0

while True: # Repete o jogo

    # Mostrar letras que já foram usadas
    letrasUsadas = []

    # Resetando as letras
    LETRA = ""

    #Muda o desenho do boneco
    C = PRIMEIROERRO = 0

    # Gerando a frase completa
    frase = []
    
    #Tema escolhido pelo usuáiro
    tema = []
    
    #Exibindo o menu do jogo
    menu(ANIMACAO, vezesJogadas, TAM, tema, SAIR)
        
        
    #Verificando se o usuário deseja sair do jogo
    if SAIR[0]:
        break    
    
    # Escolhendo a palavra de acordo com o tema escolhido
    word = choice(palavras[temasPossiveis[(tema[0]-1)]]).lower()

    # Criando o tacejado da palavra escolhida aleatóriamente
    for ele in word.split():
        frase += ["_ "] * len(ele)
        frase += [" "]

    teste = [ele.lower() for ele in frase if isinstance(ele, str) and ele != "_ "]

    
    #Rodando o jogo
    while True:

        #Tirnado acentos da palavra
        wordSemAcento = removerAcentos(word)
        
        # Título para mostrar letras inválidas digitadas
        limpaTela()
        if PRIMEIROERRO != 0:

            if LETRA not in wordSemAcento and LETRA.isalpha():
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
        #TEMPO = 0.015
        l("——", TAM)
        TEMAESCOLHIDO = "Tema Escolhido: " + "".join(temasPossiveis[tema[0]-1].capitalize())
        msgAnimada(f"{TEMAESCOLHIDO:^{TAM*2}}", ANIMACAO, "\n", TEMPO)
        TEMPO = 0.02

        # Mostrando o boneco
        l("——", TAM)
        boneco(C, LETRA, word, frase, ANIMACAO)


        # Saindo do jogo caso o usuário acerte a palavra
        if "_ " not in frase:
            break

        # Pedindo as letras para o usuário
        l("——", 40)
        msgAnimada("Insira uma letra: ", ANIMACAO, "")
        ANIMACAO = False
        LETRA = input().strip()
        
        #Tirando os acentos da letra escolhida
        LETRA = removerAcentos(LETRA)
        
        
        #Verificando se o usuário está tentando adivinhar a palavra
        if len(wordSemAcento) == len(LETRA):
            if wordSemAcento.lower().strip() == LETRA.lower():
                break
        
        
        try:
            #Verificando se não é uma letra
            if not LETRA[0].isalpha():
                valorInvalido("Números ou símbolos não são válidos", "——", 80)
                limpaTela()
                continue

            # Pegando só o primeiro caractere
            LETRA = LETRA[0]
 
            #Normalizando a frase para análise
            fraseNormalizada = [removerAcentos(e.lower().strip()) for e in frase if isinstance(e, str) and e.strip() != "_"]
 
            #Verificando se a letra está na palavra gerada aleatóriamente
            if LETRA not in wordSemAcento or LETRA.lower() in fraseNormalizada:
                C += 1
                
                if LETRA not in wordSemAcento:
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
    while True: # Consistir, jogar novamente
        
        l("——")

        if C == 6:
            msgAnimada(f"{'Você morreu! :(':^{TAM}}", ANIMACAO)
            
            #Mostrando qual era a palavra
            palavraEscolhida = "A palavra era: " + "".join(word.capitalize()) 
            l("——")
            msgAnimada(f"\n{palavraEscolhida:^{TAM}}\n", ANIMACAO)
            l("——")

        else:
            msgAnimada(f"{'Você sobreviveu! :)':^{TAM}}", ANIMACAO)
            l("——")


        # Perguntando se o jogador deseja jogar novamente
        msgAnimada("Deseja jogar novamente [S/N]: ", ANIMACAO, "")
        RESP = pegarCaracteres(["s", "n"])


        if RESP is None:
            ANIMACAO = False
            continue
        
        if RESP == "s":
            ANIMACAO = True
            vezesJogadas += 1
            break

        ANIMACAO = True
        SAIR[0] = True
        break

    if SAIR[0]:
        break

#Despedindo
limpaTela()
l("——")
msgAnimada(f"{'Obrigado por Jogar :)':^{TAM}}", ANIMACAO)
l("——")