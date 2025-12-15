import json

class Nodo:
    def __init__(self, id, nombre, tipo, contenido=None):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.contenido = contenido
        self.children = []
        self.parent = None

    def agregar_hijo(self, nodo):
        nodo.parent = self
        self.children.append(nodo)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "contenido": self.contenido,
            "children": [h.to_dict() for h in self.children]
        }

    @staticmethod
    def from_dict(data):
        nodo = Nodo(data["id"], data["nombre"], data["tipo"], data.get("contenido"))
        for h in data.get("children", []):
            hijo = Nodo.from_dict(h)
            nodo.agregar_hijo(hijo)
        return nodo


class Arbol:
    def __init__(self):
        self.root = Nodo(0, "root", "carpeta")
        self.contador_id = 1
        self.indice = {"root": self.root}

    def insertar(self, padre, nombre, tipo, contenido=None):
        nuevo = Nodo(self.contador_id, nombre, tipo, contenido)
        self.contador_id += 1
        padre.agregar_hijo(nuevo)
        self.indice[nombre] = nuevo
        return nuevo

    def renombrar(self, nodo, nuevo_nombre):
        if nodo.nombre in self.indice:
            del self.indice[nodo.nombre]
        nodo.nombre = nuevo_nombre
        self.indice[nuevo_nombre] = nodo

    def eliminar(self, nodo):
        if nodo.parent:
            nodo.parent.children.remove(nodo)
        if nodo.nombre in self.indice:
            del self.indice[nodo.nombre]

    def listar_hijos(self, nodo):
        return [h.nombre for h in nodo.children]

    def preorden(self, nodo=None, resultado=None):
        if resultado is None:
            resultado = []
        if nodo is None:
            nodo = self.root
        resultado.append(nodo.nombre)
        for h in nodo.children:
            self.preorden(h, resultado)
        return resultado

    def guardar_json(self, ruta_archivo):
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(self.root.to_dict(), f, indent=2)

    def cargar_json(self, ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.root = Nodo.from_dict(data)


if __name__ == "__main__":
    arbol = Arbol()
    docs = arbol.insertar(arbol.root, "docs", "carpeta")
    arbol.insertar(docs, "archivo.txt", "archivo", "hola mundo")

    print("Hijos de root:", arbol.listar_hijos(arbol.root))
    print("Recorrido preorden:", arbol.preorden())

    arbol.guardar_json("estructura.json")
