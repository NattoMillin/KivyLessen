from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#new!!
from kivy.core.window import Window

# Ser the app size
Window.size = (500,700)


Builder.load_file('culc.kv') #　path形式で指定可能。

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = ''

class AwsomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()