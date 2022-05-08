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
        self.ids.calc_input.text = '0'
    
    # Create Function to remove last character
    def remove(self):
        prior = self.ids.calc_input.text
        # Remove The last item in the textBox
        prior = prior[:-1]
        # Output back the textbox
        self.ids.calc_input.text = prior

    # Create function to make text box positive or negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # Test to see if there's a -sign already
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def button_press(self, button):
        # create a veriable that contains whatever was in textbox alradey
        prior = self.ids.calc_input.text

        # Test for error first
        if "Error" in  prior:
            prior = '0'

        # determine if 0 is setting there
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
        
    # Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        # Split out text box by
        num_list = prior.split("+")
        
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            # Add a decimal to the end of the text
            prior = f'{prior}.'
            self.ids.calc_input.text = prior


    def math_sign(self, sign):
        # create a variable that contains whatever was ub textbox allrady
        prior = self.ids.calc_input.text
        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.calc_input.text
        # Error Handling
        try:
            # Evaluate the from the text
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
        '''
        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            # loop thru our list
            for number in num_list:
                answer = answer + float(number)
        
        self.ids.calc_input.text = str(answer)
        '''
        
class AwsomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()