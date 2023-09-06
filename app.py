# Trabajo Práctico I - Programación II
import os
import bibloteca 
print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            #completar
            print(bibloteca.libros)
            bibloteca.prestar_ejemplar_libro()
        elif int(opt) == 2:
            #completar
            bibloteca.devolver_ejemplar_libro()
            print()
        elif int(opt) == 3:
            #completar
            bibloteca.registrar_nuevo_libro()
            print()
        elif int(opt) == 4:
            #completar
            bibloteca.eliminar_ejemplar_libro()
            print()
        elif int(opt) == 5:
            #completar
            bibloteca.ejemplares_prestados()
            print()
        elif int(opt) == 6:
            respuesta = "salir"
            print("---------MUCHAS GRACIAS---------")
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")