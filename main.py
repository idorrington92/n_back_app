from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.clock import Clock
from numpy.random import randint
from random import sample
from kivy.animation import Animation
from kivy.properties import NumericProperty, ObjectProperty, ListProperty


from kivy.core.window import Window
Window.size = (275, 600)

class GameButton(Widget):
    pass


class NBackTile(Widget):
    def highlight_tile(self):
        anim = Animation(animated_color=MDApp.get_running_app().theme_cls.primary_light, opacity=0.75, duration=.5)
        anim.bind(on_complete=self.reset)
        anim.start(self)

    def reset(self, *args):
        anim = Animation(animated_color=MDApp.get_running_app().theme_cls.primary_dark, opacity=.05, duration=.5)
        anim.start(self)

    def printIDs(self):
        print(self.ids)
        print(self.state)

class GridLine(Widget):
    pass

class NBackGame(Widget):
    # Initialise score
    score = NumericProperty(0)
    # N back
    N = 2
    # Time step in game. Tile lights up when a multiple of 3.
    timestep = NumericProperty(0)
    # Counts how many times tiles have lit up.
    lightstep = NumericProperty(0)
    # Length of round. e.g. 40 iterations at 3 seconds makes a 2 minute round.
    num_iter = N * 12
    # Choose 10 indexes to be guarenteed repeats
    rand_doubles = sample(range(N, num_iter-10), 10)
    # Create the random order for the tiles
    random_order = []
    for i in range(num_iter):
        if i in rand_doubles:
            random_order.append(random_order[-N])
        else:
            random_order.append(randint(9))

    tiles = ListProperty(['upperl', 'upperm', 'upperr', 'centerl',
                          'centertile', 'centerr', 'lowerl', 'lowerm',
                          'lowerr'])

    def printIDs(self):
        print(self.ids)

    def button_press(self):
        # Was button press correct?
        # Update score in app
        self.update_score(100)

    def update_grid(self, *args):
        # Add a rectangle
        if self.lightstep > self.num_iter:
            # End game
            pass

        if self.timestep%3==1:
            self.lightstep += 1
            self.highlight = self.tiles[self.random_order[self.lightstep]]
            self.ids[self.highlight].highlight_tile()


        self.timestep += 1

    def update_score(self, dscore):
        # Check if player was correct/incorrect and increase/decrease their score accordingly.
        if self.random_order[self.lightstep] == self.random_order[self.lightstep - self.N] and self.N < self.lightstep:
            self.score += dscore
        else:
            self.score -= dscore




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