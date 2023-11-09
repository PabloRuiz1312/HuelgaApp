from connection.students_file import Alumno
class ConfigAlumnos:
    """
    Clase que se encarga de guardar y gestionar los alumnos recibidos por el fichero
    """
    def __init__(self,alumnos:list[Alumno]) -> None:
        """
        Constructor que crea la lista de alumnos para operar con ellos\n
        PARAMETROS:\n
        alumnos: Lista cargada de alumnos 
        """
        self.alumnos = alumnos
    
    def organizarPorCurso(self) -> list[list[Alumno]]:
        alumnosCurso:list[list[Alumno]] = []