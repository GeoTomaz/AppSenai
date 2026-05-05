import asyncio

import flet
import ft
from flet import ThemeMode, View, AppBar, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Text, Card, \
    Column, Container, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption, CrossAxisAlignment
from markdown_it.rules_block import lheading

class Impressora:
    def __init__(self, modelo, cor, marca, valor):
        self.modelo = modelo
        self.cor = cor
        self.marca = marca
        self.valor = valor

def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_padrao():
        lv.controls.clear()

        for item in lista_dados:
            lv.controls.append(
                ListTile(
                    leading=Icon(Icons.PRINT),
                    title=item.modelo,
                    subtitle=item.valor,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver Detalhes", icon=Icons.REMOVE_RED_EYE, on_click=lambda _, impressora=item: ver_detalhes(impressora)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item))
                        ]
                    )
                )
            )

    def ver_detalhes(impressora):
        text_marca.value = impressora.marca
        text_modelo.value = impressora.modelo
        text_cor.value = impressora.cor
        text_valor.value = impressora.valor

        navegar("/form_detalhes")

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        modelo = input_modelo.value
        valor = input_valor.value
        cor = input_cor.value
        marca = input_marca.value

        tem_erro = False

        if modelo:
            input_modelo.error = None
        else:
            tem_erro = True
            input_modelo.error = "Campo obrigatorio"

        if marca:
            input_marca.error = None
        else:
            tem_erro = True
            input_marca.error = "Campo obrigatorio"

        if cor:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatorio"

        if valor:
            input_valor.error = None
        else:
            tem_erro = True
            input_valor.error = "Campo obrigatorio"

        if not tem_erro:
            impressora = Impressora(modelo=modelo, cor=cor, valor=valor, marca=marca)
            lista_dados.append(impressora)

            input_modelo.value = ""
            input_marca.value = ""
            input_cor.value = ""
            input_valor.value = ""

            navegar(route="/lista_d1ados")





        montar_lista_padrao()

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                controls=[
                    flet.AppBar(
                        title="Lista de Impressoras",
                    ),
                    lv
                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda : navegar("/form_cadastro"),
                )
            )
        )
        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                        ),
                        input_modelo,
                        input_cor,
                        input_valor,
                        input_marca,
                        btn_salvar,
                    ],
                )
            )
        elif page.route == "/form_detalhes":
            page.views.append(
                View(
                    route="/form_detalhes",
                    controls=[
                        flet.AppBar(
                            title="Detalhes",
                        ),
                        Container(

                            Column([
                                text_modelo,
                                Row([
                                    Icon(Icons.COLLECTIONS_BOOKMARK_ROUNDED, color=Colors.BLACK, size=20),
                                    text_marca,
                                ]),
                                Row([
                                    Icon(Icons.COLOR_LENS_ROUNDED, color=Colors.BLACK, size=20),
                                    text_cor,
                                ]),
                                Row([
                                    Icon(Icons.MONEY, color=Colors.BLACK, size=20),
                                    text_valor,
                                ],
                                ),
                            ],
                            horizontal_alignment = CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=Colors.PURPLE,
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
    text_marca = Text()
    text_modelo = Text()
    text_cor = Text()
    text_valor = Text()
    input_modelo = TextField(label="Modelo", on_submit=salvar_dados)
    input_marca = TextField(label="Marca", on_submit=salvar_dados)
    input_cor = TextField(label="Cor", on_submit=salvar_dados)
    input_valor = TextField(label="Valor", on_submit=salvar_dados)
    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())
    lv = ListView(height=500)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)