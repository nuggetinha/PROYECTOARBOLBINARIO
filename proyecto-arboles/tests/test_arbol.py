import unittest
from src.arbol import Arbol


class TestArbol(unittest.TestCase):

    def test_insertar(self):
        ...

    def test_mover(self):
        ...

    def test_persistencia(self):
        ...

    def test_busqueda_exacta(self):
        ...

    def test_autocompletado(self):
        ...

    def test_eliminar_inexistente(self):
        a = Arbol()
        a.eliminar("/root/noexiste")
        self.assertEqual(a.preorden(), ["root"])

    def test_autocompletar_vacio(self):
        a = Arbol()
        res = a.autocompletar("zzz")
        self.assertEqual(res, [])

    def test_consistencia_mover_renombrar(self):
        a = Arbol()
        a.insertar("/root", "docs", "carpeta")
        a.insertar("/root", "img", "carpeta")
        a.mover("/root/docs", "/root/img")
        a.renombrar("/root/img/docs", "docs2")
        self.assertIsNotNone(a.buscar_exacto("docs2"))


if __name__ == "__main__":
    unittest.main()
