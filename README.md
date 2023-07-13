# Library
Application to manange a library

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

# Caracteristicas tecnicas:
1) Virtual enviroment: venv-Library
2) Django project name: library_project
3) Django app name: initial, users
4) Herencia de templates en carpeta(Bootstrap): static folder: initial/static - Padre: \template\base.html - Hijos: \initial\templates\initial
5) Link al Video: https:\\
6) Pagina acerca de mi: Link 'About' en footer de paginas (\template\initial\about.html) 
7) Vista de listados: Book, Client y Users con sus respectivos crud + detail
8) Clases Basadas en Vistas: Book_detail, Client_detail, Client_update, User_detail y User_update
9) Imagen y richfield en la clase Book 
10) Forms utilizando herencia de clases para Book, Client, User  y su respectivo metodo para buscar

# Instalacion:
1) Clonar un proyecto de git account a mi pc (https): "git clone https://github.com/sarubigustavo/Library_EntFinal.git"
2) Abre el vscode en este proyecto: "code -r [folderName]"
3) Abrir terminal en VScode y para correr el servicio ejecutar: "python manage.py runserver"