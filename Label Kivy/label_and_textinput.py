import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button

class OperativeClass(BoxLayout):
	def __init__(self,**kwargs):
		super(OperativeClass, self).__init__()
		self.instance = EditableLabel(self)
		#self.var = self.ids.display.text

	def add_label(self):
		self.add_widget(EditableLabel(self))

class EditableLabel(BoxLayout):
	def __init__(self,mainwid,**kwargs):
		super(EditableLabel, self).__init__()
		self.mainwid = mainwid
		self.var2 = self.mainwid.ids.display.text
		self.button_editable = Label(markup=True, text="[size=30][b]Topic[/b][/size]" + self.var2, size=[100, 100], text_size= self.size)
		self.add_widget(self.button_editable)


class InputLabelApp(App):
	def build(self):
		Window.size = [300,500]
		return OperativeClass()

if __name__=="__main__":
	InputLabelApp().run()