import asyncio

import flet
from flet import ThemeMode, View, AppBar, Colors, Button, Text, TextField, OutlinedButton


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
        text.value = f"{input_nome.value}"
        text_cpf.value = f"{input_CPF.value}"
        text_email.value = f"{input_email.value}"
        text_salario.value = f"R$ {input_salario.value}"

        tem_erro = False

        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio"

        if input_CPF.value:
            input_CPF.error = None
        else:
            tem_erro = True
            input_CPF.error = "Campo obrigatorio"

        if input_email.value:
            input_email.error = None
        else:
            tem_erro = True
            input_email.error = "Campo obrigatorio"

        if input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = "Campo obrigatorio"

        if not tem_erro:
            input_nome.value = ""
            input_CPF.value = ""
            input_email.value = ""
            input_salario.value = ""
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
                        bgcolor=Colors.CYAN_700
                    ),
                    input_nome,
                    input_CPF,
                    input_email,
                    input_salario,
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
                            title="Mensagem",
                        ),
                        text,
                        text_cpf,
                        text_email,
                        text_salario,
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
    text_cpf = Text()
    text_email = Text()
    text_salario = Text()
    input_nome = TextField(label="Nome")
    input_CPF = TextField(label="Cpf")
    input_email = TextField(label="Email")
    input_salario = TextField(label="Salario")
    btn_salvar = OutlinedButton("Salvar", on_click=cadastrar)


    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)