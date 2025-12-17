# Proyecto Árboles – Estructura de Datos

**Lenguaje:** Python

Proyecto académico para la materia de **Estructura de Datos**. Se implementa una mini‑suite en consola que simula un sistema de archivos utilizando **árboles generales**, con **búsqueda por prefijo (Trie)**, **búsqueda exacta**, **persistencia en JSON** y **pruebas unitarias**.

---

## Objetivo
Diseñar e implementar una jerarquía de nodos (carpetas/archivos) que permita crear, mover, renombrar y eliminar nodos; buscar por prefijo con autocompletado; exportar recorridos del árbol; y mantener la consistencia de la estructura mediante pruebas.

---

## Alcance por días

### Día 1
- Definición del alcance (MVP)
- Estructuras de datos
- Formato de persistencia JSON

### Día 2–3
- Árbol general
- Inserción, eliminación, mover y renombrar
- Recorrido en **preorden**
- Pruebas unitarias iniciales

### Día 4
- Persistencia en archivo JSON (guardar / cargar)

### Día 5–6
- **Trie** para autocompletado de nombres
- **Índice hash** para búsqueda exacta
- Integración con operaciones del árbol

### Día 7–9
- **Interfaz de consola**
- Comandos tipo sistema de archivos
- Manejo de errores básicos

### Día 10–11
- Pruebas de consistencia
- Casos límite
- Validación del árbol tras movimientos y renombrados

### Día 12
- Documentación final (README)

---

## Modelo de datos
Cada nodo contiene:
- `id`: identificador único
- `nombre`: nombre del archivo o carpeta
- `tipo`: `carpeta` o `archivo`
- `contenido`: valor simple (opcional)
- `children`: lista de nodos hijos

---

## Persistencia en JSON
El árbol puede guardarse y cargarse desde archivos JSON, manteniendo:
- La jerarquía completa
- Los identificadores de nodos
- La consistencia del árbol

Ejemplo de archivo:
```
data/ejemplo.json
```

---

## Interfaz de Consola
El sistema se maneja desde consola con comandos similares a un sistema de archivos.

### Comandos disponibles

```
pwd                     Muestra la ruta actual
ls                      Lista los hijos del nodo actual
cd <ruta>               Cambia de directorio
mkdir <nombre>          Crea una carpeta
touch <nombre>          Crea un archivo
mv <origen> <destino>   Mueve un nodo
rm <ruta>               Elimina un nodo
search <prefijo>        Autocompletado de nombres
export preorden         Muestra recorrido preorden
exit                    Salir del programa
```

---

## Búsqueda
- **Búsqueda exacta:** índice hash para localizar nodos por nombre.
- **Autocompletado:** Trie para sugerir nombres por prefijo.

---

## Pruebas y Casos Límite
Se realizaron pruebas unitarias para:
- Inserción y eliminación
- Movimientos de nodos
- Persistencia JSON
- Búsqueda exacta y autocompletado
- Eliminación y búsqueda de nodos inexistentes
- Consistencia del árbol tras múltiples operaciones

Los tests se encuentran en:
```
tests/test_arbol.py
```

---

## Estructura del proyecto

```
proyecto-arboles/
│
├── src/
│   ├── __init__.py
│   ├── nodo.py
│   ├── arbol.py
│   ├── trie.py
│   ├── consola.py
│   └── main.py
│
├── tests/
│   └── test_arbol.py
│
├── data/
│   └── ejemplo.json
│
└── README.md
```

---

## Cómo ejecutar el proyecto

Desde la raíz del proyecto:

```bash
python -m src.main
```

---

## Cómo ejecutar las pruebas

```bash
python -m unittest
```

---

## Conclusión
Este proyecto refuerza el uso de **árboles generales**, **recorridos**, **estructuras auxiliares** como Trie y hash maps, así como buenas prácticas de organización, pruebas y documentación.

---

**Autores:** Ibarra peñuelas Emmanuel y Lizeth Raygoza Cuevas

