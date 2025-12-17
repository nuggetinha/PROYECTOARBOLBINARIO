import json
from src.nodo import Nodo
from src.trie import Trie



class Arbol:
    def __init__(self):
        self.root = Nodo(0, "root", "carpeta")
        self.contador_id = 1

        # Índices de búsqueda (Día 5–6)
        self.trie = Trie()          # autocompletado
        self.indice = {}            # búsqueda exacta

        # registrar root
        self.trie.insertar("root")
        self.indice["root"] = self.root

    # ---------------- BÚSQUEDA POR RUTA ----------------

    def buscar_por_ruta(self, ruta):
        partes = [p for p in ruta.split("/") if p]
        actual = self.root
        for p in partes[1:]:
            encontrado = False
            for h in actual.children:
                if h.nombre == p:
                    actual = h
                    encontrado = True
                    break
            if not encontrado:
                return None
        return actual

    # ---------------- OPERACIONES DEL ÁRBOL ----------------

    def insertar(self, ruta, nombre, tipo, contenido=None):
        padre = self.buscar_por_ruta(ruta)
        if not padre:
            return None

        nuevo = Nodo(self.contador_id, nombre, tipo, contenido)
        self.contador_id += 1
        padre.agregar_hijo(nuevo)

        # actualizar índices
        self.trie.insertar(nombre)
        self.indice[nombre] = nuevo

        return nuevo

    def eliminar(self, ruta):
        nodo = self.buscar_por_ruta(ruta)
        if nodo and nodo.parent:
            nodo.parent.children.remove(nodo)

            # actualizar índices
            self.trie.eliminar(nodo.nombre)
            if nodo.nombre in self.indice:
                del self.indice[nodo.nombre]

    def mover(self, origen, destino):
        nodo = self.buscar_por_ruta(origen)
        nuevo_padre = self.buscar_por_ruta(destino)
        if nodo and nuevo_padre and nodo.parent:
            nodo.parent.children.remove(nodo)
            nuevo_padre.agregar_hijo(nodo)

    def renombrar(self, ruta, nuevo_nombre):
        nodo = self.buscar_por_ruta(ruta)
        if nodo:
            # quitar nombre viejo
            self.trie.eliminar(nodo.nombre)
            if nodo.nombre in self.indice:
                del self.indice[nodo.nombre]

            # asignar nombre nuevo
            nodo.nombre = nuevo_nombre
            self.trie.insertar(nuevo_nombre)
            self.indice[nuevo_nombre] = nodo

    def listar_hijos(self, ruta):
        nodo = self.buscar_por_ruta(ruta)
        return [h.nombre for h in nodo.children] if nodo else []

    def preorden(self, nodo=None, res=None):
        if res is None:
            res = []
        if nodo is None:
            nodo = self.root
        res.append(nodo.nombre)
        for h in nodo.children:
            self.preorden(h, res)
        return res

    # ---------------- BÚSQUEDA (DÍA 5–6) ----------------

    def buscar_exacto(self, nombre):
        return self.indice.get(nombre)

    def autocompletar(self, prefijo):
        return self.trie.buscar_prefijo(prefijo)

    # ---------------- PERSISTENCIA JSON ----------------

    def guardar_json(self, archivo):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(self.root.to_dict(), f, indent=2)

    def cargar_json(self, archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            self.root = Nodo.from_dict(json.load(f))

        # reconstruir índices
        self.trie = Trie()
        self.indice = {}
        self._reconstruir_indices(self.root)

        self.contador_id = self._calcular_max_id(self.root) + 1

    def _reconstruir_indices(self, nodo):
        self.trie.insertar(nodo.nombre)
        self.indice[nodo.nombre] = nodo
        for h in nodo.children:
            self._reconstruir_indices(h)

    def _calcular_max_id(self, nodo):
        max_id = nodo.id
        for h in nodo.children:
            max_id = max(max_id, self._calcular_max_id(h))
        return max_id
