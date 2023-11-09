import os
class StudentsFile:
    """Clase que lee un fichero xlsx de los alumnos de la huelga reciente\n
      y los almacena en la base de datos"""
    
    def __init__(self) -> None:
      """Constructor que abre el fichero de alumnos en modo lectura para cargar los alumnos"""
      self.file = open(file="resources/LISTADOALUMNADO.csv",mode="r",encoding="utf-8")
    
    def readFile(self) -> list:
      """Metodo que carga los alumnos del fichero en una lista\n
         Returns:La lista con los alumnos cargados"""
      contenido = self.file.readlines()
      alumnos:list[Alumno] = []
      for dato in contenido:
        dato = dato.removeprefix("\"")
        datos = dato.split(",")
        datos[1] = datos[1].removesuffix("\"")
        datos[1] = datos[1].removeprefix(" ")
        if(datos.__len__()==4):
          alumnos.append(Alumno(datos[0],datos[1],datos[2],datos[3]))
      return alumnos

    def closeFile(self) -> None:
       """Metodo que cierra el fichero"""
       self.file.close()
      
class Alumno:
  """Clase que guarda la informacion de un alumno"""

  def __init__(self,apellido:str,nombre:str,dni:str,curso:str) -> None:
      self.apellido = apellido
      self.nombre = nombre
      self.dni = dni
      self.curso = curso