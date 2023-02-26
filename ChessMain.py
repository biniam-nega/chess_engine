'''
This class is responsible for storing all the information about the current state if the chess game.
It is also responsible for determining the valid moves at the current state.
It will also keep a move log
'''

import pygame as p
import ChessEngine


WIDTH = HEIGHT = 512
DIMENSION = 8 # The dimension of the board
sq_size = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''


def loadImages():
    pieces = ["wp", "wR", "wN", "wK", "wQ", "wB", "bp", "bR", "bN", "bK", "bQ", "bB"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".PNG"), (sq_size, sq_size))


'''
The main driver for the code. This will handle user input and updating the graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    print(gs.board)
    loadImages() # Only do this once, before the wile loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)


'''
Responsible for all the graphics within the current game state
'''


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs)


'''
Draws the squares on the board
'''


def drawBoard(screen):
    pass


'''
Draw the pieces on the board using the current GameState.board
'''


def drawPieces(screen, gs):
    pass


if __name__ == "__main__":
    main()
