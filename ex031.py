import os
resultado:str = ""

def gravar():
    global resultado
    arquivo = "ex31.txt"
    diretorio = "C:\\temp\\"
    caminho =  diretorio + arquivo
    modo = "w"
    enc="utf-8"

    if(os.path.exists(diretorio) and os.path.isdir(diretorio)):
        if(os.path.exists(caminho) and os.path.isfile(arquivo)):
            modo = "a"
        with open(caminho, modo, encoding=enc) as arq:
            arq.write(resultado)
    else:
        createdir(diretorio)

def createdir(dir):
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    gravar()

def quadrado(n):
    return n*n

def main():
    global resultado
    for i in range(10, 151):
        resultado += str(quadrado(i)) + "\n"
        gravar()
        
if __name__ == "__main__":
    main()
