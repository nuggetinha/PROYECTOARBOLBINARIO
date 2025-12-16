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
