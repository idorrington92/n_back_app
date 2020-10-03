from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.picker import MDThemePicker



class MainApp(MDApp):
    def open_page(self, page):
        print(f"Opening {page} page")

class Level1Window(Screen):
    pass

class Level2Window(Screen):
    pass

class Level3Window(Screen):
    pass

class HighScoreWindow(Screen):
    pass

class SettingsWindow(Screen):
    pass

class AboutWindow(Screen):
    pass

class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class NavigationBar(MDBottomNavigation):
    pass
MainApp().run()