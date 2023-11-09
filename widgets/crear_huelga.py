from toga import App
from toga import Box
from toga import Button
from toga import Label
from toga import TextInput
from toga.style.pack import *
from toga import MainWindow

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
        boxLabelsCurso.add(self.createSeparator(cantidad=100))
        boxLabelsCurso.add(self.createLabelCurso())
        boxLabelsCurso.add(self.createInputCurso())
        #SEGUNDA COLUMNA
        boxLabelsHuelga = Box(style=Pack(direction=ROW))
        mainBox.add(boxLabelsCurso)
        mainBox.add(boxLabelsHuelga)
        self.main_window.content = mainBox

        self.main_window.show()
    
    def createLabelCurso(self):
        """
        Metodo que crea un label con curso como identificador
        """
        curso = Label(text="Curso",id="LabelCurso")
        curso.style.padding = 30
        curso.style.font_size = 14
        curso.style.width = 60
        return curso
    
    def createInputCurso(self):
        """
        Metodo que crea una caja de texto para introducir datos
        """
        inputCurso = TextInput(id="InputCurso",placeholder="Introduce el curso")
        inputCurso.style.padding = 32
        inputCurso.style.width = 200
        return inputCurso
    
    def createLabelHuelga(self):
        """
        Metodo que crea un label con huelga como identificador
        """
        huelga = Label(text="Huelga",id="LabelHuelga")
        huelga
    def createSeparator(self,cantidad):
        """
        Metodo que separa horizontalmente widgets\n
        PARAMETROS:\n
        canridad: Cantidad de pixeles a separar
        """
        separator = Label(text="",id="Separator")
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