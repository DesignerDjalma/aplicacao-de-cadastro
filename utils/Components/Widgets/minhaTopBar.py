from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivy.metrics import dp

import os


class MinhaTopBar(MDTopAppBar):
    def sairApp(self, *args):
        print("Saindo do App")
        self.app = MDApp.get_running_app()
        self.app.stop()

    def fecharDialogo(self, *args):
        self.dialog.dismiss(force=True)

    def funcaoMenuDropDown(self, *args):
        print(args)

    def funcaoMenu(self, btn):
        # menu_items = [{"viewclass": "OneLineListItem","text": f"Item {i}","height": dp(56),"on_release": lambda x=f"Item {i}": self.funcaoMenuDropDown(x),} for i in range(5)]
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Ajuda...",
                "height": dp(48),
                "on_release": lambda x=f"Ajuda...": self.funcaoMenuDropDown(x),
            }
            ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        self.menu.caller = btn
        self.menu.open()


    def funcaoLogout(self, *args):
        self.dialog = MDDialog(
            title="Fechar Aplicativo?",
            text="Você está prestes a sair do aplicativo.",
            buttons=[
                MDFlatButton(
                    text="CANCELAR",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.fecharDialogo(),
                ),
                MDFlatButton(
                    text="SIM",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.sairApp(),
                ),
            ],
        )
        self.dialog.open()
