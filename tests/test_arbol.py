import unittest
from src.arbol import Arbol

class TestArbol(unittest.TestCase):
    def test_insertar(self):
        a = Arbol()
        a.insertar("/root", "docs", "carpeta")
        self.assertEqual(len(a.root.children), 1)

    def test_mover(self):
        a = Arbol()
        a.insertar("/root", "docs", "carpeta")
        a.insertar("/root", "img", "carpeta")
        a.mover("/root/docs", "/root/img")
        self.assertEqual(len(a.buscar_por_ruta("/root/img").children), 1)

if __name__ == "__main__":
    unittest.main()
