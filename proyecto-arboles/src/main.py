from arbol import Arbol

if __name__ == "__main__":
    arbol = Arbol()
    arbol.insertar("/root", "docs", "carpeta")
    arbol.insertar("/root/docs", "archivo.txt", "archivo", "hola mundo")

    arbol.guardar_json("data/ejemplo.json")

    nuevo = Arbol()
    nuevo.cargar_json("data/ejemplo.json")

    print("Preorden cargado:", nuevo.preorden())
