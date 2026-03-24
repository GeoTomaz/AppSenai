import flet
from flet import ThemeMode, OutlinedButton, Text, TextField, Column, CrossAxisAlignment
from datetime import datetime


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700

    # Funções
    def salvar_nome():
        text.value = f"Bom dia {input_nome.value} {input_sobrenome.value}"

    def verificar_par_impar():
        numero = int(input_numero.value)
        if numero % 2 == 0:
            text_par_impar.value = f"O {numero} é par"
        else:
            text_par_impar.value = f"O {numero} é ímpar"

    def verificar_idade():
        ano = int(input_idade.value)
        idade = datetime.now().year - ano

        if idade >= 18:
            text_idade.value = f"{idade}, Você é maior de idade"
        else:
            text_idade.value = f"{idade}, Você é menor de idade"

    # Componentes
    text = Text()
    text_par_impar = Text()
    text_idade = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    input_numero = TextField(label="Digite um número")
    input_idade = TextField(label="Digite ano de nascimento")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    btn_verificar = OutlinedButton("Verificar", on_click=verificar_par_impar)
    btn_verificar_idade = OutlinedButton("Comparar", on_click=verificar_idade)

    # Construção da tela

    page.add (
        Column(
            [
                input_nome,
                input_sobrenome,
                btn_salvar,
                text,
                input_numero,
                btn_verificar,
                text_par_impar,
                input_idade,
                btn_verificar_idade,
                text_idade
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

flet.run(main)