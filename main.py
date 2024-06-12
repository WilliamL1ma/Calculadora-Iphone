import flet

# Lista de botões da calculadora com suas propriedades (operador, cor da fonte, cor de fundo)
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
    # Configurações iniciais da janela do aplicativo
    page.bgcolor = '#000'  # Cor de fundo da página
    page.window_resizable = False  # Janela não redimensionável
    page.window_width = 270  # Largura da janela
    page.window_height = 455  # Altura da janela
    page.title = 'Calculadora Iphone'  # Título da janela
    page.window_always_on_top = True  # Janela sempre no topo

    # Contêiner para mostrar o resultado da calculadora
    result = flet.Container(
        content=flet.Text(value='0', color=flet.colors.WHITE, size=40),  # Texto inicial do display
        width=200,  # Largura do contêiner
        height=100,  # Altura do contêiner
        bgcolor=flet.colors.BLACK,  # Cor de fundo do contêiner
        border_radius=10,  # Bordas arredondadas
        padding=flet.Padding(10, 10, 10, 10),  # Espaçamento interno
        alignment=flet.alignment.center_right  # Alinhamento do texto à direita
    )

    # Flag para resetar o display após um cálculo
    reset_display = False

    # Função para realizar cálculos com base na expressão
    def calculo(expressao):
        expressao = expressao.replace('÷', '/').replace('X', '*')  # Substitui operadores visuais por operadores válidos
        try:
            return str(eval(expressao))  # Avalia a expressão e retorna o resultado
        except ZeroDivisionError:
            return 'Erro'  # Tratamento para divisão por zero
        except Exception:
            return 'Erro'  # Tratamento para outras exceções

    # Função chamada quando um botão é clicado
    def select(clique):
        nonlocal reset_display  # Utiliza a variável reset_display definida fora da função
        valor_atual = result.content.value if result.content.value != '0' else ''  # Valor atual do display
        valor = clique.control.content.value  # Valor do botão clicado

        if reset_display and valor.isdigit():
            valor_atual = ''  # Reseta o display se for um dígito após um cálculo
            reset_display = False

        if valor.isdigit() or valor == ',':
            if valor == ',' and ',' in valor_atual:
                return  # Evita múltiplas vírgulas
            valor = valor_atual + ('.' if valor == ',' else valor)  # Adiciona o dígito ou vírgula ao valor atual
        elif valor == 'AC':
            valor = '0'  # Reseta o display
        elif valor == '+/-':
            if valor_atual:
                if valor_atual[0] == '-':
                    valor = valor_atual[1:]  # Remove o sinal negativo
                else:
                    valor = '-' + valor_atual  # Adiciona o sinal negativo
        elif valor == '%':
            if valor_atual:
                try:
                    expressao = valor_atual.replace('÷', '/').replace('X', '*').replace(',', '.')
                    valor = str(eval(expressao) / 100)  # Calcula o valor em porcentagem
                except Exception:
                    valor = 'Erro'
        elif valor == '=':
            valor = calculo(valor_atual)  # Realiza o cálculo da expressão
            reset_display = True
        else:
            if reset_display:
                reset_display = False
            if valor_atual and valor_atual[-1] in ('/', '*', '-', '+'):
                valor_atual = valor_atual[:-1]  # Substitui o operador atual pelo novo
            valor = valor_atual + valor  # Adiciona o operador ao valor atual

        result.content.value = valor  # Atualiza o display com o novo valor
        result.update()

    # Linha para exibir o display da calculadora
    display = flet.Row(
        width=280,  # Largura do display
        controls=[result],  # Adiciona o contêiner do resultado ao display
        alignment=flet.MainAxisAlignment.END  # Alinha o display à direita
    )

    # Cria os botões da calculadora
    botao = [flet.Container(
        content=flet.Text(value=botao['operador'], color=botao['fonte']),  # Texto do botão
        width=50,  # Largura do botão
        height=50,  # Altura do botão
        bgcolor=botao['fundo'],  # Cor de fundo do botão
        border_radius=100,  # Bordas arredondadas
        alignment=flet.alignment.center,  # Alinhamento do texto no centro
        on_click=select  # Ação ao clicar no botão
    ) for botao in botoes]

    # Linha para organizar os botões em um teclado
    teclado = flet.Row(
        width=280,  # Largura do teclado
        wrap=True,  # Permite que os botões sejam organizados em múltiplas linhas
        controls=botao,  # Adiciona os botões ao teclado
        alignment=flet.MainAxisAlignment.END  # Alinha o teclado à direita
    )

    # Adiciona o display e o teclado à página
    page.add(display, teclado)


# Inicializa o aplicativo Flet com a função main
flet.app(target=main)

