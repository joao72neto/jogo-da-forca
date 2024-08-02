from estilo import limpaTela, l, msgAnimada
from random import choice

#Contantes
TAM = 40

#Título
limpaTela()
msgAnimada("——" * (TAM // 2), False)
msgAnimada(f"{'Jogo da Forca':^{TAM}}", False)
msgAnimada("——" * (TAM // 2), False)

#Definindo as palavras do jogo
palavras = ["arroz", "feijao", "batata", "uva", "morango"]

# --------------------------------------------------------------------------- 

#1ª Parte do desenho da forca
print("""
        +---+
        |   |
        O   |
       /|\  |     """, end="")


#Mostranado os espaços das letras
word = choice(palavras)
print("_ " * len(word), end="")


#2ª perte do desenho da forca 
print("""
       / \  |
            |
        ========
""", end="\n")

#Pedindo as letra para o usuário
l("——")
print("Insira uma letra: \n")
