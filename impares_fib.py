import os
import sys
leu = 0 #usada pra controlar a execucao do programa

#valida impar
def isimpar(n):
    if(n % 2 != 0):
        return n
    return -1
def leitura():
    #recursos
    diretorio = "C:\\temp\\"
    arquivo = "ex37.txt"
    caminho = diretorio + arquivo
    enc = "utf-8"
    modo = "r"
    #abre o arquivo caso exista
    if(os.path.exists(caminho) and os.path.isfile(caminho)):
        with open(caminho, modo, encoding=enc) as arq:
            for fibonaci in arq:
                #valida se termo da sequencia é impar e mostra
                if(isimpar(int(fibonaci)) != -1):
                    print(fibonaci)
    #exibe opção de criação do arquivo caso ele nao seja encontrado
    else:
        global leu
        #valida se o usuario já aceitou a solicitacao de criacao do fibonaci
        if(leu > 0):
            #congela o programa até o usuario terminar a execução do fibonaci
            if(not os.path.exists(caminho)):
                #mecanismo de parada
                input("Pressione qualquer tecla quando terminar o programa executado . . . ")
                leitura()
        else:
            #opção de criação do arquivo caso a pasta nao exista
            resposta = input(("Arquivo nao encontrado, deseja carregar o programa para gerar a sequencia de fibonaci?[s/n]: "))
            
            if(resposta == "s" or resposta == "S"):
                os.startfile(".\ex037.py") #chama o programa de criação do arquivo que contem fibonaci
                leu += 1
                leitura()
            else:
                print("saindo..")
                sys.exit()
def main():
    leitura()

if __name__ == "__main__":
    main()
