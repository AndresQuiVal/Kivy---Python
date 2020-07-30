import kivy                                # ------- 	FAILIURE!!!    ------
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window

class ScreenManagement(ScreenManager):
	def __init__(self,**kwargs):
		super(ScreenManagement, self).__init__(**kwargs)
		transition = SlideTransition()
		screen1 = Screen1()
		screen2 =  Screen2()
		self.add_widget(screen1)
		self.add_widget(screen2)


class OperativeClass(BoxLayout):
	def __init__(self,**kwargs):
		super(OperativeClass, self).__init__(**kwargs)
		#self.other = OperativeSecond()
		self.operational = OperationalAdd()
		self.add_widget(OperationalAdd())

	def print_it(self):
		print("Edit Button On!!")
		self.current = "screen2"

	def oper_main(self,*args):
		self.add_widget(OperationalAdd())

class OperativeSecond(BoxLayout):
	def __init__(self,**kwargs):
		super(OperativeSecond, self).__init__(**kwargs)
		self.operation = OperativeClass()
		self.operational = OperationalAdd()

	def modify_label(self,*args):
		variable_texto = self.display.text
		self.operation.ids.changer.text = variable_texto

	def oper(self,*args):
		self.operation.oper_main()
		#self.operation.add_widget(OperationalAdd())

class OperationalAdd(BoxLayout):
	def change_screen(self,*args):
		self.current = "screen2"


class Screen1(Screen):
	def __init__(self,**kwargs):
		super(Screen1, self).__init__(**kwargs)
		self.name = "screen1"
		#self.operation = OperativeClass()
		self.add_widget(OperativeClass())

class Screen2(Screen):
	def __init__(self,**kwargs):
		super(Screen2, self).__init__(**kwargs)
		self.name = "screen2"
		#self.other = OperativeSecond()
		self.add_widget(OperativeSecond())

class ScreenTextApp(App):
	def build(self):
		Window.size = [300,500]
		return ScreenManagement()

if __name__=="__main__":
	ScreenTextApp().run()