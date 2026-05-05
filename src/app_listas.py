import asyncio

import flet
import ft
from flet import ThemeMode, View, AppBar, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Text, Card, \
    Column, Container, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption
from markdown_it.rules_block import lheading

class Perfil:
    def __init__(self, nome, profissao, genero):
        self.nome = nome
        self.profissao = profissao
        self.genero = genero

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

    def montar_lista_texto():
        lv.controls.clear()

        for item in lista_dados:
            lv.controls.append(
                Text(item)
            )

    def montar_lista_card():
        lv.controls.clear()

        for item in lista_dados:
            lv.controls.append(
                Card(
                    height=50,
                    content=Row([
                        Icon(Icons.PERSON),
                        Text(item)
                        ],
                        margin=8
                    )
                )
            )
    def definir_imagem(p1):
        if p1 == "Masculino":
            return Icon(Icons.MAN)
        elif p1 == "Feminino":
            return Icon(Icons.WOMAN)

    def montar_lista_padrao():
        lv.controls.clear()

        for item in lista_dados:
            lv.controls.append(
                ListTile(
                    leading=definir_imagem(item.genero),
                    title=item.nome,
                    subtitle=item.profissao,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver Detalhes", icon=Icons.REMOVE_RED_EYE),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item))
                        ]
                    )
                )
            )
    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        nome = input_nome.value.strip()
        profissao = input_profissao.value.strip()
        genero = input_genero.value.strip()

        tem_erro = False

        if nome:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo Obrigatório"

        if profissao:
            input_profissao.error = None
        else:
            tem_erro = True
            input_profissao.error = "Campo Obrigatório"

        if genero:
            input_genero.error = None
        else:
            tem_erro = True
            input_genero.error = "Campo Obrigatório"

        if not tem_erro:
            pessoa = Perfil(nome=nome, profissao=profissao, genero=genero)

            lista_dados.append(pessoa)

            input_nome.value = ""
            input_profissao.value = ""
            input_genero.value = ""




        montar_lista_texto()
        montar_lista_card()
        montar_lista_padrao()

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Exemplos de Listas",
                        bgcolor=Colors.CYAN_700
                    ),
                    Button("Lista de texto", on_click= lambda: navegar("/lista_texto")),
                    Button("Lista de card", on_click= lambda: navegar("/lista_card")),
                    Button("Lista padrão Android", on_click= lambda: navegar("/lista_padrao"))
                ]
            )
        )
        if page.route == "/lista_texto":
            montar_lista_texto()
            page.views.append(
                View(
                    route="/lista_texto",
                    controls=[
                        flet.AppBar(
                            title="Lista de Texto",
                        ),
                        input_nome,
                        btn_salvar,
                        lv
                    ]
                )
            )
        elif page.route == "/lista_card":
            montar_lista_card()
            page.views.append(
                View(
                    route="/lista_card",
                    controls=[
                        flet.AppBar(
                            title="Lista de Cards",
                        ),
                        input_nome,
                        btn_salvar,
                        lv
                    ]
                )
            )
        elif page.route == "/lista_padrao":
            page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        flet.AppBar(
                            title="Lista Padrão Android",
                        ),
                        lv
                    ],
                    floating_action_button=FloatingActionButton(
                        icon=Icons.ADD,
                        on_click=lambda : navegar("/form_cadastro"),
                    )
                )
            )
        elif page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                        ),
                        input_nome,
                        input_profissao,
                        input_genero,
                        btn_salvar,
                    ],
                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    input_nome = TextField(label ="Nome", hint_text="Digite o seu nome", on_submit=salvar_dados)
    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())
    lv = ListView(height=500)
    input_profissao = TextField(hint_text="Digite a sua profissão", on_submit=salvar_dados)
    input_genero =  Dropdown(
        label="Gênero",
        editable=True,
        options=[
            DropdownOption("Feminino"),
            DropdownOption("Masculino"),
        ],
    )

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)