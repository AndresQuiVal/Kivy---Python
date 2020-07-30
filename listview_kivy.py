import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty

class StudentList(ListItemButton):
	pass

class MainClass(BoxLayout):
	studentName = ObjectProperty() # id para referir a mi textinput en mi archivo kv, al igual que en la calculadora cumple el									
	lastName = ObjectProperty()    #   mismo functionamiento, tanto el id en la clase base como el object property 
	listView = ObjectProperty()

	def newStudents(self):
		# Get the student name from the TextInputs
		studentList = self.studentName.text + " " + self.lastName.text 
 
        # Add the student to the ListView
		self.listView.adapter.data.extend([studentList]) # llamamos al adapter para agregar info! 
 
        # Reset the ListView
		self.listView._trigger_reset_populate() # RESETEAMOS LA LISTA


	def deleteStudents(self):
		# If a list item is selected
		if self.listView.adapter.selection:

            # Get the text from the item selected
			studentSelected = self.listView.adapter.selection[0].text # llamamos al adapter para seleccionar info!
 
            # Remove the matching item
			self.listView.adapter.data.remove(studentSelected) #llamamos al adapter para eliminar info!

            # Reset the ListView
			self.listView._trigger_reset_populate() # RESETEAMOS LA LISTA

	def modifyStudents(self):
		 # If a list item is selected
		if self.listView.adapter.selection:
 
            # Get the text from the item selected
			studentSelected = self.listView.adapter.selection[0].text # llamamos al adapter para seleccionar info!
 
            # Remove the matching item
			self.listView.adapter.data.remove(studentSelected) #llamamos al adapter para eliminar info!

            # Get the student name from the TextInputs
			studentList = self.studentName.text + " " + self.lastName.text 
 
            # Add the updated data to the list
			self.listView.adapter.data.extend([studentList]) # llamamos al adapter para agregar info!
 
            # Reset the ListView
			self.listView._trigger_reset_populate() # RESETEAMOS LA LISTA

class ListViewApp(App):
	def build(self):
		return MainClass()

if __name__=="__main__":
	ListViewApp().run()
