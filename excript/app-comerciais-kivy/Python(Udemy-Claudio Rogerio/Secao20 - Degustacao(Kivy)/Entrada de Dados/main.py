#conding: utf-8

from kivy.app import App
from kivy.uix.textinput import TextInput

def build ():
    return TextInput(text="Componete TextInput")

janela = App()
janela.build = build
janela.run()

