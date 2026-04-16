import os
linha = -1

def isimpar(n):
    if(n % 2 != 0):
        return n
    return -1

def leitura():
    global impar
    diretorio = "C:\\temp\\"
    arquivo = "ex37.txt"
    caminho = diretorio + arquivo
    enc = "utf-8"
    modo = "r"

    
    if(os.path.exists(caminho) and os.path.isfile(caminho)):
        with open(caminho, modo, encoding=enc) as arq:
            print(arq)
            

def main():
    global impar
    leitura()
    #print(isimpar(impar))
    
    

if __name__ == "__main__":
    main()
