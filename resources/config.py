from connection.students_file import Alumno
from logging import warning
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
    
    def organizarPorCurso(self,curso:str) -> list[Alumno]:
        """
        Metodo que organiza los alumnos por el curso introducido como parameto\n
        PARAMS:\n
        curso: Curso para filtrar los alumnos por el mismo\n
        RETURN:\n
        Lista de alumnos filtrados por el curso
        """
        alumnosCurso:list[Alumno] = []
        for alumno in self.alumnos:
            if(alumno.curso==curso):
                alumnosCurso.append(alumno)
        if(alumnosCurso.__len__()==0):
            warning("No hay alumnos con el curso "+curso)
        return alumnosCurso
    

