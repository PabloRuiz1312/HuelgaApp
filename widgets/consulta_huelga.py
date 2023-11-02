from toga import App
from toga import Button
from toga import Box

class ConsultaHuelga:
    """Clase que permite consultar una huelga y sus datos"""
    def __init__(self,vent1,vent2,vent3) -> None:
        """Constructor que crea la segunda pantalla y controla los booleanos de las demas pantallas"""
        self.app = App('HuelgaApp','es.iesjandula.toga',startup=self.build,author="Pablo Ruiz Canovas",description="App que gestiona los alumnos que van a la huelga",home_page="https://www.iesjandula.es/drupal/",)
        self.vent1 = vent1
        self.vent2 = vent2
        self.vent3 = vent3

    def build(self,app):
        box = Box()
        primerBoton = self.botonAleatorio()
        box.add(primerBoton)
        return box
    
    def botonAleatorio(self):
        button = Button(text="Pulsar",on_press=self.onPressedBack)
        button.style.padding = 45
        button.style.font_size = 14
        button.style.width = 200
        return button

    def onPressedBack(self,widget):
        self.vent2 = False
        self.vent1 = True
        self.app.exit()

    def listener(self):
        return self.vent1,self.vent2,self.vent3
        
