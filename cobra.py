import pygame
import random

# Definindo as dimensões da tela
largura = 1920
altura = 1080

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Inicializando o Pygame
pygame.init()

# Criando a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Definindo o relógio
clock = pygame.time.Clock()

# Definindo a fonte para o texto
fonte = pygame.font.SysFont(None, 60)

# Função para desenhar o texto na tela
def texto(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura/6, altura/2])

# Função para desenhar a cobrinha
def cobrinha(cor, lista_cobra, tamanho):
    for x,y in lista_cobra:
        pygame.draw.rect(tela, cor, [x,y,tamanho,tamanho])

# Função principal do jogo
def jogo():
    # Definindo as variáveis iniciais
    game_over = False
    game_close = False

    # Definindo a posição inicial da cobrinha
    x_cobra = largura/2
    y_cobra = altura/2

    # Definindo as mudanças iniciais de posição da cobrinha
    x_mudar = 0       
    y_mudar = 0

    # Definindo o tamanho da cobrinha
    tamanho_cobra = 10

    # Gerando a posição aleatória da maçã
    x_maca = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10.0
    y_maca = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10.0

    # Inicializando a lista da cobrinha
    lista_cobra = []
    comprimento_cobra = 1

    # Loop principal do jogo
    while not game_over:

        # Loop caso o jogador perca
        while game_close == True:
            tela.fill(branco)
            texto("Bem vindo! Pressione Q para sair ou C para jogar novamente.", vermelho)
            pygame.display.update()

            # Verificando as teclas pressionadas
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo()

        # Loop para verificar os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_mudar = -tamanho_cobra
                    y_mudar = 0
                elif event.key == pygame.K_RIGHT:
                    x_mudar = tamanho_cobra
                    y_mudar = 0
                elif event.key == pygame.K_UP:
                    y_mudar = -tamanho_cobra
                    x_mudar = 0
                elif event.key == pygame.K_DOWN:
                    y_mudar = tamanho_cobra

        # Verificando se a cobrinha bateu nas bordas da tela
        if x_cobra >= largura or x_cobra < 0 or y_cobra >= altura or y_cobra < 0:
            game_close = True

        # Movimentando a cobrinha
        x_cobra += x_mudar
        y_cobra += y_mudar

        # Desenhando a maçã
        pygame.draw.rect(tela, vermelho, [x_maca, y_maca, tamanho_cobra, tamanho_cobra])

        # Adicionando a cabeça da cobrinha na lista
        cabeca_cobra = []
        cabeca_cobra.append(x_cobra)
        cabeca_cobra.append(y_cobra)
        lista_cobra.append(cabeca_cobra)

        # Removendo a cauda da cobrinha caso ela fique muito grande
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Verificando se a cobrinha bateu em seu próprio corpo
        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                game_close = True

        # Desenhando a cobrinha na tela
        cobrinha(preto, lista_cobra, tamanho_cobra)

        # Atualizando a tela
        pygame.display.update()

        # Verificando se a cobrinha comeu a maçã
        if x_cobra == x_maca and y_cobra == y_maca:
            x_maca = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10.0
            y_maca = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10.0
            comprimento_cobra += 1

        # Definindo a velocidade do jogo
        clock.tick(15)

    # Finalizando o Pygame
    pygame.quit()

# Chamando a função principal do jogo
jogo()