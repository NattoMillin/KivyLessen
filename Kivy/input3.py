
from re import MULTILINE
from turtle import textinput
import kivy
from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout #2
from kivy.uix.textinput import TextInput #2
from kivy.uix.button import Button #2
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


        #//----------------------------------------------------------------------------------
        # 全開で作ったものをより、簡潔に書く。
        # クラスの中身を大幅に変更する。

        # Classの継承がWidgetに代わり、kvファイルを作成します。
        #//----------------------------------------------------------------------------------



class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f'hello {name}, you like {pizza} pizza, and your favorite color is {color}')
        # print screen
        # self.add_widget(Label(text=f'hello {name}, you like {pizza} pizza, and your favorite color is {color}'))
        print(f'hello {name}, you like {pizza} pizza, and your favorite color is {color}')

        # clera the input Boxs
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()