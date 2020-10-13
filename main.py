from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.clock import Clock
from numpy.random import randint
from kivy.animation import Animation


from kivy.core.window import Window
Window.size = (275, 600)

class GameButton(Widget):
    def __init__(self, **kwargs):
        super(GameButton, self).__init__(**kwargs)

class NBackTile(Widget):
    def __init__(self, **kwargs):
        super(NBackTile, self).__init__(**kwargs)

    def highlight_tile(self):
        anim = Animation(animated_color=MDApp.get_running_app().theme_cls.primary_light, opacity=0.75, duration=.5)
        anim.bind(on_complete=self.reset)
        anim.start(self)

    def reset(self, *args):
        anim = Animation(animated_color=MDApp.get_running_app().theme_cls.primary_dark, opacity=.05, duration=.5)
        #self.animated_color = MDApp.get_running_app().theme_cls.primary_dark
        anim.start(self)

    def printIDs(self):
        print(self.ids)
        print(self.state)

class GridLine(Widget):
    pass

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
        # Add a rectangle
        if self.lightstep%3==1:
            self.highlight = self.tiles[randint(9)]
            self.ids[self.highlight].highlight_tile()

        self.lightstep += 1


class NBackApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        game = NBackGame()
        Clock.schedule_interval(game.update_grid, 1.)
        return game

    def printIDs(self):
        print(self.root.ids)


NBackApp().run()