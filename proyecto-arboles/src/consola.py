from src.arbol import Arbol


class Consola:
    def __init__(self, arbol: Arbol):
        self.arbol = arbol
        self.ruta_actual = "/root"

    def iniciar(self):
        print("Mini gestor de archivos (escribe 'help' para comandos)")
        while True:
            comando = input(f"{self.ruta_actual}> ").strip()
            if not comando:
                continue

            partes = comando.split()
            cmd = partes[0]

            if cmd == "exit":
                print("Saliendo...")
                break

            elif cmd == "help":
                self._help()

            elif cmd == "pwd":
                print(self.ruta_actual)

            elif cmd == "ls":
                self._ls()

            elif cmd == "cd":
                self._cd(partes)

            elif cmd == "mkdir":
                self._mkdir(partes)

            elif cmd == "touch":
                self._touch(partes)

            elif cmd == "mv":
                self._mv(partes)

            elif cmd == "rm":
                self._rm(partes)

            elif cmd == "search":
                self._search(partes)

            elif cmd == "export":
                self._export(partes)

            else:
                print("Comando no reconocido")

    # ---------------- COMANDOS ----------------

    def _help(self):
        print("""
Comandos disponibles:
  pwd                     Muestra la ruta actual
  ls                      Lista hijos
  cd <ruta>               Cambia de directorio
  mkdir <nombre>          Crea carpeta
  touch <nombre>          Crea archivo
  mv <origen> <destino>   Mueve nodo
  rm <ruta>               Elimina nodo
  search <prefijo>        Autocompletar nombres
  export preorden         Muestra recorrido preorden
  exit                    Salir
""")

    def _ls(self):
        hijos = self.arbol.listar_hijos(self.ruta_actual)
        for h in hijos:
            print(h)

    def _cd(self, partes):
        if len(partes) < 2:
            print("Uso: cd <ruta>")
            return
        ruta = partes[1]
        nodo = self.arbol.buscar_por_ruta(ruta)
        if nodo and nodo.tipo == "carpeta":
            self.ruta_actual = ruta
        else:
            print("Ruta inválida")

    def _mkdir(self, partes):
        if len(partes) < 2:
            print("Uso: mkdir <nombre>")
            return
        self.arbol.insertar(self.ruta_actual, partes[1], "carpeta")

    def _touch(self, partes):
        if len(partes) < 2:
            print("Uso: touch <nombre>")
            return
        self.arbol.insertar(self.ruta_actual, partes[1], "archivo")

    def _mv(self, partes):
        if len(partes) < 3:
            print("Uso: mv <origen> <destino>")
            return
        self.arbol.mover(partes[1], partes[2])

    def _rm(self, partes):
        if len(partes) < 2:
            print("Uso: rm <ruta>")
            return
        self.arbol.eliminar(partes[1])

    def _search(self, partes):
        if len(partes) < 2:
            print("Uso: search <prefijo>")
            return
        resultados = self.arbol.autocompletar(partes[1])
        for r in resultados:
            print(r)

    def _export(self, partes):
        if len(partes) < 2 or partes[1] != "preorden":
            print("Uso: export preorden")
            return
        print(self.arbol.preorden())
