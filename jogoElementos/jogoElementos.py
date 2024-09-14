"""Biblioteca com elementos fundamentais do jogo"""

from estilo import msgAnimada, titulo, l
from tratarErros import pegarInteiros, removerAcentos

#------------------------------- Temas Possíveis ---------------------------------
def temas():

    """Todos os possíveis tema e possíveis palavras do jogo"""

    return {
    "alimentos":
    ["Pizza", "Pão", "Arroz", "Frango", "Sopa", "Bolo", "Queijo",
    "Maçã", "Batata", "Peixe", "Manga", "Torta", "Uva", "Cereal",
    "Milho", "Carne", "Salada", "Feijão", "Banana", "Melancia", "Ovo",
    "Cenoura", "Morango", "Abacate", "Laranja", "Tomate", "Coco", "Melão",
    "Biscoito", "Iogurte", "Macarrão", "Abobrinha", "Pimenta", "Pêra",
    "Alface", "Berinjela", "Espinafre", "Azeitona", "Brócolis", "Castanha",
    "Noz", "Amendoim", "Batata doce", "Granola", "Açúcar", "Mel", "Goiaba",
    "Lentilha", "Rabanete", "Couve"],
    "esportes":
    ["futebol", "basquete", "vôlei", "tênis", "natação", "ciclismo", "corrida",
    "ginástica", "boxe", "esgrima", "judô", "karatê", "surf", "skate", "golfe",
    "hóquei", "handebol", "beisebol", "críquete", "badminton", "rugby",
    "pólo aquático", "escalada", "patinação", "levantamento de peso",
    "atletismo", "arremesso de peso", "lançamento de dardo", "salto em altura",
    "salto com vara", "remo", "canoagem", "windsurf", "esqui", "snowboard",
    "biatlo", "triatlo", "pentatlo moderno", "taekwondo", "kickboxing",
    "muay thai", "jiu jitsu", "parkour", "dança esportiva", "esgrima",
    "softbol", "futsal", "esportes eletrônicos", "motocross", "rali", "fórmula 1",
    "automobilismo", "vela", "tênis de mesa", "caminhada", "maratona", "trail running",
    "corrida de aventura", "pesca esportiva", "arqueirismo", "polo", "bocha"],
    "games":
    ["Super Mario", "The Legend of Zelda", "Minecraft", "Fortnite", "Call of Duty",
    "Overwatch", "The Witcher", "Red Dead Redemption", "Grand Theft Auto", "Halo",
    "Assassins Creed", "FIFA", "League of Legends", "Valorant","Cyberpunk 2077",
    "Dark Souls", "Elden Ring", "Animal Crossing", "Pokémon", "Metroid", "Tetris",
    "Street Fighter", "Mortal Kombat", "Tekken", "Resident Evil", "Silent Hill",
    "Bloodborne", "Horizon Zero Dawn", "God of War", "Uncharted", "Tomb Raider",
    "Final Fantasy", "Dragon Quest", "World of Warcraft", "Starcraft", "Diablo",
    "The Sims", "SimCity", "Fallout", "Mass Effect", "Half Life", "Dota 2",
    "Counter Strike", "Portal", "Apex Legends", "Rocket League", "PUBG", "Among Us",
    "Celeste", "Stardew Valley", "Terraria", "Hades", "Undertale", "Bioshock",
    "Gears of War", "Borderlands", "Far Cry", "Splatoon", "Destiny"],
    "instrumentos":
    ["Guitarra", "Piano", "Violino", "Bateria", "Baixo", "Flauta", "Trompete",
    "Saxofone", "Clarinete", "Violoncelo", "Harpa", "Oboé", "Trombone", "Acordeão",
    "Banjo", "Bandolim", "Ukulele", "Sintetizador", "Xilofone", "Harmônica", "Gaita de fole",
    "Tímpano", "Marimba", "Conga", "Bongo", "Pandeiro", "Djembe", "Cajón",
    "Flauta doce", "Órgão", "Fagote", "Piccolo", "Lira", "Triângulo", "Metalofone",
    "Pratos", "Sitar", "Alaúde", "Rabeca", "Didgeridoo", "Flautas de pã", "Vibrafone",
    "Clavicórdio", "Melódica", "Cítara", "Balalaica", "Kalimba", "Koto", "Tambura",
    "Viola", "Maracas", "Tuba", "Eufônio", "Caixa", "Sinos", "Bumbo",
    "Steel drum", "Handpan", "Ocarina"],
    "filmes":
    ["Titanic", "A Origem", "Avatar", "O Poderoso Chefão", "Pulp Fiction", "O Cavaleiro das Trevas",
    "Forrest Gump", "Clube da Luta", "Matrix", "Gladiador", "Jurassic Park",
    "Um Sonho de Liberdade", "Star Wars", "O Senhor dos Anéis", "Interestelar", "Os Vingadores",
    "De Volta para o Futuro", "O Rei Leão", "A Lista de Schindler", "O Silêncio dos Inocentes",
    "O Resgate do Soldado Ryan", "Alien", "O Exterminador do Futuro", "Coração Valente",
    "Indiana Jones", "Os Bons Companheiros", "Casablanca", "Os Suspeitos", "Tubarão", "Rocky",
    "ET O Extraterrestre", "O Iluminado", "Scarface", "O Sexto Sentido",
    "Os Sete Crimes Capitais", "Coringa", "Piratas do Caribe", "Vingadores Ultimato",
    "Harry Potter", "Capitão América", "Pantera Negra", "O Homem de Ferro", "O Hobbit",
    "Guardiões da Galáxia", "O Lobo de Wall Street", "Django Livre", "O Grande Gatsby",
    "A Origem dos Guardiões", "O Código Da Vinci", "Missão Impossível", "Os Incríveis",
    "Homem Aranha", "Thor Ragnarok", "Jurassic World", "Os Oito Odiados", "A Bela e a Fera"]

}


#------------------------------------- Boneco -------------------------------------------------

# Função que anima o boneco na tela do jogo
def boneco(contador, letra, word, frase, animacao):

    """Função que Monta um boneco na Tela"""

    TEMPO = 0.02

    #Mostando o bonceco
    top = bonecoTop()
    bottom = bonecoBottom()

    #Mostrando o boneco
    msgAnimada(top[contador], animacao, "", TEMPO)
    mostrarPalavra(letra, word, frase, animacao)
    msgAnimada(bottom[contador], animacao, "\n", TEMPO)


def mostrarPalavra(letra, word, frase, animacao):
    # Montando a palavra
        for i, v in enumerate(word):
            if removerAcentos(v) == letra:
                frase[i] = f"{v.upper()} "

        # Mostrando a frase
        for ele in frase:
            msgAnimada(ele, animacao, "")


def bonecoTop():
    return ["""
                +---+
                |   |
                    |
                    |     """,
                """
                +---+
                |   |
                O   |
                    |     """,
                """
                +---+
                |   |
                O   |
                |   |     """,
                """
                +---+
                |   |
                O   |
               /|   |     """,
               """
                +---+
                |   |
                O   |
               /|\\  |     """,
               """
                +---+
                |   |
                O   |
               /|\\  |     """,
               """
                +---+
                |   |
                O   |
               /|\\  |     """]

def bonecoBottom():
    return ["""
                    |
                    |
                ========
        """,
        """
                    |
                    |
                ========
        """,
        """
                    |
                    |
                ========
        """,
        """
                    |
                    |
                ========
        """,
        """
                    |
                    |
                ========
        """,
        """
               /    |
                    |
                ========
        """,
        """
               / \\  |
                    |
                ========
        """]

    #------------------------------------- Menu ---------------------------------------------
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
        
        #Saindo do menu caso o tema tenha sido escolhido
        if len(tema) == 1:
            return
            
        
        
    
def inicio(ANIMACAO, TAM, tema):
    
    while True:
        
        titulo("OPÇÕES DE JOGO", TAM, ANIMACAO)
        
        #Opções do submenu início
        print()
        msgAnimada("1 - Escolher Tema\n", ANIMACAO)
        msgAnimada("2 - Tema Aleatório\n", ANIMACAO)
        msgAnimada("3 - Sair")
        l("——")

        #Pegando a resposta do usuário
        msgAnimada("Sua resposta: ", True, "")
        
        escolha = pegarInteiros([1, 2])
        
        #Analisando a resposta do usuário
        if escolha == 1:
            modoNormal(ANIMACAO, TAM, tema)
        
        if escolha == 2:
            modoAleatorio(tema)
            
        #Voltando para o menu pai caso o tema tenha sido escolhido
        if len(tema) == 1:
            return
    
       
    
def modoNormal(ANIMACAO, TAM, tema):
    #Título do jogo 
    while True:
        
        #Título do submenu modoNormal
        titulo("TEMAS POSSÍVEIS", TAM, ANIMACAO)
        print()
        
        for i, ele in enumerate(temas().keys()):
            msgAnimada(f"{i+1} - {ele.capitalize()}\n", ANIMACAO)
        
        l("——")
        msgAnimada(f"{'0 - Voltar':>{TAM}}", ANIMACAO)
        l("——")
        
        #Pegando a resposta do usuário
        msgAnimada("Sua resposta: ", True, "")
        
        escolha = pegarInteiros(range(len(temas())+1))
        
        
        if escolha == 0:
            return
        
        #Analisando as escolhas
        if escolha is not None:
            tema.append(escolha)
            break

        

def modoAleatorio(tema):
    
    #Import para a geração de números aleatórios 
    from random import randint
    
    #Escolhendo o tema de forma aleatória
    tema.append(randint(1, len(temas())))
    