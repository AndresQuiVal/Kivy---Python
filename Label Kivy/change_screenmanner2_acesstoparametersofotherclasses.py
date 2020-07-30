import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


class ManagerScreen(ScreenManager):
	def __init__(self, **kwargs):
		super(ManagerScreen, self).__init__()
		self.transition = SlideTransition()
		self.MainClass = MainClass(self)
		
		screen1 = Screen(name="screen1")
		screen1.add_widget(self.MainClass)
		self.add_widget(screen1)

	def unto_screen2(self):
		self.current = "screen2"

	def unto_screen1(self):
		self.current = "screen1"



class MainClass(BoxLayout):
	def __init__(self,mainwid,**kwargs):
		super(MainClass, self).__init__()
		self.mainwid = mainwid
		self.add_widget(AddButton(self))

class AddButton(Button):
	def __init__(self,mainwid,**kwargs):
		super(AddButton, self).__init__()
		self.mainwid = mainwid

	def change_screen(self):
		self.mainwid.unto_screen1()

class AccesEasyClassApp(App):
	def build(self):
		Window.size = [300,500]
		return ManagerScreen()


if __name__=="__main__":
	AccesEasyClassApp().run()