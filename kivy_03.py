import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class operativeFunction(GridLayout):
	
	def __init__(self, **kwargs):
		super(operativeFunction, self). __init__(**kwargs)
		self.cols=2 
		self.rows=4
		self.widgetlab=Label(text="hello World")
		self.add_widget(self.widgetlab)
		self.widgetbut=Button(text="Send!", size_hint=[.2,.2], on_release=self.anotherMethod)
		self.add_widget(self.widgetbut)
		self.labelWidget=Label(text="Username:")
		self.add_widget(self.labelWidget)
		self.txtInput=TextInput(multiline=False, password=True, password_mask="°")
		self.add_widget(self.txtInput)
		self.textMessage="HolaMundo!"

	def anotherMethod(self, instance):
		if (self.txtInput.select_all())==(self.textMessage):
			print("Contraseña Correcta!")	
		

class myApp(App):
	def build(self):
		return operativeFunction()

if __name__=="__main__":
	myApp().run()