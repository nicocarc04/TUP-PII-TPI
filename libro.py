import cod_generator as C
# Crear un diccionario para cada libro

libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    #completar
    libro_add={'cod': C.generar() , 'cant_ej_ad': 1 ,   'cant_ej_pr': 0 }
    
    
    return libro_add

#No entendimos esta funcion para que especificamente servia debido a que intentamos pero nos saltaba error
"""def generar_codigo():
    #completar"""
   
    