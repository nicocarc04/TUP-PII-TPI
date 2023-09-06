import libro as l


# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    # completar
    for libro in libros:  
        if libro['cant_ej_pr'] > 0:
            print(f"ejemplares prestados: cod {libro['cod']} con la cantidad de {libro['cant_ej_pr']}")
        
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    libros.append(nuevo_libro)
    print(f"Libro introducido correctamente de codigo {nuevo_libro}")
    for libro in libros:  
        print(f"codigo: {libro['cod']}\n" f"{libro['cant_ej_ad']}")
    return None



def eliminar_ejemplar_libro():
    #completar
    ingreso_codigo= input(str("Ingrese el codigo del libro correspondiente. "))
    for libro in libros:  
        if libro["cod"] == ingreso_codigo:
            if libro['cant_ej_ad'] > 0:
                libro['cant_ej_ad'] -= 1
                print("se ha eliminado correctamente...")
                print(f"cantidad de ejemplares disponibles actualmente: {libro['cant_ej_ad']}")
            else:
                print("no se encuentran ejemplares adquiridos.")
            break
    else:
        print("codigo incorrecto!")        
    return None

def prestar_ejemplar_libro():
    #completar  
    ingreso_codigo= input(str("Ingrese el codigo del libro correspondiente. "))
    for libro in libros:  
        if libro["cod"] == ingreso_codigo:
            print(f"{ingreso_codigo} encontrado en la lista.")
            if libro['cant_ej_ad'] > 0:
                print("Confirmacion de prestacion...\n")
                libro['cant_ej_ad'] -= 1
                libro['cant_ej_pr'] += 1
                print("Prestacion completada")
            else:
                print("No hay ejemplares disponibles para prestar.\n")
            break
    else:
        print(f"{ingreso_codigo} No encontrado en la lista.")

    

def devolver_ejemplar_libro():
    #completar
    ingreso_codigo= input(str("Ingrese el codigo del libro correspondiente. "))
    for libro in libros:  
        if libro["cod"] == ingreso_codigo and libro['cant_ej_pr'] > 0:
            print("Confirmacion de Devolucion...\n")
            libro['cant_ej_pr'] += 1
            libro['cant_ej_ad'] -= 1
        else:
            print("la cantidad de prestados es 0\n")
        break
       
    else:
         print("No se ha encontrado el codigo \n")  
    return None

"""def nuevo_libro():
    #completar

    return None"""