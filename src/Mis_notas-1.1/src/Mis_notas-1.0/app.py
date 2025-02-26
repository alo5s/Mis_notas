from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
import os
import re



directorio_base="notas"

console = Console ()

def listar_elementos(directorio):
    """ Devuelve una lista de archivos y carpetas en el directorio que estamos. """
    return [f for f in os.listdir(directorio)]


def leer_archivo(ruta):
    """ Lee un archivo de texto y devuelve su contenido. """
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def obtener_descripcion(archivo):
    """ Extrae la primera línea de un archivo como descripción. """
    contenido = leer_archivo(f"{archivo}")
    return contenido[0].strip() if contenido else "Sin descripción"

def leer_nota_procesar(ruta):
    """ Extrae los títulos y secciones de una nota. """
    contenido = leer_archivo(f"{ruta}")
    if not contenido:
        return "Nota vacía", []

    titulo = contenido[2].strip() if len(contenido) > 2 else "Sin título"
    texto_completo = "".join(contenido)

    print("DEBUG - Contenido de la nota:\n", texto_completo)  # <- Agregar esta línea

    bloques = re.findall(r'([^\n]+?)\n-+\n(.*?)(?=\n[^\n]+\n-+\n|\Z)', texto_completo, re.DOTALL)

    print("DEBUG - Bloques encontrados:", bloques)  # <- Agregar esta línea

    return titulo, [f"{t[0]}\n{'-'*10}\n{t[1]}" for t in bloques]


def mostrar_menu(directorio):
    """ Muestra un menú con las notas y carpetas disponibles. """
    menu = Table(title="Menú Principal", box=box.ROUNDED, style="cyan")

    menu.add_column("Opción", justify="center", style="bold green")
    menu.add_column("Descripción", justify="left", style="bold yellow")

    opciones = {str(i+1): f for i, f in enumerate(listar_elementos(directorio))}
    
    for i, f in opciones.items():
        nombre_sin_ext, ext = os.path.splitext(f)
       
        # CORRECCIÓN: Ahora `ruta` usa el directorio actual y no `directorio_base`
        ruta = os.path.join(directorio, f)

        desc = obtener_descripcion(ruta) if ext == ".md" else "Carpeta"
        menu.add_row(i, f"{nombre_sin_ext}: {desc}")
    
    console.print(Panel(menu, title="Mis Notas", title_align="left"))
    return opciones




def mostrar_nota(ruta):
    """ Muestra el contenido de una nota de forma paginada. """
    titulo, bloques = leer_nota_procesar(ruta)

    if not bloques:  # Si la nota está vacía o sin formato válido
        console.print(Panel("[red]Nota vacía o sin formato válido[/]", title=titulo, style="bold red"))    
        Prompt.ask("Presione Enter para volver")
        console.clear()
        return

    i = 0
    while True:
        console.clear()
        console.print(Panel(bloques[i], title=f"{titulo} - {i+1}/{len(bloques)}", style="green"))
        accion = Prompt.ask("[1] Anterior [2] Siguiente [3] Volver", choices=["1", "2", "3"])
        
        if accion == "1" and i > 0:
            i -= 1
        elif accion == "2" and i < len(bloques) - 1:
            i += 1
        elif accion == "3":
            console.clear()
            break




def opciones_menu(opciones):
    """ Maneja el flujo de opcion del menu principal """
    while True:  # Bucle para evitar que `Enter` cierre el programa
        opcion = Prompt.ask("Seleccione una opción (o 'Esc' para salir)").strip()
        if opcion in opciones.keys() or opcion.lower() == "esc":
            return  opcion
            break  # Solo salir del bucle si la opción es válida
            
        console.print("[red]Opción no válida. Intente de nuevo.[/]")
    
    

def ejecutar_submenu(directorio):
    """ Maneja la navegación dentro de un directorio de notas. """ 
    console.clear()
    while True:
        opciones = mostrar_menu(directorio)
        
        opcion = opciones_menu(opciones)
        if opcion == "esc":
            console.clear()
            break

        ruta = os.path.join(directorio, opciones[opcion])
        mostrar_nota(ruta)


def ejecutar():
    """ Maneja la navegación del menú principal. """
    console.clear()
    while True:
        opciones = mostrar_menu(directorio_base)
        
        opcion = opciones_menu(opciones)
        
        if opcion.lower() == "esc":
            console.clear()
            console.print(Panel("[bold red]¡Gracias por usar el programa![/]", style="red"))
            break

        # Ruta base 
        ruta = os.path.join(directorio_base, opciones[opcion])
        if os.path.isdir(ruta):
            ejecutar_submenu(ruta)
        else:
            mostrar_nota(ruta)



def main():
    ejecutar()

if __name__ == "__main__":
    main()


