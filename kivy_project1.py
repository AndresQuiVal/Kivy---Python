import kivy
kivy.require("1.9.1")

from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder
from kivy.graphics import Line
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class CursorApplication(Widget):
	def on_touch_down(self, touch):
		#print(touch)
		with self.canvas:
			touch.ud["line"] = Line(points=(touch.x, touch.y))

	def on_touch_move(self, touch):
		#print(touch)
		touch.ud["line"].points+=(touch.x, touch.y)

class MainScreen(Screen):
	pass

class SecondScreen(Screen):
	pass

class ScreenManage(ScreenManager):
	pass

myKVFile = Builder.load_file("FirstAndroidApp.kv")

class FirstAndroidApp(App):
	def build(self):
		return myKVFile

if __name__=="__main__":
	FirstAndroidApp().run()