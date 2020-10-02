from kivymd.app import MDApp

class MainApp(MDApp):
    def open_about(self, *args):
        print("Opening about page")


MainApp().run()