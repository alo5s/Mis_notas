¿Cómo gestionar permisos en Linux?

Gestión de Permisos

Permisos en Linux:
-------------------
chmod: Cambia permisos de archivos y directorios.
- r: Lectura
- w: Escritura
- x: Ejecución
    
Ejemplo básico:
    chmod u+rwx archivo
    # Concede lectura, escritura y ejecución al propietario.

Más sobre permisos:
--------------------
Cambiar permisos con números:
- 7: rwx (lectura, escritura, ejecución)
- 6: rw- (lectura, escritura)
- 5: r-x (lectura, ejecución)

Ejemplo:
    chmod 755 script.sh
    # Propietario: rwx, Grupo: r-x, Otros: r-x
