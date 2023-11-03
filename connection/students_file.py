import os
class StudentsFile:
    """Clase que lee un fichero xlsx de los alumnos de la huelga reciente\n
      y los almacena en la base de datos"""
    
    def __init__(self) -> None:
        self.file = open("resources/LISTADOALUMNADO.xlsx","r")
    

