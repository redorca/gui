#!/home/hal/Project/gui/bin/python
'''
    blah
'''


from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button


class ClockExample(App):
    '''
        blah
    '''

    i = 0

    def build(self):
        '''
            blah
        '''
        self.mybtn = Button(text='Number of Calls')
        Clock.schedule_interval(self.clock_callback, 2)
        return self.mybtn

    def clock_callback(self, dt):
        '''
            blah
        '''

        self.i += 1
        self.mybtn.text = "Call = %d"%self.i


ClockExample().run()
