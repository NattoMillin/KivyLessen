
from re import MULTILINE
from turtle import textinput
import kivy
from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout #2
from kivy.uix.textinput import TextInput #2
from kivy.uix.button import Button #2


        #//----------------------------------------------------------------------------------
        # グリッドレイアウトでレイアウトの中にレイアウトを定義し、
        # その中にラベルとインプットボックスを設置
        # 設置した”top_grid（Columnは2行）”を元のインスタンスに加えることで、定義できた。
        #//----------------------------------------------------------------------------------



class MyGridLayout(GridLayout):
    # initialize infinite Keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set coumns
        self.cols = 1
        self.row_force_default=True 
        self.row_default_height=120 
        self.col_force_default=True
        self.col_default_width=200

        # Create a second gridlayout
        self.top_grid = GridLayout(
            row_force_default=True, 
            row_default_height=40, 
            col_force_default=True, 
            col_default_width=100
            )
        self.top_grid.cols = 2

        # Add widgets
        self.top_grid.add_widget(Label(text="Name: "# , 
        #    size_hint_y = None,
        #    height = 50, 
        #    size_hint_x = None, 
        #    width = 200
            ))
        # Add Input Box
        self.name = TextInput(multiline=False #, 
        #    size_hint_y = None,
        #    height = 50, 
        #    size_hint_x = None, 
        #    width = 400
            )
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favorite Pizza: "))
        # Add Input Box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Favorite Color: "))
        # Add Input Box
        self.Color = TextInput(multiline=False)
        self.top_grid.add_widget(self.Color)

        # Add the new tp_grid to our app
        self.add_widget(self.top_grid)

        # Create a Submit Button
        self.submit = Button(text="Submit", 
            font_size=32 , 
            size_hint_y = None,
            height = 50, 
            size_hint_x = None, 
            width = 200
            )
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