import kivy
kivy.require("1.10.1")

from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.widget import Widget
from kivy.lang import Builder


class MainScreen(Screen):
	pass

class SecondScreen(Screen):
	pass

class ScreenManage(ScreenManager):
	pass

myFile=Builder.load_file("ScreenManager.kv")

class ScreenManager(App):
	def build(self):
		return myFile

if __name__=="__main__":
	ScreenManager().run()