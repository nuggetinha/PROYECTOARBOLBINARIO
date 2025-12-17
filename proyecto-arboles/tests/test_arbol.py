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
        self.assertEqual(
            len(a.buscar_por_ruta("/root/img").children),
            1
        )

    def test_persistencia(self):
        a = Arbol()
        a.insertar("/root", "docs", "carpeta")
        a.insertar("/root/docs", "archivo.txt", "archivo")

        a.guardar_json("test.json")

        b = Arbol()
        b.cargar_json("test.json")

        self.assertEqual(a.preorden(), b.preorden())

    # ---------------- NUEVOS TESTS (DÍA 5–6 / 7–9) ----------------

    def test_busqueda_exacta(self):
        a = Arbol()
        a.insertar("/root", "docs", "carpeta")
        nodo = a.buscar_exacto("docs")
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.nombre, "docs")

    def test_autocompletado(self):
        a = Arbol()
        a.insertar("/root", "docs", "carpeta")
        a.insertar("/root", "downloads", "carpeta")
        resultados = a.autocompletar("do")
        self.assertIn("docs", resultados)
        self.assertIn("downloads", resultados)


if __name__ == "__main__":
    unittest.main()
