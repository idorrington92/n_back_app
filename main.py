from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.clock import Clock
from numpy.random import randint


class NBackTile(Widget):
    def __init__(self, **kwargs):
        super(NBackTile, self).__init__(**kwargs)
        self.state = "dark"


    def printIDs(self):
        print(self.ids)
        self.state = "lit"

class NBackGame(Widget):
    def __init__(self):
        super().__init__()
        self.lightstep = 1
        self.tiles = ['upperl', 'upperm', 'upperr',
                      'centerl', 'centertile', 'centerr',
                      'lowerl', 'lowerm', 'lowerr']

    def printIDs(self):
        print(self.ids)

    def update_grid(self, *args):
        self.canvas.clear()
        with self.canvas:
            self.sqsize = self.size[1] / 4
            # Add a rectangle
            if self.lightstep%3==1:
                highlight = self.tiles[randint(9)]
                self.ids[highlight].state = 'lit'
                print(highlight)
                self.lightstep += 1


class NBackApp(MDApp):
    def build(self):
        grid = NBackGame()
        Clock.schedule_interval(grid.update_grid, 1)
        return grid

    def printIDs(self):
        print(self.root.ids)

NBackApp().run()