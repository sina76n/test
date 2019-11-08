from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.theming import ThemeManager
from kivy.lang import Builder



kv = """
ScreenManager:
    Screen:
        NavigationLayout:
            id: nav_layout

            MDNavigationDrawer:
                id: nav_drawer

                NavigationDrawerSubheader:
                    text: "Menu:"

                NavigationDrawerIconButton:
                    text: "Home"
                    on_release: 

            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: app.mainpage_title
                    md_bg_color: app.theme_cls.primary_color
                    background_palette: 'Primary'
                    background_hue: '500'
                    elevation: 10
                    left_action_items:
                        [ ['dots-vertical', lambda x: nav_layout.toggle_nav_drawer()] ]
                BoxLayout:
                    orientation: 'vertical'
                    MDFlatButton:
                        text: app.reshaper("یشسیشسی")

                    MDTextField:
                        base_direction : 'rtl'



"""
class PongApp(App):

    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'DeepPurple'
    title = "AA"
    theme_cls.theme_style = "Light"
    mainpage_title = "Ask Answer"

    def reshaper(self,name):
        import bidi.algorithm
        import arabic_reshaper
        name = str(name)
        name = arabic_reshaper.reshape(name)
        name = bidi.algorithm.get_display(name)
        return name

    def build(self):
        main_kv = Builder.load_string(kv)
        return main_kv


if __name__ == '__main__':
    PongApp().run()