import os
class StudentsFile:
  """
  _summary_ Clase que carga los alumnos de un fichero a una lista
  """
    
  def __init__(self) -> None:
    """_summary_ Constructor que carga el fichero para leer los alumnos
    """
    self.file = open(file="resources/LISTADOALUMNADO.csv",mode="r",encoding="utf-8")
  
  def readFile(self) -> list:
    """_summary_
    Metodo que lee el fichero y carga los alumnos en una lista
    Returns:
        list: _description_ Los alumnos cargados en la lista
    """
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
    """_summary_ Metodo que cierra el fichero de alumnos
    """
    self.file.close()
      
class Alumno:
  """_summary_ Clase que guarda la informacion de un alumno
  """

  def __init__(self,apellido:str,nombre:str,dni:str,curso:str) -> None:
    """_summary_
    Constructor que crea un alumno con su informacion
    Args:
        apellido (str): _description_ Apellido del alumno
        nombre (str): _description_ Nombre del alumno
        dni (str): _description_ DNI del alumno
        curso (str): _description_ Curso del alumno
    """
    self.apellido = apellido
    self.nombre = nombre
    self.dni = dni
    self.curso = curso