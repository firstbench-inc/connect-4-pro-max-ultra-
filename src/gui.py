"""
Our program, who art in memory,
    called by thy name;
  thy operating system run;
thy function be done at 
  as it was on development.runtime
Give us this day our daily output.
And forgive us our code duplication,
    as we forgive those who
  duplicate code against us.
And lead us not into frustration;
  but deliver us from GOTOs.
    For thine is algorithm,
the computation, and the solution,
    looping forever and ever.
          Return;
"""

import pygame
import game


class Button:
    def __init__(self, img_path: str, pos: (int, int)):
        self.image = pygame.image.load(img_path).convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(topleft=pos)
        return


def get_board_cord(x: int, y: int) -> (int, int):
    imgx, imgy = 780, 490
    return ((x // 2) - (imgx // 2), (y // 2) - (imgy // 2))


def place_coin(surface, col_no: int, row_no: int, board_pos: (int, int), player: int):
    pos_x = board_pos[0] + 71 + 106 * (col_no)
    pos_y = board_pos[1] + 51 + 77 * (row_no)
    return pygame.draw.circle(surface, (255, 255 * (2 - player), 0), (pos_x, pos_y), 37)


# ------------ pygame init -------------
pygame.init()
screen = pygame.display.set_mode((1366, 780))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
board = pygame.image.load(r"./assets/board.png")
board_pos = get_board_cord(screen.get_width(), screen.get_height())

# ----------- game init -----------------
game_state = game.Game()
coins = []

# ------------ columns ------------------
columns = []
start_point = board_pos[0] + 32
for i in range(1, 8):
    columns.append(
        Button(f"assets/button_r ({i}).png", (start_point + 106 * (i - 1), 50))
    )
    pass

# ------------ game loop ----------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for col_no, col in enumerate(columns):
                if col.rect.collidepoint(mouse_pos):
                    print(f"col {col_no + 1} was pressed!")
                    row_no = 5 - game_state.add_coin(col_no)
                    print(row_no)
                    coins.append(
                        place_coin(
                            screen, col_no, row_no, board_pos, game_state.player_turn
                        )
                    )
                pass
            pass

    screen.blits(((col.image, (col.pos[0], col.pos[1])) for col in columns))
    screen.blit(board, board_pos)
    pygame.display.update()
    clock.tick(60)
    pass
