class TrieNode:
    def __init__(self):
        self.children = {}
        self.fin = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertar(self, palabra):
        nodo = self.root
        for c in palabra:
            if c not in nodo.children:
                nodo.children[c] = TrieNode()
            nodo = nodo.children[c]
        nodo.fin = True

    def buscar_prefijo(self, prefijo):
        nodo = self.root
        for c in prefijo:
            if c not in nodo.children:
                return []
            nodo = nodo.children[c]
        return self._recoger(palabra_actual=prefijo, nodo=nodo)

    def _recoger(self, palabra_actual, nodo):
        resultados = []
        if nodo.fin:
            resultados.append(palabra_actual)
        for c, hijo in nodo.children.items():
            resultados.extend(
                self._recoger(palabra_actual + c, hijo)
            )
        return resultados

    def eliminar(self, palabra):
        self._eliminar(self.root, palabra, 0)

    def _eliminar(self, nodo, palabra, i):
        if i == len(palabra):
            nodo.fin = False
            return len(nodo.children) == 0

        c = palabra[i]
        if c not in nodo.children:
            return False

        borrar = self._eliminar(nodo.children[c], palabra, i + 1)

        if borrar:
            del nodo.children[c]
            return not nodo.fin and len(nodo.children) == 0

        return False
