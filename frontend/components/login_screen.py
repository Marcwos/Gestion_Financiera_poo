from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):
    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        if username == "user" and password == "pass":
            self.ids.message.text = "¡Inicio de sesión exitoso!"
        else:
            self.ids.message.text = "Nombre de usuario o contraseña incorrectos."

class MainApp(MDApp):
    def build(self):
        Builder.load_file('frontend/components/login_screen.kv')
        from kivy.uix.screenmanager import ScreenManager
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        return sm

if __name__ == "__main__":
    MainApp().run()
