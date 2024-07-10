import pygame
from checkersinner.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkersinner.board import Board
from checkersinner.game import Game



FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    game = Game(WIN)

    piece = board.get_piece(0,1)
  

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if game.turn == RED:
                    game.select(row, col)

        game.update()

    pygame.quit()

main()