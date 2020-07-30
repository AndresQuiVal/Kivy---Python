import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.switch import Switch

def pressedButton(instance):
	print("Hello World")

def myFunction(checkButton, value):
	if value==True:
		print("the Check IS Active")
	else:
		print("The Check Is Not Selected!")


def callback(instance):
 	print('The button {} is being pressed'.format(instance.text)) #<-- method do define on_pressed Button command!


hola=Widget()#***Button Widget**
btn1 = Button(text='Hello world 1', pos=[400,400])
btn1.bind(on_press=callback)
btn2 = Button(text='Hello world 2', pos=[300,300])
btn2.bind(on_press=callback)
hola.add_widget(btn1)
hola.add_widget(btn2)

#***Label Widget***
label=Label(text="Hola Mundo", pos=[500,500])
hola.add_widget(label)
#****CheckBox Widget***
checkButton=CheckBox(color=[0,1,0,1])
checkButton.bind(active=myFunction)
hola.add_widget(checkButton)
#***Slider***
slider=Slider(min=-100, max=100, value=0, orientation="vertical", pos=[400, 10])
hola.add_widget(slider)
#***Progress Bar***
myProgress=ProgressBar(value=50, max="100", pos=[500, 10])
hola.add_widget(myProgress)
#***Switch***
switch = Switch(pos=[500, 200])
switch.bind(active=callback)
hola.add_widget(switch)




class MyApp(App):
	def build(self):
		return hola


if __name__=="__main__":
	MyApp().run()
