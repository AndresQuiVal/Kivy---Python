import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.textinput  import TextInput

class MyApplication(App):
    def build(self):
        return GridLayout()

if __name__=="__main__":
    MyApplication().run()

#editDojo=GridLayout(cols=2)
#**Label**
#createMonLabel=Label(text="UserName", size_hint_x=20)
#editDojo.add_widget(createMonLabel)
#**Text Input**
#myInput=TextInput(size_hint_x=20)#size_hint=[20, 5])
#editDojo.add_widget(myInput)
