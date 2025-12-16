from arbol import Arbol

if __name__ == "__main__":
    arbol = Arbol()
    arbol.insertar("/root", "docs", "carpeta")
    arbol.insertar("/root/docs", "archivo.txt", "archivo", "hola mundo")

    print("Hijos de /root:", arbol.listar_hijos("/root"))
    print("Preorden:", arbol.preorden())

    arbol.guardar_json("estructura.json")
