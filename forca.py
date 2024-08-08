#Imports Gerais
from estilo import limpaTela, l, msgAnimada, valorInvalido
from random import choice

#Contantes
TAM = 40

#Variáveis globais
animacao = True
letra = ""
frase = []
c=0

#Definindo as palavras 
palavras = ["arroz", "feijao", "batata", "uva", "morango"]
word = choice(palavras)

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


    #Mostranado os espaços das letras
    for ele in word:
        msgAnimada(f"{letra} ", animacao, "") if ele == letra else msgAnimada("_ ", animacao, "")
        frase.append(letra)
    
    #Mostando a palavra
    #for ele in word:
        #if ele == letra:
            #frase.append(f"{ele} ")
     
    
    #Mostrando a palavra
    #for i, ele in enumerate(word):
        #print(f"{frase[i]} ", end="") if frase[i] == ele else print("_ ", end="")


    #2ª perte do desenho da forca 
    msgAnimada("""
           / \  |
                |
            ========
    """, animacao, "\n", 0.018)

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
            if c == 6: break
            continue

    except IndexError:
        #Bloco inválido 2
        valorInvalido("Espaços não são válidos", "——")
        continue
