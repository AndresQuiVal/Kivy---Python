import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.popup import Popup 

class PopClass(Popup):
	pass

class OperativeClass(BoxLayout):
	def __init__(self, **kwargs):
		super(OperativeClass, self).__init__()
		self.instance = PopClass()

class PopupApp(App):
	def build(self):
		return OperativeClass()

if __name__=="__main__":
	PopupApp().run()