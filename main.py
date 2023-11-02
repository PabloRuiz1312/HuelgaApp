import toga
from widgets.home_window import HomeWindow
from widgets.consulta_huelga import ConsultaHuelga
if __name__ == "__main__":
    vent1 = True
    vent2 = False
    vent3 = False
    while(vent1 or vent2 or vent3):
        if(vent1):
            appInit = HomeWindow(vent1,vent2,vent3)
            homeApp = appInit.app
            homeApp.main_loop()
            vent1,vent2,vent3 = appInit.listener()
        if(vent2):
            appInit = ConsultaHuelga(vent1,vent2,vent3)
            consultaApp = appInit.app
            consultaApp.main_loop()
            vent1,vent2,vent3 = appInit.listener()
