# Proyecto_Battleship
Este proyecto implementa un juego de tablero simple en Python, utilizando las clases `Tablero`, `TableroJugador`, y `TableroOrdenador`.

## Contenido

1. [Descripción](#descripción)
2. [Requisitos](#requisitos)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Uso](#uso)
5. [Clases](#clases)
6. [Funciones Auxiliares](#funciones-auxiliares)

## Descripción

Este juego de tablero permite a un jugador humano competir contra un bot. El juego utiliza matrices NumPy para representar los tableros y ofrece funcionalidades para mostrar el estado del juego y cargar bots desde archivos pickle.

## Requisitos

- Python 3.x
- NumPy
- Pandas

## Estructura del Proyecto

El proyecto consta de las siguientes clases principales:

- `Tablero`: Clase base para representar un tablero genérico.
- `TableroJugador`: Clase para representar el tablero del jugador humano.
- `TableroOrdenador`: Clase para representar el tablero del bot.

## Uso

Para ejecutar el juego, asegúrate de tener instaladas las dependencias necesarias y ejecuta el script principal. El script creará instancias de `TableroJugador` y `TableroOrdenador`, mostrará información sobre el jugador y intentará cargar un bot.

```python
if __name__ == "__main__":
    # Código de ejemplo en el script principal
    ...
```

## Clases

### Tablero

Clase base que representa un tablero genérico.

Atributos:
- `id_user`: ID del usuario
- `tabla_op`: Matriz de operaciones
- `tabla_visible`: Matriz visible

### TableroJugador

Hereda de `Tablero` y representa el tablero del jugador humano.

Atributos adicionales:
- `nombre_jugador`: Nombre del jugador
- `aciertos`: Número de aciertos del jugador

Métodos:
- `player_show()`: Muestra información del jugador

### TableroOrdenador

Hereda de `Tablero` y representa el tablero del bot.

Atributos adicionales:
- `nombre_bot`: Nombre del bot
- `url_bot`: URL para cargar el bot

Métodos:
- `load_bot()`: Intenta cargar el bot desde un archivo pickle

## Funciones Auxiliares

- `mostrar_tablero(tablero: TableroJugador, tablero_pc: TableroOrdenador)`: Muestra los tableros del jugador y del bot en la consola.

## Notas

- Asegúrate de manejar correctamente las excepciones al crear objetos o cargar bots.
- El método `load_bot()` espera encontrar un archivo pickle en la URL especificada.
- La visualización de los tableros se realiza a través de la consola.