import toga
def onPress(widget):
    print("Hola mundo")
def new_button():
    button = toga.Button(text="Boton prueba", on_press=onPress)
    return button
def build(app):
    box = toga.Box()
    boton = new_button()
    box.add(boton)
    return box
def main():
    app = toga.App('HuelgaApp','es.iesjandula.toga',startup=build,author="Pablo Ruiz Canovas",description="App que gestiona los alumnos que van a la huelga",home_page="https://www.iesjandula.es/drupal/",)
    return app

if __name__ == "__main__":
    app = main()
    app.main_loop()