import flet

botoes = [
    {'operador': 'AC', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY},
    {'operador': '+/-', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY},
    {'operador': '%', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY},
    {'operador': '÷', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.ORANGE},
    {'operador': '7', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY_800},
    {'operador': '8', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY_800},
    {'operador': '9', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY_800},
    {'operador': 'X', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.ORANGE},
    {'operador': '4', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY_800},
    {'operador': '5', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY_800},
    {'operador': '6', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY_800},
    {'operador': '-', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.ORANGE},
    {'operador': '1', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY_800},
    {'operador': '2', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY_800},
    {'operador': '3', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY_800},
    {'operador': '+', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.ORANGE},
    {'operador': '0', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY_800},
    {'operador': ',', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.GREY_800},
    {'operador': '=', 'fonte': flet.colors.BLACK, 'fundo': flet.colors.ORANGE},





]


def main(page: flet.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 270
    page.window_height = 380
    page.title = 'Calculadora Iphone'
    page.window_always_on_top = True

    result = flet.Text(value='0', color=flet.colors.WHITE, size=20)

    def calculo(expressao):
        expressao = expressao.replace('÷', '/').replace('X', '*')

        try:
            return str(eval(expressao))
        except ZeroDivisionError:
            return 'ERRO'
        except Exception:
            return 'ERRO'

    def select(clique):
        valor_atual = result.value if result.value != '0' else ''
        valor = clique.control.content.value

        if valor.isdigit() or valor == ',':
            if valor == ',' and ',' in valor_atual:
                return
            valor = valor_atual + valor

        elif valor == 'AC':
            valor = '0'

        elif valor == '+/-':
            if valor_atual:
                if valor_atual[0] == '-':
                    valor = valor_atual[1:]
                else:
                    valor = '-' + valor_atual

        elif valor == '%':
            if valor_atual:
                valor = str(float(valor_atual) / 100)

        elif valor == '=':
            valor = calculo(valor_atual)

        else:
            if valor_atual and valor_atual[-1] in ('/', '*', '-', '+'):
                valor_atual = valor_atual[:-1]
            valor = valor_atual + valor

        result.value = valor
        result.update()

    display = flet.Row(
        width=280,
        controls=[result],
        alignment=flet.MainAxisAlignment.END
    )

    botao = [flet.Container(
        content=flet.Text(value=botao['operador'], color=botao['fonte']),
        width=50,
        height=50,
        bgcolor=botao['fundo'],
        border_radius=100,
        alignment=flet.alignment.center,
        on_click=select
    ) for botao in botoes]

    teclado = flet.Row(
        width=280,
        wrap=True,
        controls=botao,
        alignment=flet.MainAxisAlignment.END

    )

    page.add(display, teclado)


flet.app(target=main)