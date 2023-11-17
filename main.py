import toga
#from widgets.home_window import HomeWindow
from widgets.home_window import HomeWindow
from widgets.crear_huelga import CrearHuelga
from widgets.consulta_huelga import ConsultaHuelga
if __name__ == "__main__":
    vent1 = True
    vent2 = False
    vent3 = False
    
    while(vent1 or vent2 or vent3):
        if(vent1):
            appInit = HomeWindow(title="HuelgaApp",id="es.iesjandula",vent1=vent1,vent2=vent2,vent3=vent3)
            appInit.main_loop()
            vent1,vent2,vent3 = appInit.listener()
        if(vent2):
            appInit = CrearHuelga(title="HuelgaApp",id="es.iesjandula",vent1=vent1,vent2=vent2)
            appInit.main_loop()
            vent1,vent2,vent3 = appInit.listener()
        if(vent3):
            appInit = ConsultaHuelga(title="HuelgaApp",id="es.iesjandula",vent1=vent1,vent3=vent3)
            appInit.main_loop()
            vent1,vent2,vent3 = appInit.listener()