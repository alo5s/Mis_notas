# Mis Notas

Mis Notas es una aplicación de terminal que permite gestionar notas organizadas en archivos .md. La aplicación permite explorar directorios, visualizar archivos y navegar por su contenido de manera interactiva.

## Estructura de Archivos `.md`

El programa lee archivos `.md` y los estructura de una forma legible para leer en la terminal. Las reglas a la hora de escribir las notas son las siguientes:

1. **Descripción inicial**: El primer texto debe ser la descripción de la nota.
2. **Título**: El texto en la tercera línea o párrafo debe ser el título.
3. **Paginación**: El texto se divide en páginas. La página se define de la siguiente manera: 

    Un texto ejemplo

    ```markdown
    ¿Cómo gestionar permisos en Linux?  ## Este es la discripcion

    Gestión de Permisos  ## Este es el titulo
   
    Permisos en Linux:
    -------------------   ## Este divide el paginado
    chmod: Cambia permisos de archivos y directorios.
    - r: Lectura
    - w: Escritura
    - x: Ejecución
    
    Ejemplo básico:
    ```bash
    chmod u+rwx archivo
    # Concede lectura, escritura y ejecución al propietario.
    ```

## Funcionalidades

- **Navegación interactiva**: La aplicación permite navegar por los archivos y directorios de tus notas de manera sencilla y clara.
- **Visualización**: Muestra las notas de forma estructurada, respetando las reglas de formato para facilitar la lectura en la terminal.
- **Gestión de notas**: Permite agregar, eliminar y modificar notas desde la terminal.

## Instalación

Para instalar y usar **Mis Notas** en tu sistema, sigue estos pasos:

1. Clona este repositorio:

    ```bash
    git clone https://github.com/alo5s/Mis_notas.git
    ```

2. Navega a la carpeta del proyecto:

    ```bash
    cd Mis_notas
    ```

3. (Opcional) Si es necesario, instala las dependencias o realiza cualquier configuración adicional indicada en los archivos del proyecto.

## Uso

Una vez que el proyecto esté instalado, puedes iniciar la aplicación desde la terminal para comenzar a gestionar y explorar tus notas. El comando y la forma de interactuar con el programa dependerán de la implementación que hayas hecho, pero el flujo general será:

```bash
./mis_notas

```

## Contribuciones
Si deseas contribuir al desarrollo de Mis Notas, puedes hacerlo de la siguiente manera:

Haz un fork de este repositorio.
Realiza tus cambios o mejoras.
Abre un pull request con una descripción clara de los cambios realizados.


## Licencia
Este proyecto está bajo la licencia MIT.


