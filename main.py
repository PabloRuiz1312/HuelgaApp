import toga

def build(app):
    box = toga.Box()
    return box
def main():
    app = toga.App('HuelgaApp','es.iesjandula.toga',startup=build,author="Pablo Ruiz Canovas",description="App que gestiona los alumnos que van a la huelga",home_page="https://www.iesjandula.es/drupal/")
    return app

if __name__ == "__main__":
    app = main()
    app.main_loop()