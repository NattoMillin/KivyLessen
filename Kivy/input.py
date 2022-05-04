
from re import MULTILINE
from turtle import textinput
import kivy
from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout #2
from kivy.uix.textinput import TextInput #2
from kivy.uix.button import Button #2

class MyGridLayout(GridLayout):
    # initialize infinite Keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set coumns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="Name: "))
        # Add Input Box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite Pizza: "))
        # Add Input Box
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favorite Color: "))
        # Add Input Box
        self.Color = TextInput(multiline=False)
        self.add_widget(self.Color)

        # Create a Submit Button
        self.submit = Button(text="Submit",font_size=32)
        # bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.Color.text

        # print(f'hello {name}, you like {pizza} pizza, and your favorite color is {color}')
        # print screen
        self.add_widget(Label(text=f'hello {name}, you like {pizza} pizza, and your favorite color is {color}'))

        # clera the input Boxs
        self.name.text = ""
        self.pizza.text = ""
        self.Color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()