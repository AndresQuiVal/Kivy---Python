import kivy
kivy.require("1.9.1")

from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


class mainCalculator(GridLayout):
					#en la listView pusimos Object properties, pero an datos numericos no se puede realizar solo al
		 						#los string o caracteres de texto, tal como ya mencione en la list view!
	def calculate(self, instance):
		try:
			self.display.text = str(eval(instance)) 

		except:
			self.display.text = "Error!"

	def appendFunction(self, num):
		self.display.text += num

class CalculatorApp(App):
	def build(self):
		Window.clearcolor = [1,0,0,1]
		return mainCalculator()

if __name__=="__main__":
	CalculatorApp().run()