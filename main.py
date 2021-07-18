
from module import *
import json

""" 
db = {  '1':    ["Soren Kierkegaard",   ["Latin","Historia","Existencialismo"],     True ],
        '2':    ["Howard Lovecraft",    ["Astronomia","Quimica","Matematicas"],     False],
        '3':    ["Isaac Asimov",        ["Fisica","Ciencia ficcion","Quimica"],     False],
        '5':    ["Carl Jung",           ["Psiquiatria","Alquimia","Antropologia"],  True ],
        '6':    ["Vanessa Duries",      ["Economia","Realismo","Inteligencia Vial"],False],
            }

with open("db_file.json", "w") as write_file: # Creo el archivo json
    json.dump(db, write_file, indent=4)
 """ # Todo lo que esta en comillas se utilizo para inicializar el diccionario.

if __name__ == "__main__":
    menu()
