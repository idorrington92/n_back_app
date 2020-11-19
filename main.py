from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.clock import Clock
from numpy.random import randint
from random import sample
from kivy.animation import Animation
from kivy.properties import NumericProperty, ListProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
#import os
#os.environ['KIVY_AUDIO'] = 'sdl2'
from kivy.core.audio import SoundLoader


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

    tiles = ListProperty(['upperl', 'upperm', 'upperr', 'centerl',
                          'centertile', 'centerr', 'lowerl', 'lowerm',
                          'lowerr'])

    # N back
    N = NumericProperty(1)

    # Time step in game. Tile lights up when a multiple of 3.
    timestep = NumericProperty(0)

    # Counts how many times tiles have lit up.
    lightstep = NumericProperty(21)

    def on_start(self):
        # Length of round. e.g. 40 iterations at 3 seconds makes a 2 minute round.
        self.num_iter = self.N * 12

        # Choose 10 indexes to be guarenteed repeats
        rand_doubles = sample(range(self.N, self.num_iter-10), 10)

        # Create the random order for the tiles
        random_order = []
        for i in range(self.num_iter):
            if i in rand_doubles:
                random_order.append(random_order[-self.N])
            else:
                random_order.append(randint(9))
        self.random_order = random_order

        self.clock = Clock.schedule_interval(self.update_grid, 1.)


    def printIDs(self):
        print(self.ids)

    def button_press(self):
        # Update score in app
        self.update_score(100)

    def start_game_popup(self):
        # Disable game buttons until after first tile lights up
        self.clicked = True

        # Define start game pop up
        self.popup = MDDialog(title="N-Back to the Future",
                            text="Score: " + str(self.score),
                            size_hint=[.8, .8],
                            #background_color=MDApp.get_running_app().theme_cls.bg_darkest,
                            md_bg_color=MDApp.get_running_app().theme_cls.bg_dark,
                            buttons=[
                                MDFlatButton(
                                    text="Start Game",
                                    text_color=MDApp.get_running_app().theme_cls.primary_color,
                                    on_release=self.level_start
                                ),
                                MDFlatButton(
                                    text="Menu", text_color=MDApp.get_running_app().theme_cls.primary_color,
                                )],
                            auto_dismiss=False,
                            )

        # Open pop up
        self.popup.open()

    def end_game_popup(self):
        self.popup = MDDialog(title="Level Complete",
                            text="Score: " + str(self.score),
                            size_hint=[.8, .8],
                            background_color=MDApp.get_running_app().theme_cls.bg_darkest,
                            md_bg_color=MDApp.get_running_app().theme_cls.bg_dark,
                            buttons=[
                                MDFlatButton(
                                    text="Next Level",
                                    text_color=MDApp.get_running_app().theme_cls.primary_color,
                                    on_release=self.level_start
                                ),
                                MDFlatButton(
                                    text="Menu", text_color=MDApp.get_running_app().theme_cls.primary_color,
                                )],
                            auto_dismiss=False,
                            )
        self.popup.open()

    def level_start(self, *args):
        """
        Restart the game.
        """
        self.N += 1
        self.timestep = 0
        self.lightstep = 0
        self.popup.dismiss()

        self.on_start()
        print("New Level", self.N)


    def update_grid(self, *args):
        if self.lightstep == self.num_iter-1:
            # End game
            self.end_game_popup()
            self.clock.cancel()

        elif self.timestep%3==1:
            self.clicked = False
            self.lightstep += 1
            self.highlight = self.tiles[self.random_order[self.lightstep]]
            self.play_sound()
            self.ids[self.highlight].highlight_tile()

        self.timestep += 1

    def update_score(self, dscore):
        # Check if player was correct/incorrect and increase/decrease their score accordingly.
        if self.clicked == False:
            if self.random_order[self.lightstep] == self.random_order[self.lightstep - self.N] and self.N < self.lightstep:
                self.score += dscore
            else:
                self.score -= dscore
        self.clicked = True

    def play_sound(self):
        sound = SoundLoader.load('p.wav')
        sound.play()
        print(sound)




class NBackApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        self.game = NBackGame()
        self.game.start_game_popup()
        return self.game

    def printIDs(self):
        print(self.root.ids)




NBackApp().run()