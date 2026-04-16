import os
fib: int = 0
linha = ""
def fibonaci(num):
    i = 0
    atual: int = 0
    anterior: int = 0
    global fib
    global linha
            
    while(i < num):
        if(i < 2):
            fib = i
            anterior = atual
            atual = fib
        else:
            fib = atual + anterior
            anterior = atual
            atual = fib
        linha += str(fib) + "\n".
        i += 1
    print(linha)
    gravar()
        
def gravar():
    global linha
    modo = "w"
    enc = "utf-8"
    diretorio = "C:\\temp\\"
    arquivo = "ex37.txt"
    caminho = diretorio + arquivo

    if(os.path.exists(diretorio) and os.path.isdir(diretorio)):
        with open(caminho, modo, encoding=enc) as arq:
            arq.write(linha)
    else:
        createdir(diretorio)
        
def createdir(dir):
    os.makedirs(dir)
    os.chmod(dir, 0o744)
    gravar()

def main():
    n = int(input("Quantidade de termos fibonaci: "))
    fibonaci(n)
   
if __name__ == "__main__":
    main()
