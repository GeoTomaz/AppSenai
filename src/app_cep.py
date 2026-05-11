import asyncio

import flet
from flet import ThemeMode, View, AppBar, Colors, Button, Text, TextField, OutlinedButton, Card, Row, Column, \
    FontWeight, TextOverflow, ListView, Pagelet, NavigationBar, NavigationBarDestination
from flet.controls.core import list_view

from api_cep import get_cep

def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_cep():
        cep = input_cep.value
        numero = input_numero.value
        tem_erro = False

        if cep:
            input_cep.error = None
        else:
            tem_erro = True
            input_cep.error = "Campo invalido"

        if not tem_erro:
            endereco = get_cep(cep)
            input_cidade.value = endereco["localidade"]
            input_uf.value = endereco["uf"]
            input_logradouro.value = endereco["logradouro"]
            input_bairro.value = endereco["bairro"]

    def route_change():
        montar_cep()

        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Cadastro Endereço",
                    ),
                    input_cep,
                    input_numero,
                    input_cidade,
                    input_uf,
                    input_logradouro,
                    input_bairro,
                ]
            )
        )

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    input_cep = TextField(label="CEP", on_submit=lambda: montar_cep())
    input_numero = TextField(label="número")

    input_cidade = TextField(label="cidade",disabled=True)
    input_uf = TextField(label="uf",disabled=True)
    input_logradouro = TextField(label="logradouro",disabled=True)
    input_bairro = TextField(label="bairro",disabled=True)


    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)