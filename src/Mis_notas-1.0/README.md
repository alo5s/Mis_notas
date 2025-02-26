Mis Notas
Mis Notas es una aplicación de terminal que permite gestionar notas organizadas en archivos .md. La aplicación permite explorar directorios, visualizar archivos y navegar por su contenido de manera interactiva.

Requisitos
Para ejecutar esta aplicación, necesitas tener Python 3.x y la librería rich instalada.

Instalación de Dependencias
Puedes instalar las dependencias necesarias desde el archivo requirements.txt usando pip:

bash
Copiar
Editar
pip install -r requirements.txt
Estructura del Proyecto
bash
Copiar
Editar
mis_notas/
│
├── app.py             # Código principal de la aplicación
├── requirements.txt   # Lista de dependencias de Python
└── notas/             # Directorio que contiene las notas en formato .md
    ├── nota1.md
    ├── nota2.md
    └── ...
Cómo Ejecutar la Aplicación
Clona el repositorio en tu máquina local:

bash
Copiar
Editar
git clone https://github.com/usuario/mis_notas.git
cd mis_notas
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecuta la aplicación:

bash
Copiar
Editar
python app.py
Comandos de Navegación
Una vez que la aplicación esté en ejecución, puedes interactuar con las notas de la siguiente forma:

[1] Anterior: Para ver el bloque anterior de la nota.
[2] Siguiente: Para ver el siguiente bloque de la nota.
[3] Volver: Para regresar al menú principal y seleccionar otra nota.
Contribución
Si deseas contribuir al proyecto:

Haz un fork del repositorio.
Crea una nueva rama con tus cambios.
Realiza un pull request con tus mejoras.
Por favor, asegúrate de seguir el estilo de código del proyecto y agrega documentación cuando sea necesario.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.


