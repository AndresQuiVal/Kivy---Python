import kivy
kivy.require("1.10.1")

from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.button import Button
from kivy.uix.label import Label

class CursorApplication(Widget):
	def __init__(self, **kwargs):
		super(CursorApplication, self). __init__(**kwargs)
		with self.canvas:
			self.editLabel=Label(text="Be Free To Draw!\nBy Andres_QuiVal", pos=[350, 500])
			self.clearButton=Button(text="Clear Window!", size=[800, 60], pos=[0, 0], background_color=[0,1,0,1])
		self.add_widget(self.clearButton)
		self.add_widget(self.editLabel)
		super 
	def on_touch_down(self, touch):
		#print(touch)
		with self.canvas:
			touch.ud["line"] = Line(points=(touch.x, touch.y))
	def on_touch_move(self, touch):
		#print(touch)
		touch.ud["line"].points+=(touch.x, touch.y)

	#def on_touch_up(self, touch):
	#	print("Final Touch", touch)

class TouchApplication(App):
	def build(self):
		return CursorApplication()

if __name__=="__main__":
	TouchApplication().run()