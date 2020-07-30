import kivy
kivy.require("1.9.1")

from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder



class ClassApplication(FloatLayout):
	def __init__(self, **kwargs):
		super(ClassApplication, self). __init__(**kwargs)
		self.label=Label(text="My Inc!", font_size="35sp", pos=[-265,250], bold=True, color=[0,0,0,1])
		self.add_widget(self.label)
		self.label=Label(text="Andres Quiroz Valdovinos    |    Ingeniero de Software   |   60,000 Pesos Mensuales!",
			pos=[-80, 180])
		self.add_widget(self.label)
		self.finalLabel=Label(text="Andres Quiroz Murguia    |    Ingeniero Civil   |   60,000 Pesos Mensuales!",
			pos=[-116, 130])
		self.add_widget(self.finalLabel)
		#self.editLabel=Label(text="Edit!", color=[0,0,1,1], pos=[270,180], underline=True)
		#self.add_widget(self.editLabel)
		self.counter=0
		self.counter+=10
		for a in range(180, 120, -53):
			self.editLabel=Label(text="[ref=Edit!]Edit![/ref]", color=[0,0,1,1], pos=[270,a], underline=True, markup=True)
			self.editLabel.bind(on_ref_press=self.anotherMethod)
			self.add_widget(self.editLabel)
			
		#self.button=Button(text="New Person +", pos=[-300,-300], background_color=[1,0,1,1], size=[0.2,0.2])
		#self.add_widget(self.button)
		#self.anotherButton=Button(text="Delete Person -", pos=[300,-300], background_color=[1,0,1,1], size=(1,.2))
		#self.add_widget(self.anotherButton)

	def anotherMethod(self, instance, value):
		print("Your Command Is On Function!")

class MainWindow(Screen):
	pass

class SecondWindow(Screen):
	pass

class ThirdWindow(Screen):
	pass

class ScreenManagment(ScreenManager):
	pass

file = Builder.load_file("kvfile.kv")

class MyApp(App):
	def build(self):
		Window.clearcolor = [1,1,0,1]
		return file

if __name__=="__main__":
	MyApp().run()


#