import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

class widgetClass(Widget):
	pass

class MySecondApp(App):
	def build(self):
		return widgetClass()

if __name__=="__main__":
	MySecondApp().run()
#pos: 2, 71