#!/home/hal/Project/gui/bin/python

'''
    A simple hello world window.
'''

from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder

Builder.load_string('''

<ExampleRV>:

    viewclass: 'Button'

    RecycleBoxLayout:

        size_hint_y: None

        height: self.minimum_height

        orientation: 'vertical'

''')


class ExampleRV(RecycleView):
    '''
        blah
    '''
    def __init__(self, **kwargs):
        '''
            blah
        '''
        super(ExampleRV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(20)]


class RecycleApp(App):
    '''
        blah
    '''

    def build(self):
        '''
            blah
        '''
        return ExampleRV()


RecycleApp().run()
