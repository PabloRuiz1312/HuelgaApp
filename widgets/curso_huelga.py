from toga import App
from toga import Box
from toga import Button
from toga import Label
from toga import TextInput
from toga.style.pack import *
from toga import MainWindow
from toga import Selection
from toga import Table
from connection.students_file import StudentsFile
from connection.students_file import Alumno
from connection.mongo_connection import MongoConnection
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

class CursoHuelga (App):
    """
    Clase que se encarga de gestionar la ventana donde se consulta una huelga por cursos 
    """
    def __init__(self,title,id,vent1,vent4) -> None:
        """
        Constructor que mediante atributos del padre App crea \n
        una app que gestionara mas adelante un MainWindow \n
        PARAMETROS:\n
        title: Titulo de la app\n
        id: Identificador de la app\n
        vent1: Booleano que hace referencia a HomeWindow\n
        vent4: Booleano que hace referencia a esta ventana
        """
        App.__init__(self,title,id)
        self.title = title
        self.vent1 = vent1
        self.vent2 = False
        self.vent3 = False
        self.vent4 = vent4
        self.file = StudentsFile()
        self.listaALumnos = self.file.readFile()
        self.client:MongoClient = None
        self.database:Database = None
        self.collection:Collection = None
        self.mongo = MongoConnection(databaseName="HuelgaDB",collectionName="huelga")
        self.client,self.database,self.collection = self.mongo.connection()
    
    def startup(self):
        """Metodo que crea la instancia de la ventana"""
        self.main_window = MainWindow(id="CrearHuelga",title=self.title,size=[500,350])

        mainBox = Box(style=Pack(direction=COLUMN))
        #PRIMERA COLUMNA
        boxSelectionCurso = Box(style=Pack(direction=ROW))
        boxSelectionCurso.add(self.createSeparator(cantidad=90,id="CursoSeparator"))
        boxSelectionCurso.add(self.createLabelCurso())
        self.selectionCurso = self.createSelectionCurso()
        boxSelectionCurso.add(self.selectionCurso)
        #SEGUNDA COLUMNA
        boxInputFecha = Box(style=Pack(direction=ROW))
        boxInputFecha.add(self.createSeparator(cantidad=90,id="FechaSeparator"))
        boxInputFecha.add(self.createLabelFecha())
        self.inputFecha = self.createInputFecha()
        boxInputFecha.add(self.inputFecha)
        #TERCERA COLUMNA
        boxTablaAlumnos = Box(style=Pack(direction=ROW))
        boxTablaAlumnos.add(self.createSeparator(cantidad=40,id="TablaSeparator"))
        self.tablaAlumnos = self.createTable()
        boxTablaAlumnos.add(self.tablaAlumnos)
        #CUARTA COLUMNA
        boxBotones = Box(style=Pack(direction=ROW))
        boxBotones.add(self.createSeparator(cantidad=130,id="BotonesSeparator"))
        boxBotones.add(self.crearBotonAceptar())
        boxBotones.add(self.crearBotonSalir())
        #BOX PRINCIPAL
        mainBox.add(boxSelectionCurso)
        mainBox.add(boxInputFecha)
        mainBox.add(boxTablaAlumnos)
        mainBox.add(boxBotones)
        self.main_window.content = mainBox
        self.main_window.show()
    

    def createSeparator(self,cantidad:int,id:str):
        """
        Metodo que separa horizontalmente widgets\n
        PARAMETROS:\n
        canridad: Cantidad de pixeles a separar
        """
        separator = Label(text="",id=id)
        separator.style.width = cantidad
        return separator
    
    def createLabelCurso(self):
        label = Label(text="Curso:",id="LabelCurso")
        label.style.padding = 10
        label.style.font_size = 14
        return label

    def createSelectionCurso(self):
        selection = Selection(id="SelectionCurso",on_select=self.onChangeCurso)
        selection.style.padding = 10
        return selection
    
    def createLabelFecha(self):
        label = Label(text="Fecha:",id="LabelFecha")
        label.style.padding = 10
        label.style.font_size = 14
        return label
    
    def createInputFecha(self):
        inputFecha = TextInput(id="InputFecha",placeholder="--/--/----")
        inputFecha.style.padding = 10
        inputFecha.style.width = 200
        return inputFecha
    
    def createTable(self):
        table = Table(id="TablaAlumnos",headings=["Alumnos"])
        table.style.width = 400
        table.style.padding = 15
        return table
    
    def crearBotonAceptar(self):
        boton = Button(text="Aceptar",id="BotonAceptar",on_press=self.onPressAceptar)
        boton.style.font_size = 14
        boton.style.padding = 10
        return boton

    def crearBotonSalir(self):
        boton = Button(text="Salir",id="BotonSalir",on_press=self.onPressSalir)
        boton.style.font_size = 14
        boton.style.padding = 10
        return boton

    def listener(self):
        if(self.vent1==False):
            self.on_exit = self.appClosed()
        return self.vent1,self.vent2,self.vent3,self.vent4

    def appClosed(self):
        self.vent1 = False
        self.vent2 = False
        self.vent3 = False
        self.vent4 = False
    
    def onPressAceptar(self,widget):
        huelga = self.collection.find_one({"fecha":self.inputFecha.value})
        alumnos:list = huelga.get("alumnos")
        self.cursos = []
        repetido = False
        for i in alumnos:
            if(self.cursos.__len__()==0):
                self.cursos.append(i.get("curso"))
            else:
                for j in self.cursos:
                    if(i.get("curso")==j):
                        repetido = True
            if(repetido==False):
                self.cursos.append(i.get("curso"))
            repetido = False
        self.selectionCurso.items = self.cursos
    
    def onChangeCurso(self,widget):
        huelga = self.collection.find_one({"fecha":self.inputFecha.value})
        alumnos:list = huelga.get("alumnos")
        alumnosTabla:list = []
        alumno = ""
        for i in alumnos:
            alumno+=i.get("nombre")+" "+i.get("apellido")+" "+i.get("dni")
            if(i.get("curso")==self.selectionCurso.value):
                alumnosTabla.append(alumno)
            alumno = ""
        self.tablaAlumnos.data = alumnosTabla
    
    def onPressSalir(self,widget):
        self.vent4 = False
        self.vent1 = True
        self.app.exit()