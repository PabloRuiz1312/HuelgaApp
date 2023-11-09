from toga import App
from toga import Box
from toga import Button
from toga.style.pack import *
from toga import MainWindow

class HomeWindow(App):
    """
    Clase que se encarga de gestionar la ventana principal
    """
    def __init__(self,title,id,vent1,vent2,vent3) -> None:
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
        self.main_window = MainWindow(id="HomeView",title=self.title,size=(250,480))

        box = Box(style=Pack(direction=COLUMN))
        box.add(self.crearHuelga())
        box.add(self.consultarHuelgas())
        box.add(self.crearHuelgaCurso())
        box.add(self.crearBotonSalir())

        self.main_window.content = box

        self.main_window.show()
    
    def crearHuelga(self):
        """
        Boton para crear una huelga\n
        Returns: El boton con sus atributos
        """
        button = Button(text="Crear huelga", on_press=self.onPressCrearHuelga)#, on_press=onPress)
        button.style.padding = 30
        button.style.font_size = 14
        button.style.width = 200
        return button
    
    def consultarHuelgas(self):
        """
        Boton para consultar una huelga \n
        Returns: El boton con sus atributos
        """
        button = Button(text="Consultar huelga")#, on_press=onPress)
        button.style.padding = 30
        button.style.font_size = 14
        button.style.width = 200
        return button
    
    def crearHuelgaCurso(self):
        """
        Boton para consultar una huelga por cursos\n
        Returns: El boton con sus atributos
        """
        button = Button(text="Consultar huelga curso")
        button.style.padding = 30
        button.style.font_size = 14
        button.style.width = 200
        return button

    def crearBotonSalir(self):
        """
        Boton para salir de la aplicacion\n
        Returns: El boton con sus atributos
        """
        button = Button(text="Salir",on_press=self.onPressSalir)
        button.style.padding = 30
        button.style.font_size = 14
        button.style.width = 200
        return button
    
    def onPressCrearHuelga(self,widget):
        self.vent1=False
        self.vent2=True
        self.app.exit()

    def onPressSalir(self,widget):
        self.vent1 = False
        self.vent2 = False
        self.vent3 = False
        self.app.exit()

    def listener(self):
        if(self.vent2==False and self.vent3==False):
            self.on_exit = self.appClosed()
        return self.vent1,self.vent2,self.vent3

    def appClosed(self):
        self.vent1 = False
        self.vent2 = False
        self.vent3 = False
