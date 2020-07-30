import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class operClass(BoxLayout):
	pass

class mainApp(App):
	def build(self):
		title = "BoxLayout App!"
		Window.size = [300,500]
		return operClass()

if __name__=="__main__":
	mainApp().run()