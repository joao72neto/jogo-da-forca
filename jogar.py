"""Programa que simula um jogo da forca"""


# pylint: disable=c0103, r0912

# Imports Gerais
from random import choice, randint
from estilo import limpaTela, l, msgAnimada
from tratarErros import valorInvalido, pegarCaracteres
from jogoElementos import temas, boneco, menu


#Definindo um tamanho para a centralização
TAM = 40

#Definindo se o usuário quer mudar de modo ou não
MUDARMODO = True

#Animações
ANIMACAO = True
TEMPO = 0.02

# Definindo as palavras do jogo
palavras = temas()

# Temas disponíveis
temasPossiveis = list({tema for tema in palavras.keys()})

#Qtd de vezes que o jogador jogou
vezesJogadas = 0

#Modo escolhido pelo usuaŕio
escolhaModo = []

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
    
    if MUDARMODO:
        
        #Exibindo o menu do jogo
        menu(ANIMACAO, vezesJogadas, TAM, tema, escolhaModo)
        
    if escolhaModo[0] == 2 and vezesJogadas >= 1:
        
        #Mudando o tema caso o jogador tenha escolhido o modo aleatório
        tema.append(randint(1, len(temasPossiveis)))


    # Escolhendo a palavra de acordo com o tema escolhido
    word = choice(palavras[temasPossiveis[(tema[0]-1)]]).lower()

    # Criando o tacejado da palavra escolhida aleatóriamente
    for ele in word.split():
        frase += ["_ "] * len(ele)
        frase += " "

    #Rodando o jogo
    while True:

        # Título para mostrar letras inválidas digitadas
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
        TEMPO = 0.015
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
        
        #Verificando se o usuário está tentando adivinhar a palavra
        if len(word) == len(LETRA):
            if word.lower().strip() == LETRA.lower():
                break
        
        
        try:
            if not LETRA[0].isalpha():
                # Bloco inválido
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
        msgAnimada(f"A palavra era: {word}")
        l("——")

    else:
        msgAnimada(f"{'Você sobreviveu!':^{TAM}}", ANIMACAO)
        l("——")



    # Perguntando se o jogador deseja jogar novamente
    SAIR = False
    while True: # Consistir S ou N

        msgAnimada("Deseja jogar novamente [S/N]: ", ANIMACAO, "")
        RESP = pegarCaracteres(["s", "n"])

        if RESP is None:
            continue
        
        if RESP == "s":
            #Perguntando se o jogador quer mudar de modo de jogo
            while True:
                limpaTela()
                l("——")
                msgAnimada("Deseja mudar de modo de jogo? [S/N]: ", ANIMACAO, "")
                RESP2 = pegarCaracteres(["s", "n"])
                
                if RESP2 is None:
                    continue
                    
                if RESP2 == "n":
                    MUDARMODO = False
                    break
                
                MUDARMODO = True
                break    
            
            # Atualizando a qtd de vezes que o usuaŕio jogou o jogo
            vezesJogadas = 1
            break

        if RESP == "n":
            SAIR = True
            break

    if SAIR:
        break
