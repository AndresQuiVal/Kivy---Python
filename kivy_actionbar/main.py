import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar, ActionItem

class OperativeClass(ScreenManager):
	def __init__(self, **kwargs):
		super(OperativeClass, self).__init__()
		self.instance1 = CurrentScreen(self)
		self.instance2 = SecondScreen(self)
		screen1 = Screen(name="current_screen")
		screen2 = Screen(name="second_screen")
		screen1.add_widget(self.instance1)
		screen2.add_widget(self.instance2)
		self.add_widget(screen1)
		self.add_widget(screen2)

	def print_it(self):
		print("Hello World!")

class CurrentScreen(BoxLayout):
	def __init__(self,operative_class,**kwargs):
		super(CurrentScreen, self).__init__()
		self.operative_class = operative_class

class SecondScreen(GridLayout):
	def __init__(self,operative_class,**kwargs):
		super(SecondScreen, self).__init__()
		self.operative_class = operative_class
		#self.btn_personalize = PersonalizeButton(self)

	def call_operative_class2(self):
		self.operative_class.print_it()

	def open_dropMenu(self):
		self.instance = DropMenu()
		if self.instance.open:
			print("Open!")

	def print_it(self):
		print("HelloWorld!")

class DropMenu(DropDown, ActionItem):
	pass

class PersonalizeButton(Button, ActionItem):
	pass

class ActionBarApp(App):
	def build(self):
		return OperativeClass()

	def print_text(self):
		print("HolaMundo!")
if __name__=="__main__":
	ActionBarApp().run()