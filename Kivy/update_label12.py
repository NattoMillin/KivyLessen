
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#new!!

Builder.load_file('update_label.kv') #　path形式で指定可能。

        #//----------------------------------------------------------------------------------
        # 
        #//----------------------------------------------------------------------------------

class MyLayout(Widget):
    def press(self):
        # Create vatiables for our widget
        name = self.ids.name_imput.text
        # update the label
        self.ids.name_label.text = f'hello! {name}!'
        # clear input box
        self.ids.name_imput.text = ""

class AwsomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()