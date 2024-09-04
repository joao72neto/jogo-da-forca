"""Programa que simula um jogo da forca"""

'''
                    ------------------------
                    Jogo da Forca
                    ------------------------
                    1 - Start
                        0 - Voltar
                        -----------------------
                        Escolha um modo de jogo
                        -----------------------
                        1 - Modo normal
                            0 - voltar
                            ---------------
                            Temas
                            ---------------
                            1 - Alimento
                            2 - Sentimentos
                            3 - games
                            4 - Instrumentos
                            5 - Filmes
                            ---------------
                            Sua escolha:
                            ---------------
                                <inicia o game>
                        2 - Modo aleatório
                            <inicia o game>
                    2 - Settings
                        0 - Voltar
                        -----------------------
                        Configurações
                        ------------------------
                        1 - Desativar animações
                '''

# pylint: disable=c0103, r0912

# Imports Gerais
from random import choice
from estilo import limpaTela, l, msgAnimada, valorInvalido
from jogoDependencias import temas, boneco

#Função pegaInteiros
def pegarInteiros(inter=[]):
  
    try:
        resp = int(input())
        
        if inter == []:
            return resp
        
        elif resp not in inter:
            valorInvalido("Valor fora do intervalo", "——")
            limpaTela()
            return None
            
        return resp
        
    except ValueError:
        valorInvalido("Digite apenas números inteiros", "——")
        limpaTela()
        return None

#Funão que mostra um título na tela 
def titulo(msg, TAM, ANIMACAO):
    limpaTela()
    l("——")
    msgAnimada(f"{msg:^{TAM}}", ANIMACAO)
    l("——")
    
#----------------------------------------------------------------------------------------------
#Criando o menu
def menu(ANIMACAO, vezesJogadas, TAM, tema):
    
    # Menu principal
    while True:
        
        if vezesJogadas == 0:
            ANIMACAO = True
            
            #Título do jogo 
            titulo("JOGO DA FORCA", TAM, ANIMACAO)

            #Opções do menu 
            print()
            msgAnimada(f"{'Enter para Iniciar':^{TAM}}", ANIMACAO)
            print()
            l("——")
            
            #Esperando o usuário pressionar qualquer tecla
            input()
        
        #Indo para o submenu "Início"
        ANIMACAO = False
        inicio(ANIMACAO, TAM, tema)
        
        vezesJogadas = 0
        
        if len(tema) == 1:
            return
            
        
        
    
def inicio(ANIMACAO, TAM, tema):
    while True:
        titulo("MODOS DE JOGO", TAM, ANIMACAO)
        
        #Opções do submenu início
        print()
        msgAnimada("1 - Modo Normal\n", ANIMACAO)
        msgAnimada("2 - Modo Aleatório\n", ANIMACAO)
        l("——")
        msgAnimada(f"{'0 - Voltar':>{TAM}}", ANIMACAO)
        l("——")

        #Pegando a resposta do usuário
        msgAnimada("Sua resposta: ", True, "")
        
        escolha = pegarInteiros([0, 1, 2])
        
        #Analisando a resposta do usuário
        if escolha == 0:
            return
        
        if escolha == 1:
            modoNormal(ANIMACAO, TAM, tema)
            
            if len(tema) == 1:
                return
        
        if escolha == 2:
            modoAleatorio()
    
       
    
def modoNormal(ANIMACAO, TAM, tema):
    #Título do jogo 
    while True:
        
        #Título do submenu modoNormal
        titulo("TEMAS POSSÍVEIS", TAM, ANIMACAO)
        print()
        msgAnimada("1 - Alimentos\n", ANIMACAO)
        msgAnimada("2 - Sentimentos\n", ANIMACAO)
        msgAnimada("3 - Games\n", ANIMACAO)
        msgAnimada("4 - Instrumentos\n", ANIMACAO)
        msgAnimada("5 - Filmes\n", ANIMACAO)
        l("——")
        msgAnimada(f"{'0 - Voltar':>{TAM}}", ANIMACAO)
        l("——")
        
        #Pegando a resposta do usuário
        msgAnimada("Sua resposta: ", True, "")
        
        escolha = pegarInteiros([0, 1, 2, 3, 4, 5])
        
        
        if escolha == 0:
            return
        
        #Analisando as escolhas
        if escolha is not None:
            tema.append(escolha)
            break

        

def modoAleatorio():
    msgAnimada("Teste")


#------------------------------------------------------------------------------------------------
#Centralização
TAM = 40

#Animações
ANIMACAO = True
TEMPO = 0.02

# Definindo as palavras
palavras = temas()

# Temas disponíveis
temasPossiveis = ["alimentos", "sentimentos", "games", "instrumentos", "filmes"]


while True: # Repete o jogo

    # Mostrar erros
    letrasUsadas = []

    # Resetando as letras
    LETRA = ""
    C = PRIMEIROERRO = vezesJogadas = 0

    # Gerando a frase completa
    frase = []
    
    #Tema escolhido pelo usuáiro
    tema = []

    # --------------------------------------------------------------------------- 
    #Exibindo o menu do jogo
    menu(ANIMACAO, vezesJogadas, TAM, tema)
    print(tema)

    # Escolhendo a palavra de acordo com o tema
    word = choice(palavras[temasPossiveis[(tema[0]-1)]]).lower()

    # Espaço para preencher as palavras
    for ele in word.split():
        frase += ["_ "] * len(ele)
        frase += " "
    # ---------------------------------------------------------------------------
    
    #Rodando o jogo
    while True:
        
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
        TEMAESCOLHIDO = "Tema Escolhido: " + "".join(temasPossiveis[tema[0]-1])
        msgAnimada(f"{TEMAESCOLHIDO:^{TAM*2}}", ANIMACAO)

        # 1ª Mostrando o boneco
        l("——", TAM)
        boneco(C, LETRA, word, frase, ANIMACAO)

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
        msgAnimada(f"A palavra era: {word}")
        l("——")

    else:
        msgAnimada(f"{'Você sobreviveu!':^{TAM}}", ANIMACAO)
        l("——")

    # Perguntando se o jogador deseja jogar novamente
    SAIR = False
    while True: # Consistir S ou N

        msgAnimada("Deseja jogar novamente [S/N]: ", ANIMACAO, "")
        RESP = str(input())

        if RESP[0] in ["s", "S"]:
            vezesJogadas = 1
            break

        if RESP[0] in ["n", "N"]:
            SAIR = True
            break

        valorInvalido('Digite apenas "S" ou "N"', "——")
        continue

    if SAIR:
        break
