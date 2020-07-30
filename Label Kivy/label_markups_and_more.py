import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class OperativeClass(BoxLayout):
	def print_it(self):
		print("Hello World!")

class LabelFormatApp(App):
	def build(self):
		title = "Markup Text Label Operators"
		return OperativeClass()

if __name__=="__main__":
	LabelFormatApp().run()