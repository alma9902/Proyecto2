Proyecto 2 : Reproductor mp3
Alumna : Sánchez Salgado Alma Rocío
No. cuenta : 315153406

El proyecto lo hice con interfaz de qt5 por lo que es
necesario instalarlo para que corra adecuadamente.
La versión de python que usé es la 3.7.0
Usé para la base de datos sqlite3, el programa
supone que la base de datos ya está instalada en
root y supone que la carpeta de música también está ahí.

De cualquier manera no es difícil cambiar las rutas en las
cuales tiene que buscar.

Las consultas son de la siguiente forma:
si introducimos texto sin comas la considera como
una sola cadena y busca en títulos, género, albums y año;
si empieza con "album:" buscará en todos los albums,
es necesario poner "," después para que lo detecte
como otra palabra o frase.
Ejemplo : "album:, nombre"
si se requiere consultar más de un nombre en cualquiera
de las modalidades :
Ejemplo: "album:, nombre1, nombre2"

Para correr el proyecto se hace en un directorio antes
de Proyecto2 y se escribe en terminal: python3.7 -m Proyecto2.GUI.Player
