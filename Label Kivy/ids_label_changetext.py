import kivy
kivy.require("1.9.1")

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout


class OperativeClass(BoxLayout):

	def election(self,choice):
		var="You Have Selected"+choice
		self.ids.operation.text = var 

class IdsChangeApp(App):
	def build(self):
		title = "Hello World"
		return OperativeClass()

if __name__=="__main__":
	IdsChangeApp().run()