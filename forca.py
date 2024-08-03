#Imports Gerais
from estilo import limpaTela, l, msgAnimada, valorInvalido
from random import choice
from time import sleep

#Contantes
TAM = 40

#Variáveis globais
animacao = True

while True:
    #Título
    limpaTela()
    msgAnimada("——" * (TAM // 2), animacao)
    msgAnimada(f"{'Jogo da Forca':^{TAM}}", animacao)
    msgAnimada("——" * (TAM // 2), animacao)

    #Definindo as palavras do jogo
    palavras = ["arroz", "feijao", "batata", "uva", "morango"]
    word = palavras[0]
    # --------------------------------------------------------------------------- 

    #1ª Parte do desenho da forca
    msgAnimada("""
            +---+
            |   |
            O   |
           /|\  |     """, animacao, "", 0.018)


    #Mostranado os espaços das letras
    msgAnimada("_ " * len(word), animacao, "", 0.018)


    #2ª perte do desenho da forca 
    msgAnimada("""
           / \  |
                |
            ========
    """, animacao, "\n", 0.018)

    #Pedindo as letra para o usuário
    l("——")
    letra = input("Insira uma letra: ").strip()
    try:
        if not letra[0].isalpha():
            valorInvalido("Números ou símbolos não são válidos", "——")
            animacao = False
            continue
        else:
            word = choice(palavras)
            animacao = True
            break
    except IndexError:
        valorInvalido("Espaços não são válidos", "——")
        animacao = False
        continue
   