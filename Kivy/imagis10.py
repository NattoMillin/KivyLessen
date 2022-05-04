
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#new!!
#from kivy.uix.images import images

Builder.load_file('imagis.kv') #　path形式で指定可能。

        #//----------------------------------------------------------------------------------
        # 
        #//----------------------------------------------------------------------------------

class MyLayout(Widget):
    pass

class AwsomeApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1) # kvファイルのcanvasが優先されるということ。
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()