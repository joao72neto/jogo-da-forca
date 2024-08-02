from estilo import limpaTela, l, msgAnimada
from random import choice

#Contantes
TAM = 40

#Título
limpaTela()
msgAnimada("-=" * (TAM // 2), False)
msgAnimada(f"{'Jogo da Forca':^{TAM}}", False)
msgAnimada("-=" * (TAM // 2), False)

#Definindo as palavras do jogo
palavras = ["arroz", "feijao", "batata", "uva", "morango"]

#Desenhado a forca 
print("""
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
                ========
""", end="\n")

#Mostrando traços do tamanho da palavra
for word in choice(palavras):
    for letras in word:
        print("_ ", end="")
print("\n")

l()