
# from main import db
import os
import time
import json

with open("db_file.json") as file:
    db = json.load(file)


def menu ():
    borrar_pantalla()
    print ("< Bienvenido al programa de registro (Aun en alfa) >")
    print ("--"*30)
    print ("1 para registrar datos")
    print ("2 para consultar datos")
    print ("3 para modificar datos")
    print ("4 para eliminar registros")
    
    registro = pedir_numero("")
    if registro == 1:
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
    key = pedir_numero("Ingrese el numero del registro a agregar: ")
    key = str(key)
    if key in db.keys():
        print ("El numero de registro ya existe.")
        print (f"{sugerir_key()} esta disponible")
        print ("Regresando al menu >> Registrar <<")
        time.sleep(2)
        borrar_pantalla()
        registrar ()
    
    registro = []
    registro.append(input("Ingrese el nombre del estudiante: "))
    
    cantidad_materias = pedir_numero("Numero de materias a agregar: ")
    registro.append([])
    for i in range(cantidad_materias):
        registro[1].append(input("Ingrese la materia: "))
    registro.append(boolean_from_input("Esta el estudiante activo? (Y)/(N): "))
    borrar_pantalla()
    db[key] = registro
    añadir_datos_json ()
    imprimir_registro(key)
    print ("--"*10)
    input ("registro realizado correctamente \n < Presione cualquier tecla para continuar >")
    menu ()


def consultar ():
    """consultar"""
    borrar_pantalla()
    registro = existe_key(consultar)
    borrar_pantalla()
    print ("Registro encontrado satisfactoriamente")
    imprimir_registro(registro)
    input ("Presione >> Enter << para ir al menu inicial")
    menu()
    return


def modificar ():
    """modificar"""
    borrar_pantalla()
    registro = str(existe_key(modificar))
    imprimir_registro(registro)
    print("")
    print ("1 para modificar el nombre")
    print ("2 para modificar las materias")
    print ("3 para modificar el estado")
    
    opcion = pedir_numero(">>> ")
    if opcion == 1:     #Cambio en nombre
        borrar_pantalla()
        imprimir_registro(registro)
        db[registro][0] = input("Ingrese el nuevo nombre: \n>>> ")
        añadir_datos_json ()
        borrar_pantalla()
        print ("Cambio realizado correctamente")
        print ("")
        imprimir_registro(registro)
        input("\n>>> Presione cualquier tecla para volver al inicio <<<")
        menu()
    elif opcion == 2: # Cambio en materia
        borrar_pantalla()
        imprimir_registro(registro)
        print ("1 para modificar materia")
        print ("2 para eliminar materia")
        print ("3 para agregar materia")
        opcion_materia = pedir_numero(">>> ")

        if opcion_materia == 1: #Modifica materia
            imprimir_materias(registro)
            numero_materia = pedir_numero("Numero de materia a modificar: ")
            print ("**--"*8)
            print (f"Materia a modificar: {db[registro][1][numero_materia - 1]}")
            db[registro][1][numero_materia - 1] = input ("Nueva materia: ")
            añadir_datos_json ()
            borrar_pantalla()
            print ("Modificacion realizada satisfactoriamente")
            print ("")
            imprimir_registro(registro)
            input ("\n>> Enter para volver al inicio <<")
            menu()

        elif opcion_materia == 2: #Elimina materia
            imprimir_materias(registro)
            numero_materia = pedir_numero("Numero de materia a eliminar: ")
            print ("**--"*20)
            print (f"Materia a eliminar: {db[registro][1][numero_materia - 1]}")
            borrar_pantalla()
            if boolean_from_input():
                db[registro][1].pop(numero_materia - 1)
                añadir_datos_json ()
                print ("Materia eliminada correctamente")
                print ("")
                imprimir_registro(registro)
                input ("\n>> Enter para volver al inicio <<")
                menu()
            else:
                print (">>> Regresando a menu inicial <<<")
                time.sleep(1)
                menu()

        elif opcion_materia == 3: #agregar materia
            imprimir_materias(registro)
            nueva_materia = input ("Ingrese la nueva materia: ")
            if nueva_materia == "":
                print (">>> Regresando a menu inicial <<<")
                time.sleep(1)
                menu()
            
            borrar_pantalla()
            db[registro][1].append(nueva_materia)
            añadir_datos_json ()
            print ("Materia agregada correctamente")
            print ("")
            imprimir_registro(registro)
            input ("\n>> Enter para volver al inicio <<")
            menu()
    
    elif opcion == 3: #Cambia el estado
        borrar_pantalla()
        imprimir_registro(registro)
        if boolean_from_input("Esta seguro de cambiar el estado del registro? (Y)(N): "):
            db[registro][2] = not db[registro][2]
            añadir_datos_json ()
            print ("Estado cambiado correctamente")
            print ("")
            imprimir_registro(registro)
            input ("\n>> Enter para volver al inicio <<")
            menu()
        else:
            print (">>> Regresando a menu inicial <<<")
            time.sleep(1)
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
    print (f"registro # {key} eliminado satisfactoriamente")
    input (">>> Enter para ir al inicio <<<")
    menu()


def borrar_pantalla(): 
   #if os.name == "posix":
    os.system ("clear")
   #elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    #  os.system ("cls")


def sugerir_key ():
    for i in range(1, len(db)+2):
        if not (str(i) in db.keys()):
            return i


def boolean_from_input(parla = " Esta seguro? (Y)/(N): "):
    yn = (input (parla)).upper()
    if yn == "Y":
        return True
    elif yn == "N":
        return False
    else:
        print("Solo se admiten los caracteres (Y) o (N)")
        boolean_from_input(parla)


def pedir_numero(parla = "Ingrese un numero: "):
    #Solicita y retorna un int, 0 == exit()
    try:
        print ("> 0 para salir <")
        num = int(input(parla))
    except:
        print ("< Error: intenta agregando un numero >")
        return pedir_numero(parla)
    if num == 0:
            borrar_pantalla()
            exit()
    return num


def existe_key (funcion_base):
    registro = str(pedir_numero(f"Ingrese el numero de registro que desea {funcion_base.__doc__}: "))
    if not registro in db.keys():
        borrar_pantalla()
        input (f"El registro >> {registro} << no existe \n Presione cualquier tecla para continuar")
        funcion_base()
    return registro


def imprimir_registro (registro):
    registro = str(registro)
    if db[registro][2]:
        estado = "Activo"
    else:
        estado = "No activo"
    print (f"Registro:  # {registro}")
    print (f"Nombre:    {db[registro][0]}")
    print (f"Materias:  {', '.join(db[registro][1])}")
    print (f"Estado:    {estado}")
    return


def imprimir_materias(registro):
    borrar_pantalla()
    print ("Registro #" + registro)
    print ("Materias: ")
    for i in range(len(db[registro][1])):
                print (f"{i+1}. {db[registro][1][i]}")
    return

def añadir_datos_json ():
    with open("db_file.json", "w") as write_file:
        json.dump(db, write_file, ensure_ascii=False, sort_keys=True, indent=2)


def barra_carga(segundos):
    print ()
    pass
