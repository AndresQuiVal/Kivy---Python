#***** Ejercicio De Clases
import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class LabelWidgets(GridLayout):
	def __init__(self, **kwargs):
		super(LabelWidgets, self). __init__(**kwargs)
		self.cols=2
		self.widget = Label(text='HelloWorld', markup=True)
		self.widget.bind(on_ref_press=self.print_it)
		self.add_widget(self.widget)
		self.anotherWidget=Label(text='[s]HelloWorld[/s]', markup=True)
		self.add_widget(self.anotherWidget)

	def print_it(self, instance, value):
		print('User clicked on', value)



class MyApp(App):
	 def build(self):
	 	return LabelWidgets()

if __name__=="__main__":
	MyApp().run()

#Font Text Properties -- Label Widget!

#[b][/b] <-- Bold!
#[i][/i] <-- Cursiva!
#[u][/u] <-- Underlined Text! 
#[s][/s] <-- Crossed Text!


#[b][/b] 
 #     <-- Activar texto en negrita
#[i][/i] 
 #     <-- Activar texto en cursiva
#[u][/u] 
#      <-- Texto subrayado
#[s][/s] 
#      <-- Tachado de texto
#[font=<str>][/font] 
#      <--- Cambiar la fuente
#[size=<integer>][/size] 
#      <-- Cambiar el tamaño de fuente
#[color="#"<color>][/color] 
#      <-- Cambiar el color del texto
#[ref=<str>][/ref]
#      <-- Añadir una zona interactiva. El cuadro de referencia + delimitación dentro de la referencia estará disponible enLabel.refs
#[anchor=<str>]
#      <-- Pon un ancla en el texto. Puede obtener la posición de su ancla dentro del texto conLabel.anchors
#[sub][/sub]
#      <-- Muestra el texto en una posición de subíndice en relación con el texto anterior.
#[sup][/sup]
 #     <-- Muestra el texto en una posición de superíndice en relación con el texto anterior.
