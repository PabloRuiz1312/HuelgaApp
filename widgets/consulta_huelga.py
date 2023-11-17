from toga import App
from toga import Button
from toga import Box
from toga import MainWindow
from toga.style.pack import *
from toga import TextInput
from toga import Label
from toga import Selection
from connection.mongo_connection import MongoConnection
from pymongo import MongoClient 
from pymongo.database import Database
from pymongo.collection import Collection
from connection.students_file import Alumno, StudentsFile

class ConsultaHuelga (App):
    """
    Clase que se encarga de gestionar la ventana donde se consulta una huelga
    """
    def __init__(self,title,id,vent1,vent3) -> None:
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
        self.vent4 = False
        self.client:MongoClient = None
        self.database:Database = None
        self.collection:Collection = None
        self.mongo = MongoConnection(databaseName="HuelgaDB",collectionName="huelga")
        self.client,self.database,self.collection = self.mongo.connection()
        self.file = StudentsFile()
        self.listaAlumnos:list[Alumno] = self.file.readFile()
        
    
    def startup(self) -> None:
        """
        Metodo que crea la instancia de la ventana
        """
        self.main_window = MainWindow(id="ConsultarHuelga",title=self.title,size=[500,350])
        #PRIMERA COLUMNA
        boxInputFecha = Box(style=Pack(direction=ROW))
        boxInputFecha.add(self.createSeparator(cantidad=90,id="InputFechaSeparator"))
        boxInputFecha.add(self.createLabelFecha())
        self.inputFecha = self.crearInputFecha()
        boxInputFecha.add(self.inputFecha)
        #SEGUNDA COLUMNA
        boxNumAlumnos = Box(style=Pack(direction=ROW))
        boxNumAlumnos.add(self.createSeparator(cantidad=90,id="NumAlumnosSeparator"))
        self.labelNumAlumnos = self.createLabelNumAlumnos()
        boxNumAlumnos.add(self.labelNumAlumnos)
        #TERCERA COLUMNA
        boxMaxCurso = Box(style=Pack(direction=ROW))
        boxMaxCurso.add(self.createSeparator(cantidad=90,id="CursoMaxAlumnosSeparator"))
        self.labelMaxCurso = self.createLabelCursoMasAlumnos()
        boxMaxCurso.add(self.labelMaxCurso)
        #CUARTA COLUMNA
        boxMinCurso = Box(style=Pack(direction=ROW))
        boxMinCurso.add(self.createSeparator(cantidad=90,id="CursoMinAlumnosSeparator"))
        self.labelMinCurso = self.createLabelCursoMenosAlumnos()
        boxMinCurso.add(self.labelMinCurso)
        #QUINTA COLUMNA
        boxNoCursos = Box(style=Pack(direction=ROW))
        boxNoCursos.add(self.createSeparator(cantidad=90,id="NoCursosSeparator"))
        self.labelNoCurso = self.createLabelNoCursos()
        self.selectionCursos = self.createSelectionCursos()
        boxNoCursos.add(self.labelNoCurso)
        boxNoCursos.add(self.selectionCursos)
        #SEXTA COLUMNA
        boxBotones = Box(style=Pack(direction=ROW))
        boxBotones.add(self.createSeparator(cantidad=150,id="BotonesSeparator"))
        boxBotones.add(self.createAceptarBoton())
        boxBotones.add(self.createSalirBoton())
        #BOX PRINCIPAL
        mainBox = Box(style=Pack(direction=COLUMN))
        mainBox.add(boxInputFecha)
        mainBox.add(boxNumAlumnos)
        mainBox.add(boxMaxCurso)
        mainBox.add(boxMinCurso)
        mainBox.add(boxNoCursos)
        mainBox.add(boxBotones)
        self.main_window.content = mainBox
        self.main_window.show()
    
    def createLabelFecha(self):
        label = Label(text="Fecha:",id="LabelFecha")
        label.style.padding = 10
        label.style.font_size = 14
        return label
    
    def crearInputFecha(self):
        inputFecha = TextInput(id="InputFecha",placeholder="--/--/----")
        inputFecha.style.width = 200
        inputFecha.style.padding = 10
        return inputFecha
    
    def createLabelNumAlumnos(self):
        label = Label(text="Nº de alumnos en huelga:",id="LabelNumAlumnos")
        label.style.font_size = 14
        label.style.padding = 10
        return label

    def createLabelCursoMasAlumnos(self):
        label = Label(text="Curso con mas alumnado:",id="LabelMaxCurso")
        label.style.font_size = 14
        label.style.padding = 10
        return label
    
    def createLabelCursoMasAlumnos(self):
        label = Label(text="Curso con mas alumnado:",id="LabelMaxCurso")
        label.style.font_size = 14
        label.style.padding = 10
        return label
    
    def createLabelCursoMenosAlumnos(self):
        label = Label(text="Curso con menos alumnado:",id="LabelMinCurso")
        label.style.font_size = 14
        label.style.padding = 10
        return label
    
    def createLabelNoCursos(self):
        label = Label(text="Cursos que no van:",id="LabelNoCurso")
        label.style.font_size = 14
        label.style.padding = 10
        return label
    
    def createSelectionCursos(self):
        selection = Selection(id="SelectionCursos")
        selection.style.padding = 10
        return selection
    
    def createAceptarBoton(self):
        boton = Button(text="Aceptar",id="BotonAceptar",on_press=self.onPressedAceptar)
        boton.style.padding = 10
        boton.style.font_size = 14
        return boton
    
    def createSalirBoton(self):
        boton = Button(text="Salir",id="SalirBoton",on_press=self.onPressedSalir)
        boton.style.padding = 10
        boton.style.font_size = 14
        return boton

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
        return self.vent1,self.vent2,self.vent3,self.vent4

    def appClosed(self):
        self.vent1 = False
        self.vent2 = False
        self.vent3 = False
        self.vent4 = False

    def onPressedSalir(self,widget):
        self.vent1 = True
        self.vent3=False
        self.app.exit()
    
    def onPressedAceptar(self,widget):
        huelga = self.collection.find_one({"fecha":self.inputFecha.value})
        array:list = huelga.get("alumnos")
        self.labelNumAlumnos.text = "Nº de alumnos en huelga: "+str(array.__len__())
        curso:list = []
        repetido = False
        for i in array:
            if(curso.__len__()==0):
                curso.append(i.get("curso"))
            else:
                for j in curso:
                    if(i.get("curso")==j):
                        repetido=True
                if(repetido==False):
                    curso.append(i.get("curso"))
            repetido=False
        mayorCurso = ""
        lastCount = 0
        count = 0
        for i in curso:
            for j in array:
                if(i==j.get("curso")):
                    count+=1
            if(count>lastCount):
                mayorCurso = i
                lastCount = count
            count = 0
        self.labelMaxCurso.text = "Curso con mas alumnado: "+str(mayorCurso)
        lastCount = 0
        count = 0
        minCurso = ""
        for i in curso:
            for j in array:
                if(i!=j.get("curso")):
                    count+=1
            if(count>lastCount):
                minCurso = i
                lastCount = count
            count = 0
        self.labelMinCurso.text = "Curso con menos alumnado: "+str(minCurso)
        listaCursos = self.obtenerCursos()
        noCursos = []
        noCurso = True
        for i in listaCursos:
            for j in curso:
                if(j==i):
                    noCurso=False
            if(noCurso):
                noCursos.append(i)
            noCurso=True
        self.selectionCursos.items = noCursos
    
    def obtenerCursos(self) -> list[str]:
        """
        Metodo que recoge los cursos del fichero de alumnos para guardarlos en un selection
        """
        self.cursos = []
        alumnos:list[Alumno] = self.listaAlumnos
        for curso in alumnos:
            if(self.cursos.__len__()==0): 
                self.cursos.append(curso.curso)
            elif(self.comprobarCursoRepetido(cursos=self.cursos,checkCurso=curso.curso)):
                self.cursos.append(curso.curso)

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