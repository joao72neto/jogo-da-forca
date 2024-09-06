

# Imports gerais
import platform
from os import system
from time import sleep
from sys import stdin
from sistema import matarInput, reviverInput, limparBuffer

#Constantes
TAM = 40


#Funão que mostra um título na tela
def titulo(msg, TAM, ANIMACAO):
    limpaTela()
    l("——")
    msgAnimada(f"{msg:^{TAM}}", ANIMACAO)
    l("——")

#Função que limpa a tela
limpaTela = lambda comando="clear" : system("cls") if platform.system() == "Windows" else system(comando)

#Função anônima que imprime uma linha na tela
l = lambda simb="-=", tam=20 : print(simb * tam)

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
