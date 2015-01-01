import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class HelloWorld(App):
	def build(self):
         f = FloatLayout()
         s = Scatter()
         l = Label(text="Hello World!",
				   font_size=50,
                   pos=(200,200))
              
         f.add_widget(s)
         s.add_widget(l)
         return f
    
if __name__ == '__main__':
    HelloWorld().run()
