from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

fatorEscala = 1.4
fe = fatorEscala
Window.size = (360*fe, 640*fe)



class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]

class TelaPrincipal(Screen):
    pass

class MeuAplicativoApp(MDApp):
    def build(self):
        return 



MeuAplicativoApp().run()