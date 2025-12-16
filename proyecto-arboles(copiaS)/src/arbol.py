import json
from nodo import Nodo

class Arbol:
    def __init__(self):
        self.root = Nodo(0, "root", "carpeta")
        self.contador_id = 1

    def buscar_por_ruta(self, ruta):
        partes = [p for p in ruta.split("/") if p]
        actual = self.root
        for p in partes[1:]:
            for h in actual.children:
                if h.nombre == p:
                    actual = h
                    break
            else:
                return None
        return actual

    def insertar(self, ruta, nombre, tipo, contenido=None):
        padre = self.buscar_por_ruta(ruta)
        if not padre:
            return None
        nuevo = Nodo(self.contador_id, nombre, tipo, contenido)
        self.contador_id += 1
        padre.agregar_hijo(nuevo)
        return nuevo

    def eliminar(self, ruta):
        nodo = self.buscar_por_ruta(ruta)
        if nodo and nodo.parent:
            nodo.parent.children.remove(nodo)

    def mover(self, origen, destino):
        nodo = self.buscar_por_ruta(origen)
        nuevo_padre = self.buscar_por_ruta(destino)
        if nodo and nuevo_padre and nodo.parent:
            nodo.parent.children.remove(nodo)
            nuevo_padre.agregar_hijo(nodo)

    def renombrar(self, ruta, nuevo_nombre):
        nodo = self.buscar_por_ruta(ruta)
        if nodo:
            nodo.nombre = nuevo_nombre

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

    def guardar_json(self, archivo):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(self.root.to_dict(), f, indent=2)
