import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

class OperativeClass(AnchorLayout):
	def __init__(self,**kwargs):
		super(OperativeClass,self).__init__(**kwargs)
		self.instancia = InsiderButton()
		self.add_widget(self.instancia)

class InsiderButton(AnchorLayout):
	pass

class AnchorLayoutApp(App):
	def build(self):
		Window.size = [300,500]
		return OperativeClass()

if __name__=="__main__":
	AnchorLayoutApp().run()