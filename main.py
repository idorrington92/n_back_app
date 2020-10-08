from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from random import randint
from kivy.graphics.instructions import Canvas

class NBackGrid(Widget):
    pass

class NBackGame(Widget):
    def __init__(self):
        super().__init__()
        self.sqsize = 200
        self.lightstep = 1

    def update_grid(self, *args):
        with self.canvas:
            # Add a rectangle
            grid = {}
            highlight = ()
            if self.lightstep%3==0:
                highlight = (randint(0, 2), randint(0, 2))
            self.lightstep += 1
            for row in range(3):
                grid[row] = {}
                for col in range(3):
                    Color(0, 0, 0.5)
                    if highlight == (row, col):
                        Color(0, 0, 1)
                    grid[row][col] = Rectangle(pos=(row*self.sqsize*1.1+10, col*1.1*self.sqsize + 10),
                                               size=(self.sqsize, self.sqsize))

class NBackApp(MDApp):
    def build(self):
        #grid = NBackGame()
        #Clock.schedule_interval(grid.update_grid, 1)
        return NBackGame() #grid

NBackApp().run()