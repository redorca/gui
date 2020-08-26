
'''
    A simple hello world window.
'''

from kivy.app import App
from kivy.uix.label import Label


class FirstKivy(App):
    '''
        The window generator.
    '''

    def build(self):
        return Label(text="Hello Kivy World!")


FirstKivy().run()
