import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class OperativeClass(GridLayout):
	def __init__(self,**kwargs):
		super(OperativeClass,self).__init__(**kwargs)
		self.command_on = FirstLayout()

	def on_command(self):
		self.add_widget(FirstLayout())
		print("New Person Added Sucesfully!")

class FirstLayout(GridLayout):

	def print_result(self):
		print("Hello World!")

class AddRectangleApp(App):
	def build(self):
		Window.size = [300,500]
		return OperativeClass()

if __name__=="__main__":
	AddRectangleApp().run()