import toga
from widgets.home_window import HomeWindow

if __name__ == "__main__":
    appInit = HomeWindow().app
    appInit.main_loop()