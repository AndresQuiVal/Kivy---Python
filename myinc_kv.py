import kivy 
kivy.require("1.9.1")

from kivy.app import App
#from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget

class MainWindow(Widget):
	pass

class mainFilekivy(App):
	def build(self):
		return MainWindow()


if __name__=="__main__":
	mainFilekivy().run()