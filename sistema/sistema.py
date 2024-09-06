# Imports por plataforma

import platform
from sys import stdin

if platform.system() == "Windows":
    import msvcrt
else:
    import termios
    from tty import setcbreak



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
