from toga import App
from toga import Box
from toga import Button
from toga import Label
from toga import TextInput
from toga.style.pack import *
from toga import MainWindow
from toga import Selection
from connection.students_file import StudentsFile
from connection.students_file import Alumno
ALUMNOS_OPERATOR = StudentsFile()
class CrearHuelga (App):
    """
    Clase que se encarga de gestionar la ventana donde se crea una huelga
    """
    def __init__(self,title,id,vent1,vent2) -> None:
        """
        Constructor que mediante atributos del padre App crea \n
        una app que gestionara mas adelante un MainWindow \n
        PARAMETROS:\n
        title: Titulo de la app\n
        id: Identificador de la app\n
        vent1: Booleano que hace referencia a HomeWindow\n
        vent2: Booleano que hace referencia a CrearHuelga\n
        vent3: Booleano que hace referencia a ConsultaHuelga
        """
        App.__init__(self,title,id)
        self.title = title
        self.vent1 = False
        self.vent2 = False
        self.vent3 = False

    def startup(self):
        """Metodo que crea la instancia de la ventana"""
        self.main_window = MainWindow(id="CrearHuelga",title=self.title,)

        mainBox = Box(style=Pack(direction=COLUMN))
        #PRIMERA COLUMNA
        boxLabelsCurso = Box(style=Pack(direction=ROW))
        boxLabelsCurso.add(self.createSeparator(cantidad=100,id="separatorCurso"))
        boxLabelsCurso.add(self.createLabelCurso())
        self.selectionCurso = self.createSelectionCurso()
        boxLabelsCurso.add(self.selectionCurso)
        #self.inputCurso = self.createInputCurso()
        #boxLabelsCurso.add(self.inputCurso)
        #SEGUNDA COLUMNA
        boxLabelsHuelga = Box(style=Pack(direction=ROW))
        boxLabelsHuelga.add(self.createSeparator(cantidad=130,id="separatorHuelga"))
        boxLabelsHuelga.add(self.createLabelHuelga())
        self.inputHuelga = self.createInputHuelga()
        boxLabelsHuelga.add(self.inputHuelga)
        #TERCERA COLUMNA
        boxAlumnos = Box(style=Pack(direction=ROW))
        boxAlumnos.add(self.createSeparator(cantidad=100,id="separatorAlumnos"))
        boxAlumnos.add(self.createLabelAlumnos())
        self.selectionAlumnos = self.createSelectionAlumno()
        boxAlumnos.add(self.selectionAlumnos)
        #BOX PRINCIPAL
        mainBox.add(boxLabelsCurso)
        mainBox.add(boxLabelsHuelga)
        mainBox.add(boxAlumnos)
        self.main_window.content = mainBox
        self.main_window.show()
    def createLabelCurso(self):
        """
        Metodo que crea un label con curso como identificador
        """
        curso = Label(text="Curso:",id="LabelCurso")
        curso.style.padding = 30
        curso.style.font_size = 14
        curso.style.width = 60
        return curso
    
    def createLabelHuelga(self):
        """
        Metodo que crea un label con huelga como identificador
        """
        huelga = Label(text="Huelga:",id="LabelHuelga")
        huelga.style.font_size = 14
        huelga.style.width = 122
        return huelga
    
    def createLabelAlumnos(self):
        """
        Metodo que crea un label con alumno como identificador
        """
        alumno = Label(text="Alumnos:",id="LabelAlumnos")
        alumno.style.font_size = 14
        alumno.style.width = 90
        alumno.style.padding = 30
        return alumno
    
    def createInputCurso(self):
        """
        Metodo que crea una caja de texto para introducir datos\n
        !DEPRECATED Actualmente esta en desarrollo otro metodo que elige los cursos 
        """
        inputCurso = TextInput(id="InputCurso",placeholder="Introduce el curso")
        inputCurso.style.padding = 32
        inputCurso.style.width = 200
        return inputCurso

    def createSelectionCurso(self):
        """
        Metodo que crea una caja donde puedes seleccionar los cursos que existen
        """
        listaCursos = self.obtenerCursos()
        selectionCurso = Selection(id="SelectionCurso",enabled=True,items=listaCursos,on_select=self.onChangeCurso)
        selectionCurso.style.padding = 32
        selectionCurso.style.width = 200
        return selectionCurso
    
    def createInputHuelga(self):
        """
        Metodo que crea una caja de texto para introducir datos
        """
        inputHuelga = TextInput(id="InputHuelga",placeholder="--/--/----")
        inputHuelga.style.width = 200
        return inputHuelga 

    def createSelectionAlumno(self):
        """
        Metodo que que crea una caja donde puedes seleccionar los alumnos que existen
        """ 
        selectionAlumnos = Selection(id="SelectionAlumnos")
        selectionAlumnos.style.width = 200
        selectionAlumnos.style.padding = 30
        return selectionAlumnos
    
    def createSeparator(self,cantidad:int,id:str):
        """
        Metodo que separa horizontalmente widgets\n
        PARAMETROS:\n
        canridad: Cantidad de pixeles a separar
        """
        separator = Label(text="",id=id)
        separator.style.width = cantidad
        return separator
    
    def listener(self):
        if(self.vent1==False):
            self.on_exit = self.appClosed()
        return self.vent1,self.vent2,self.vent3

    def appClosed(self):
        self.vent1 = False
        self.vent2 = False
        self.vent3 = False

    def obtenerCursos(self) -> list[str]:
        """
        Metodo que recoge los cursos del fichero de alumnos para guardarlos en un selection
        """
        self.cursos = []
        alumnos:list[Alumno] = ALUMNOS_OPERATOR.readFile()
        for curso in alumnos:
            if(self.cursos.__len__()==0): 
                self.cursos.append(curso.curso)
            elif(self.comprobarCursoRepetido(cursos=self.cursos,checkCurso=curso.curso)):
                self.cursos.append(curso.curso)
        self.cursos.append("Todos")
        return self.cursos
    def comprobarCursoRepetido(self,cursos:list,checkCurso:str) -> bool:
        comprobar = True
        i = 0
        while(i<cursos.__len__()):
            if(cursos[i]==checkCurso):
                comprobar=False
                break
            i+=1
        return comprobar

    def mostrarAlumnoPorCurso(self,curso:str) -> list:
        """
        Metodo que devuelve una lista de alumnos en funcion de su curso
        """
        listaAlumnos:list[Alumno] = ALUMNOS_OPERATOR.readFile()
        alumnos:list[Alumno] = []
        if(curso!="Todos"):
            for alumno in listaAlumnos:
                if(alumno.curso==curso):
                    alumnos.append(alumno)
        else:
            alumnos = listaAlumnos
        alumnosParse = []
        for alumno in alumnos:
            alumnosParse = alumno.nombre+", "+alumno.apellido
        return alumnosParse

    def onChangeCurso(self,widget):
        self.selectionAlumnos.items = self.mostrarAlumnoPorCurso(curso=self.selectionCurso.value)

