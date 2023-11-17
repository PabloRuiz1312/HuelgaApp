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
        self.file = StudentsFile()
        self.listaALumnos = self.file.readFile()
        self.client:MongoClient = None
        self.database:Database = None
        self.collection:Collection = None
        self.mongo = MongoConnection(databaseName="HuelgaDB",collectionName="huelga")
        self.client,self.database,self.collection = self.mongo.connection()
    

    def startup(self):
        """Metodo que crea la instancia de la ventana"""
        self.main_window = MainWindow(id="CrearHuelga",title=self.title,size=[640,520])

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
        boxAlumnos.add(self.createSeparator(cantidad=150,id="separatorAlumnos"))
        self.tablaAlumnos = self.createTablaAlumnos()
        boxAlumnos.add(self.tablaAlumnos)
        #CUARTA COLUMNA
        boxBotonAdd = Box(style=Pack(direction=ROW))
        boxBotonAdd.add(self.createSeparator(cantidad=150,id="separatorLabelAlumnos"))
        boxBotonAdd.add(self.crearBotonTablaAlumnos())
        boxBotonAdd.add(self.crearBotonDeleteAlumno())
        boxBotonAdd.add(self.crearBotonLimpiarAlumno())
        #QUINTA COLUMNA
        boxTablaAdded = Box(style=Pack(direction=ROW))
        boxTablaAdded.add(self.createSeparator(cantidad=160,id="separatorAlumnosAdded"))
        self.tablaAlumnosAdded = self.createTablaAlumnosAdded()
        boxTablaAdded.add(self.tablaAlumnosAdded)
        #SEXTA COLUMNA
        boxLabelInfo = Box(style=Pack(direction=ROW))
        boxLabelInfo.add(self.createSeparator(cantidad=160,id="separatorLabelInfo"))
        self.labelInfo = self.createLabelInfo()
        boxLabelInfo.add(self.labelInfo)
        #SEPTIMA COLUMNA
        boxBotonAction = Box(style=Pack(direction=ROW))
        boxBotonAction.add(self.createSeparator(cantidad=210,id="separatorBotonAction"))
        boxBotonAction.add(self.crearBotonAddHuelga())
        boxBotonAction.add(self.crearBotonSalir())
        #BOX PRINCIPAL
        mainBox.add(boxLabelsCurso)
        mainBox.add(boxLabelsHuelga)      
        mainBox.add(boxAlumnos)
        mainBox.add(boxBotonAdd)
        mainBox.add(boxTablaAdded)
        mainBox.add(boxLabelInfo)
        mainBox.add(boxBotonAction)
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
        selectionCurso = Selection(id="SelectionCurso",enabled=True,items=listaCursos,on_change=self.onChangeCurso)
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
        !DEPRECATED Este widget sera sustituido mas adelante por el de una tabla
        """ 
        curso = self.selectionCurso.value
        listaAlumnos = self.mostrarAlumnoPorCurso(curso=curso)
        selectionAlumnos = Selection(id="SelectionAlumnos",items=listaAlumnos)
        selectionAlumnos.style.width = 200
        selectionAlumnos.style.padding = 30
        return selectionAlumnos
    
    def crearBotonTablaAlumnos(self):
        boton = Button(text="Añadir alumno",id="BotonAddAlumnos",on_press=self.onPressBotonAlumnos)
        boton.style.padding = 8
        return boton

    def crearBotonDeleteAlumno(self):
        boton = Button(text="Borrar alumno",id="BotonBorrarAlumno",on_press=self.onPressBotonBorrarAlumnos)
        boton.style.padding = 8
        return boton
    
    def crearBotonLimpiarAlumno(self):
        boton = Button(text="Limpiar",id="BotonLimpiarAlumno",on_press=self.onPressBotonLimpiarAlumnos)
        boton.style.padding = 8
        return boton

    def crearBotonAddHuelga(self):
        boton = Button(text="Crear Huelga",id="CrearHuelga",on_press=self.uploadHuelga)
        boton.style.padding = 10
        return boton
    
    def crearBotonSalir(self):
        boton = Button(text="Salir",id="Salir",on_press=self.onPressSalir)
        boton.style.padding = 10
        return boton
    
    def createTablaAlumnos(self):
        curso = self.selectionCurso.value
        listaAlumnos = self.mostrarAlumnoPorCurso(curso=curso)
        tabla = Table(headings=["Alumnos"],id="TablaAlumno",data=listaAlumnos,multiple_select=True)
        tabla.style.padding = 20
        tabla.style.width=250
        return tabla
    
    def createTablaAlumnosAdded(self):
        tabla = Table(headings=["Alumnos añadidos"],id="TablaAlumnoAdded",multiple_select=True)
        tabla.style.width=250
        tabla.style.padding = 10
        return tabla

    def createLabelInfo(self):
        label = Label(text="",id="InfoLabel")
        label.style.font_size = 8
        return label
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
        alumnos:list[Alumno] = self.listaALumnos
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
        listaAlumnos:list[Alumno] = self.listaALumnos
        alumnos:list[Alumno] = []
        if(curso=="Todos"):
            alumnos = listaAlumnos
        else:
            for alumno in listaAlumnos:
                if(alumno.curso==curso):
                    alumnos.append(alumno)
        alumnosParse = []
        for alumno in alumnos:
            alumnosParse.append(alumno.nombre+", "+alumno.apellido)
        return alumnosParse

    def onChangeCurso(self,widget):
        """
        Este metodo cambia el valor de los alumnos\n 
        """
        curso = self.selectionCurso.value
        array = self.mostrarAlumnoPorCurso(curso=curso)
        self.tablaAlumnos.data = array

    def onPressBotonAlumnos(self,widget):
        alumno = self.tablaAlumnos.selection
        datosAlumnos = self.tablaAlumnos.data
        datosAlumnosAdded = self.tablaAlumnosAdded.data
   
        for i in alumno:
            if(self.comprobacionTabla(i,datosAlumnosAdded)==False):
                sourceStr = ""+str(i)
                sourceList = sourceStr.split("'")
                datosAlumnosAdded.append(sourceList[1])
        self.tablaAlumnosAdded.data = datosAlumnosAdded
    
    def onPressBotonBorrarAlumnos(self,widget):
        alumno = self.tablaAlumnosAdded.selection
        oldTable = self.tablaAlumnosAdded.data
        data = []
        newTable = []
        if(alumno.__len__()!=0):
            for i in oldTable:
                sourceStr = ""+str(i)
                sourceList = sourceStr.split("'")
                data.append(sourceList[1])
            for i in alumno:
                sourceStr = ""+str(i)
                sourceList = sourceStr.split("'")
                for j in data:
                    if(sourceList[1]!=j):
                        newTable.append(j)
            self.labelInfo.text = ""
            self.tablaAlumnosAdded.data = newTable
        else:
            self.labelInfo.text = "No has seleccionado ningun alumno"
    
    def onPressBotonLimpiarAlumnos(self,widget):
        self.tablaAlumnosAdded.data = []
            

    def comprobacionTabla(self,dato,datosOtraTabla) -> bool:
        repetido = False
        if(datosOtraTabla.__len__()!=0):
            sourceStr = ""+str(dato)
            sourceList = sourceStr.split("'")
            for j in datosOtraTabla:
                sourceStr2 = ""+str(j)
                sourceList2 = sourceStr2.split("'")
                if(sourceList[1]==sourceList2[1]):
                    repetido=True
                    self.labelInfo.text = "Alumno "+str(sourceList[1])+" repetido"
                    break
                else:
                    self.labelInfo.text = ""
        return repetido
    
    def onPressSalir(self,widget):
        self.vent2 = False
        self.vent1 = True
        self.file.closeFile()
        self.mongo.closeConnection()
        self.app.exit()
    
    def getAlumnosAdded(self):
        data = self.tablaAlumnosAdded.data
        alumnos:list[Alumno] = self.listaALumnos
        alumnosToAdd = []
        
        for i in data:
            sourceStr = ""+str(i)
            sourceList = sourceStr.split("'")
            sourceAlumno = sourceList[1].split(",")
            sourceAlumno[1] = sourceAlumno[1].removeprefix(" ")
            for j in alumnos:
                if(j.nombre==sourceAlumno[0] and j.apellido==sourceAlumno[1]):
                    alumnosToAdd.append(j)
        return alumnosToAdd
    
    def uploadHuelga(self,widget):
        alumnos:list[Alumno] = []
        array:list[dict] = []
        if(self.inputHuelga.value!=""):
            textFormat = self.inputHuelga.value.split("/")
            if(textFormat.__len__()==3):
                textFormat[1] = textFormat[1].removeprefix(" ")
                textFormat[2] = textFormat[2].removeprefix(" ")
                if(textFormat[0].__len__()==2 and textFormat[1].__len__()==2 and textFormat[2].__len__()==4):
                    if(self.checkFecha(textFormat)):
                        alumnos = self.getAlumnosAdded()
                        if(alumnos.__len__()!=0):
                            for i in alumnos:
                                alumno = dict(apellido=i.apellido,nombre=i.nombre,dni=i.dni,curso=i.curso)
                                array.append(alumno)
                            huelga=dict(fecha=self.inputHuelga.value,alumnos=array)
                            self.collection.insert_one(huelga)
                        else:
                            self.labelInfo.text = "Error, no hay ningun alumno para añadir"
                    else:
                        self.labelInfo.text = "Error los meses o dias no coinciden"
                else:
                    self.labelInfo.text = "Error, fecha mal introducida el formato debe de ser --/--/----"
            else:
                self.labelInfo.text = "Error el formato de fecha debe de ser --/--/----"
        else:
            self.labelInfo.text = "Error, la fecha esta vacia"
    
    def checkFecha(self,fecha:list) -> bool:
        checked = False
        mes = int(fecha[1])
        dia = int(fecha[0])
        year = int(fecha[2])

        if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
            checked = dia>0 and dia<=31
        elif(mes==4 or mes==6 or mes==9 or mes==11):
            checked = dia>0 and dia<=30
        elif(mes==2):
            if(year%4 == 0):
                checked = dia>0 and dia<=29
            else:
                checked = dia>0 and dia<=28
        return checked


#alumno = dict(apellido=apellido,nombre=nombre,dni=dni,curso=curso)
#coleccion.insert_one(alumno)
        

