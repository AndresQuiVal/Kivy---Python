import kivy
kivy.require("1.10.1")

from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.widget import *

class MyApp(App):
	def build(self):
		return Label()

if __name__=="__main__":
	MyApp().run()

