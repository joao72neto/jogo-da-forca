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
            valorInvalido("Valor fora do intervalo")
            limpaTela()
            return None
            
        return resp
        
    except ValueError:
        valorInvalido("Digite apenas números inteiros")
        limpaTela()
        return None

    
    

#Criando o menu
def menu(ANIMACAO, tema=[]):
    
    # Menu principal
    while True:
        l("——")
        msgAnimada("1 - Iniciar")
        msgAnimada("2 - Configurações")
        l("——")
        #Pegando a respota do usuário
        msgAnimada("Sua escolha: ", True, "")
        resp = pegarInteiros([1, 2])
        
        if resp == 1:
            inicio(ANIMACAO, tema)
            break
        
        elif resp == 2:
            configuracoes()
            break
            
        
    
def inicio(ANIMACAO, tema=[]):
    
    while True:
        
        l("——")
        msgAnimada("1 - Alimentos", ANIMACAO)
        msgAnimada("2 - Sentimentos", ANIMACAO)
        msgAnimada("3 - Games", ANIMACAO)
        msgAnimada("4 - Instrumentos", ANIMACAO)
        msgAnimada("5 - Filmes", ANIMACAO)
        l("——")
        
        #Pegando a resposta do usuário
        msgAnimada("Sua resposta: ", True, "")
        
        escolha = pegarInteiros([1, 2, 3, 4, 5])
        
        if escolha is not None:
            tema.append(escolha)
            break
        
        
  
    
def modoNormal():
    msgAnimada("Teste")

def modoAleatorio():
    msgAnimada("Teste")

def configuracoes():
    msgAnimada("Teste")


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
    C = PRIMEIROERRO = 0

    # Gerando a frase completa
    frase = []
    
    #Tema escolhido pelo usuáiro
    tema = []

    # --------------------------------------------------------------------------- 
    #Exibindo o menu do jogo
    menu(ANIMACAO, tema)
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
