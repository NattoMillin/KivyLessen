from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#new!!
from kivy.core.window import Window

# Ser the app size
Window.size = (500,700)


Builder.load_file('culc2.kv') #　path形式で指定可能。

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = ''
    
    def button_press(self, button):
        # create a veriable that contains whatever was in textbox alradey
        prior = self.ids.calc_input.text

        # deternube if 0 is setting there
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
        
    #create addition function
    def add(self):
        # create a variable that contains whatever was ub textbox allrady
        prior = self.ids.calc_input.text
        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}+'
    def subtract(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}-'
    def multiply(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}X'
    def divide(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}/'
    def equals(self):
        prior = self.ids.calc_input.text

        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            # loop thru our list
            for number in num_list:
                answer = answer + int(number)
        
        self.ids.calc_input.text = str(answer)

        
class AwsomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()