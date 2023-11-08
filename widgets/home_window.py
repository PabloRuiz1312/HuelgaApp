from toga import App
from toga import Box
from toga import Button
from toga.style.pack import *
from toga import MainWindow
class HomeWindow:
    """
    Clase que se encarga de controlar la ventana principal al iniciar la app y de llamar \n
    a las otras ventanas una vez que se empiece a operar con ellas
    """
    def __init__(self,vent1,vent2,vent3) -> None:
        '''
        Constructor que crea la ventana principal
        '''
        self.app = App(formal_name='HuelgaApp',
                       app_id='es.iesjandula.toga',
                       startup=self.build,
                       author="Pablo Ruiz Canovas",
                       description="App que gestiona los alumnos que van a la huelga",
                       home_page="https://www.iesjandula.es/drupal/"
                       )#App
        self.vent1 = vent1
        self.vent2 = vent2
        self.vent3 = vent3

    def build(self,app):
        """
        Contenedor de la ventana principal que guarda botones
        """
        self.mainWindow = MainWindow(id="es.iesjandula.toga",title="HuelgaApp",size=(250,480),resizeable=False)
        box = Box(style=Pack(direction=COLUMN))
        botonCrearHuelga = self.crearHuelga()
        botonConsultarHuelga = self.consultarHuelgas()
        botonConsultaHuelgaCurso = self.crearHuelgaCurso()
        botonSalir = self.crearBotonSalir()
        box.add(botonCrearHuelga)
        box.add(botonConsultarHuelga)
        box.add(botonConsultaHuelgaCurso)
        box.add(botonSalir)
        self.mainWindow.content = box
        self.mainWindow.show()
        return self.mainWindow

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
        return self.vent1,self.vent2,self.vent3
