from kivy.lang import Builder
from kivymd.app import MDApp
from  kivymd.uix.label import MDLabel

kv = '''
<LoginApp>
MDFloatLayout:

    md_bg_color: 1, 1, 1, 1
    Image: 
        source:"userlogin.png"
        pos_hint: .5,.5
    MDLabel:
        text: "Log In"
        pos_hint:{"center_x: .5","center_y: .5"}
        halign: "center"
        font_name: "Poppins-SemiBold.ttf"
        font_size: "40sp"
        theme_text_color: "Costom" 
    MDFloatLayout:
        size_hint: .85, .08
        pos_hint: {"center_x: .5","center_y: .5"}
        canvas:
            Color:
                rgb:(223/255, 237/255, 240/255, 0)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [(40, 40), (40, 40), (20, 20), (20, 20)] 
    TextInput:
        hint_text: "Username"
        size_hint: 1, None
        pos_hint: {"center_x: .5","center_y: .5"}
        multiline: False
        cursor_color:   
        cursor_width:"2sp" 
        background_color:
        padding: 10
        font_name: "Poppins-SemiBold.ttf"
        font_size: "18sp"
               
    MDFloatLayout:
        size_hint: .85, .08
        pos_hint: {"center_x: .5","center_y: .28"}
        canvas:
            Color:
                rgb:(223/255, 237/255, 240/255, 0)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [(40, 40), (40, 40), (20, 20), (20, 20)] 
    TextInput:
        hint_text: "Password"
        password: True
        size_hint: 1, None
        pos_hint: {"center_x: .5","center_y: .5"}
        multiline: False
        cursor_color:   
        cursor_width:"2sp" 
        background_color:
        padding: 10
        font_name: "Poppins-SemiBold.ttf"
        font_size: "18sp" 
    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_y: .5"}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field.password = False if text_field.password is True else True

    MDTextButton:
        text:"Forget you password?"
        font_name: "Poppins-Regular.tff"
        theme_text_color: "Custom"
        text_color:
        pos_hint:{"center_y: .5","center_y: .21"}
    Button:
        id: btn
        text: "LOGIN"
        font_name:"Poppins-Regular.ttf"
        font_size:"20sp"
        size_hint:.5, .08 
        pos_hint: {"center_x: .5","center_y: .12"}
        background_color: 0, 0, 0, 0
        canvas.before:
            color:
                rgd:(223/255, 237/255, 240/255, 0)
            RoundedRectangle: 
                size: self.size
                pos: self.pos
                radius: [(40, 40), (40, 40), (20, 20), (20, 20)]    
                
          
                    
'''


class LoginApp(MDApp):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    LoginApp().run()
