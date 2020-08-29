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

label_text = '[u][color=ff0066][b]Better days[/b][/color]'\
             ' are coming; They are called '\
             '[i][color=ff9933]Saturday[/i] and '\
             '[i]Sunday[/color][/i][/u]'

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
        self.key_words["text"] = label_text
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
        self.key_words["text"] = label_text
        self.key_words["markup"] = True
        # self.key_words["background_color"] = (155, 0, 51, 53)
        self.key_words["size_hint"] = (.15, .18)
        self.key_words["font_size"] = "20"
        super().__init__()

    def build(self):
        return Label(**self.key_words)


class ButtonUp(App, BoxLayout):
    '''
        The window generator.
    '''
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

        return mybtn
        # return self


class Generic(App):
    '''
        Wrapper for building multiple types of windows.
    '''

    def __init__(self, appname="label", text="Hello World"):
        '''
            Blah blah blah.
        '''
        self.__build__ = 0
        if appname == "button":
            from kivy.uix.button import Button
            self.__build__ = Button
            self.set_args = self.__keywords_button__
        elif appname == "label":
            from kivy.uix.label import Label
            self.__build__ = Label
            self.set_args = self.__keywords_label__

        self.key_words = dict()
        self.key_words["text"] = text
        self.set_args()
        super().__init__()

    def __keywords_button__(self):
        self.key_words["background_color"] = (155, 0, 51, 53)
        self.key_words["size_hint"] = (.25, .18)
        self.key_words["font_size"] = "30"
        self.key_words["markup"] = True

    def __keywords_label__(self):
        self.key_words["text"] = '[u][color=ff0066][b]Better days[/b][/color]'\
                                 ' are coming; They are called '\
                                 '[i][color=ff9933]Saturday[/i] and '\
                                 '[i]Sunday[/color][/i][/u]'
        self.key_words["markup"] = True

    def build(self):
        '''
            Build the app type specified when instantiating the class object.
        '''
        mybtn = self.__build__(**self.key_words)
        mybtn.bind(on_press=partial(self.disable, mybtn))
        mybtn.bind(on_press=partial(self.update, mybtn))
        return self

    def kw(self):
        print("Key Words ", self.key_words)


# app = Generic("label", text="Hello Kivy World")
# app = Generic("button", text="Hello Ivy World")
# app = ButtonUp()
# app.run()
# Generic().run()
# LabelIt().run()
ButtonUp().run()
# KivyButton().run()
