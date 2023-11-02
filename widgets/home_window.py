from toga import App
from toga import Box
from toga import Button
class HomeWindow:
    """
    Clase que se encarga de controlar la ventana principal al iniciar la app y de llamar \n
    a las otras ventanas una vez que se empiece a operar con ellas
    """
    def __init__(self,vent1,vent2,vent3) -> None:
        '''
        Constructor que crea la ventana principal
        '''
        self.app = App('HuelgaApp','es.iesjandula.toga',startup=self.build,author="Pablo Ruiz Canovas",description="App que gestiona los alumnos que van a la huelga",home_page="https://www.iesjandula.es/drupal/",)
        self.vent1 = vent1
        self.vent2 = vent2
        self.vent3 = vent3

    def build(self,app):
        """
        Contenedor de la ventana principal que guarda botones
        """
        box = Box()
        botonCrearHuelga = self.crearHuelga()
        botonConsultarHuelga = self.consultarHuelgas()
        box.add(botonCrearHuelga)
        box.add(botonConsultarHuelga)
        return box

    def crearHuelga(self):
        """
        Boton para crear una huelga\n
        Retorna el boton
        """
        button = Button(text="Crear huelga", on_press=self.onPressCrearHuelga)#, on_press=onPress)
        button.style.padding = 45
        button.style.font_size = 14
        button.style.width = 200
        return button
    
    def consultarHuelgas(self):
        """
        Boton para consultar una huelga \n
        Retorna el boton
        """
        button = Button(text="Consultar huelga")#, on_press=onPress)
        button.style.padding = 45
        
        button.style.font_size = 14
        button.style.width = 200
        return button
    
    def onPressCrearHuelga(self,widget):
        self.vent1=False
        self.vent2=True
        self.app.exit()
    def listener(self):
        return self.vent1,self.vent2,self.vent3
