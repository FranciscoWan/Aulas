import flet as ft

# Função principal que executa o aplicativo
def main(page: ft.Page):
    # Configuração inicial da página
    page.title = "Calculadora"
    page.window_width = 300  # Largura da janela
    page.window_height = 450  # Altura da janela
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Alinhamento horizontal centralizado
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Alinhamento vertical centralizado
    
    # Criação do display onde o resultado será exibido
    resultado = ft.Text("0", size=32, text_align=ft.TextAlign.RIGHT, expand=True)
    entrada = ""  # Armazena os números digitados e operações
    nova_operacao = False  # Indica se uma nova operação deve ser iniciada
    
    # Função para atualizar o display com os valores digitados e calcular os resultados
    def atualizar_display(valor):
        nonlocal entrada, nova_operacao
        
        if valor == "C":  # Limpa o display
            entrada = ""
            nova_operacao = False
        elif valor == "=":  # Realiza o cálculo
            try:
                entrada = str(eval(entrada))  # Calcula a expressão matemática digitada
                nova_operacao = True  # Indica que a próxima entrada deve limpar o display
            except Exception:
                entrada = "Erro"  # Em caso de erro, exibe "Erro"
                nova_operacao = True
        else:
            if nova_operacao and valor.isdigit():  # Se um novo número for digitado após um resultado, limpa o display
                entrada = valor
            else:
                entrada += valor  # Continua adicionando valores à expressão
            nova_operacao = False
        
        resultado.value = entrada  # Atualiza o display com o novo valor
        page.update()  # Atualiza a página
    
    # Lista com os botões da calculadora organizados em linhas
    botoes = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"]
    ]
    
    # Criação dos botões
    botoes_widgets = []
    for linha in botoes:
        botoes_widgets.append(
            ft.Row([
                ft.ElevatedButton(
                    txt,  # Texto do botão
                    on_click=lambda e, t=txt: atualizar_display(t),  # Chama a função ao clicar
                    width=60,  # Largura do botão
                    height=60,  # Altura do botão
                    bgcolor=ft.colors.LIGHT_BLUE_300 if txt.isdigit() else ft.colors.GREY_300  # Cor azul para números, cinza para operações
                )
                for txt in linha  # Cria os botões para cada linha
            ], alignment=ft.MainAxisAlignment.CENTER)  # Centraliza os botões na linha
        )
    
    # Criando o container principal da calculadora
    calculadora_container = ft.Container(
        content=ft.Column([
            # Área do display onde os números e resultados são mostrados
            ft.Container(resultado, alignment=ft.alignment.bottom_right, padding=10, height=60),
            # Área dos botões
            ft.Column(botoes_widgets, alignment=ft.MainAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER),
        width=280,  # Largura do container da calculadora
        height=400,  # Altura do container
        bgcolor=ft.colors.TRANSPARENT,  # Fundo transparente
        border_radius=10,  # Bordas arredondadas
        padding=10  # Espaçamento interno
    )
    
    # Adiciona a calculadora na página
    page.add(calculadora_container)

# Inicia o aplicativo chamando a função principal
ft.app(target=main)
