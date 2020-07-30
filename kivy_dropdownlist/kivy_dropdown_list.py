import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout

class OperativeClass(BoxLayout):
	def __init__(self, **kwargs):
		super(OperativeClass, self).__init__()
		self.drop_menu = DropMenu()
		self.instance = OperativeButton()
		#self.add_widget(self.drop_menu)
		self.edit_btn = Button(text="Open DropMenu", on_press=self.drop_menu.open, size_hint=[None,None], size=[300,100])
		self.add_widget(self.instance)
		self.add_widget(self.edit_btn)

class DropMenu(DropDown):
	pass
	"""def __init__(self, **kwargs):
		super(DropMenu, self):__init__()"""

	#def __init__(self,**kwargs):
#		super(DropMenu, self).__init__()
		

class OperativeButton(BoxLayout):
	pass

class MyApp(App):
	def build(self):
		return OperativeClass()

if __name__=="__main__":
	MyApp().run()