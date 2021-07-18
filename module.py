
import os
import time
import json
from pyfiglet import Figlet

with open("db_file.json") as file:
    db = json.load(file)


def menu ():
    borrar_pantalla()
    f = Figlet(font="slant")
    print (f.renderText(" json Edit"))
    print (("≈≈"*23).center(50, " " ))
    print ("< Bienvenido al programa de registro (Alfa) >".center(50, " " ))
    print (("≈≈"*23).center(50, " " ), "\n")
    print ("> 1 para registrar datos <"   .center(50, " " ))
    print ("> 2 para consultar datos <"   .center(50, " " ))
    print ("> 3 para modificar datos <"   .center(50, " " ))
    print ("> 4 para eliminar registros <".center(50, " " ))
    print ("< 0 para salir >"             .center(50, " " ))

    registro = pedir_numero(" >>> ")
    if registro == 1:
        barra_carga(0.6)
        borrar_pantalla()
        registrar ()
    if registro == 2:
        borrar_pantalla()
        consultar ()
    if registro == 3:
        borrar_pantalla()
        modificar ()
    if registro == 4:
        borrar_pantalla()
        eliminar ()
    return


def registrar ():
    """registrar"""
    borrar_pantalla()
    key = pedir_numero("\n Ingrese el numero del registro a agregar: ")
    key = str(key)
    if key in db.keys():
        print (" El numero de registro ya existe.")
        print (f" ( {sugerir_key()} ) esta disponible")
        input(" >> Presione cualquier tecla para regresar <<")
        print (" Regresando al menu >> Registrar <<")
        barra_carga(1)
        borrar_pantalla()
        registrar ()
    
    registro = []
    registro.append(solicita_str(" Ingrese el nombre del estudiante: "))
    cantidad_materias = pedir_numero(" Numero de materias a agregar: ")
    registro.append([])
    for i in range(cantidad_materias):
        registro[1].append(solicita_str(" Ingrese la materia: "))
    registro.append(boolean_from_input(" Esta el estudiante activo? (Y)/(N): "))

    barra_carga(1)
    borrar_pantalla()
    db[key] = registro
    añadir_datos_json ()
    imprimir_registro(key)
    input (" registro realizado correctamente \n < Presione cualquier tecla para continuar >")
    menu ()


def consultar ():
    """consultar"""
    borrar_pantalla()
    print ("")
    registro = existe_key(consultar)
    borrar_pantalla()
    print ("\n Registro encontrado satisfactoriamente")
    imprimir_registro(registro)
    input (" Presione >> Enter << para ir al menu inicial")
    menu()
    return


def modificar ():
    """modificar"""
    borrar_pantalla()
    print("")
    registro = str(existe_key(modificar))
    imprimir_registro(registro)
    print (" > 1 Para modificar el nombre <")
    print (" > 2 Para modificar materias  <")
    print (" > 3 Para modificar el estado <")
    
    opcion = pedir_numero(" >>> ")
    if opcion == 1:     #Cambio en nombre
        borrar_pantalla()
        imprimir_registro(registro)
        db[registro][0] = solicita_str(" Ingrese el nuevo nombre: \n >>> ")
        añadir_datos_json ()
        borrar_pantalla()
        print ("\n Cambio realizado correctamente")
        imprimir_registro(registro)
        input(" >>> Presione cualquier tecla para volver al inicio <<<")
        menu()
    elif opcion == 2: # Cambio en materia
        borrar_pantalla()
        imprimir_registro(registro)
        print (" > 1 Para modificar materia <")
        print (" > 2 Para eliminar materia <")
        print (" > 3 Para agregar materia <")
        opcion_materia = pedir_numero(" >>> ")

        if opcion_materia == 1: #Modifica materia
            imprimir_materias(registro)
            numero_materia = pedir_numero(" Numero de materia a modificar: ")
            print ("**--"*8)
            print (f" Materia a modificar: {db[registro][1][numero_materia - 1]}")
            db[registro][1][numero_materia - 1] = solicita_str(" Nueva materia: ")
            añadir_datos_json ()
            borrar_pantalla()
            print ("\n Modificacion realizada satisfactoriamente")
            imprimir_registro(registro)
            input (" >> Enter para volver al inicio <<")
            menu()

        elif opcion_materia == 2: #Elimina materia
            imprimir_materias(registro)
            numero_materia = pedir_numero("Numero de materia a eliminar: ")
            borrar_pantalla()
            print (f"\n Materia a eliminar: {db[registro][1][numero_materia - 1]}")
            if boolean_from_input():
                db[registro][1].pop(numero_materia - 1)
                añadir_datos_json ()
                print ("\n Materia eliminada correctamente")
                imprimir_registro(registro)
                input (" >> Enter para volver al inicio <<")
                menu()
            else:
                print (">>> Regresando a menu inicial <<<")
                time.sleep(1)
                menu()

        elif opcion_materia == 3: #agregar materia
            imprimir_materias(registro)
            nueva_materia = solicita_str("Ingrese la nueva materia: ")        
            borrar_pantalla()
            db[registro][1].append(nueva_materia)
            añadir_datos_json ()
            print (" Materia agregada correctamente")
            imprimir_registro(registro)
            input (" >> Enter para volver al inicio <<")
            menu()
    
    elif opcion == 3: #Cambia el estado
        borrar_pantalla()
        imprimir_registro(registro)
        if boolean_from_input(" Esta seguro de cambiar el estado del registro? (Y)(N): "):
            db[registro][2] = not db[registro][2]
            añadir_datos_json ()
            print ("\n Estado cambiado correctamente")
            imprimir_registro(registro)
            input (" >> Enter para volver al inicio <<")
            menu()
        else:
            print (">>> Regresando a menu inicial <<<")
            time.sleep(2)
            menu()
    else: 
        modificar()
    return


def eliminar ():
    """eliminar"""
    key = existe_key(eliminar)
    del db[key]
    añadir_datos_json ()
    borrar_pantalla()
    print (f"\n registro # {key} eliminado satisfactoriamente")
    input (" >>> Enter para ir al inicio <<<")
    menu()

# Secundarias

def borrar_pantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def sugerir_key ():
    for i in range(1, len(db)+2):
        if not (str(i) in db.keys()):
            return i


def boolean_from_input(texto = " Esta seguro? (Y)/(N): "):
    yn = (input (texto)).upper()
    if yn == "Y":
        return True
    elif yn == "N":
        return False
    else:
        print("Solo se admiten los caracteres (Y) o (N)")
        boolean_from_input(texto)


def pedir_numero(texto = " Ingrese un numero: "):
    #Solicita y retorna un int, 0 == exit()
    try:
        # print ("< 0 para salir >".center(50, " " ))
        num = int(input(texto))
    except:
        print ("< Error: intenta agregando un numero >")
        return pedir_numero(texto)
    if num == 0:
            borrar_pantalla()
            exit()
    return num


def solicita_str (texto = " >>> "):
    string = input(texto)
    if not string:
            print (" Error: Este campo no puede estar vacio\n Saliendo del programa...")
            time.sleep(4)
            borrar_pantalla()
            exit ()
    return string


def existe_key (funcion_base):
    registro = str(pedir_numero(f" Ingrese el numero de registro que desea {funcion_base.__doc__}: "))
    if not registro in db.keys():
        borrar_pantalla()
        input (f" El registro >> {registro} << no existe \n Presione cualquier tecla para continuar")
        funcion_base()
    return registro


def imprimir_registro (registro):
    registro = str(registro)
    if db[registro][2]:
        estado = "Activo"
    else:
        estado = "No activo"
    print ("")
    print (f" Registro:  # {registro}")
    print (f" Nombre:    {db[registro][0]}")
    print (f" Materias:  {', '.join(db[registro][1])}")
    print (f" Estado:    {estado}\n")
    return


def imprimir_materias(registro):
    borrar_pantalla()
    print ("\n Registro #" + registro)
    print (" Materias: ")
    for i in range(len(db[registro][1])):
                print (f" {i+1}. {db[registro][1][i]}")
    print ("")
    return


def añadir_datos_json ():
    with open("db_file.json", "w") as write_file:
        json.dump(db, write_file, ensure_ascii=False, sort_keys=True, indent=2)


def barra_carga (sec):
    # Solo añadido a registrar

    barra = "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
    lapse = sec / 20
    for i in range(0,101, 5):
        time.sleep(lapse)
        barra = barra.replace("▒", "▓", 1)
        print ((f" {barra} {i}%").center(40, " " ), end= "\r")
    print ("")
    return


if __name__ == "__name__":
    pass
