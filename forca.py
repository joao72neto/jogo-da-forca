#Imports Gerais
from estilo import limpaTela, l, msgAnimada, valorInvalido
from random import choice

#Contantes
TAM = 40

#Variáveis globais
animacao = True
letra = ""

c=0

#Definindo as palavras 
palavras = ["arroz", "feijao", "batata", "uva", "morango"]
word = choice(palavras)

#Espaço para preencher as palavras
frase = ["_ "] * len(word)

while True:

    #Título
    limpaTela()
    msgAnimada("——" * (TAM // 2), animacao)
    msgAnimada(f"{'Jogo da Forca':^{TAM}}", animacao)
    msgAnimada("——" * (TAM // 2), animacao)

    #Definindo as palavras do jogo
    if frase == word: word = choice(palavras)
    # --------------------------------------------------------------------------- 

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

    #Verificando a vitória ou derrota
    if "_ " not in frase: break

    #Pedindo as letra para o usuário
    animacao = False
    l("——")
    letra = input("Insira uma letra: ").strip()
    try:
        if not letra[0].isalpha():
            #Bloco inválido 1
            valorInvalido("Números ou símbolos não são válidos", "——")
            continue

        else:
            #Bloco verdadeiro
            if letra not in word : c += 1
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
