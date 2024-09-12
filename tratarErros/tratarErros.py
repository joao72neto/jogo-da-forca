from estilo import msgAnimada, l, limpaTela
from time import sleep
from sistema import matarInput, reviverInput, limparBuffer
import unicodedata

#Definindo um tamanho padrão
TAM = 40

#Mostrando mensagem de valor não correspondente 
def valorInvalido(texto="Valor Inválido", simb = "-=", tam=TAM, tempo=0.03, animacao=True):
    old = matarInput()
    try:
        limpaTela()
        l(simb, (tam // 2))
        msgAnimada(f"{texto:^{tam}}", animacao, "\n", tempo)
        l(simb, (tam // 2))
        sleep(0.3) if animacao else sleep(1)
    finally:
        reviverInput(old)
        limparBuffer()


#Pegando apenas valores inteiros
def pegarInteiros(inter=[]):
  
    try:
        resp = int(input())
        
        if inter == []:
            return resp
        
        elif resp not in inter:
            valorInvalido("Valor fora do intervalo", "——")
            limpaTela()
            return None
            
        return resp
        
    except ValueError:
        valorInvalido("Digite apenas números inteiros", "——")
        limpaTela()
        return None
    
    
#Pegando apenas valores inteiros
def pegarCaracteres(inter=[]):
  
    resp = str(input()).strip().lower()
    
    if inter == []:
        return resp
    
    elif resp not in inter:
        valorInvalido("Caracteres Inválido", "——")
        limpaTela()
        return None
        
    return resp
        


#Função que remove os acentos das palavras
def removerAcentos(msg):
    msgNormalizado = unicodedata.normalize("NFKD", msg)
    
    msgSemAcentos = ''.join(letra for letra in msgNormalizado if not unicodedata.combining(letra))
    
    return msgSemAcentos
#---------------------------------------------------------------------