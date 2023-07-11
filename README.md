# Library
Application to manange a library

# Caracteristicas tecnicas:
1) Virtual enviroment: venv-Library
2) django project name: library_project
3) django app name: initial, users

# Concepto:
Sistema para el manejo de una biblioteca en su version mvp. 
El model consta de tres entidades u objetos: Libro, Cliente, Usuario.
La aplicacion permite crear registros de cada entidad de forma independiente.

# Modelo de clases
1) Book: Son los libros que forman parte de la biblioteca y los que van a ser prestados/alquilados por los clientes. 
    Atributos: isbn (identificador universal de los libros), título (utilizado para buscar los libros), autor y fecha de edicion del mismo.
2) Client: Define los clientes de la libreria, aquellos que van a llevarse los libros.
    Atributos: dni(como identificador unico), nombre y apellido (usado para buscar los clientes).
3) User: Son los que usan el sistema, quines ayudan a los clientes a encontrar el libro que buscan en el sistema. Quienes dan de alta los libros y los clientes.

# Instalacion:
1) Clonar un proyecto de git account a mi pc (https): "git clone https://github.com/sarubigustavo/Python_Coderhouse.git"
2) Abre el vscode en este proyecto: "code -r [folderName]"
3) Abrir terminal en VScode y para correr el servicio ejecutar: "python manage.py runserver"