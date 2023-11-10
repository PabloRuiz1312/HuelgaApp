from connection.students_file import Alumno
from logging import warning
class ConfigAlumnos:
    """_summary_:
        Clase que se encarga de filtrar los alumnos por sus atributos
    """
    def __init__(self,alumnos:list[Alumno]) -> None:
        """_summary_
        Constructor que inicializa la lista de alumnos cargada en el fichero
        Args:
            alumnos (list[Alumno]): _description_ Lista de alumnos cargada en el fichero
        """
        self.alumnos = alumnos
    
    def organizarPorCurso(self,curso:str) -> list[Alumno]:
        """_summary_
        Metodo que filtra los alumnos por un curso pasado por parametro
        Args:
            curso (str): _description_ Curso que filtra los alumnos por el mismo

        Returns:
            list[Alumno]: _description_ La lista de alumnos filtrados por curso
        """
        alumnosCurso:list[Alumno] = []
        for alumno in self.alumnos:
            if(alumno.curso==curso):
                alumnosCurso.append(alumno)
        if(alumnosCurso.__len__()==0):
            warning("No hay alumnos con el curso "+curso)
        return alumnosCurso
    

