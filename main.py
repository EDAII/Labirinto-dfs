import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 40, 40
CELL = WIDTH // COLS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirinto + DFS")

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,200,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GRAY = (120,120,120)

def gerar_labirinto(prob_obstaculo=0.25):
    grid = []
    for r in range(ROWS):
        grid.append([])
        for c in range(COLS):
            if random.random() < prob_obstaculo:
                grid[r].append(1)  # obstáculo
            else:
                grid[r].append(0)  # livre
    return grid


def labirinto_impossivel():
    grid = gerar_labirinto(0.05)

    # parede inteira no meio
    meio = COLS // 2
    for r in range(ROWS):
        grid[r][meio] = 1

    return grid


def draw_grid(grid, visited, path, start, end, message=None):
    WIN.fill(WHITE)

    for r in range(ROWS):
        for c in range(COLS):
            x = c * CELL
            y = r * CELL

            if grid[r][c] == 1:
                pygame.draw.rect(WIN, BLACK, (x, y, CELL, CELL))
            elif path[r][c]:
                pygame.draw.rect(WIN, YELLOW, (x, y, CELL, CELL))
            elif visited[r][c]:
                pygame.draw.rect(WIN, BLUE, (x, y, CELL, CELL))
            else:
                pygame.draw.rect(WIN, GRAY, (x, y, CELL, CELL), 1)

    if start:
        pygame.draw.rect(WIN, GREEN, (start[1]*CELL, start[0]*CELL, CELL, CELL))

    if end:
        pygame.draw.rect(WIN, RED, (end[1]*CELL, end[0]*CELL, CELL, CELL))

    if message:
        font = pygame.font.SysFont(None, 40)
        text = font.render(message, True, RED)
        WIN.blit(text, (WIDTH//2 - text.get_width()//2, 10))

    pygame.display.update()


def dfs(grid, start, end):
    stack = [(start, [start])]
    visited = [[False]*COLS for _ in range(ROWS)]
    path_mask = [[False]*COLS for _ in range(ROWS)]
    clock = pygame.time.Clock()

    while stack:
        (r, c), caminho = stack.pop()

        if visited[r][c]:
            continue

        visited[r][c] = True
        draw_grid(grid, visited, path_mask, start, end)
        clock.tick(120)

        if (r, c) == end:
            for rr, cc in caminho:
                path_mask[rr][cc] = True
                draw_grid(grid, visited, path_mask, start, end)
            return caminho

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if not visited[nr][nc] and grid[nr][nc] == 0:
                    stack.append(((nr, nc), caminho + [(nr, nc)]))

    return None


def main():
    grid = gerar_labirinto()
    start = None
    end = None
    caminho_final = None
    mensagem = None

    running = True

    while running:
        draw_grid(grid, [[False]*COLS for _ in range(ROWS)],
                  [[False]*COLS for _ in range(ROWS)], start, end, mensagem)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

            # Teclas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # randomizar
                    grid = gerar_labirinto()
                    start = None
                    end = None
                    mensagem = None
                    caminho_final = None

                if event.key == pygame.K_i:  # mapa impossível
                    grid = labirinto_impossivel()
                    start = None
                    end = None
                    mensagem = None
                    caminho_final = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                r = event.pos[1] // CELL
                c = event.pos[0] // CELL

                if start is None:
                    if grid[r][c] == 0:
                        start = (r, c)

                elif end is None:
                    if grid[r][c] == 0:
                        end = (r, c)
                        caminho_final = dfs(grid, start, end)

                        if caminho_final is None:
                            mensagem = "CAMINHO INEXISTENTE!"
                        else:
                            mensagem = f"Caminho encontrado ({len(caminho_final)} passos)"

                else:
                    start = None
                    end = None
                    grid = gerar_labirinto()
                    mensagem = None
                    caminho_final = None

    pygame.quit()


if __name__ == "__main__":
    main()
