
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('color_label.kv') #　path形式で指定可能。

        #//----------------------------------------------------------------------------------
        # Labelを変更する。
        #//----------------------------------------------------------------------------------



class MyLayout(Widget):
    pass

class AwsomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()