
import pygame
from pygame.locals import *
import os
import os.path
import random
import time

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Chess")

tile_size = 125

class Board():

    def __init__(self):

        self.dark_square = pygame.image.load(os.path.join("textures/dark_square.png")).convert_alpha()
        self.dark_square = pygame.transform.scale(self.dark_square, (tile_size, tile_size))
        self.dark_square_rect = self.dark_square.get_rect()

        self.light_square = pygame.image.load(os.path.join("textures/light_square.png")).convert_alpha()
        self.light_square = pygame.transform.scale(self.light_square, (tile_size, tile_size))
        self.light_square_rect = self.light_square.get_rect()

    def draw_board(self):

        for i in range(0, 8):
            
            x = tile_size * i
            
            for j in range(0, 8):

                y = tile_size * j

                if (x + y) % 2 == 0:

                    self.light_square_rect.x = x
                    self.light_square_rect.y = y
                    
                    tile = self.light_square, self.light_square_rect

                else:
                    
                    self.dark_square_rect.x = x
                    self.dark_square_rect.y = y
                    
                    tile = self.dark_square, self.dark_square_rect
                    
                screen.blit(tile[0], tile[1])
                
class Pieces():

    def __init__(self):

        #[xpos, ypos, alive, unmoved]
        
        self.white_pawns_inf = [[0, 1, True, True], [1, 1, True, True], [2, 1, True, True], [3, 1, True, True], [4, 1, True, True], [5, 1, True, True], [6, 1, True, True], [7, 1, True, True]]
        self.white_bishops_inf = [[2, 0, True], [5, 0, True], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False]]
        self.white_knights_inf = [[1, 0, True], [6, 0, True], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False]]
        self.white_rooks_inf = [[0, 0, True, True], [7, 0, True, True], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False]]
        self.white_queens_inf = [[3, 0, True], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False]]
        self.white_king_inf = [[4, 0, True, True]]

        self.black_pawns_inf = [[0, 6, True, True], [1, 6, True, True], [2, 6, True, True], [3, 6, True, True], [4, 6, True, True], [5, 6, True, True], [6, 6, True, True], [7, 6, True, True]]
        self.black_bishops_inf = [[2, 7, True], [5, 7, True], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False]]
        self.black_knights_inf = [[1, 7, True], [6, 7, True], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False]]
        self.black_rooks_inf = [[0, 7, True, True], [7, 7, True, True], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False]]
        self.black_queens_inf = [[3, 7, True], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False]]
        self.black_king_inf = [[4, 7, True, True]]
        
        self.white_pawn_img = pygame.image.load(os.path.join("textures/white_pawn.png")).convert_alpha()
        self.white_pawn_img = pygame.transform.scale(self.white_pawn_img, (tile_size, tile_size))
        self.white_pawn_img_rect = self.white_pawn_img.get_rect()

        self.white_knight_img = pygame.image.load(os.path.join("textures/white_knight.png")).convert_alpha()
        self.white_knight_img = pygame.transform.scale(self.white_knight_img, (tile_size, tile_size))
        self.white_knight_img_rect = self.white_knight_img.get_rect()

        self.white_bishop_img = pygame.image.load(os.path.join("textures/white_bishop.png")).convert_alpha()
        self.white_bishop_img = pygame.transform.scale(self.white_bishop_img, (tile_size, tile_size))
        self.white_bishop_img_rect = self.white_bishop_img.get_rect()

        self.white_rook_img = pygame.image.load(os.path.join("textures/white_rook.png")).convert_alpha()
        self.white_rook_img = pygame.transform.scale(self.white_rook_img, (tile_size, tile_size))
        self.white_rook_img_rect = self.white_rook_img.get_rect()

        self.white_queen_img = pygame.image.load(os.path.join("textures/white_queen.png")).convert_alpha()
        self.white_queen_img = pygame.transform.scale(self.white_queen_img, (tile_size, tile_size))
        self.white_queen_img_rect = self.white_queen_img.get_rect()

        self.white_king_img = pygame.image.load(os.path.join("textures/white_king.png")).convert_alpha()
        self.white_king_img = pygame.transform.scale(self.white_king_img, (tile_size, tile_size))
        self.white_king_img_rect = self.white_king_img.get_rect()

        self.black_pawn_img = pygame.image.load(os.path.join("textures/black_pawn.png")).convert_alpha()
        self.black_pawn_img = pygame.transform.scale(self.black_pawn_img, (tile_size, tile_size))
        self.black_pawn_img_rect = self.black_pawn_img.get_rect()

        self.black_knight_img = pygame.image.load(os.path.join("textures/black_knight.png")).convert_alpha()
        self.black_knight_img = pygame.transform.scale(self.black_knight_img, (tile_size, tile_size))
        self.black_knight_img_rect = self.black_knight_img.get_rect()

        self.black_bishop_img = pygame.image.load(os.path.join("textures/black_bishop.png")).convert_alpha()
        self.black_bishop_img = pygame.transform.scale(self.black_bishop_img, (tile_size, tile_size))
        self.black_bishop_img_rect = self.black_bishop_img.get_rect()

        self.black_rook_img = pygame.image.load(os.path.join("textures/black_rook.png")).convert_alpha()
        self.black_rook_img = pygame.transform.scale(self.black_rook_img, (tile_size, tile_size))
        self.black_rook_img_rect = self.black_rook_img.get_rect()

        self.black_queen_img = pygame.image.load(os.path.join("textures/black_queen.png")).convert_alpha()
        self.black_queen_img = pygame.transform.scale(self.black_queen_img, (tile_size, tile_size))
        self.black_queen_img_rect = self.black_queen_img.get_rect()

        self.black_king_img = pygame.image.load(os.path.join("textures/black_king.png")).convert_alpha()
        self.black_king_img = pygame.transform.scale(self.black_king_img, (tile_size, tile_size))
        self.black_king_img_rect = self.black_king_img.get_rect()

        self.white_occupation_x = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
        self.white_occupation_y = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

        self.black_occupation_x = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
        self.black_occupation_y = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

    def draw_pieces_white(self):

        for i in range(0, 8):

            if self.white_pawns_inf[i][2] == True:

                self.white_pawn_img_rect.x = self.white_pawns_inf[i][0] * tile_size
                self.white_pawn_img_rect.y = self.white_pawns_inf[i][1] * tile_size
                self.white_pawn_img_rect.y = self.white_pawn_img_rect.y - (self.white_pawn_img_rect.y * 2) + 875

                screen.blit(self.white_pawn_img, self.white_pawn_img_rect)

        for i in range(0, 10):

            if self.white_bishops_inf[i][2] == True:

                self.white_bishop_img_rect.x = self.white_bishops_inf[i][0] * tile_size
                self.white_bishop_img_rect.y = self.white_bishops_inf[i][1] * tile_size
                self.white_bishop_img_rect.y = self.white_bishop_img_rect.y - (self.white_bishop_img_rect.y * 2) + 875

                screen.blit(self.white_bishop_img, self.white_bishop_img_rect)

        for i in range(0, 10):

            if self.white_knights_inf[i][2] == True:

                self.white_knight_img_rect.x = self.white_knights_inf[i][0] * tile_size
                self.white_knight_img_rect.y = self.white_knights_inf[i][1] * tile_size
                self.white_knight_img_rect.y = self.white_knight_img_rect.y - (self.white_knight_img_rect.y * 2) + 875

                screen.blit(self.white_knight_img, self.white_knight_img_rect)

        for i in range(0, 10):

            if self.white_rooks_inf[i][2] == True:

                self.white_rook_img_rect.x = self.white_rooks_inf[i][0] * tile_size
                self.white_rook_img_rect.y = self.white_rooks_inf[i][1] * tile_size
                self.white_rook_img_rect.y = self.white_rook_img_rect.y - (self.white_rook_img_rect.y * 2) + 875

                screen.blit(self.white_rook_img, self.white_rook_img_rect)

        for i in range(0, 9):
            
            if self.white_queens_inf[i][2] == True:

                self.white_queen_img_rect.x = self.white_queens_inf[i][0] * tile_size
                self.white_queen_img_rect.y = self.white_queens_inf[i][1] * tile_size
                self.white_queen_img_rect.y = self.white_queen_img_rect.y - (self.white_queen_img_rect.y * 2) + 875

                screen.blit(self.white_queen_img, self.white_queen_img_rect)

        if self.white_king_inf[0][2] == True:

            self.white_king_img_rect.x = self.white_king_inf[0][0] * tile_size
            self.white_king_img_rect.y = self.white_king_inf[0][1] * tile_size
            self.white_king_img_rect.y = self.white_king_img_rect.y - (self.white_king_img_rect.y * 2) + 875

            screen.blit(self.white_king_img, self.white_king_img_rect)

        for i in range(0, 8):

            if self.black_pawns_inf[i][2] == True:

                self.black_pawn_img_rect.x = self.black_pawns_inf[i][0] * tile_size
                self.black_pawn_img_rect.y = self.black_pawns_inf[i][1] * tile_size
                self.black_pawn_img_rect.y = self.black_pawn_img_rect.y - (self.black_pawn_img_rect.y * 2) + 875

                screen.blit(self.black_pawn_img, self.black_pawn_img_rect)

        for i in range(0, 10):

            if self.black_bishops_inf[i][2] == True:

                self.black_bishop_img_rect.x = self.black_bishops_inf[i][0] * tile_size
                self.black_bishop_img_rect.y = self.black_bishops_inf[i][1] * tile_size
                self.black_bishop_img_rect.y = self.black_bishop_img_rect.y - (self.black_bishop_img_rect.y * 2) + 875

                screen.blit(self.black_bishop_img, self.black_bishop_img_rect)

        for i in range(0, 10):

            if self.black_knights_inf[i][2] == True:

                self.black_knight_img_rect.x = self.black_knights_inf[i][0] * tile_size
                self.black_knight_img_rect.y = self.black_knights_inf[i][1] * tile_size
                self.black_knight_img_rect.y = self.black_knight_img_rect.y - (self.black_knight_img_rect.y * 2) + 875

                screen.blit(self.black_knight_img, self.black_knight_img_rect)

        for i in range(0, 10):

            if self.black_rooks_inf[i][2] == True:

                self.black_rook_img_rect.x = self.black_rooks_inf[i][0] * tile_size
                self.black_rook_img_rect.y = self.black_rooks_inf[i][1] * tile_size
                self.black_rook_img_rect.y = self.black_rook_img_rect.y - (self.black_rook_img_rect.y * 2) + 875

                screen.blit(self.black_rook_img, self.black_rook_img_rect)

        for i in range(0, 9):

            if self.black_queens_inf[i][2] == True:

                self.black_queen_img_rect.x = self.black_queens_inf[i][0] * tile_size
                self.black_queen_img_rect.y = self.black_queens_inf[i][1] * tile_size
                self.black_queen_img_rect.y = self.black_queen_img_rect.y - (self.black_queen_img_rect.y * 2) + 875

                screen.blit(self.black_queen_img, self.black_queen_img_rect)

        if self.black_king_inf[0][2] == True:

            self.black_king_img_rect.x = self.black_king_inf[0][0] * tile_size
            self.black_king_img_rect.y = self.black_king_inf[0][1] * tile_size
            self.black_king_img_rect.y = self.black_king_img_rect.y - (self.black_king_img_rect.y * 2) + 875

            screen.blit(self.black_king_img, self.black_king_img_rect)

    def draw_pieces_black(self):

        for i in range(0, 8):

            if self.white_pawns_inf[i][2] == True:

                self.white_pawn_img_rect.x = self.white_pawns_inf[i][0] * tile_size
                self.white_pawn_img_rect.x = self.white_pawn_img_rect.x - (self.white_pawn_img_rect.x * 2) + 875
                self.white_pawn_img_rect.y = self.white_pawns_inf[i][1] * tile_size

                screen.blit(self.white_pawn_img, self.white_pawn_img_rect)

        for i in range(0, 2):

            if self.white_bishops_inf[i][2] == True:

                self.white_bishop_img_rect.x = self.white_bishops_inf[i][0] * tile_size
                self.white_bishop_img_rect.x = self.white_bishop_img_rect.x - (self.white_bishop_img_rect.x * 2) + 875
                self.white_bishop_img_rect.y = self.white_bishops_inf[i][1] * tile_size

                screen.blit(self.white_bishop_img, self.white_bishop_img_rect)

        for i in range(0, 2):

            if self.white_knights_inf[i][2] == True:

                self.white_knight_img_rect.x = self.white_knights_inf[i][0] * tile_size
                self.white_knight_img_rect.x = self.white_knight_img_rect.x - (self.white_knight_img_rect.x * 2) + 875
                self.white_knight_img_rect.y = self.white_knights_inf[i][1] * tile_size

                screen.blit(self.white_knight_img, self.white_knight_img_rect)

        for i in range(0, 2):

            if self.white_rooks_inf[i][2] == True:

                self.white_rook_img_rect.x = self.white_rooks_inf[i][0] * tile_size
                self.white_rook_img_rect.x = self.white_rook_img_rect.x - (self.white_rook_img_rect.x * 2) + 875
                self.white_rook_img_rect.y = self.white_rooks_inf[i][1] * tile_size

                screen.blit(self.white_rook_img, self.white_rook_img_rect)

        if self.white_queens_inf[0][2] == True:

            self.white_queen_img_rect.x = self.white_queens_inf[0][0] * tile_size
            self.white_queen_img_rect.x = self.white_queen_img_rect.x - (self.white_queen_img_rect.x * 2) + 875
            self.white_queen_img_rect.y = self.white_queens_inf[0][1] * tile_size

            screen.blit(self.white_queen_img, self.white_queen_img_rect)

        if self.white_king_inf[0][2] == True:

            self.white_king_img_rect.x = self.white_king_inf[0][0] * tile_size
            self.white_king_img_rect.x = self.white_king_img_rect.x - (self.white_king_img_rect.x * 2) + 875
            self.white_king_img_rect.y = self.white_king_inf[0][1] * tile_size

            screen.blit(self.white_king_img, self.white_king_img_rect)

        for i in range(0, 8):

            if self.black_pawns_inf[i][2] == True:

                self.black_pawn_img_rect.x = self.black_pawns_inf[i][0] * tile_size
                self.black_pawn_img_rect.x = self.black_pawn_img_rect.x - (self.black_pawn_img_rect.x * 2) + 875
                self.black_pawn_img_rect.y = self.black_pawns_inf[i][1] * tile_size

                screen.blit(self.black_pawn_img, self.black_pawn_img_rect)

        for i in range(0, 2):

            if self.black_bishops_inf[i][2] == True:

                self.black_bishop_img_rect.x = self.black_bishops_inf[i][0] * tile_size
                self.black_bishop_img_rect.x = self.black_bishop_img_rect.x - (self.black_bishop_img_rect.x * 2) + 875
                self.black_bishop_img_rect.y = self.black_bishops_inf[i][1] * tile_size

                screen.blit(self.black_bishop_img, self.black_bishop_img_rect)

        for i in range(0, 2):

            if self.black_knights_inf[i][2] == True:

                self.black_knight_img_rect.x = self.black_knights_inf[i][0] * tile_size
                self.black_knight_img_rect.x = self.black_knight_img_rect.x - (self.black_knight_img_rect.x * 2) + 875
                self.black_knight_img_rect.y = self.black_knights_inf[i][1] * tile_size

                screen.blit(self.black_knight_img, self.black_knight_img_rect)

        for i in range(0, 2):

            if self.black_rooks_inf[i][2] == True:

                self.black_rook_img_rect.x = self.black_rooks_inf[i][0] * tile_size
                self.black_rook_img_rect.x = self.black_rook_img_rect.x - (self.black_rook_img_rect.x * 2) + 875
                self.black_rook_img_rect.y = self.black_rooks_inf[i][1] * tile_size

                screen.blit(self.black_rook_img, self.black_rook_img_rect)

        if self.black_queens_inf[0][2] == True:

            self.black_queen_img_rect.x = self.black_queens_inf[0][0] * tile_size
            self.black_queen_img_rect.x = self.black_queen_img_rect.x - (self.black_queen_img_rect.x * 2) + 875
            self.black_queen_img_rect.y = self.black_queens_inf[0][1] * tile_size

            screen.blit(self.black_queen_img, self.black_queen_img_rect)

        if self.black_king_inf[0][2] == True:

            self.black_king_img_rect.x = self.black_king_inf[0][0] * tile_size
            self.black_king_img_rect.x = self.black_king_img_rect.x - (self.black_king_img_rect.x * 2) + 875
            self.black_king_img_rect.y = self.black_king_inf[0][1] * tile_size

            screen.blit(self.black_king_img, self.black_king_img_rect)

    def white_black_occupation(self):

        self.white_occupation_x = []
        self.white_occupation_y = []
        
        self.black_occupation_x = []
        self.black_occupation_y = []

        for i in range(0, 8):

            if self.white_pawns_inf[i][2] == True:

                self.white_occupation_x.append(self.white_pawns_inf[i][0])
                self.white_occupation_y.append(self.white_pawns_inf[i][1])

        for i in range(0, 10):

            if self.white_knights_inf[i][2] == True:

                self.white_occupation_x.append(self.white_knights_inf[i][0])
                self.white_occupation_y.append(self.white_knights_inf[i][1])

        for i in range(0, 10):

            if self.white_bishops_inf[i][2] == True:

                self.white_occupation_x.append(self.white_bishops_inf[i][0])
                self.white_occupation_y.append(self.white_bishops_inf[i][1])

        for i in range(0, 10):

            if self.white_rooks_inf[i][2] == True:

                self.white_occupation_x.append(self.white_rooks_inf[i][0])
                self.white_occupation_y.append(self.white_rooks_inf[i][1])

        for i in range(0, 9):

            if self.white_queens_inf[i][2] == True:

                self.white_occupation_x.append(self.white_queens_inf[i][0])
                self.white_occupation_y.append(self.white_queens_inf[i][1])

        if self.white_king_inf[0][2] == True:

            self.white_occupation_x.append(self.white_king_inf[0][0])
            self.white_occupation_y.append(self.white_king_inf[0][1])

        for i in range(0, 8):

            if self.black_pawns_inf[i][2] == True:

                self.black_occupation_x.append(self.black_pawns_inf[i][0])
                self.black_occupation_y.append(self.black_pawns_inf[i][1])

        for i in range(0, 10):

            if self.black_knights_inf[i][2] == True:

                self.black_occupation_x.append(self.black_knights_inf[i][0])
                self.black_occupation_y.append(self.black_knights_inf[i][1])
                
        for i in range(0, 10):

            if self.black_bishops_inf[i][2] == True:

                self.black_occupation_x.append(self.black_bishops_inf[i][0])
                self.black_occupation_y.append(self.black_bishops_inf[i][1])

        for i in range(0, 10):

            if self.black_rooks_inf[i][2] == True:

                self.black_occupation_x.append(self.black_rooks_inf[i][0])
                self.black_occupation_y.append(self.black_rooks_inf[i][1])

        for i in range(0, 9):

            if self.black_queens_inf[i][2] == True:

                self.black_occupation_x.append(self.black_queens_inf[i][0])
                self.black_occupation_y.append(self.black_queens_inf[i][1])

        if self.black_king_inf[0][2] == True:

            self.black_occupation_x.append(self.black_king_inf[0][0])
            self.black_occupation_y.append(self.black_king_inf[0][1])

#        print(self.white_occupation_x)
#        print(self.white_occupation_y)
#        print(self.black_occupation_x)
#        print(self.black_occupation_y)

    def calc_legal_moves(self):

        self.legal_moves = []

        if white_turn == True:

            for i in range(0, 8):

                if self.white_pawns_inf[i][2] == True:

                    pawn_N_1 = True
                    pawn_N_2 = True
                    pawn_NE_11 = False
                    pawn_NW_11 = False

                    for j in range(0, len(self.white_occupation_x)):

                        if self.white_pawns_inf[i][0] == self.white_occupation_x[j] and self.white_pawns_inf[i][1] + 1 == self.white_occupation_y[j]:

                            pawn_N_1 = False

                        if self.white_pawns_inf[i][3] == True and self.white_pawns_inf[i][0] == self.white_occupation_x[j] and self.white_pawns_inf[i][1] + 2 == self.white_occupation_y[j]:

                            pawn_N_2 = False

                    for j in range(0, len(self.black_occupation_x)):

                        if self.white_pawns_inf[i][0] == self.black_occupation_x[j] and self.white_pawns_inf[i][1] + 1 == self.black_occupation_y[j]:

                            pawn_N_1 = False

                        if self.white_pawns_inf[i][3] == True and self.white_pawns_inf[i][0] == self.black_occupation_x[j] and self.white_pawns_inf[i][1] + 2 == self.black_occupation_y[j]:

                            pawn_N_2 = False

                        if self.white_pawns_inf[i][0] + 1 == self.black_occupation_x[j] and self.white_pawns_inf[i][1] + 1 == self.black_occupation_y[j]:

                            pawn_NE_11 = True

                        if self.white_pawns_inf[i][0] - 1 == self.black_occupation_x[j] and self.white_pawns_inf[i][1] + 1 == self.black_occupation_y[j]:

                            pawn_NW_11 = True

                    if pawn_N_1 == True:

                        self.legal_moves.append(notation.get_notation("P", self.white_pawns_inf[i][0], self.white_pawns_inf[i][1], self.white_pawns_inf[i][0], self.white_pawns_inf[i][1] + 1))

                    if pawn_N_2 == True and pawn_N_1 == True and self.white_pawns_inf[i][3] == True:

                        self.legal_moves.append(notation.get_notation("P", self.white_pawns_inf[i][0], self.white_pawns_inf[i][1], self.white_pawns_inf[i][0], self.white_pawns_inf[i][1] + 2))

                    if pawn_NE_11 == True:

                        self.legal_moves.append(notation.get_notation("P", self.white_pawns_inf[i][0], self.white_pawns_inf[i][1], self.white_pawns_inf[i][0] + 1, self.white_pawns_inf[i][1] + 1))

                    if pawn_NW_11 == True:

                        self.legal_moves.append(notation.get_notation("P", self.white_pawns_inf[i][0], self.white_pawns_inf[i][1], self.white_pawns_inf[i][0] - 1, self.white_pawns_inf[i][1] + 1))

            for i in range(0, 10):

                if self.white_bishops_inf[i][2] == True:

                    move_list = ["bishop_NE_1", "bishop_NE_2", "bishop_NE_3", "bishop_NE_4", "bishop_NE_5", "bishop_NE_6", "bishop_NE_7", "bishop_SE_1", "bishop_SE_2", "bishop_SE_3", "bishop_SE_4", "bishop_SE_5", "bishop_SE_6", "bishop_SE_7", "bishop_SW_1", "bishop_SW_2", "bishop_SW_3", "bishop_SW_4", "bishop_SW_5", "bishop_SW_6", "bishop_SW_7", "bishop_NW_1", "bishop_NW_2", "bishop_NW_3", "bishop_NW_4", "bishop_NW_5", "bishop_NW_6", "bishop_NW_7"]

                    bishop_moves = {
                        "bishop_NE_1" : True,
                        "bishop_NE_2" : True,
                        "bishop_NE_3" : True,
                        "bishop_NE_4" : True,
                        "bishop_NE_5" : True,
                        "bishop_NE_6" : True,
                        "bishop_NE_7" : True,
                        "bishop_SE_1" : True,
                        "bishop_SE_2" : True,
                        "bishop_SE_3" : True,
                        "bishop_SE_4" : True,
                        "bishop_SE_5" : True,
                        "bishop_SE_6" : True,
                        "bishop_SE_7" : True,
                        "bishop_SW_1" : True,
                        "bishop_SW_2" : True,
                        "bishop_SW_3" : True,
                        "bishop_SW_4" : True,
                        "bishop_SW_5" : True,
                        "bishop_SW_6" : True,
                        "bishop_SW_7" : True,
                        "bishop_NW_1" : True,
                        "bishop_NW_2" : True,
                        "bishop_NW_3" : True,
                        "bishop_NW_4" : True,
                        "bishop_NW_5" : True,
                        "bishop_NW_6" : True,
                        "bishop_NW_7" : True,
                        }

                    for j in range(1, 8):
                        
                        if self.white_bishops_inf[i][0] - j < 0:

                            for move in move_list:

                                if move[8] == "W" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                        if self.white_bishops_inf[i][1] - j < 0:

                            for move in move_list:

                                if move[7] == "S" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                        if self.white_bishops_inf[i][0] + j > 7:

                            for move in move_list:

                                if move[8] == "E" and int(move[10]) >= j:

                                    bishop_moves[move] = False
                                    
                        if self.white_bishops_inf[i][1] + j > 7:

                            for move in move_list:

                                if move[7] == "N" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.white_occupation_x)):

                            if self.white_bishops_inf[i][0] + j == self.white_occupation_x[k] and self.white_bishops_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "N" and move[8] == "E" and int(move[10]) >= j:

                                        bishop_moves[move] = False

                            elif self.white_bishops_inf[i][0] + j == self.white_occupation_x[k] and self.white_bishops_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "S" and move[8] == "E" and int(move[10]) >= j:

                                        bishop_moves[move] = False

                            elif self.white_bishops_inf[i][0] - j == self.white_occupation_x[k] and self.white_bishops_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "S" and move[8] == "W" and int(move[10]) >= j:

                                        bishop_moves[move] = False

                            elif self.white_bishops_inf[i][0] - j == self.white_occupation_x[k] and self.white_bishops_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "N" and move[8] == "W" and int(move[10]) >= j:

                                        bishop_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.black_occupation_x)):

                            if self.white_bishops_inf[i][0] + j == self.black_occupation_x[k] and self.white_bishops_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "N" and move[8] == "E" and int(move[10]) > j:

                                        bishop_moves[move] = False

                            elif self.white_bishops_inf[i][0] + j == self.black_occupation_x[k] and self.white_bishops_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "S" and move[8] == "E" and int(move[10]) > j:

                                        bishop_moves[move] = False

                            elif self.white_bishops_inf[i][0] - j == self.black_occupation_x[k] and self.white_bishops_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "S" and move[8] == "W" and int(move[10]) > j:

                                        bishop_moves[move] = False

                            elif self.white_bishops_inf[i][0] - j == self.black_occupation_x[k] and self.white_bishops_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "N" and move[8] == "W" and int(move[10]) > j:

                                        bishop_moves[move] = False

                    for move in move_list:

                        if bishop_moves[move] == True:

                            if move[7] == "N" and move[8] == "E":
                            
                                self.legal_moves.append(notation.get_notation("B", self.white_bishops_inf[i][0], self.white_bishops_inf[i][1], self.white_bishops_inf[i][0] + int(move[10]), self.white_bishops_inf[i][1] + int(move[10])))

                            elif move[7] == "S" and move[8] == "E":
                            
                                self.legal_moves.append(notation.get_notation("B", self.white_bishops_inf[i][0], self.white_bishops_inf[i][1], self.white_bishops_inf[i][0] + int(move[10]), self.white_bishops_inf[i][1] - int(move[10])))

                            elif move[7] == "S" and move[8] == "W":
                            
                                self.legal_moves.append(notation.get_notation("B", self.white_bishops_inf[i][0], self.white_bishops_inf[i][1], self.white_bishops_inf[i][0] - int(move[10]), self.white_bishops_inf[i][1] - int(move[10])))

                            elif move[7] == "N" and move[8] == "W":
                            
                                self.legal_moves.append(notation.get_notation("B", self.white_bishops_inf[i][0], self.white_bishops_inf[i][1], self.white_bishops_inf[i][0] - int(move[10]), self.white_bishops_inf[i][1] + int(move[10])))
                                
            for i in range(0, 10):

                if self.white_knights_inf[i][2] == True:

                    knight_NE_21 = True
                    knight_NE_12 = True
                    knight_SE_12 = True
                    knight_SE_21 = True
                    knight_SW_21 = True
                    knight_SW_12 = True
                    knight_NW_12 = True
                    knight_NW_21 = True

                    if self.white_knights_inf[i][0] - 1 < 0:

                        knight_SW_21 = False
                        knight_SW_12 = False
                        knight_NW_12 = False
                        knight_NW_21 = False

                    elif self.white_knights_inf[i][0] - 2 < 0:

                        knight_SW_12 = False
                        knight_NW_12 = False

                    if self.white_knights_inf[i][0] + 1 > 7:

                        knight_NE_21 = False
                        knight_NE_12 = False
                        knight_SE_12 = False
                        knight_SE_21 = False

                    elif self.white_knights_inf[i][0] + 2 > 7:

                        knight_NE_12 = False
                        knight_SE_12 = False

                    if self.white_knights_inf[i][1] - 1 < 0:

                        knight_SE_12 = False
                        knight_SE_21 = False
                        knight_SW_21 = False
                        knight_SW_12 = False

                    elif self.white_knights_inf[i][1] - 2 < 0:

                        knight_SE_21 = False
                        knight_SW_21 = False

                    if self.white_knights_inf[i][1] + 1 > 7:

                        knight_NE_21 = False
                        knight_NE_12 = False
                        knight_NW_12 = False
                        knight_NW_21 = False

                    elif self.white_knights_inf[i][1] + 2 > 7:

                        knight_NE_21 = False
                        knight_NW_21 = False

                    for j in range(0, len(self.white_occupation_x)):

                        if self.white_knights_inf[i][0] + 1 == self.white_occupation_x[j] and self.white_knights_inf[i][1] + 2 == self.white_occupation_y[j]:

                            knight_NE_21 = False

                        if self.white_knights_inf[i][0] + 2 == self.white_occupation_x[j] and self.white_knights_inf[i][1] + 1 == self.white_occupation_y[j]:

                            knight_NE_12 = False

                        if self.white_knights_inf[i][0] + 2 == self.white_occupation_x[j] and self.white_knights_inf[i][1] - 1 == self.white_occupation_y[j]:

                            knight_SE_12 = False

                        if self.white_knights_inf[i][0] + 1 == self.white_occupation_x[j] and self.white_knights_inf[i][1] - 2 == self.white_occupation_y[j]:

                            knight_SE_21 = False

                        if self.white_knights_inf[i][0] - 1 == self.white_occupation_x[j] and self.white_knights_inf[i][1] - 2 == self.white_occupation_y[j]:

                            knight_SW_21 = False

                        if self.white_knights_inf[i][0] - 2 == self.white_occupation_x[j] and self.white_knights_inf[i][1] - 1 == self.white_occupation_y[j]:

                            knight_SW_12 = False

                        if self.white_knights_inf[i][0] - 2 == self.white_occupation_x[j] and self.white_knights_inf[i][1] + 1 == self.white_occupation_y[j]:

                            knight_NW_12 = False

                        if self.white_knights_inf[i][0] - 1 == self.white_occupation_x[j] and self.white_knights_inf[i][1] + 2 == self.white_occupation_y[j]:

                            knight_NW_21 = False

                    if knight_NE_21 == True:

                        self.legal_moves.append(notation.get_notation("N", self.white_knights_inf[i][0], self.white_knights_inf[i][1], self.white_knights_inf[i][0] + 1, self.white_knights_inf[i][1] + 2))

                    if knight_NE_12 == True:

                        self.legal_moves.append(notation.get_notation("N", self.white_knights_inf[i][0], self.white_knights_inf[i][1], self.white_knights_inf[i][0] + 2, self.white_knights_inf[i][1] + 1))

                    if knight_SE_12 == True:

                        self.legal_moves.append(notation.get_notation("N", self.white_knights_inf[i][0], self.white_knights_inf[i][1], self.white_knights_inf[i][0] + 2, self.white_knights_inf[i][1] - 1))

                    if knight_SE_21 == True:

                        self.legal_moves.append(notation.get_notation("N", self.white_knights_inf[i][0], self.white_knights_inf[i][1], self.white_knights_inf[i][0] + 1, self.white_knights_inf[i][1] - 2))

                    if knight_SW_21 == True:

                        self.legal_moves.append(notation.get_notation("N", self.white_knights_inf[i][0], self.white_knights_inf[i][1], self.white_knights_inf[i][0] - 1, self.white_knights_inf[i][1] - 2))

                    if knight_SW_12 == True:

                        self.legal_moves.append(notation.get_notation("N", self.white_knights_inf[i][0], self.white_knights_inf[i][1], self.white_knights_inf[i][0] - 2, self.white_knights_inf[i][1] - 1))

                    if knight_NW_12 == True:

                        self.legal_moves.append(notation.get_notation("N", self.white_knights_inf[i][0], self.white_knights_inf[i][1], self.white_knights_inf[i][0] - 2, self.white_knights_inf[i][1] + 1))

                    if knight_NW_21 == True:

                        self.legal_moves.append(notation.get_notation("N", self.white_knights_inf[i][0], self.white_knights_inf[i][1], self.white_knights_inf[i][0] - 1, self.white_knights_inf[i][1] + 2))

            for i in range(0, 10):

                if self.white_rooks_inf[i][2] == True:

                    move_list = ["rook_N_1", "rook_N_2", "rook_N_3", "rook_N_4", "rook_N_5", "rook_N_6", "rook_N_7", "rook_E_1", "rook_E_2", "rook_E_3", "rook_E_4", "rook_E_5", "rook_E_6", "rook_E_7", "rook_S_1", "rook_S_2", "rook_S_3", "rook_S_4", "rook_S_5", "rook_S_6", "rook_S_7", "rook_W_1", "rook_W_2", "rook_W_3", "rook_W_4", "rook_W_5", "rook_W_6", "rook_W_7"]

                    rook_moves = {
                        "rook_N_1" : True,
                        "rook_N_2" : True,
                        "rook_N_3" : True,
                        "rook_N_4" : True,
                        "rook_N_5" : True,
                        "rook_N_6" : True,
                        "rook_N_7" : True,
                        "rook_E_1" : True,
                        "rook_E_2" : True,
                        "rook_E_3" : True,
                        "rook_E_4" : True,
                        "rook_E_5" : True,
                        "rook_E_6" : True,
                        "rook_E_7" : True,
                        "rook_S_1" : True,
                        "rook_S_2" : True,
                        "rook_S_3" : True,
                        "rook_S_4" : True,
                        "rook_S_5" : True,
                        "rook_S_6" : True,
                        "rook_S_7" : True,
                        "rook_W_1" : True,
                        "rook_W_2" : True,
                        "rook_W_3" : True,
                        "rook_W_4" : True,
                        "rook_W_5" : True,
                        "rook_W_6" : True,
                        "rook_W_7" : True,
                        }

                    for j in range(1, 8):
                        
                        if self.white_rooks_inf[i][0] - j < 0:

                            for move in move_list:

                                if move[5] == "W" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        if self.white_rooks_inf[i][1] - j < 0:

                            for move in move_list:

                                if move[5] == "S" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        if self.white_rooks_inf[i][0] + j > 7:

                            for move in move_list:

                                if move[5] == "E" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        if self.white_rooks_inf[i][1] + j > 7:

                            for move in move_list:

                                if move[5] == "N" and int(move[7]) >= j:

                                    rook_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.white_occupation_x)):

                            if self.white_rooks_inf[i][0] == self.white_occupation_x[k] and self.white_rooks_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "N" and int(move[7]) >= j:

                                        rook_moves[move] = False

                            elif self.white_rooks_inf[i][0] + j == self.white_occupation_x[k] and self.white_rooks_inf[i][1] == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "E" and int(move[7]) >= j:

                                        rook_moves[move] = False

                            elif self.white_rooks_inf[i][0] == self.white_occupation_x[k] and self.white_rooks_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "S" and int(move[7]) >= j:

                                        rook_moves[move] = False

                            elif self.white_rooks_inf[i][0] - j == self.white_occupation_x[k] and self.white_rooks_inf[i][1] == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "W" and int(move[7]) >= j:

                                        rook_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.black_occupation_x)):

                            if self.white_rooks_inf[i][0] == self.black_occupation_x[k] and self.white_rooks_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "N" and int(move[7]) > j:

                                        rook_moves[move] = False

                            elif self.white_rooks_inf[i][0] + j == self.black_occupation_x[k] and self.white_rooks_inf[i][1] == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "E" and int(move[7]) > j:

                                        rook_moves[move] = False

                            elif self.white_rooks_inf[i][0] == self.black_occupation_x[k] and self.white_rooks_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "S" and int(move[7]) > j:

                                        rook_moves[move] = False

                            elif self.white_rooks_inf[i][0] - j == self.black_occupation_x[k] and self.white_rooks_inf[i][1] == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "W" and int(move[7]) > j:

                                        rook_moves[move] = False

                    for move in move_list:

                        if rook_moves[move] == True:

                            if move[5] == "N":
                            
                                self.legal_moves.append(notation.get_notation("R", self.white_rooks_inf[i][0], self.white_rooks_inf[i][1], self.white_rooks_inf[i][0], self.white_rooks_inf[i][1] + int(move[7])))

                            elif move[5] == "E":
                            
                                self.legal_moves.append(notation.get_notation("R", self.white_rooks_inf[i][0], self.white_rooks_inf[i][1], self.white_rooks_inf[i][0] + int(move[7]), self.white_rooks_inf[i][1]))

                            elif move[5] == "S":
                            
                                self.legal_moves.append(notation.get_notation("R", self.white_rooks_inf[i][0], self.white_rooks_inf[i][1], self.white_rooks_inf[i][0], self.white_rooks_inf[i][1] - int(move[7])))

                            elif move[5] == "W":
                            
                                self.legal_moves.append(notation.get_notation("R", self.white_rooks_inf[i][0], self.white_rooks_inf[i][1], self.white_rooks_inf[i][0] - int(move[7]), self.white_rooks_inf[i][1]))

            for i in range(0, 9):

                if self.white_queens_inf[i][2] == True:

                    move_list = ["queen_N_1", "queen_N_2", "queen_N_3", "queen_N_4", "queen_N_5", "queen_N_6", "queen_N_7", "queen_NE_1", "queen_NE_2", "queen_NE_3", "queen_NE_4", "queen_NE_5", "queen_NE_6", "queen_NE_7", "queen_E_1", "queen_E_2", "queen_E_3", "queen_E_4", "queen_E_5", "queen_E_6", "queen_E_7", "queen_SE_1", "queen_SE_2", "queen_SE_3", "queen_SE_4", "queen_SE_5", "queen_SE_6", "queen_SE_7", "queen_S_1", "queen_S_2", "queen_S_3", "queen_S_4", "queen_S_5", "queen_S_6", "queen_S_7", "queen_SW_1", "queen_SW_2", "queen_SW_3", "queen_SW_4", "queen_SW_5", "queen_SW_6", "queen_SW_7", "queen_W_1", "queen_W_2", "queen_W_3", "queen_W_4", "queen_W_5", "queen_W_6", "queen_W_7", "queen_NW_1", "queen_NW_2", "queen_NW_3", "queen_NW_4", "queen_NW_5", "queen_NW_6", "queen_NW_7"]

                    queen_moves = {
                        "queen_N_1" : True,
                        "queen_N_2" : True,
                        "queen_N_3" : True,
                        "queen_N_4" : True,
                        "queen_N_5" : True,
                        "queen_N_6" : True,
                        "queen_N_7" : True,
                        "queen_NE_1" : True,
                        "queen_NE_2" : True,
                        "queen_NE_3" : True,
                        "queen_NE_4" : True,
                        "queen_NE_5" : True,
                        "queen_NE_6" : True,
                        "queen_NE_7" : True,
                        "queen_E_1" : True,
                        "queen_E_2" : True,
                        "queen_E_3" : True,
                        "queen_E_4" : True,
                        "queen_E_5" : True,
                        "queen_E_6" : True,
                        "queen_E_7" : True,
                        "queen_SE_1" : True,
                        "queen_SE_2" : True,
                        "queen_SE_3" : True,
                        "queen_SE_4" : True,
                        "queen_SE_5" : True,
                        "queen_SE_6" : True,
                        "queen_SE_7" : True,
                        "queen_S_1" : True,
                        "queen_S_2" : True,
                        "queen_S_3" : True,
                        "queen_S_4" : True,
                        "queen_S_5" : True,
                        "queen_S_6" : True,
                        "queen_S_7" : True,
                        "queen_SW_1" : True,
                        "queen_SW_2" : True,
                        "queen_SW_3" : True,
                        "queen_SW_4" : True,
                        "queen_SW_5" : True,
                        "queen_SW_6" : True,
                        "queen_SW_7" : True,
                        "queen_W_1" : True,
                        "queen_W_2" : True,
                        "queen_W_3" : True,
                        "queen_W_4" : True,
                        "queen_W_5" : True,
                        "queen_W_6" : True,
                        "queen_W_7" : True,
                        "queen_NW_1" : True,
                        "queen_NW_2" : True,
                        "queen_NW_3" : True,
                        "queen_NW_4" : True,
                        "queen_NW_5" : True,
                        "queen_NW_6" : True,
                        "queen_NW_7" : True,
                        }

                    for j in range(1, 8):
                        
                        if self.white_queens_inf[i][0] - j < 0:

                            for move in move_list:

                                if move[6] == "W" or move[7] == "W":

                                    if move[7] == "_":

                                        if int(move[8]) >= j:

                                            queen_moves[move] = False

                                    elif int(move[9]) >= j:

                                        queen_moves[move] = False

                        if self.white_queens_inf[i][1] - j < 0:

                            for move in move_list:

                                if move[6] == "S":

                                    if move[7] == "_":

                                        if int(move[8]) >= j:

                                            queen_moves[move] = False

                                    elif int(move[9]) >= j:

                                        queen_moves[move] = False

                        if self.white_queens_inf[i][0] + j > 7:

                            for move in move_list:

                                if move[6] == "E" or move[7] == "E":

                                    if move[7] == "_":

                                        if int(move[8]) >= j:

                                            queen_moves[move] = False

                                    elif int(move[9]) >= j:

                                        queen_moves[move] = False

                        if self.white_queens_inf[i][1] + j > 7:

                            for move in move_list:

                                if move[6] == "N":

                                    if move[7] == "_":

                                        if int(move[8]) >= j:

                                            queen_moves[move] = False

                                    elif int(move[9]) >= j:

                                        queen_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.white_occupation_x)):

                            if self.white_queens_inf[i][0] == self.white_occupation_x[k] and self.white_queens_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "_" and int(move[8]) >= j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] + j == self.white_occupation_x[k] and self.white_queens_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "E" and int(move[9]) >= j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] + j == self.white_occupation_x[k] and self.white_queens_inf[i][1] == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "E" and move[7] == "_" and int(move[8]) >= j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] + j == self.white_occupation_x[k] and self.white_queens_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "E" and int(move[9]) >= j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] == self.white_occupation_x[k] and self.white_queens_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "_" and int(move[8]) >= j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] - j == self.white_occupation_x[k] and self.white_queens_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "W" and int(move[9]) >= j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] - j == self.white_occupation_x[k] and self.white_queens_inf[i][1] == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "W" and move[7] == "_" and int(move[8]) >= j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] - j == self.white_occupation_x[k] and self.white_queens_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "W" and int(move[9]) >= j:

                                        queen_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.black_occupation_x)):

                            if self.white_queens_inf[i][0] == self.black_occupation_x[k] and self.white_queens_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "_" and int(move[8]) > j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] + j == self.black_occupation_x[k] and self.white_queens_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "E" and int(move[9]) > j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] + j == self.black_occupation_x[k] and self.white_queens_inf[i][1] == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "E" and move[7] == "_" and int(move[8]) > j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] + j == self.black_occupation_x[k] and self.white_queens_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "E" and int(move[9]) > j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] == self.black_occupation_x[k] and self.white_queens_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "_" and int(move[8]) > j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] - j == self.black_occupation_x[k] and self.white_queens_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "W" and int(move[9]) > j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] - j == self.black_occupation_x[k] and self.white_queens_inf[i][1] == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "W" and move[7] == "_" and int(move[8]) > j:

                                        queen_moves[move] = False

                            elif self.white_queens_inf[i][0] - j == self.black_occupation_x[k] and self.white_queens_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "W" and int(move[9]) > j:

                                        queen_moves[move] = False

                    for move in move_list:

                        if queen_moves[move] == True:

                            if move[6] == "N" and move[7] == "_":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.white_queens_inf[i][0], self.white_queens_inf[i][1], self.white_queens_inf[i][0], self.white_queens_inf[i][1] + int(move[8])))

                            elif move[6] == "N" and move[7] == "E":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.white_queens_inf[i][0], self.white_queens_inf[i][1], self.white_queens_inf[i][0] + int(move[9]), self.white_queens_inf[i][1] + int(move[9])))

                            elif move[6] == "E" and move[7] == "_":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.white_queens_inf[i][0], self.white_queens_inf[i][1], self.white_queens_inf[i][0] + int(move[8]), self.white_queens_inf[i][1]))

                            elif move[6] == "S" and move[7] == "E":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.white_queens_inf[i][0], self.white_queens_inf[i][1], self.white_queens_inf[i][0] + int(move[9]), self.white_queens_inf[i][1] - int(move[9])))

                            elif move[6] == "S" and move[7] == "_":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.white_queens_inf[i][0], self.white_queens_inf[i][1], self.white_queens_inf[i][0], self.white_queens_inf[i][1] - int(move[8])))

                            elif move[6] == "S" and move[7] == "W":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.white_queens_inf[i][0], self.white_queens_inf[i][1], self.white_queens_inf[i][0] - int(move[9]), self.white_queens_inf[i][1] - int(move[9])))

                            elif move[6] == "W" and move[7] == "_":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.white_queens_inf[i][0], self.white_queens_inf[i][1], self.white_queens_inf[i][0] - int(move[8]), self.white_queens_inf[i][1]))

                            elif move[6] == "N" and move[7] == "W":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.white_queens_inf[i][0], self.white_queens_inf[i][1], self.white_queens_inf[i][0] - int(move[9]), self.white_queens_inf[i][1] + int(move[9])))

            if self.white_king_inf[0][2] == True:

                move_list = ["king_N_1", "king_NE_1", "king_E_1", "king_SE_1", "king_S_1", "king_SW_1", "king_W_1", "king_NW_1"]

                king_moves = {
                    "king_N_1" : True,
                    "king_NE_1" : True,
                    "king_E_1" : True,
                    "king_SE_1" : True,
                    "king_S_1" : True,
                    "king_SW_1" : True,
                    "king_W_1" : True,
                    "king_NW_1" : True,
                    }
                        
                if self.white_king_inf[0][0] - 1 < 0:

                    for move in move_list:

                        if move[5] == "W" or move[6] == "W":

                            king_moves[move] = False

                if self.white_king_inf[0][1] - 1 < 0:

                    for move in move_list:

                        if move[5] == "S":

                            king_moves[move] = False

                if self.white_king_inf[0][0] + 1 > 7:

                    for move in move_list:

                        if move[5] == "E" or move[6] == "E":

                            king_moves[move] = False

                if self.white_king_inf[0][1] + 1 > 7:

                    for move in move_list:

                        if move[5] == "N":

                            king_moves[move] = False

                for i in range(0, len(self.white_occupation_x)):

                    if self.white_king_inf[0][0] == self.white_occupation_x[i] and self.white_king_inf[0][1] + 1 == self.white_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "N" and move[6] == "_":

                                king_moves[move] = False

                    elif self.white_king_inf[0][0] + 1 == self.white_occupation_x[i] and self.white_king_inf[0][1] + 1 == self.white_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "N" and move[6] == "E":

                                king_moves[move] = False

                    elif self.white_king_inf[0][0] + 1 == self.white_occupation_x[i] and self.white_king_inf[0][1] == self.white_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "E" and move[6] == "_":

                                king_moves[move] = False

                    elif self.white_king_inf[0][0] + 1 == self.white_occupation_x[i] and self.white_king_inf[0][1] - 1 == self.white_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "S" and move[6] == "E":

                                king_moves[move] = False

                    elif self.white_king_inf[0][0] == self.white_occupation_x[i] and self.white_king_inf[0][1] - 1 == self.white_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "S" and move[6] == "_":

                                king_moves[move] = False

                    elif self.white_king_inf[0][0] - 1 == self.white_occupation_x[i] and self.white_king_inf[0][1] - 1 == self.white_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "S" and move[6] == "W":

                                king_moves[move] = False

                    elif self.white_king_inf[0][0] - 1 == self.white_occupation_x[i] and self.white_king_inf[0][1] == self.white_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "W" and move[6] == "_":

                                king_moves[move] = False

                    elif self.white_king_inf[0][0] - 1 == self.white_occupation_x[i] and self.white_king_inf[0][1] + 1 == self.white_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "N" and move[6] == "W":

                                king_moves[move] = False

                for move in move_list:

                    if king_moves[move] == True:

                        if move[5] == "N" and move[6] == "_":
                            
                            self.legal_moves.append(notation.get_notation("K", self.white_king_inf[0][0], self.white_king_inf[0][1], self.white_king_inf[0][0], self.white_king_inf[0][1] + 1))

                        elif move[5] == "N" and move[6] == "E":
                            
                            self.legal_moves.append(notation.get_notation("K", self.white_king_inf[0][0], self.white_king_inf[0][1], self.white_king_inf[0][0] + 1, self.white_king_inf[0][1] + 1))

                        elif move[5] == "E" and move[6] == "_":
                            
                            self.legal_moves.append(notation.get_notation("K", self.white_king_inf[0][0], self.white_king_inf[0][1], self.white_king_inf[0][0] + 1, self.white_king_inf[0][1]))

                        elif move[5] == "S" and move[6] == "E":
                            
                            self.legal_moves.append(notation.get_notation("K", self.white_king_inf[0][0], self.white_king_inf[0][1], self.white_king_inf[0][0] + 1, self.white_king_inf[0][1] - 1))

                        elif move[5] == "S" and move[6] == "_":
                            
                            self.legal_moves.append(notation.get_notation("K", self.white_king_inf[0][0], self.white_king_inf[0][1], self.white_king_inf[0][0], self.white_king_inf[0][1] - 1))

                        elif move[5] == "S" and move[6] == "W":
                            
                            self.legal_moves.append(notation.get_notation("K", self.white_king_inf[0][0], self.white_king_inf[0][1], self.white_king_inf[0][0] - 1, self.white_king_inf[0][1] - 1))

                        elif move[5] == "W" and move[6] == "_":
                            
                            self.legal_moves.append(notation.get_notation("K", self.white_king_inf[0][0], self.white_king_inf[0][1], self.white_king_inf[0][0] - 1, self.white_king_inf[0][1]))

                        elif move[5] == "N" and move[6] == "W":
                            
                            self.legal_moves.append(notation.get_notation("K", self.white_king_inf[0][0], self.white_king_inf[0][1], self.white_king_inf[0][0] - 1, self.white_king_inf[0][1] + 1))
                            
        else:

            for i in range(0, 8):

                if self.black_pawns_inf[i][2] == True:

                    pawn_S_1 = True
                    pawn_S_2 = True
                    pawn_SE_11 = False
                    pawn_SW_11 = False

                    for j in range(0, len(self.black_occupation_x)):

                        if self.black_pawns_inf[i][0] == self.black_occupation_x[j] and self.black_pawns_inf[i][1] - 1 == self.black_occupation_y[j]:

                            pawn_S_1 = False

                        if self.black_pawns_inf[i][3] == True and self.black_pawns_inf[i][0] == self.black_occupation_x[j] and self.black_pawns_inf[i][1] - 2 == self.black_occupation_y[j]:

                            pawn_S_2 = False

                    for j in range(0, len(self.white_occupation_x)):

                        if self.black_pawns_inf[i][0] == self.white_occupation_x[j] and self.black_pawns_inf[i][1] - 1 == self.white_occupation_y[j]:

                            pawn_S_1 = False

                        if self.black_pawns_inf[i][3] == True and self.black_pawns_inf[i][0] == self.white_occupation_x[j] and self.black_pawns_inf[i][1] - 2 == self.white_occupation_y[j]:

                            pawn_S_2 = False

                        if self.black_pawns_inf[i][0] + 1 == self.white_occupation_x[j] and self.black_pawns_inf[i][1] - 1 == self.white_occupation_y[j]:

                            pawn_SE_11 = True

                        if self.black_pawns_inf[i][0] - 1 == self.white_occupation_x[j] and self.black_pawns_inf[i][1] - 1 == self.white_occupation_y[j]:

                            pawn_SW_11 = True

                    if pawn_S_1 == True:

                        self.legal_moves.append(notation.get_notation("P", self.black_pawns_inf[i][0], self.black_pawns_inf[i][1], self.black_pawns_inf[i][0], self.black_pawns_inf[i][1] - 1))

                    if pawn_S_2 == True and pawn_S_1 == True and self.black_pawns_inf[i][3] == True:

                        self.legal_moves.append(notation.get_notation("P", self.black_pawns_inf[i][0], self.black_pawns_inf[i][1], self.black_pawns_inf[i][0], self.black_pawns_inf[i][1] - 2))

                    if pawn_SE_11 == True:

                        self.legal_moves.append(notation.get_notation("P", self.black_pawns_inf[i][0], self.black_pawns_inf[i][1], self.black_pawns_inf[i][0] + 1, self.black_pawns_inf[i][1] - 1))

                    if pawn_SW_11 == True:

                        self.legal_moves.append(notation.get_notation("P", self.black_pawns_inf[i][0], self.black_pawns_inf[i][1], self.black_pawns_inf[i][0] - 1, self.black_pawns_inf[i][1] - 1))

            for i in range(0, 10):

                if self.black_bishops_inf[i][2] == True:

                    move_list = ["bishop_NE_1", "bishop_NE_2", "bishop_NE_3", "bishop_NE_4", "bishop_NE_5", "bishop_NE_6", "bishop_NE_7", "bishop_SE_1", "bishop_SE_2", "bishop_SE_3", "bishop_SE_4", "bishop_SE_5", "bishop_SE_6", "bishop_SE_7", "bishop_SW_1", "bishop_SW_2", "bishop_SW_3", "bishop_SW_4", "bishop_SW_5", "bishop_SW_6", "bishop_SW_7", "bishop_NW_1", "bishop_NW_2", "bishop_NW_3", "bishop_NW_4", "bishop_NW_5", "bishop_NW_6", "bishop_NW_7"]

                    bishop_moves = {
                        "bishop_NE_1" : True,
                        "bishop_NE_2" : True,
                        "bishop_NE_3" : True,
                        "bishop_NE_4" : True,
                        "bishop_NE_5" : True,
                        "bishop_NE_6" : True,
                        "bishop_NE_7" : True,
                        "bishop_SE_1" : True,
                        "bishop_SE_2" : True,
                        "bishop_SE_3" : True,
                        "bishop_SE_4" : True,
                        "bishop_SE_5" : True,
                        "bishop_SE_6" : True,
                        "bishop_SE_7" : True,
                        "bishop_SW_1" : True,
                        "bishop_SW_2" : True,
                        "bishop_SW_3" : True,
                        "bishop_SW_4" : True,
                        "bishop_SW_5" : True,
                        "bishop_SW_6" : True,
                        "bishop_SW_7" : True,
                        "bishop_NW_1" : True,
                        "bishop_NW_2" : True,
                        "bishop_NW_3" : True,
                        "bishop_NW_4" : True,
                        "bishop_NW_5" : True,
                        "bishop_NW_6" : True,
                        "bishop_NW_7" : True,
                        }

                    for j in range(1, 8):
                        
                        if self.black_bishops_inf[i][0] - j < 0:

                            for move in move_list:

                                if move[8] == "W" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                        if self.black_bishops_inf[i][1] - j < 0:

                            for move in move_list:

                                if move[7] == "S" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                        if self.black_bishops_inf[i][0] + j > 7:

                            for move in move_list:

                                if move[8] == "E" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                        if self.black_bishops_inf[i][1] + j > 7:

                            for move in move_list:

                                if move[7] == "N" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.black_occupation_x)):

                            if self.black_bishops_inf[i][0] + j == self.black_occupation_x[k] and self.black_bishops_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "N" and move[8] == "E" and int(move[10]) >= j:

                                        bishop_moves[move] = False

                            elif self.black_bishops_inf[i][0] + j == self.black_occupation_x[k] and self.black_bishops_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "S" and move[8] == "E" and int(move[10]) >= j:

                                        bishop_moves[move] = False

                            elif self.black_bishops_inf[i][0] - j == self.black_occupation_x[k] and self.black_bishops_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "S" and move[8] == "W" and int(move[10]) >= j:

                                        bishop_moves[move] = False

                            elif self.black_bishops_inf[i][0] - j == self.black_occupation_x[k] and self.black_bishops_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "N" and move[8] == "W" and int(move[10]) >= j:

                                        bishop_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.white_occupation_x)):

                            if self.black_bishops_inf[i][0] + j == self.white_occupation_x[k] and self.black_bishops_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "N" and move[8] == "E" and int(move[10]) > j:

                                        bishop_moves[move] = False

                            elif self.black_bishops_inf[i][0] + j == self.white_occupation_x[k] and self.black_bishops_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "S" and move[8] == "E" and int(move[10]) > j:

                                        bishop_moves[move] = False

                            elif self.black_bishops_inf[i][0] - j == self.white_occupation_x[k] and self.black_bishops_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "S" and move[8] == "W" and int(move[10]) > j:

                                        bishop_moves[move] = False

                            elif self.black_bishops_inf[i][0] - j == self.white_occupation_x[k] and self.black_bishops_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[7] == "N" and move[8] == "W" and int(move[10]) > j:

                                        bishop_moves[move] = False

                    for move in move_list:

                        if bishop_moves[move] == True:

                            if move[7] == "N" and move[8] == "E":
                            
                                self.legal_moves.append(notation.get_notation("B", self.black_bishops_inf[i][0], self.black_bishops_inf[i][1], self.black_bishops_inf[i][0] + int(move[10]), self.black_bishops_inf[i][1] + int(move[10])))

                            elif move[7] == "S" and move[8] == "E":
                            
                                self.legal_moves.append(notation.get_notation("B", self.black_bishops_inf[i][0], self.black_bishops_inf[i][1], self.black_bishops_inf[i][0] + int(move[10]), self.black_bishops_inf[i][1] - int(move[10])))

                            elif move[7] == "S" and move[8] == "W":
                            
                                self.legal_moves.append(notation.get_notation("B", self.black_bishops_inf[i][0], self.black_bishops_inf[i][1], self.black_bishops_inf[i][0] - int(move[10]), self.black_bishops_inf[i][1] - int(move[10])))

                            elif move[7] == "N" and move[8] == "W":
                            
                                self.legal_moves.append(notation.get_notation("B", self.black_bishops_inf[i][0], self.black_bishops_inf[i][1], self.black_bishops_inf[i][0] - int(move[10]), self.black_bishops_inf[i][1] + int(move[10])))

            for i in range(0, 10):

                if self.black_knights_inf[i][2] == True:

                    knight_NE_21 = True
                    knight_NE_12 = True
                    knight_SE_12 = True
                    knight_SE_21 = True
                    knight_SW_21 = True
                    knight_SW_12 = True
                    knight_NW_12 = True
                    knight_NW_21 = True

                    if self.black_knights_inf[i][0] - 1 < 0:

                        knight_SW_21 = False
                        knight_SW_12 = False
                        knight_NW_12 = False
                        knight_NW_21 = False

                    elif self.black_knights_inf[i][0] - 2 < 0:

                        knight_SW_12 = False
                        knight_NW_12 = False

                    if self.black_knights_inf[i][0] + 1 > 7:

                        knight_NE_21 = False
                        knight_NE_12 = False
                        knight_SE_12 = False
                        knight_SE_21 = False

                    elif self.black_knights_inf[i][0] + 2 > 7:

                        knight_NE_12 = False
                        knight_SE_12 = False

                    if self.black_knights_inf[i][1] - 1 < 0:

                        knight_SE_12 = False
                        knight_SE_21 = False
                        knight_SW_21 = False
                        knight_SW_12 = False

                    elif self.black_knights_inf[i][1] - 2 < 0:

                        knight_SE_21 = False
                        knight_SW_21 = False

                    if self.black_knights_inf[i][1] + 1 > 7:

                        knight_NE_21 = False
                        knight_NE_12 = False
                        knight_NW_12 = False
                        knight_NW_21 = False

                    elif self.black_knights_inf[i][1] + 2 > 7:

                        knight_NE_21 = False
                        knight_NW_21 = False

                    for j in range(0, len(self.black_occupation_x)):

                        if self.black_knights_inf[i][0] + 1 == self.black_occupation_x[j] and self.black_knights_inf[i][1] + 2 == self.black_occupation_y[j]:

                            knight_NE_21 = False

                        if self.black_knights_inf[i][0] + 2 == self.black_occupation_x[j] and self.black_knights_inf[i][1] + 1 == self.black_occupation_y[j]:

                            knight_NE_12 = False

                        if self.black_knights_inf[i][0] + 2 == self.black_occupation_x[j] and self.black_knights_inf[i][1] - 1 == self.black_occupation_y[j]:

                            knight_SE_12 = False

                        if self.black_knights_inf[i][0] + 1 == self.black_occupation_x[j] and self.black_knights_inf[i][1] - 2 == self.black_occupation_y[j]:

                            knight_SE_21 = False

                        if self.black_knights_inf[i][0] - 1 == self.black_occupation_x[j] and self.black_knights_inf[i][1] - 2 == self.black_occupation_y[j]:

                            knight_SW_21 = False

                        if self.black_knights_inf[i][0] - 2 == self.black_occupation_x[j] and self.black_knights_inf[i][1] - 1 == self.black_occupation_y[j]:

                            knight_SW_12 = False

                        if self.black_knights_inf[i][0] - 2 == self.black_occupation_x[j] and self.black_knights_inf[i][1] + 1 == self.black_occupation_y[j]:

                            knight_NW_12 = False

                        if self.black_knights_inf[i][0] - 1 == self.black_occupation_x[j] and self.black_knights_inf[i][1] + 2 == self.black_occupation_y[j]:

                            knight_NW_21 = False

                    if knight_NE_21 == True:

                        self.legal_moves.append(notation.get_notation("N", self.black_knights_inf[i][0], self.black_knights_inf[i][1], self.black_knights_inf[i][0] + 1, self.black_knights_inf[i][1] + 2))

                    if knight_NE_12 == True:

                        self.legal_moves.append(notation.get_notation("N", self.black_knights_inf[i][0], self.black_knights_inf[i][1], self.black_knights_inf[i][0] + 2, self.black_knights_inf[i][1] + 1))

                    if knight_SE_12 == True:

                        self.legal_moves.append(notation.get_notation("N", self.black_knights_inf[i][0], self.black_knights_inf[i][1], self.black_knights_inf[i][0] + 2, self.black_knights_inf[i][1] - 1))

                    if knight_SE_21 == True:

                        self.legal_moves.append(notation.get_notation("N", self.black_knights_inf[i][0], self.black_knights_inf[i][1], self.black_knights_inf[i][0] + 1, self.black_knights_inf[i][1] - 2))

                    if knight_SW_21 == True:

                        self.legal_moves.append(notation.get_notation("N", self.black_knights_inf[i][0], self.black_knights_inf[i][1], self.black_knights_inf[i][0] - 1, self.black_knights_inf[i][1] - 2))

                    if knight_SW_12 == True:

                        self.legal_moves.append(notation.get_notation("N", self.black_knights_inf[i][0], self.black_knights_inf[i][1], self.black_knights_inf[i][0] - 2, self.black_knights_inf[i][1] - 1))

                    if knight_NW_12 == True:

                        self.legal_moves.append(notation.get_notation("N", self.black_knights_inf[i][0], self.black_knights_inf[i][1], self.black_knights_inf[i][0] - 2, self.black_knights_inf[i][1] + 1))

                    if knight_NW_21 == True:

                        self.legal_moves.append(notation.get_notation("N", self.black_knights_inf[i][0], self.black_knights_inf[i][1], self.black_knights_inf[i][0] - 1, self.black_knights_inf[i][1] + 2))

            for i in range(0, 10):

                if self.black_rooks_inf[i][2] == True:

                    move_list = ["rook_N_1", "rook_N_2", "rook_N_3", "rook_N_4", "rook_N_5", "rook_N_6", "rook_N_7", "rook_E_1", "rook_E_2", "rook_E_3", "rook_E_4", "rook_E_5", "rook_E_6", "rook_E_7", "rook_S_1", "rook_S_2", "rook_S_3", "rook_S_4", "rook_S_5", "rook_S_6", "rook_S_7", "rook_W_1", "rook_W_2", "rook_W_3", "rook_W_4", "rook_W_5", "rook_W_6", "rook_W_7"]

                    rook_moves = {
                        "rook_N_1" : True,
                        "rook_N_2" : True,
                        "rook_N_3" : True,
                        "rook_N_4" : True,
                        "rook_N_5" : True,
                        "rook_N_6" : True,
                        "rook_N_7" : True,
                        "rook_E_1" : True,
                        "rook_E_2" : True,
                        "rook_E_3" : True,
                        "rook_E_4" : True,
                        "rook_E_5" : True,
                        "rook_E_6" : True,
                        "rook_E_7" : True,
                        "rook_S_1" : True,
                        "rook_S_2" : True,
                        "rook_S_3" : True,
                        "rook_S_4" : True,
                        "rook_S_5" : True,
                        "rook_S_6" : True,
                        "rook_S_7" : True,
                        "rook_W_1" : True,
                        "rook_W_2" : True,
                        "rook_W_3" : True,
                        "rook_W_4" : True,
                        "rook_W_5" : True,
                        "rook_W_6" : True,
                        "rook_W_7" : True,
                        }

                    for j in range(1, 8):
                        
                        if self.black_rooks_inf[i][0] - j < 0:

                            for move in move_list:

                                if move[5] == "W" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        if self.black_rooks_inf[i][1] - j < 0:

                            for move in move_list:

                                if move[5] == "S" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        if self.black_rooks_inf[i][0] + j > 7:

                            for move in move_list:

                                if move[5] == "E" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        if self.black_rooks_inf[i][1] + j > 7:

                            for move in move_list:

                                if move[5] == "N" and int(move[7]) >= j:

                                    rook_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.black_occupation_x)):

                            if self.black_rooks_inf[i][0] == self.black_occupation_x[k] and self.black_rooks_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "N" and int(move[7]) >= j:

                                        rook_moves[move] = False

                            elif self.black_rooks_inf[i][0] + j == self.black_occupation_x[k] and self.black_rooks_inf[i][1] == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "E" and int(move[7]) >= j:

                                        rook_moves[move] = False

                            elif self.black_rooks_inf[i][0] == self.black_occupation_x[k] and self.black_rooks_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "S" and int(move[7]) >= j:

                                        rook_moves[move] = False

                            elif self.black_rooks_inf[i][0] - j == self.black_occupation_x[k] and self.black_rooks_inf[i][1] == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "W" and int(move[7]) >= j:

                                        rook_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.white_occupation_x)):

                            if self.black_rooks_inf[i][0] == self.white_occupation_x[k] and self.black_rooks_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "N" and int(move[7]) > j:

                                        rook_moves[move] = False

                            elif self.black_rooks_inf[i][0] + j == self.white_occupation_x[k] and self.black_rooks_inf[i][1] == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "E" and int(move[7]) > j:

                                        rook_moves[move] = False

                            elif self.black_rooks_inf[i][0] == self.white_occupation_x[k] and self.black_rooks_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "S" and int(move[7]) > j:

                                        rook_moves[move] = False

                            elif self.black_rooks_inf[i][0] - j == self.white_occupation_x[k] and self.black_rooks_inf[i][1] == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[5] == "W" and int(move[7]) > j:

                                        rook_moves[move] = False

                    for move in move_list:

                        if rook_moves[move] == True:

                            if move[5] == "N":
                            
                                self.legal_moves.append(notation.get_notation("R", self.black_rooks_inf[i][0], self.black_rooks_inf[i][1], self.black_rooks_inf[i][0], self.black_rooks_inf[i][1] + int(move[7])))

                            elif move[5] == "E":
                            
                                self.legal_moves.append(notation.get_notation("R", self.black_rooks_inf[i][0], self.black_rooks_inf[i][1], self.black_rooks_inf[i][0] + int(move[7]), self.black_rooks_inf[i][1]))

                            elif move[5] == "S":
                            
                                self.legal_moves.append(notation.get_notation("R", self.black_rooks_inf[i][0], self.black_rooks_inf[i][1], self.black_rooks_inf[i][0], self.black_rooks_inf[i][1] - int(move[7])))

                            elif move[5] == "W":
                            
                                self.legal_moves.append(notation.get_notation("R", self.black_rooks_inf[i][0], self.black_rooks_inf[i][1], self.black_rooks_inf[i][0] - int(move[7]), self.black_rooks_inf[i][1]))

            for i in range(0, 9):

                if self.black_queens_inf[i][2] == True:

                    move_list = ["queen_N_1", "queen_N_2", "queen_N_3", "queen_N_4", "queen_N_5", "queen_N_6", "queen_N_7", "queen_NE_1", "queen_NE_2", "queen_NE_3", "queen_NE_4", "queen_NE_5", "queen_NE_6", "queen_NE_7", "queen_E_1", "queen_E_2", "queen_E_3", "queen_E_4", "queen_E_5", "queen_E_6", "queen_E_7", "queen_SE_1", "queen_SE_2", "queen_SE_3", "queen_SE_4", "queen_SE_5", "queen_SE_6", "queen_SE_7", "queen_S_1", "queen_S_2", "queen_S_3", "queen_S_4", "queen_S_5", "queen_S_6", "queen_S_7", "queen_SW_1", "queen_SW_2", "queen_SW_3", "queen_SW_4", "queen_SW_5", "queen_SW_6", "queen_SW_7", "queen_W_1", "queen_W_2", "queen_W_3", "queen_W_4", "queen_W_5", "queen_W_6", "queen_W_7", "queen_NW_1", "queen_NW_2", "queen_NW_3", "queen_NW_4", "queen_NW_5", "queen_NW_6", "queen_NW_7"]

                    queen_moves = {
                        "queen_N_1" : True,
                        "queen_N_2" : True,
                        "queen_N_3" : True,
                        "queen_N_4" : True,
                        "queen_N_5" : True,
                        "queen_N_6" : True,
                        "queen_N_7" : True,
                        "queen_NE_1" : True,
                        "queen_NE_2" : True,
                        "queen_NE_3" : True,
                        "queen_NE_4" : True,
                        "queen_NE_5" : True,
                        "queen_NE_6" : True,
                        "queen_NE_7" : True,
                        "queen_E_1" : True,
                        "queen_E_2" : True,
                        "queen_E_3" : True,
                        "queen_E_4" : True,
                        "queen_E_5" : True,
                        "queen_E_6" : True,
                        "queen_E_7" : True,
                        "queen_SE_1" : True,
                        "queen_SE_2" : True,
                        "queen_SE_3" : True,
                        "queen_SE_4" : True,
                        "queen_SE_5" : True,
                        "queen_SE_6" : True,
                        "queen_SE_7" : True,
                        "queen_S_1" : True,
                        "queen_S_2" : True,
                        "queen_S_3" : True,
                        "queen_S_4" : True,
                        "queen_S_5" : True,
                        "queen_S_6" : True,
                        "queen_S_7" : True,
                        "queen_SW_1" : True,
                        "queen_SW_2" : True,
                        "queen_SW_3" : True,
                        "queen_SW_4" : True,
                        "queen_SW_5" : True,
                        "queen_SW_6" : True,
                        "queen_SW_7" : True,
                        "queen_W_1" : True,
                        "queen_W_2" : True,
                        "queen_W_3" : True,
                        "queen_W_4" : True,
                        "queen_W_5" : True,
                        "queen_W_6" : True,
                        "queen_W_7" : True,
                        "queen_NW_1" : True,
                        "queen_NW_2" : True,
                        "queen_NW_3" : True,
                        "queen_NW_4" : True,
                        "queen_NW_5" : True,
                        "queen_NW_6" : True,
                        "queen_NW_7" : True,
                        }

                    for j in range(1, 8):
                        
                        if self.black_queens_inf[i][0] - j < 0:

                            for move in move_list:

                                if move[6] == "W" or move[7] == "W":

                                    if move[7] == "_":

                                        if int(move[8]) >= j:

                                            queen_moves[move] = False

                                    elif int(move[9]) >= j:

                                        queen_moves[move] = False

                        if self.black_queens_inf[i][1] - j < 0:

                            for move in move_list:

                                if move[6] == "S":

                                    if move[7] == "_":

                                        if int(move[8]) >= j:

                                            queen_moves[move] = False

                                    elif int(move[9]) >= j:

                                        queen_moves[move] = False

                        if self.black_queens_inf[i][0] + j > 7:

                            for move in move_list:

                                if move[6] == "E" or move[7] == "E":

                                    if move[7] == "_":

                                        if int(move[8]) >= j:

                                            queen_moves[move] = False

                                    elif int(move[9]) >= j:

                                        queen_moves[move] = False

                        if self.black_queens_inf[i][1] + j > 7:

                            for move in move_list:

                                if move[6] == "N":

                                    if move[7] == "_":

                                        if int(move[8]) >= j:

                                            queen_moves[move] = False

                                    elif int(move[9]) >= j:

                                        queen_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.black_occupation_x)):

                            if self.black_queens_inf[i][0] == self.black_occupation_x[k] and self.black_queens_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "_" and int(move[8]) >= j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] + j == self.black_occupation_x[k] and self.black_queens_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "E" and int(move[9]) >= j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] + j == self.black_occupation_x[k] and self.black_queens_inf[i][1] == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "E" and move[7] == "_" and int(move[8]) >= j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] + j == self.black_occupation_x[k] and self.black_queens_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "E" and int(move[9]) >= j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] == self.black_occupation_x[k] and self.black_queens_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "_" and int(move[8]) >= j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] - j == self.black_occupation_x[k] and self.black_queens_inf[i][1] - j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "W" and int(move[9]) >= j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] - j == self.black_occupation_x[k] and self.black_queens_inf[i][1] == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "W" and move[7] == "_" and int(move[8]) >= j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] - j == self.black_occupation_x[k] and self.black_queens_inf[i][1] + j == self.black_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "W" and int(move[9]) >= j:

                                        queen_moves[move] = False

                    for j in range(1, 8):

                        for k in range(0, len(self.white_occupation_x)):

                            if self.black_queens_inf[i][0] == self.white_occupation_x[k] and self.black_queens_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "_" and int(move[8]) > j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] + j == self.white_occupation_x[k] and self.black_queens_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "E" and int(move[9]) > j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] + j == self.white_occupation_x[k] and self.black_queens_inf[i][1] == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "E" and move[7] == "_" and int(move[8]) > j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] + j == self.white_occupation_x[k] and self.black_queens_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "E" and int(move[9]) > j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] == self.white_occupation_x[k] and self.black_queens_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "_" and int(move[8]) > j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] - j == self.white_occupation_x[k] and self.black_queens_inf[i][1] - j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "S" and move[7] == "W" and int(move[9]) > j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] - j == self.white_occupation_x[k] and self.black_queens_inf[i][1] == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "W" and move[7] == "_" and int(move[8]) > j:

                                        queen_moves[move] = False

                            elif self.black_queens_inf[i][0] - j == self.white_occupation_x[k] and self.black_queens_inf[i][1] + j == self.white_occupation_y[k]:

                                for move in move_list:

                                    if move[6] == "N" and move[7] == "W" and int(move[9]) > j:

                                        queen_moves[move] = False

                    for move in move_list:

                        if queen_moves[move] == True:

                            if move[6] == "N" and move[7] == "_":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.black_queens_inf[i][0], self.black_queens_inf[i][1], self.black_queens_inf[i][0], self.black_queens_inf[i][1] + int(move[8])))

                            elif move[6] == "N" and move[7] == "E":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.black_queens_inf[i][0], self.black_queens_inf[i][1], self.black_queens_inf[i][0] + int(move[9]), self.black_queens_inf[i][1] + int(move[9])))

                            elif move[6] == "E" and move[7] == "_":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.black_queens_inf[i][0], self.black_queens_inf[i][1], self.black_queens_inf[i][0] + int(move[8]), self.black_queens_inf[i][1]))

                            elif move[6] == "S" and move[7] == "E":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.black_queens_inf[i][0], self.black_queens_inf[i][1], self.black_queens_inf[i][0] + int(move[9]), self.black_queens_inf[i][1] - int(move[9])))

                            elif move[6] == "S" and move[7] == "_":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.black_queens_inf[i][0], self.black_queens_inf[i][1], self.black_queens_inf[i][0], self.black_queens_inf[i][1] - int(move[8])))

                            elif move[6] == "S" and move[7] == "W":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.black_queens_inf[i][0], self.black_queens_inf[i][1], self.black_queens_inf[i][0] - int(move[9]), self.black_queens_inf[i][1] - int(move[9])))

                            elif move[6] == "W" and move[7] == "_":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.black_queens_inf[i][0], self.black_queens_inf[i][1], self.black_queens_inf[i][0] - int(move[8]), self.black_queens_inf[i][1]))

                            elif move[6] == "N" and move[7] == "W":
                            
                                self.legal_moves.append(notation.get_notation("Q", self.black_queens_inf[i][0], self.black_queens_inf[i][1], self.black_queens_inf[i][0] - int(move[9]), self.black_queens_inf[i][1] + int(move[9])))

            if self.black_king_inf[0][2] == True:

                move_list = ["king_N_1", "king_NE_1", "king_E_1", "king_SE_1", "king_S_1", "king_SW_1", "king_W_1", "king_NW_1"]

                king_moves = {
                    "king_N_1" : True,
                    "king_NE_1" : True,
                    "king_E_1" : True,
                    "king_SE_1" : True,
                    "king_S_1" : True,
                    "king_SW_1" : True,
                    "king_W_1" : True,
                    "king_NW_1" : True,
                    }
                        
                if self.black_king_inf[0][0] - 1 < 0:

                    for move in move_list:

                        if move[5] == "W" or move[6] == "W":

                            king_moves[move] = False

                if self.black_king_inf[0][1] - 1 < 0:

                    for move in move_list:

                        if move[5] == "S":

                            king_moves[move] = False

                if self.black_king_inf[0][0] + 1 > 7:

                    for move in move_list:

                        if move[5] == "E" or move[6] == "E":

                            king_moves[move] = False

                if self.black_king_inf[0][1] + 1 > 7:

                    for move in move_list:

                        if move[5] == "N":

                            king_moves[move] = False

                for i in range(0, len(self.black_occupation_x)):

                    if self.black_king_inf[0][0] == self.black_occupation_x[i] and self.black_king_inf[0][1] + 1 == self.black_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "N" and move[6] == "_":

                                king_moves[move] = False

                    elif self.black_king_inf[0][0] + 1 == self.black_occupation_x[i] and self.black_king_inf[0][1] + 1 == self.black_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "N" and move[6] == "E":

                                king_moves[move] = False

                    elif self.black_king_inf[0][0] + 1 == self.black_occupation_x[i] and self.black_king_inf[0][1] == self.black_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "E" and move[6] == "_":

                                king_moves[move] = False

                    elif self.black_king_inf[0][0] + 1 == self.black_occupation_x[i] and self.black_king_inf[0][1] - 1 == self.black_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "S" and move[6] == "E":

                                king_moves[move] = False

                    elif self.black_king_inf[0][0] == self.black_occupation_x[i] and self.black_king_inf[0][1] - 1 == self.black_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "S" and move[6] == "_":

                                king_moves[move] = False

                    elif self.black_king_inf[0][0] - 1 == self.black_occupation_x[i] and self.black_king_inf[0][1] - 1 == self.black_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "S" and move[6] == "W":

                                king_moves[move] = False

                    elif self.black_king_inf[0][0] - 1 == self.black_occupation_x[i] and self.black_king_inf[0][1] == self.black_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "W" and move[6] == "_":

                                king_moves[move] = False

                    elif self.black_king_inf[0][0] - 1 == self.black_occupation_x[i] and self.black_king_inf[0][1] + 1 == self.black_occupation_y[i]:

                        for move in move_list:

                            if move[5] == "N" and move[6] == "W":

                                king_moves[move] = False

                for move in move_list:

                    if king_moves[move] == True:

                        if move[5] == "N" and move[6] == "_":
                            
                            self.legal_moves.append(notation.get_notation("K", self.black_king_inf[0][0], self.black_king_inf[0][1], self.black_king_inf[0][0], self.black_king_inf[0][1] + 1))

                        elif move[5] == "N" and move[6] == "E":
                            
                            self.legal_moves.append(notation.get_notation("K", self.black_king_inf[0][0], self.black_king_inf[0][1], self.black_king_inf[0][0] + 1, self.black_king_inf[0][1] + 1))

                        elif move[5] == "E" and move[6] == "_":
                            
                            self.legal_moves.append(notation.get_notation("K", self.black_king_inf[0][0], self.black_king_inf[0][1], self.black_king_inf[0][0] + 1, self.black_king_inf[0][1]))

                        elif move[5] == "S" and move[6] == "E":
                            
                            self.legal_moves.append(notation.get_notation("K", self.black_king_inf[0][0], self.black_king_inf[0][1], self.black_king_inf[0][0] + 1, self.black_king_inf[0][1] - 1))

                        elif move[5] == "S" and move[6] == "_":
                            
                            self.legal_moves.append(notation.get_notation("K", self.black_king_inf[0][0], self.black_king_inf[0][1], self.black_king_inf[0][0], self.black_king_inf[0][1] - 1))

                        elif move[5] == "S" and move[6] == "W":
                            
                            self.legal_moves.append(notation.get_notation("K", self.black_king_inf[0][0], self.black_king_inf[0][1], self.black_king_inf[0][0] - 1, self.black_king_inf[0][1] - 1))

                        elif move[5] == "W" and move[6] == "_":
                            
                            self.legal_moves.append(notation.get_notation("K", self.black_king_inf[0][0], self.black_king_inf[0][1], self.black_king_inf[0][0] - 1, self.black_king_inf[0][1]))

                        elif move[5] == "N" and move[6] == "W":
                            
                            self.legal_moves.append(notation.get_notation("K", self.black_king_inf[0][0], self.black_king_inf[0][1], self.black_king_inf[0][0] - 1, self.black_king_inf[0][1] + 1))

        self.legal_moves_move_notation = self.legal_moves
        print(self.legal_moves)

    def check_checks(self):

        if white_turn == True:

            for move in self.legal_moves:

                pass

    def move_piece(self, notation_val):

        take = False

        if notation_val[-1] == "+":
            
            notation_val = notation_val.replace("+", "")

            print(notation_val)

        for character in notation_val:

            if character == "x":
                
                take = True
                notation_val = notation_val.replace("x", "")

        if notation_val[0] == "B":

            from_x = notation.get_column_char(notation_val[1])
            from_y = int(notation_val[2]) - 1

            to_x = notation.get_column_char(notation_val[3])
            to_y = int(notation_val[4]) - 1

            if white_turn == True:

                for i in range(0, 10):

                    if self.white_bishops_inf[i][2] == True and self.white_bishops_inf[i][0] == from_x and self.white_bishops_inf[i][1] == from_y:
                        
                        self.white_bishops_inf[i][0] = to_x
                        self.white_bishops_inf[i][1] = to_y

            else:

                for i in range(0, 10):

                    if self.black_bishops_inf[i][2] == True and self.black_bishops_inf[i][0] == from_x and self.black_bishops_inf[i][1] == from_y:
                        
                        self.black_bishops_inf[i][0] = to_x
                        self.black_bishops_inf[i][1] = to_y

        elif notation_val[0] == "N":

            from_x = notation.get_column_char(notation_val[1])
            from_y = int(notation_val[2]) - 1

            to_x = notation.get_column_char(notation_val[3])
            to_y = int(notation_val[4]) - 1

            if white_turn == True:

                for i in range(0, 10):

                    if self.white_knights_inf[i][2] == True and self.white_knights_inf[i][0] == from_x and self.white_knights_inf[i][1] == from_y:
                        
                        self.white_knights_inf[i][0] = to_x
                        self.white_knights_inf[i][1] = to_y

            else:

                for i in range(0, 10):

                    if self.black_knights_inf[i][2] == True and self.black_knights_inf[i][0] == from_x and self.black_knights_inf[i][1] == from_y:
                        
                        self.black_knights_inf[i][0] = to_x
                        self.black_knights_inf[i][1] = to_y

        elif notation_val[0] == "R":

            from_x = notation.get_column_char(notation_val[1])
            from_y = int(notation_val[2]) - 1

            to_x = notation.get_column_char(notation_val[3])
            to_y = int(notation_val[4]) - 1

            if white_turn == True:

                for i in range(0, 10):

                    if self.white_rooks_inf[i][2] == True and self.white_rooks_inf[i][0] == from_x and self.white_rooks_inf[i][1] == from_y:
                        
                        self.white_rooks_inf[i][0] = to_x
                        self.white_rooks_inf[i][1] = to_y
                        self.white_rooks_inf[i][3] = False

            else:

                for i in range(0, 10):

                    if self.black_rooks_inf[i][2] == True and self.black_rooks_inf[i][0] == from_x and self.black_rooks_inf[i][1] == from_y:
                        
                        self.black_rooks_inf[i][0] = to_x
                        self.black_rooks_inf[i][1] = to_y
                        self.black_rooks_inf[i][3] = False

        elif notation_val[0] == "Q":

            from_x = notation.get_column_char(notation_val[1])
            from_y = int(notation_val[2]) - 1

            to_x = notation.get_column_char(notation_val[3])
            to_y = int(notation_val[4]) - 1

            if white_turn == True:

                for i in range(0, 9):

                    if self.white_queens_inf[i][2] == True and self.white_queens_inf[i][0] == from_x and self.white_queens_inf[i][1] == from_y:
                        
                        self.white_queens_inf[i][0] = to_x
                        self.white_queens_inf[i][1] = to_y

            else:

                for i in range(0, 9):

                    if self.black_queens_inf[i][2] == True and self.black_queens_inf[i][0] == from_x and self.black_queens_inf[i][1] == from_y:
                        
                        self.black_queens_inf[i][0] = to_x
                        self.black_queens_inf[i][1] = to_y

        elif notation_val[0] == "K":

            from_x = notation.get_column_char(notation_val[1])
            from_y = int(notation_val[2]) - 1

            to_x = notation.get_column_char(notation_val[3])
            to_y = int(notation_val[4]) - 1

            if white_turn == True:

                if self.white_king_inf[0][2] == True and self.white_king_inf[0][0] == from_x and self.white_king_inf[0][1] == from_y:
                        
                    self.white_king_inf[0][0] = to_x
                    self.white_king_inf[0][1] = to_y
                    self.white_king_inf[0][3] = False

            else:

                if self.black_king_inf[0][2] == True and self.black_king_inf[0][0] == from_x and self.black_king_inf[0][1] == from_y:
                        
                    self.black_king_inf[0][0] = to_x
                    self.black_king_inf[0][1] = to_y
                    self.black_king_inf[0][3] = False

        else:

            if notation_val[-2] == "=":

                pass

            else:
                
                to_x = notation.get_column_char(notation_val[-2])
                to_y = int(notation_val[-1]) - 1

                if take == True:

                    from_x = notation.get_column_char(notation_val[-3])

                    if white_turn == True:
                        
                        from_y = to_y - 1

                    else:

                        from_y = to_y + 1

                    print(to_x)
                    print(to_y)
                    print(from_x)
                    print(from_y)

                else:

                    from_x = to_x

                    if white_turn == True:

                        if to_y == 3:

                            from_y = to_y - 2

                            for i in range(0, 8):

                                if self.white_pawns_inf[i][2] == True and self.white_pawns_inf[i][0] == from_x and self.white_pawns_inf[i][1] == to_y - 1:

                                    from_y = to_y - 1

                        else:

                            from_y = to_y - 1

                    else:

                        if to_y == 4:

                            from_y = to_y + 2

                            for i in range(0, 8):

                                if self.black_pawns_inf[i][2] == True and self.black_pawns_inf[i][0] == from_x and self.black_pawns_inf[i][1] == to_y + 1:

                                    from_y = to_y + 1

                        else:

                            from_y = to_y + 1

                if white_turn == True:

                    for i in range(0, 8):

                        if self.white_pawns_inf[i][2] == True and self.white_pawns_inf[i][0] == from_x and self.white_pawns_inf[i][1] == from_y:
                        
                            self.white_pawns_inf[i][0] = to_x
                            self.white_pawns_inf[i][1] = to_y
                            self.white_pawns_inf[i][3] = False

                            print(to_x)
                            print(to_y)
                            print(self.white_pawns_inf[i])

                else:

                    for i in range(0, 8):

                        if self.black_pawns_inf[i][2] == True and self.black_pawns_inf[i][0] == from_x and self.black_pawns_inf[i][1] == from_y:
                        
                            self.black_pawns_inf[i][0] = to_x
                            self.black_pawns_inf[i][1] = to_y
                            self.black_pawns_inf[i][3] = False

                            print(to_x)
                            print(to_y)
                            print(self.black_pawns_inf[i])

        if take == True:

            if white_turn == True:

                for i in range(0, 8):

                    if self.black_pawns_inf[i][2] == True and self.black_pawns_inf[i][0] == to_x and self.black_pawns_inf[i][1] == to_y:

                        self.black_pawns_inf[i][2] = False

                for i in range(0, 10):

                    if self.black_bishops_inf[i][2] == True and self.black_bishops_inf[i][0] == to_x and self.black_bishops_inf[i][1] == to_y:

                        self.black_bishops_inf[i][2] = False

                for i in range(0, 10):

                    if self.black_knights_inf[i][2] == True and self.black_knights_inf[i][0] == to_x and self.black_knights_inf[i][1] == to_y:

                        self.black_knights_inf[i][2] = False

                for i in range(0, 10):

                    if self.black_rooks_inf[i][2] == True and self.black_rooks_inf[i][0] == to_x and self.black_rooks_inf[i][1] == to_y:

                        self.black_rooks_inf[i][2] = False

                for i in range(0, 9):

                    if self.black_queens_inf[i][2] == True and self.black_queens_inf[i][0] == to_x and self.black_queens_inf[i][1] == to_y:

                        self.black_queens_inf[i][2] = False
                        
            else:

                for i in range(0, 8):

                    if self.white_pawns_inf[i][2] == True and self.white_pawns_inf[i][0] == to_x and self.white_pawns_inf[i][1] == to_y:

                        self.white_pawns_inf[i][2] = False

                for i in range(0, 10):

                    if self.white_bishops_inf[i][2] == True and self.white_bishops_inf[i][0] == to_x and self.white_bishops_inf[i][1] == to_y:

                        self.white_bishops_inf[i][2] = False

                for i in range(0, 10):

                    if self.white_knights_inf[i][2] == True and self.white_knights_inf[i][0] == to_x and self.white_knights_inf[i][1] == to_y:

                        self.white_knights_inf[i][2] = False

                for i in range(0, 10):

                    if self.white_rooks_inf[i][2] == True and self.white_rooks_inf[i][0] == to_x and self.white_rooks_inf[i][1] == to_y:

                        self.white_rooks_inf[i][2] = False

                for i in range(0, 9):

                    if self.white_queens_inf[i][2] == True and self.white_queens_inf[i][0] == to_x and self.white_queens_inf[i][1] == to_y:

                        self.white_queens_inf[i][2] = False

class Notation():

    def __init__(self):

        pass

    def get_notation(self, piece, from_x, from_y, to_x, to_y):

        notation_val = "error"

        capture = False

        if piece == "P":

            if to_x == from_x and (to_y == from_y + 1 or to_y == from_y - 1 or to_y == from_y + 2 or to_y == from_y - 2):
                
                notation_val = self.get_column(to_x) + self.get_row(to_y)

            elif (to_x == from_x + 1 or to_x == from_x - 1) and (to_y == from_y + 1 or to_y == from_y - 1):

                notation_val = self.get_column(from_x) + "x" + self.get_column(to_x) + self.get_row(to_y)

        else:

            if white_turn == True:

                for i in range(0, len(pieces.black_occupation_x)):

                    if to_x == pieces.black_occupation_x[i] and to_y == pieces.black_occupation_y[i]:

                        capture = True

            else:

                for i in range(0, len(pieces.white_occupation_x)):

                    if to_x == pieces.white_occupation_x[i] and to_y == pieces.white_occupation_y[i]:

                        capture = True

            if capture == True:
                        
                notation_val = piece + self.get_column(from_x) + self.get_row(from_y) + "x" + self.get_column(to_x) + self.get_row(to_y)

            else:

                notation_val = piece + self.get_column(from_x) + self.get_row(from_y) + self.get_column(to_x) + self.get_row(to_y)

        return notation_val

    def get_column(self, x):
        
        if x == 0:

            return "a"

        elif x == 1:

            return "b"

        elif x == 2:

            return "c"

        elif x == 3:

            return "d"

        elif x == 4:

            return "e"

        elif x == 5:

            return "f"

        elif x == 6:

            return "g"

        elif x == 7:

            return "h"

    def get_column_char(self, x):
        
        if x == "a":

            return 0

        elif x == "b":

            return 1

        elif x == "c":

            return 2

        elif x == "d":

            return 3

        elif x == "e":

            return 4

        elif x == "f":

            return 5

        elif x == "g":

            return 6

        elif x == "h":

            return 7

    def get_row(self, y):

        for i in range(0, 8):

            if y == i:

                return str(i + 1)

        if y != 0 and y != 1 and y != 2 and y != 3 and y != 4 and y != 5 and y != 6 and y != 7:

            return "9"
                
board = Board()
board.draw_board()

pieces = Pieces()

notation = Notation()

run = True
update = True
white_turn = True
playing_as_white = True

if playing_as_white == True:
    
    pieces.draw_pieces_white()

else:

    pieces.draw_pieces_black()

auto_move = True

while run:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            run = False

    if update == True:
        
        pygame.display.update()
        update = False

        time.sleep(0)

    if auto_move == True:
        
        pieces.white_black_occupation()
        pieces.calc_legal_moves()

        pieces.move_piece(pieces.legal_moves[random.randint(0, len(pieces.legal_moves) - 1)])
        
        board.draw_board()
        
        if playing_as_white == True:
            
            pieces.draw_pieces_white()

        else:
            
            pieces.draw_pieces_black()
            
        white_turn = not white_turn
        
        update = True

pygame.quit()
