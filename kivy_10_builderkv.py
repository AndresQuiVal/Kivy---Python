import kivy
kivy.require("1.10.1")

from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

builder = Builder.load_file("BuilderApplication.kv")

class BuilderApplication(App):
	def builder(self):
		return builder()

if __name__=="__main__":
	BuilderApplication().run()