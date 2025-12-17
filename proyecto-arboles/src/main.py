from src.arbol import Arbol
from src.consola import Consola

def main():
    arbol = Arbol()
    consola = Consola(arbol)
    consola.iniciar()

if __name__ == "__main__":
    main()
