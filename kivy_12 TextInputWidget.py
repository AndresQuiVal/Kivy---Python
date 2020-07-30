import kivy
kivy.require("1.10.1")

from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.label import Label 
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Widget(GridLayout):

	def __init__(self, **kwargs):
		super(Widget, self). __init__(**kwargs)
		self.textinput = TextInput(text='Hello world', multiline=False)
		self.textinput.bind(on_text_validate=self.on_enter)
		self.add_widget(self.textinput)

	def on_enter(self, instance):
		print("User pressed enter in", instance)

class MyApp(App):
	def build(self):
		return Widget()

if __name__=="__main__":
	MyApp().run()