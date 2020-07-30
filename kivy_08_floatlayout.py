import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout  import FloatLayout

class FloatApplication(App):
	def build(self): 
		return FloatLayout()

if __name__=="__main__":
	FloatApplication().run()