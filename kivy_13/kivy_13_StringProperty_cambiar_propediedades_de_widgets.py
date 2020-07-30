import kivy
kivy.require("1.9.1")

from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.core.window import Window

class ObjectificationClass(GridLayout):
	def __init__(self,**kwargs):
		super(ObjectificationClass, self).__init__(**kwargs)
		self.default = Call_Button()
	
	change_var = StringProperty("DefaultTxt")

	def change_text(self):
		if self.change_var == "Default Txt":
			self.change_var = "Text Changed!"
		else:
			self.change_var = "Default Txt"

	def agregarButton(self):
		self.default

class Call_Button(GridLayout):
	pass

class StringPropertyApp(App):
	def build(self):
		Window.size = [300, 200]
		Window.color  = [1,0,0,1]
		return ObjectificationClass()

if __name__=="__main__":
	StringPropertyApp().run()
