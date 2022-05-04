
from re import MULTILINE
from turtle import textinput
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('whatever.kv') #　path形式で指定可能。

        #//----------------------------------------------------------------------------------
        # ボタンの色を変えるぜ！！
        # kivyのRGBの指定方法は、0～1の間の数値で指定する必要がある。
        # 例えば、238R値だった場合、233/255　で指定する。
        # background_normal: '' を指定しないと色がブラック系になる。
        #//----------------------------------------------------------------------------------



class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f'hello {name}, you like {pizza} pizza, and your favorite color is {color}')

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class AwsomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    AwsomeApp().run()