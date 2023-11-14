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

file = open(file="resources/LISTADOALUMNADO.csv",mode="r",encoding="utf-8")
contenido = file.readlines()
alumnos:list[Alumno] = []
for dato in contenido:
    dato = dato.removeprefix("\"")
    datos = dato.split(",")
    datos[1] = datos[1].removesuffix("\"")
    datos[1] = datos[1].removeprefix(" ")
    if(datos.__len__()==4):
        alumnos.append(Alumno(datos[0],datos[1],datos[2],datos[3]))
print(alumnos[0].curso)
if(alumnos[0].__eq__("1 DAM")):    
    print("Accept")
else:
   print("Don't accept")

alumnos2:list[Alumno] = []
curso = "1 DAM"
curso+="\n"
if(curso.__eq__("Todos")==False):
    for alumno1 in alumnos:
        if(alumno1.curso.__eq__(curso)):
            alumnos2.append(alumno1)
else:
    alumnos2 = alumnos
alumnosParse = []
for alumno2 in alumnos2:
    alumnosParse.append(alumno2.nombre+", "+alumno2.apellido)
print(alumnosParse)