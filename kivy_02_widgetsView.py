import kivy 

kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 4
        self.add_widget(Label(text='User Name', background_color="red"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.texto = "HolaMundo"
        self.boton=Button(text="Send!", on_press=anotherMethod)
        self.add_widget(self.boton)

    def anotherMethod(self, instance):
    	if self.password.select_all()==self.texto:
    		print("The Password is Correct")

class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()