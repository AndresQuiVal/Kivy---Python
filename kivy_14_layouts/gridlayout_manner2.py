import kivy           #Agregar los Widgets desde el archivo.py y su diseño en en archivo.kv
kivy.require("1.9.1")

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window


class OperativeClass(BoxLayout):
	def __init__(self,**kwargs):
		super(OperativeClass, self).__init__(**kwargs)
		self.first_instance = RedBox()
		self.second_instance = BlueBox()
		self.third_instance = GreenBox()

		self.first_instance.add_widget(self.second_instance)
		self.first_instance.add_widget(BlueBox())
		self.first_instance.add_widget(GreenBox())
		self.add_widget(self.first_instance)

class RedBox(BoxLayout):
	pass

class BlueBox(BoxLayout):
	pass

class GreenBox(BoxLayout):
	pass
	

class BoxLayout2App(App):
	def build(self):
		return OperativeClass()

if __name__=="__main__":
	BoxLayout2App().run()