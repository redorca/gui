#!/usr/bin/python3
'''
    A simple hello world window.
'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial

Builder.load_string("""

<KivyButton>:

    Button:

        text: "Hello Button!"

        size_hint: .22, .22

        Image:

            source: 'images/index.png'

            center_x: self.parent.center_x

            center_y: self.parent.center_y 
  
""")


class KivyButton(App, BoxLayout):
    '''
        sljdfalkjfdlkj
    '''
    def __init__(self):
        self.key_words = dict()
        # self.key_words["text"] = "blah blah blah"
        self.key_words["text"] = "[u][color=ff0066][b]Better days[/b][/color] are coming; They are called [i][color=ff9933]Saturday[/i] and [i]Sunday[/color][/i][/u]"
        self.key_words["markup"] = True
        self.key_words["background_color"] = (155, 0, 51, 53)
        self.key_words["size_hint"] = (.25, .18)
        self.key_words["font_size"] = "30"
        # self.key_words[""] =
        # self.key_words[""] =
        # self.key_words[""] =

        super().__init__()

    def build(self):
        return self


class LabelIt(App):
    '''
        The window generator.
    '''
    def __init__(self):
        # self.text = "Hello Kivy World"
        self.key_words = dict()
        # self.key_words["text"] = "blah blah blah"
        # self.key_words["text"] = "[u][color=ff0066][b]Better days[/b][/color] are coming; They are called [i][color=ff9933]Saturday[/i] and [i]Sunday[/color][/i][/u]"
        self.key_words["text"] = '[u][color=ff0066][b]Welcome[/b][/color] To [i][color=ff9933]Like[/i]Geeks[/color][/u]'
        self.key_words["markup"] = True
        # self.key_words["background_color"] = (155, 0, 51, 53)
        self.key_words["size_hint"] = (.15, .18)
        self.key_words["font_size"] = "20"
#   def __init__(self):
#       self.text="Hello Kivy World"
        super().__init__()

    def build(self):
        return Label(**self.key_words)


class ButtonUp(App, BoxLayout):
    '''
        The window generator.
    def __init(self):
        self.text = "Welcome to LikeGeeks"
        self.background_color = (155, 0, 51, 53)
        super().__init__()

    def disable(self, instance, *args):
        instance.disabled = True

    def update(self, instance, *args):
        instance.text = "I am disabled."

    def build(self):
        # return Button(text="Welcome to LikeGeeks",
        #               background_color=(155, 0, 51, 53))

        mybtn = Button(text="Click me to disable", pos=(300, 350),
                       background_color=(155, 0, 51, 53),
                       size_hint=(.25, .18))
        mybtn.bind(on_press=partial(self.disable, mybtn))
        mybtn.bind(on_press=partial(self.update, mybtn))

        # return mybtn
        return self
    '''
    def build(self):
        return self


class Generic(App):
    '''
        Wrapper for building multiple types of windows.
    '''

    def __init__(self, appname="label", text="Hello Kivy World"):
        '''
            Blah blah blah.
        '''
#       if appname == "button":
#           from kivy.uix.button import Button
#           self.build = Button()
#       elif appname == "label":
#           from kivy.uix.label import Label
#           self.build = Label

        self.build = Label()
        self.text = text
        super().__init__()

    def build(self):
        '''
            Build the app type specified when instantiating the class object.
        '''
#       return self.build(text=self.text)
        return Label(text="Hello Kivy World")


# app = Generic("button", text="Welcome to LikeGeeks")
# Generic().run()
LabelIt().run()
# ButtonUp().run()
# KivyButton().run()
