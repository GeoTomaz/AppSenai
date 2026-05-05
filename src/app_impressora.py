import asyncio

import flet
from flet import ThemeMode, View, AppBar, Colors, Button, Text, TextField, OutlinedButton, Container, Column, Row, Icon, \
    Icons, CrossAxisAlignment


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

    # Funções
    def cadastrar():
        text.value = f"{input_modelo.value}"
        text_marca.value = f"{input_marca.value}"
        text_cor.value = f"{input_cor.value}"
        text_valor.value = f"R$ {input_valor.value}"

        tem_erro = False

        if input_modelo.value:
            input_modelo.error = None
        else:
            tem_erro = True
            input_modelo.error = "Campo obrigatorio"

        if input_marca.value:
            input_marca.error = None
        else:
            tem_erro = True
            input_marca.error = "Campo obrigatorio"

        if input_cor.value:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatorio"

        if input_valor.value:
            input_valor.error = None
        else:
            tem_erro = True
            input_valor.error = "Campo obrigatorio"

        if not tem_erro:
            input_modelo.value = ""
            input_marca.value = ""
            input_cor.value = ""
            input_valor.value = ""
            navegar(route="/mensagem")

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Cadastro Funcionário",
                        bgcolor=Colors.PURPLE
                    ),
                    input_modelo,
                    input_marca,
                    input_cor,
                    input_valor,
                    btn_salvar,
                ]
            )
        )
        if page.route == "/mensagem":
            page.views.append(
                View(
                    route="/mensagem",
                    controls=[
                        flet.AppBar(
                            title="Segunda página",
                        ),
                        Container(

                            Column([
                                text,
                                Row([
                                    Icon(Icons.COLLECTIONS_BOOKMARK_ROUNDED, color=Colors.PURPLE, size=20),
                                    text_marca,
                                ]),
                                Row([
                                    Icon(Icons.COLOR_LENS_ROUNDED, color=Colors.PURPLE, size=20),
                                    text_cor,
                                ]),
                                Row([
                                    Icon(Icons.MONEY, color=Colors.PURPLE, size=20),
                                    text_valor,
                                ],
                                ),
                            ],
                            horizontal_alignment = CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=Colors.BLUE,
                            border_radius=10,
                            padding=10,
                        ),
                    ]
                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    text = Text()
    text_marca = Text()
    text_cor = Text()
    text_valor = Text()
    input_modelo = TextField(label="Modelo")
    input_marca = TextField(label="Marca")
    input_cor = TextField(label="Cor")
    input_valor = TextField(label="Valor")
    btn_salvar = OutlinedButton("Salvar", on_click=cadastrar)


    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)