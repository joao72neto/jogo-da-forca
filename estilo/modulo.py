#Imports gerais
import platform
from os import system
from time import sleep
from sys import stdin

#Imports por plataforma
if platform.system() == "Windows":
    import msvcrt
else:
    import termios
    from tty import setcbreak


#Função que limpa a tela
limpaTela = lambda comando="clear" : system("cls") if platform.system() == "Windows" else system(comando)

#Função anônima que imprime uma linha na tela
l = lambda tam=20: print("-=" * tam)

#Função que imprime uma mensagem animada na tela
def msgAnimada(msg="teste", animacao=True, end="\n", tempo=0.03):
    if animacao:
        old = matarInput()
        try:
            for letra in msg:
                print(f"{letra}", end="", flush=True)
                sleep(tempo)
            print(end, end="")
        finally:
            reviverInput(old)
            limparBuffer()
    else:
        print(msg, end=end)

#------------------------------------Dependências-----------------------------------------#

#Desabilitando inputs
def matarInput():
    if platform.system() == "Windows":
        pass
    else:
        descritor = stdin.fileno()
        old_settings = termios.tcgetattr(descritor)
        setcbreak(descritor)
        return old_settings

#Habilita os inputs
def reviverInput(old_settings):
    if platform.system() == "Windows":
        pass
    else:
        termios.tcsetattr(stdin.fileno(), termios.TCSADRAIN, old_settings)

#Limpa o buffer de entrada
def limparBuffer():
    if platform.system() == "Windows":
        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        termios.tcflush(stdin, termios.TCIFLUSH)

