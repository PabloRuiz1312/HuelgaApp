from toga import App
from toga import Box
from toga import Button
class HomeWindow:
    """
    Clase que se encarga de controlar la ventana principal al iniciar la app y de llamar \n
    a las otras ventanas una vez que se empiece a operar con ellas
    """
    def __init__(self) -> None:
        '''
        Constructor que crea la ventana principal
        '''
        self.app = App('HuelgaApp','es.iesjandula.toga',startup=self.build,author="Pablo Ruiz Canovas",description="App que gestiona los alumnos que van a la huelga",home_page="https://www.iesjandula.es/drupal/",)

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
        button = Button(text="Crear huelga")#, on_press=onPress)
        button.style.padding = 20
        button.style.font_size = 14
        button.style.width = 200
        return button
    
    def consultarHuelgas(self):
        """
        Boton para consultar una huelga \n
        Retorna el boton
        """
        button = Button(text="Consultar huelga")#, on_press=onPress)
        button.style.padding = 90
        button.style.font_size = 14
        button.style.width = 200
        return button
    
    #def onPress(widget):
    #    print("Hola mundo")