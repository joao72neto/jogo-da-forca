from estilo import limpaTela, l, msgAnimada
from random import choice

#Contantes
TAM = 40

#Título
limpaTela()
msgAnimada("——" * (TAM // 2))
msgAnimada(f"{'Jogo da Forca':^{TAM}}")
msgAnimada("——" * (TAM // 2))

#Definindo as palavras do jogo
palavras = ["arroz", "feijao", "batata", "uva", "morango"]

# --------------------------------------------------------------------------- 

#1ª Parte do desenho da forca
msgAnimada("""
        +---+
        |   |
        O   |
       /|\  |     """, True, "", 0.018)


#Mostranado os espaços das letras
word = choice(palavras)
msgAnimada("_ " * len(word), True, "", 0.018)


#2ª perte do desenho da forca 
msgAnimada("""
       / \  |
            |
        ========
""", True, "\n", 0.018)

#Pedindo as letra para o usuário
l("——")
while True:
    letra = input("Insira uma letra: ")
    
    if letra[0].isnumeric():
        print("")
        continue
    else:
        break
l("——")
