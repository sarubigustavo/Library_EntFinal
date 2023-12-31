# Library
Application to manange a library

# Concepto:
Sistema para el manejo de una biblioteca en su version mvp. 
El modelo consta de tres entidades u objetos: Libro, Cliente, Usuario.
La aplicacion permite crear registros de cada entidad de forma independiente.

# Modelo de clases
1) Book: Son los libros que forman parte de la biblioteca y los que van a ser prestados/alquilados por los clientes. 
    Atributos: isbn (identificador universal de los libros), título (utilizado para buscar los libros), autor y fecha de edicion del mismo. Descripcion para el comentario sobre el libro de texto enriquecido. Atributo Created by para saber que usuario lo creo.
2) Client: Define los clientes de la libreria, aquellos que van a llevarse los libros.
    Atributos: dni(como identificador unico), nombre y apellido (usado para buscar los clientes). Email para notificaciones y observaciones de camnpo enriquecido para almacenar caracteristicas del cliente. Atributo Created by para saber que usuario lo creo.
3) Inbox: Es el lugar para ver los mensajes de los usuarios de la librería que usan el sistema, quines ayudan a los clientes a encontrar el libro que buscan en el sistema. Quienes dan de alta los libros y los clientes. Acá es donde estos usuarios pueden enviarse mensajes entre ellos desde el menu principal.

# Caracteristicas tecnicas:
1) Virtual enviroment: venv-Library
2) Django project name: Library_EntFinal
3) Django app names: initial, users
4) Herencia de templates en carpeta(Bootstrap): static folder: initial/static - Ubicaciones del Padre: \template\base.html - Hijos: \initial\templates\initial, \user\templates\user
5) Link al Video: "youtu.be/5jnJGbRKsUM" (agregar al link anterior el "https://" adelante para que el filtro de urls no lo quite.)
6) Pagina acerca de mi: Link 'About' en footer de paginas (\template\initial\about.html) 
7) Vista de listados: Book, Client y Inbox con sus respectivos crud + detail
8) Clases Basadas en Vistas: Book_detail, Client_detail, Client_update, User_detail y User_update
9) Imagen y richfield en la clase Book (tapa del libro y descripcion)
10) Forms utilizando herencia de clases para Book, Client, Inbox y su respectivo metodo para buscar
11) Fueron incluidas imagenes para los avatar de los usuarios y las tapas (book cover) de los libros. Para faciliatar el testeo fueron dejadas imagenes de ambos tipos en /static y aproposito no incluidas en el archivo: .gitignore.
12) Agrego la parte de mensajería en el menu principal 'Inbox' y el problema del RichTextField solucionado en Book y Client (atributos comments y description respectivamente)


# Instalacion:
1) Clonar un proyecto de git account a mi pc (https): "git clone https://github.com/sarubigustavo/Library_EntFinal.git"
2) Abre el vscode en este proyecto: "code -r [folderName]"
3) Instalar dependencias del proyecto: "pip install -r requirements.txt"
4) Abrir terminal en VScode y para correr el servicio ejecutar: "python manage.py runserver"