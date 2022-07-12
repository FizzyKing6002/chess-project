import multiprocessing
import threading
import pygame
from pygame.locals import *
import os
import os.path
import random
import time
from tkinter import Tk
import math
from copy import deepcopy
import numpy
import Chess_v1 as chess

def engine(legal_moves, fen):

    get_move_thread = threading.Thread(target = get_move, args = (fen,))
    get_move_thread.start()

    #while chess.startup.run:

        #pass

    return legal_moves[random.randint(0, len(legal_moves) - 1)]
    #white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf

def get_move(fen):

    white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf, white_turn, en_passant_x_y, half_moves, turn_num = load_fen_position(fen)

    white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y = white_black_occupation(white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf)
    legal_moves = calc_legal_moves(white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y, en_passant_x_y)
    legal_moves = check_checks(legal_moves, white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf, white_turn)

    evaluation = evaluate(white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf)

    print(legal_moves)

    for move in legal_moves:

        

def evaluate(white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf):

    evaluation = 0

    for i in range(0, len(white_pawns_inf)):

        if white_pawns_inf[i][2] = True:

            evaluation += 1

    for i in range(0, len(white_bishops_inf)):

        if white_bishops_inf[i][2] = True:

            evaluation += 3

    for i in range(0, len(white_knights_inf)):

        if white_knights_inf[i][2] = True:

            evaluation += 3

    for i in range(0, len(white_rooks_inf)):

        if white_rooks_inf[i][2] = True:

            evaluation += 5

    for i in range(0, len(white_queens_inf)):

        if white_queens_inf[i][2] = True:

            evaluation += 9

    for i in range(0, len(black_pawns_inf)):

        if black_pawns_inf[i][2] = True:

            evaluation -= 1

    for i in range(0, len(black_bishops_inf)):

        if black_bishops_inf[i][2] = True:

            evaluation -= 3

    for i in range(0, len(black_knights_inf)):

        if black_knights_inf[i][2] = True:

            evaluation -= 3

    for i in range(0, len(black_rooks_inf)):

        if black_rooks_inf[i][2] = True:

            evaluation -= 5

    for i in range(0, len(black_queens_inf)):

        if black_queens_inf[i][2] = True:

            evaluation -= 9

    return evaluation

def white_black_occupation(white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf):

    white_occupation_x = []
    white_occupation_y = []
    
    black_occupation_x = []
    black_occupation_y = []

    for i in range(0, 8):

        if white_pawns_inf[i][2] == True:

            white_occupation_x.append(white_pawns_inf[i][0])
            white_occupation_y.append(white_pawns_inf[i][1])

    for i in range(0, 10):

        if white_knights_inf[i][2] == True:

            white_occupation_x.append(white_knights_inf[i][0])
            white_occupation_y.append(white_knights_inf[i][1])

    for i in range(0, 10):

        if white_bishops_inf[i][2] == True:

            white_occupation_x.append(white_bishops_inf[i][0])
            white_occupation_y.append(white_bishops_inf[i][1])

    for i in range(0, 10):

        if white_rooks_inf[i][2] == True:

            white_occupation_x.append(white_rooks_inf[i][0])
            white_occupation_y.append(white_rooks_inf[i][1])

    for i in range(0, 9):

        if white_queens_inf[i][2] == True:

            white_occupation_x.append(white_queens_inf[i][0])
            white_occupation_y.append(white_queens_inf[i][1])

    if white_king_inf[0][2] == True:

        white_occupation_x.append(white_king_inf[0][0])
        white_occupation_y.append(white_king_inf[0][1])

    for i in range(0, 8):

        if black_pawns_inf[i][2] == True:

            black_occupation_x.append(black_pawns_inf[i][0])
            black_occupation_y.append(black_pawns_inf[i][1])

    for i in range(0, 10):

        if black_knights_inf[i][2] == True:

            black_occupation_x.append(black_knights_inf[i][0])
            black_occupation_y.append(black_knights_inf[i][1])
            
    for i in range(0, 10):

        if black_bishops_inf[i][2] == True:

            black_occupation_x.append(black_bishops_inf[i][0])
            black_occupation_y.append(black_bishops_inf[i][1])

    for i in range(0, 10):

        if black_rooks_inf[i][2] == True:

            black_occupation_x.append(black_rooks_inf[i][0])
            black_occupation_y.append(black_rooks_inf[i][1])

    for i in range(0, 9):

        if black_queens_inf[i][2] == True:

            black_occupation_x.append(black_queens_inf[i][0])
            black_occupation_y.append(black_queens_inf[i][1])

    if black_king_inf[0][2] == True:

        black_occupation_x.append(black_king_inf[0][0])
        black_occupation_y.append(black_king_inf[0][1])

    return white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y

def calc_legal_moves(white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y, en_passant_x_y):

    legal_moves = []

    if white_turn == True:

        for i in range(0, 8):

            if white_pawns_inf[i][2] == True:

                pawn_N_1 = True
                pawn_N_2 = True
                pawn_NE_11 = False
                pawn_NW_11 = False
                en_p_NE_11 = False
                en_p_NW_11 = False

                for j in range(0, len(white_occupation_x)):

                    if white_pawns_inf[i][0] == white_occupation_x[j] and white_pawns_inf[i][1] + 1 == white_occupation_y[j]:

                        pawn_N_1 = False

                    if white_pawns_inf[i][3] == True and white_pawns_inf[i][0] == white_occupation_x[j] and white_pawns_inf[i][1] + 2 == white_occupation_y[j]:

                        pawn_N_2 = False

                for j in range(0, len(black_occupation_x)):

                    if white_pawns_inf[i][0] == black_occupation_x[j] and white_pawns_inf[i][1] + 1 == black_occupation_y[j]:

                        pawn_N_1 = False

                    if white_pawns_inf[i][3] == True and white_pawns_inf[i][0] == black_occupation_x[j] and white_pawns_inf[i][1] + 2 == black_occupation_y[j]:

                        pawn_N_2 = False

                    if white_pawns_inf[i][0] + 1 == black_occupation_x[j] and white_pawns_inf[i][1] + 1 == black_occupation_y[j]:

                        pawn_NE_11 = True

                    if white_pawns_inf[i][0] - 1 == black_occupation_x[j] and white_pawns_inf[i][1] + 1 == black_occupation_y[j]:

                        pawn_NW_11 = True

                if white_pawns_inf[i][0] + 1 == en_passant_x_y[0] and white_pawns_inf[i][1] == en_passant_x_y[1]:

                    pawn_NE_11 = True

                elif white_pawns_inf[i][0] - 1 == en_passant_x_y[0] and white_pawns_inf[i][1] == en_passant_x_y[1]:

                    pawn_NW_11 = True

                if pawn_N_1 == True:

                    legal_move_notation = get_notation("P", white_pawns_inf[i][0], white_pawns_inf[i][1], white_pawns_inf[i][0], white_pawns_inf[i][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y)

                    if legal_move_notation[-1] == "=":

                        legal_moves.append(legal_move_notation + "Q")
                        legal_moves.append(legal_move_notation + "R")
                        legal_moves.append(legal_move_notation + "B")
                        legal_moves.append(legal_move_notation + "N")

                    else:

                        legal_moves.append(legal_move_notation)

                if pawn_N_2 == True and pawn_N_1 == True and white_pawns_inf[i][3] == True:

                    legal_move_notation = get_notation("P", white_pawns_inf[i][0], white_pawns_inf[i][1], white_pawns_inf[i][0], white_pawns_inf[i][1] + 2, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y)

                    if legal_move_notation[-1] == "=":

                        legal_moves.append(legal_move_notation + "Q")
                        legal_moves.append(legal_move_notation + "R")
                        legal_moves.append(legal_move_notation + "B")
                        legal_moves.append(legal_move_notation + "N")

                    else:

                        legal_moves.append(legal_move_notation)

                if pawn_NE_11 == True:

                    legal_move_notation = get_notation("P", white_pawns_inf[i][0], white_pawns_inf[i][1], white_pawns_inf[i][0] + 1, white_pawns_inf[i][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y)

                    if legal_move_notation[-1] == "=":

                        legal_moves.append(legal_move_notation + "Q")
                        legal_moves.append(legal_move_notation + "R")
                        legal_moves.append(legal_move_notation + "B")
                        legal_moves.append(legal_move_notation + "N")

                    else:

                        legal_moves.append(legal_move_notation)

                if pawn_NW_11 == True:

                    legal_move_notation = get_notation("P", white_pawns_inf[i][0], white_pawns_inf[i][1], white_pawns_inf[i][0] - 1, white_pawns_inf[i][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y)

                    if legal_move_notation[-1] == "=":

                        legal_moves.append(legal_move_notation + "Q")
                        legal_moves.append(legal_move_notation + "R")
                        legal_moves.append(legal_move_notation + "B")
                        legal_moves.append(legal_move_notation + "N")

                    else:

                        legal_moves.append(legal_move_notation)

        for i in range(0, 10):

            if white_bishops_inf[i][2] == True:

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
                    
                    if white_bishops_inf[i][0] - j < 0:

                        for move in move_list:

                            if move[8] == "W" and int(move[10]) >= j:

                                bishop_moves[move] = False

                    if white_bishops_inf[i][1] - j < 0:

                        for move in move_list:

                            if move[7] == "S" and int(move[10]) >= j:

                                bishop_moves[move] = False

                    if white_bishops_inf[i][0] + j > 7:

                        for move in move_list:

                            if move[8] == "E" and int(move[10]) >= j:

                                bishop_moves[move] = False
                                
                    if white_bishops_inf[i][1] + j > 7:

                        for move in move_list:

                            if move[7] == "N" and int(move[10]) >= j:

                                bishop_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(white_occupation_x)):

                        if white_bishops_inf[i][0] + j == white_occupation_x[k] and white_bishops_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "N" and move[8] == "E" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                        elif white_bishops_inf[i][0] + j == white_occupation_x[k] and white_bishops_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "S" and move[8] == "E" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                        elif white_bishops_inf[i][0] - j == white_occupation_x[k] and white_bishops_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "S" and move[8] == "W" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                        elif white_bishops_inf[i][0] - j == white_occupation_x[k] and white_bishops_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "N" and move[8] == "W" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(black_occupation_x)):

                        if white_bishops_inf[i][0] + j == black_occupation_x[k] and white_bishops_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "N" and move[8] == "E" and int(move[10]) > j:

                                    bishop_moves[move] = False

                        elif white_bishops_inf[i][0] + j == black_occupation_x[k] and white_bishops_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "S" and move[8] == "E" and int(move[10]) > j:

                                    bishop_moves[move] = False

                        elif white_bishops_inf[i][0] - j == black_occupation_x[k] and white_bishops_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "S" and move[8] == "W" and int(move[10]) > j:

                                    bishop_moves[move] = False

                        elif white_bishops_inf[i][0] - j == black_occupation_x[k] and white_bishops_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "N" and move[8] == "W" and int(move[10]) > j:

                                    bishop_moves[move] = False

                for move in move_list:

                    if bishop_moves[move] == True:

                        if move[7] == "N" and move[8] == "E":
                        
                            legal_moves.append(get_notation("B", white_bishops_inf[i][0], white_bishops_inf[i][1], white_bishops_inf[i][0] + int(move[10]), white_bishops_inf[i][1] + int(move[10]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[7] == "S" and move[8] == "E":
                        
                            legal_moves.append(get_notation("B", white_bishops_inf[i][0], white_bishops_inf[i][1], white_bishops_inf[i][0] + int(move[10]), white_bishops_inf[i][1] - int(move[10]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[7] == "S" and move[8] == "W":
                        
                            legal_moves.append(get_notation("B", white_bishops_inf[i][0], white_bishops_inf[i][1], white_bishops_inf[i][0] - int(move[10]), white_bishops_inf[i][1] - int(move[10]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[7] == "N" and move[8] == "W":
                        
                            legal_moves.append(get_notation("B", white_bishops_inf[i][0], white_bishops_inf[i][1], white_bishops_inf[i][0] - int(move[10]), white_bishops_inf[i][1] + int(move[10]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))
                            
        for i in range(0, 10):

            if white_knights_inf[i][2] == True:

                knight_NE_21 = True
                knight_NE_12 = True
                knight_SE_12 = True
                knight_SE_21 = True
                knight_SW_21 = True
                knight_SW_12 = True
                knight_NW_12 = True
                knight_NW_21 = True

                if white_knights_inf[i][0] - 1 < 0:

                    knight_SW_21 = False
                    knight_SW_12 = False
                    knight_NW_12 = False
                    knight_NW_21 = False

                elif white_knights_inf[i][0] - 2 < 0:

                    knight_SW_12 = False
                    knight_NW_12 = False

                if white_knights_inf[i][0] + 1 > 7:

                    knight_NE_21 = False
                    knight_NE_12 = False
                    knight_SE_12 = False
                    knight_SE_21 = False

                elif white_knights_inf[i][0] + 2 > 7:

                    knight_NE_12 = False
                    knight_SE_12 = False

                if white_knights_inf[i][1] - 1 < 0:

                    knight_SE_12 = False
                    knight_SE_21 = False
                    knight_SW_21 = False
                    knight_SW_12 = False

                elif white_knights_inf[i][1] - 2 < 0:

                    knight_SE_21 = False
                    knight_SW_21 = False

                if white_knights_inf[i][1] + 1 > 7:

                    knight_NE_21 = False
                    knight_NE_12 = False
                    knight_NW_12 = False
                    knight_NW_21 = False

                elif white_knights_inf[i][1] + 2 > 7:

                    knight_NE_21 = False
                    knight_NW_21 = False

                for j in range(0, len(white_occupation_x)):

                    if white_knights_inf[i][0] + 1 == white_occupation_x[j] and white_knights_inf[i][1] + 2 == white_occupation_y[j]:

                        knight_NE_21 = False

                    if white_knights_inf[i][0] + 2 == white_occupation_x[j] and white_knights_inf[i][1] + 1 == white_occupation_y[j]:

                        knight_NE_12 = False

                    if white_knights_inf[i][0] + 2 == white_occupation_x[j] and white_knights_inf[i][1] - 1 == white_occupation_y[j]:

                        knight_SE_12 = False

                    if white_knights_inf[i][0] + 1 == white_occupation_x[j] and white_knights_inf[i][1] - 2 == white_occupation_y[j]:

                        knight_SE_21 = False

                    if white_knights_inf[i][0] - 1 == white_occupation_x[j] and white_knights_inf[i][1] - 2 == white_occupation_y[j]:

                        knight_SW_21 = False

                    if white_knights_inf[i][0] - 2 == white_occupation_x[j] and white_knights_inf[i][1] - 1 == white_occupation_y[j]:

                        knight_SW_12 = False

                    if white_knights_inf[i][0] - 2 == white_occupation_x[j] and white_knights_inf[i][1] + 1 == white_occupation_y[j]:

                        knight_NW_12 = False

                    if white_knights_inf[i][0] - 1 == white_occupation_x[j] and white_knights_inf[i][1] + 2 == white_occupation_y[j]:

                        knight_NW_21 = False

                if knight_NE_21 == True:

                    legal_moves.append(get_notation("N", white_knights_inf[i][0], white_knights_inf[i][1], white_knights_inf[i][0] + 1, white_knights_inf[i][1] + 2, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_NE_12 == True:

                    legal_moves.append(get_notation("N", white_knights_inf[i][0], white_knights_inf[i][1], white_knights_inf[i][0] + 2, white_knights_inf[i][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_SE_12 == True:

                    legal_moves.append(get_notation("N", white_knights_inf[i][0], white_knights_inf[i][1], white_knights_inf[i][0] + 2, white_knights_inf[i][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_SE_21 == True:

                    legal_moves.append(get_notation("N", white_knights_inf[i][0], white_knights_inf[i][1], white_knights_inf[i][0] + 1, white_knights_inf[i][1] - 2, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_SW_21 == True:

                    legal_moves.append(get_notation("N", white_knights_inf[i][0], white_knights_inf[i][1], white_knights_inf[i][0] - 1, white_knights_inf[i][1] - 2, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_SW_12 == True:

                    legal_moves.append(get_notation("N", white_knights_inf[i][0], white_knights_inf[i][1], white_knights_inf[i][0] - 2, white_knights_inf[i][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_NW_12 == True:

                    legal_moves.append(get_notation("N", white_knights_inf[i][0], white_knights_inf[i][1], white_knights_inf[i][0] - 2, white_knights_inf[i][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_NW_21 == True:

                    legal_moves.append(get_notation("N", white_knights_inf[i][0], white_knights_inf[i][1], white_knights_inf[i][0] - 1, white_knights_inf[i][1] + 2, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

        for i in range(0, 10):

            if white_rooks_inf[i][2] == True:

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
                    
                    if white_rooks_inf[i][0] - j < 0:

                        for move in move_list:

                            if move[5] == "W" and int(move[7]) >= j:

                                rook_moves[move] = False

                    if white_rooks_inf[i][1] - j < 0:

                        for move in move_list:

                            if move[5] == "S" and int(move[7]) >= j:

                                rook_moves[move] = False

                    if white_rooks_inf[i][0] + j > 7:

                        for move in move_list:

                            if move[5] == "E" and int(move[7]) >= j:

                                rook_moves[move] = False

                    if white_rooks_inf[i][1] + j > 7:

                        for move in move_list:

                            if move[5] == "N" and int(move[7]) >= j:

                                rook_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(white_occupation_x)):

                        if white_rooks_inf[i][0] == white_occupation_x[k] and white_rooks_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "N" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        elif white_rooks_inf[i][0] + j == white_occupation_x[k] and white_rooks_inf[i][1] == white_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "E" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        elif white_rooks_inf[i][0] == white_occupation_x[k] and white_rooks_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "S" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        elif white_rooks_inf[i][0] - j == white_occupation_x[k] and white_rooks_inf[i][1] == white_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "W" and int(move[7]) >= j:

                                    rook_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(black_occupation_x)):

                        if white_rooks_inf[i][0] == black_occupation_x[k] and white_rooks_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "N" and int(move[7]) > j:

                                    rook_moves[move] = False

                        elif white_rooks_inf[i][0] + j == black_occupation_x[k] and white_rooks_inf[i][1] == black_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "E" and int(move[7]) > j:

                                    rook_moves[move] = False

                        elif white_rooks_inf[i][0] == black_occupation_x[k] and white_rooks_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "S" and int(move[7]) > j:

                                    rook_moves[move] = False

                        elif white_rooks_inf[i][0] - j == black_occupation_x[k] and white_rooks_inf[i][1] == black_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "W" and int(move[7]) > j:

                                    rook_moves[move] = False

                for move in move_list:

                    if rook_moves[move] == True:

                        if move[5] == "N":
                        
                            legal_moves.append(get_notation("R", white_rooks_inf[i][0], white_rooks_inf[i][1], white_rooks_inf[i][0], white_rooks_inf[i][1] + int(move[7]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[5] == "E":
                        
                            legal_moves.append(get_notation("R", white_rooks_inf[i][0], white_rooks_inf[i][1], white_rooks_inf[i][0] + int(move[7]), white_rooks_inf[i][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[5] == "S":
                        
                            legal_moves.append(get_notation("R", white_rooks_inf[i][0], white_rooks_inf[i][1], white_rooks_inf[i][0], white_rooks_inf[i][1] - int(move[7]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[5] == "W":
                        
                            legal_moves.append(get_notation("R", white_rooks_inf[i][0], white_rooks_inf[i][1], white_rooks_inf[i][0] - int(move[7]), white_rooks_inf[i][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

        for i in range(0, 9):

            if white_queens_inf[i][2] == True:

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
                    
                    if white_queens_inf[i][0] - j < 0:

                        for move in move_list:

                            if move[6] == "W" or move[7] == "W":

                                if move[7] == "_":

                                    if int(move[8]) >= j:

                                        queen_moves[move] = False

                                elif int(move[9]) >= j:

                                    queen_moves[move] = False

                    if white_queens_inf[i][1] - j < 0:

                        for move in move_list:

                            if move[6] == "S":

                                if move[7] == "_":

                                    if int(move[8]) >= j:

                                        queen_moves[move] = False

                                elif int(move[9]) >= j:

                                    queen_moves[move] = False

                    if white_queens_inf[i][0] + j > 7:

                        for move in move_list:

                            if move[6] == "E" or move[7] == "E":

                                if move[7] == "_":

                                    if int(move[8]) >= j:

                                        queen_moves[move] = False

                                elif int(move[9]) >= j:

                                    queen_moves[move] = False

                    if white_queens_inf[i][1] + j > 7:

                        for move in move_list:

                            if move[6] == "N":

                                if move[7] == "_":

                                    if int(move[8]) >= j:

                                        queen_moves[move] = False

                                elif int(move[9]) >= j:

                                    queen_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(white_occupation_x)):

                        if white_queens_inf[i][0] == white_occupation_x[k] and white_queens_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "_" and int(move[8]) >= j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] + j == white_occupation_x[k] and white_queens_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "E" and int(move[9]) >= j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] + j == white_occupation_x[k] and white_queens_inf[i][1] == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "E" and move[7] == "_" and int(move[8]) >= j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] + j == white_occupation_x[k] and white_queens_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "E" and int(move[9]) >= j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] == white_occupation_x[k] and white_queens_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "_" and int(move[8]) >= j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] - j == white_occupation_x[k] and white_queens_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "W" and int(move[9]) >= j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] - j == white_occupation_x[k] and white_queens_inf[i][1] == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "W" and move[7] == "_" and int(move[8]) >= j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] - j == white_occupation_x[k] and white_queens_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "W" and int(move[9]) >= j:

                                    queen_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(black_occupation_x)):

                        if white_queens_inf[i][0] == black_occupation_x[k] and white_queens_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "_" and int(move[8]) > j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] + j == black_occupation_x[k] and white_queens_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "E" and int(move[9]) > j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] + j == black_occupation_x[k] and white_queens_inf[i][1] == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "E" and move[7] == "_" and int(move[8]) > j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] + j == black_occupation_x[k] and white_queens_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "E" and int(move[9]) > j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] == black_occupation_x[k] and white_queens_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "_" and int(move[8]) > j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] - j == black_occupation_x[k] and white_queens_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "W" and int(move[9]) > j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] - j == black_occupation_x[k] and white_queens_inf[i][1] == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "W" and move[7] == "_" and int(move[8]) > j:

                                    queen_moves[move] = False

                        elif white_queens_inf[i][0] - j == black_occupation_x[k] and white_queens_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "W" and int(move[9]) > j:

                                    queen_moves[move] = False

                for move in move_list:

                    if queen_moves[move] == True:

                        if move[6] == "N" and move[7] == "_":
                        
                            legal_moves.append(get_notation("Q", white_queens_inf[i][0], white_queens_inf[i][1], white_queens_inf[i][0], white_queens_inf[i][1] + int(move[8]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "N" and move[7] == "E":
                        
                            legal_moves.append(get_notation("Q", white_queens_inf[i][0], white_queens_inf[i][1], white_queens_inf[i][0] + int(move[9]), white_queens_inf[i][1] + int(move[9]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "E" and move[7] == "_":
                        
                            legal_moves.append(get_notation("Q", white_queens_inf[i][0], white_queens_inf[i][1], white_queens_inf[i][0] + int(move[8]), white_queens_inf[i][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "S" and move[7] == "E":
                        
                            legal_moves.append(get_notation("Q", white_queens_inf[i][0], white_queens_inf[i][1], white_queens_inf[i][0] + int(move[9]), white_queens_inf[i][1] - int(move[9]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "S" and move[7] == "_":
                        
                            legal_moves.append(get_notation("Q", white_queens_inf[i][0], white_queens_inf[i][1], white_queens_inf[i][0], white_queens_inf[i][1] - int(move[8]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "S" and move[7] == "W":
                        
                            legal_moves.append(get_notation("Q", white_queens_inf[i][0], white_queens_inf[i][1], white_queens_inf[i][0] - int(move[9]), white_queens_inf[i][1] - int(move[9]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "W" and move[7] == "_":
                        
                            legal_moves.append(get_notation("Q", white_queens_inf[i][0], white_queens_inf[i][1], white_queens_inf[i][0] - int(move[8]), white_queens_inf[i][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "N" and move[7] == "W":
                        
                            legal_moves.append(get_notation("Q", white_queens_inf[i][0], white_queens_inf[i][1], white_queens_inf[i][0] - int(move[9]), white_queens_inf[i][1] + int(move[9]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

        if white_king_inf[0][2] == True:

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
                    
            if white_king_inf[0][0] - 1 < 0:

                for move in move_list:

                    if move[5] == "W" or move[6] == "W":

                        king_moves[move] = False

            if white_king_inf[0][1] - 1 < 0:

                for move in move_list:

                    if move[5] == "S":

                        king_moves[move] = False

            if white_king_inf[0][0] + 1 > 7:

                for move in move_list:

                    if move[5] == "E" or move[6] == "E":

                        king_moves[move] = False

            if white_king_inf[0][1] + 1 > 7:

                for move in move_list:

                    if move[5] == "N":

                        king_moves[move] = False

            for i in range(0, len(white_occupation_x)):

                if white_king_inf[0][0] == white_occupation_x[i] and white_king_inf[0][1] + 1 == white_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "N" and move[6] == "_":

                            king_moves[move] = False

                elif white_king_inf[0][0] + 1 == white_occupation_x[i] and white_king_inf[0][1] + 1 == white_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "N" and move[6] == "E":

                            king_moves[move] = False

                elif white_king_inf[0][0] + 1 == white_occupation_x[i] and white_king_inf[0][1] == white_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "E" and move[6] == "_":

                            king_moves[move] = False

                elif white_king_inf[0][0] + 1 == white_occupation_x[i] and white_king_inf[0][1] - 1 == white_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "S" and move[6] == "E":

                            king_moves[move] = False

                elif white_king_inf[0][0] == white_occupation_x[i] and white_king_inf[0][1] - 1 == white_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "S" and move[6] == "_":

                            king_moves[move] = False

                elif white_king_inf[0][0] - 1 == white_occupation_x[i] and white_king_inf[0][1] - 1 == white_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "S" and move[6] == "W":

                            king_moves[move] = False

                elif white_king_inf[0][0] - 1 == white_occupation_x[i] and white_king_inf[0][1] == white_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "W" and move[6] == "_":

                            king_moves[move] = False

                elif white_king_inf[0][0] - 1 == white_occupation_x[i] and white_king_inf[0][1] + 1 == white_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "N" and move[6] == "W":

                            king_moves[move] = False

            for move in move_list:

                if king_moves[move] == True:

                    if move[5] == "N" and move[6] == "_":
                        
                        legal_moves.append(get_notation("K", white_king_inf[0][0], white_king_inf[0][1], white_king_inf[0][0], white_king_inf[0][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "N" and move[6] == "E":
                        
                        legal_moves.append(get_notation("K", white_king_inf[0][0], white_king_inf[0][1], white_king_inf[0][0] + 1, white_king_inf[0][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "E" and move[6] == "_":
                        
                        legal_moves.append(get_notation("K", white_king_inf[0][0], white_king_inf[0][1], white_king_inf[0][0] + 1, white_king_inf[0][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "S" and move[6] == "E":
                        
                        legal_moves.append(get_notation("K", white_king_inf[0][0], white_king_inf[0][1], white_king_inf[0][0] + 1, white_king_inf[0][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "S" and move[6] == "_":
                        
                        legal_moves.append(get_notation("K", white_king_inf[0][0], white_king_inf[0][1], white_king_inf[0][0], white_king_inf[0][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "S" and move[6] == "W":
                        
                        legal_moves.append(get_notation("K", white_king_inf[0][0], white_king_inf[0][1], white_king_inf[0][0] - 1, white_king_inf[0][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "W" and move[6] == "_":
                        
                        legal_moves.append(get_notation("K", white_king_inf[0][0], white_king_inf[0][1], white_king_inf[0][0] - 1, white_king_inf[0][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "N" and move[6] == "W":
                        
                        legal_moves.append(get_notation("K", white_king_inf[0][0], white_king_inf[0][1], white_king_inf[0][0] - 1, white_king_inf[0][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

        if white_king_inf[0][2] == True and white_king_inf[0][3] == True:

            move_list = ["O-O", "O-O-O"]

            king_moves = {
                "O-O" : True,
                "O-O-O" : True,
                }

            for i in range(0, len(white_occupation_x)):

                if white_king_inf[0][0] + 2 == white_occupation_x[i] and white_king_inf[0][1] == white_occupation_y[i]:

                    king_moves["O-O"] = False

                elif white_king_inf[0][0] + 1 == white_occupation_x[i] and white_king_inf[0][1] == white_occupation_y[i]:

                    king_moves["O-O"] = False

                if white_king_inf[0][0] - 3 == white_occupation_x[i] and white_king_inf[0][1] == white_occupation_y[i]:

                    king_moves["O-O-O"] = False

                elif white_king_inf[0][0] - 2 == white_occupation_x[i] and white_king_inf[0][1] == white_occupation_y[i]:

                    king_moves["O-O-O"] = False

                elif white_king_inf[0][0] - 1 == white_occupation_x[i] and white_king_inf[0][1] == white_occupation_y[i]:

                    king_moves["O-O-O"] = False

            for i in range(0, len(black_occupation_x)):

                if white_king_inf[0][0] + 2 == black_occupation_x[i] and white_king_inf[0][1] == black_occupation_y[i]:

                    king_moves["O-O"] = False

                elif white_king_inf[0][0] + 1 == black_occupation_x[i] and white_king_inf[0][1] == black_occupation_y[i]:

                    king_moves["O-O"] = False

                if white_king_inf[0][0] - 3 == black_occupation_x[i] and white_king_inf[0][1] == black_occupation_y[i]:

                    king_moves["O-O-O"] = False

                elif white_king_inf[0][0] - 2 == black_occupation_x[i] and white_king_inf[0][1] == black_occupation_y[i]:

                    king_moves["O-O-O"] = False

                elif white_king_inf[0][0] - 1 == black_occupation_x[i] and white_king_inf[0][1] == black_occupation_y[i]:

                    king_moves["O-O-O"] = False

            for i in range(0, 2):

                if white_rooks_inf[i][2] == False or white_rooks_inf[i][3] == False:

                    if i == 0:

                        king_moves["O-O-O"] = False

                    elif i == 1:

                        king_moves["O-O"] = False

            for move in move_list:

                if king_moves[move] == True:

                    legal_moves.append(move)
                        
    else:

        for i in range(0, 8):

            if black_pawns_inf[i][2] == True:

                pawn_S_1 = True
                pawn_S_2 = True
                pawn_SE_11 = False
                pawn_SW_11 = False
                en_p_SE_11 = False
                en_p_SW_11 = False

                for j in range(0, len(black_occupation_x)):

                    if black_pawns_inf[i][0] == black_occupation_x[j] and black_pawns_inf[i][1] - 1 == black_occupation_y[j]:

                        pawn_S_1 = False

                    if black_pawns_inf[i][3] == True and black_pawns_inf[i][0] == black_occupation_x[j] and black_pawns_inf[i][1] - 2 == black_occupation_y[j]:

                        pawn_S_2 = False

                for j in range(0, len(white_occupation_x)):

                    if black_pawns_inf[i][0] == white_occupation_x[j] and black_pawns_inf[i][1] - 1 == white_occupation_y[j]:

                        pawn_S_1 = False

                    if black_pawns_inf[i][3] == True and black_pawns_inf[i][0] == white_occupation_x[j] and black_pawns_inf[i][1] - 2 == white_occupation_y[j]:

                        pawn_S_2 = False

                    if black_pawns_inf[i][0] + 1 == white_occupation_x[j] and black_pawns_inf[i][1] - 1 == white_occupation_y[j]:

                        pawn_SE_11 = True

                    if black_pawns_inf[i][0] - 1 == white_occupation_x[j] and black_pawns_inf[i][1] - 1 == white_occupation_y[j]:

                        pawn_SW_11 = True

                if black_pawns_inf[i][0] + 1 == en_passant_x_y[0] and black_pawns_inf[i][1] == en_passant_x_y[1]:

                    pawn_SE_11 = True

                elif black_pawns_inf[i][0] - 1 == en_passant_x_y[0] and black_pawns_inf[i][1] == en_passant_x_y[1]:

                    pawn_SW_11 = True

                if pawn_S_1 == True:

                    legal_move_notation = get_notation("P", black_pawns_inf[i][0], black_pawns_inf[i][1], black_pawns_inf[i][0], black_pawns_inf[i][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y)

                    if legal_move_notation[-1] == "=":

                        legal_moves.append(legal_move_notation + "Q")
                        legal_moves.append(legal_move_notation + "R")
                        legal_moves.append(legal_move_notation + "B")
                        legal_moves.append(legal_move_notation + "N")

                    else:

                        legal_moves.append(legal_move_notation)

                if pawn_S_2 == True and pawn_S_1 == True and black_pawns_inf[i][3] == True:

                    legal_move_notation = get_notation("P", black_pawns_inf[i][0], black_pawns_inf[i][1], black_pawns_inf[i][0], black_pawns_inf[i][1] - 2, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y)

                    if legal_move_notation[-1] == "=":

                        legal_moves.append(legal_move_notation + "Q")
                        legal_moves.append(legal_move_notation + "R")
                        legal_moves.append(legal_move_notation + "B")
                        legal_moves.append(legal_move_notation + "N")

                    else:

                        legal_moves.append(legal_move_notation)

                if pawn_SE_11 == True:

                    legal_move_notation = get_notation("P", black_pawns_inf[i][0], black_pawns_inf[i][1], black_pawns_inf[i][0] + 1, black_pawns_inf[i][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y)

                    if legal_move_notation[-1] == "=":

                        legal_moves.append(legal_move_notation + "Q")
                        legal_moves.append(legal_move_notation + "R")
                        legal_moves.append(legal_move_notation + "B")
                        legal_moves.append(legal_move_notation + "N")

                    else:

                        legal_moves.append(legal_move_notation)

                if pawn_SW_11 == True:

                    legal_move_notation = get_notation("P", black_pawns_inf[i][0], black_pawns_inf[i][1], black_pawns_inf[i][0] - 1, black_pawns_inf[i][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y)

                    if legal_move_notation[-1] == "=":

                        legal_moves.append(legal_move_notation + "Q")
                        legal_moves.append(legal_move_notation + "R")
                        legal_moves.append(legal_move_notation + "B")
                        legal_moves.append(legal_move_notation + "N")

                    else:

                        legal_moves.append(legal_move_notation)

        for i in range(0, 10):

            if black_bishops_inf[i][2] == True:

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
                    
                    if black_bishops_inf[i][0] - j < 0:

                        for move in move_list:

                            if move[8] == "W" and int(move[10]) >= j:

                                bishop_moves[move] = False

                    if black_bishops_inf[i][1] - j < 0:

                        for move in move_list:

                            if move[7] == "S" and int(move[10]) >= j:

                                bishop_moves[move] = False

                    if black_bishops_inf[i][0] + j > 7:

                        for move in move_list:

                            if move[8] == "E" and int(move[10]) >= j:

                                bishop_moves[move] = False

                    if black_bishops_inf[i][1] + j > 7:

                        for move in move_list:

                            if move[7] == "N" and int(move[10]) >= j:

                                bishop_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(black_occupation_x)):

                        if black_bishops_inf[i][0] + j == black_occupation_x[k] and black_bishops_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "N" and move[8] == "E" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                        elif black_bishops_inf[i][0] + j == black_occupation_x[k] and black_bishops_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "S" and move[8] == "E" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                        elif black_bishops_inf[i][0] - j == black_occupation_x[k] and black_bishops_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "S" and move[8] == "W" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                        elif black_bishops_inf[i][0] - j == black_occupation_x[k] and black_bishops_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "N" and move[8] == "W" and int(move[10]) >= j:

                                    bishop_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(white_occupation_x)):

                        if black_bishops_inf[i][0] + j == white_occupation_x[k] and black_bishops_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "N" and move[8] == "E" and int(move[10]) > j:

                                    bishop_moves[move] = False

                        elif black_bishops_inf[i][0] + j == white_occupation_x[k] and black_bishops_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "S" and move[8] == "E" and int(move[10]) > j:

                                    bishop_moves[move] = False

                        elif black_bishops_inf[i][0] - j == white_occupation_x[k] and black_bishops_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "S" and move[8] == "W" and int(move[10]) > j:

                                    bishop_moves[move] = False

                        elif black_bishops_inf[i][0] - j == white_occupation_x[k] and black_bishops_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[7] == "N" and move[8] == "W" and int(move[10]) > j:

                                    bishop_moves[move] = False

                for move in move_list:

                    if bishop_moves[move] == True:

                        if move[7] == "N" and move[8] == "E":
                        
                            legal_moves.append(get_notation("B", black_bishops_inf[i][0], black_bishops_inf[i][1], black_bishops_inf[i][0] + int(move[10]), black_bishops_inf[i][1] + int(move[10]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[7] == "S" and move[8] == "E":
                        
                            legal_moves.append(get_notation("B", black_bishops_inf[i][0], black_bishops_inf[i][1], black_bishops_inf[i][0] + int(move[10]), black_bishops_inf[i][1] - int(move[10]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[7] == "S" and move[8] == "W":
                        
                            legal_moves.append(get_notation("B", black_bishops_inf[i][0], black_bishops_inf[i][1], black_bishops_inf[i][0] - int(move[10]), black_bishops_inf[i][1] - int(move[10]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[7] == "N" and move[8] == "W":
                        
                            legal_moves.append(get_notation("B", black_bishops_inf[i][0], black_bishops_inf[i][1], black_bishops_inf[i][0] - int(move[10]), black_bishops_inf[i][1] + int(move[10]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

        for i in range(0, 10):

            if black_knights_inf[i][2] == True:

                knight_NE_21 = True
                knight_NE_12 = True
                knight_SE_12 = True
                knight_SE_21 = True
                knight_SW_21 = True
                knight_SW_12 = True
                knight_NW_12 = True
                knight_NW_21 = True

                if black_knights_inf[i][0] - 1 < 0:

                    knight_SW_21 = False
                    knight_SW_12 = False
                    knight_NW_12 = False
                    knight_NW_21 = False

                elif black_knights_inf[i][0] - 2 < 0:

                    knight_SW_12 = False
                    knight_NW_12 = False

                if black_knights_inf[i][0] + 1 > 7:

                    knight_NE_21 = False
                    knight_NE_12 = False
                    knight_SE_12 = False
                    knight_SE_21 = False

                elif black_knights_inf[i][0] + 2 > 7:

                    knight_NE_12 = False
                    knight_SE_12 = False

                if black_knights_inf[i][1] - 1 < 0:

                    knight_SE_12 = False
                    knight_SE_21 = False
                    knight_SW_21 = False
                    knight_SW_12 = False

                elif black_knights_inf[i][1] - 2 < 0:

                    knight_SE_21 = False
                    knight_SW_21 = False

                if black_knights_inf[i][1] + 1 > 7:

                    knight_NE_21 = False
                    knight_NE_12 = False
                    knight_NW_12 = False
                    knight_NW_21 = False

                elif black_knights_inf[i][1] + 2 > 7:

                    knight_NE_21 = False
                    knight_NW_21 = False

                for j in range(0, len(black_occupation_x)):

                    if black_knights_inf[i][0] + 1 == black_occupation_x[j] and black_knights_inf[i][1] + 2 == black_occupation_y[j]:

                        knight_NE_21 = False

                    if black_knights_inf[i][0] + 2 == black_occupation_x[j] and black_knights_inf[i][1] + 1 == black_occupation_y[j]:

                        knight_NE_12 = False

                    if black_knights_inf[i][0] + 2 == black_occupation_x[j] and black_knights_inf[i][1] - 1 == black_occupation_y[j]:

                        knight_SE_12 = False

                    if black_knights_inf[i][0] + 1 == black_occupation_x[j] and black_knights_inf[i][1] - 2 == black_occupation_y[j]:

                        knight_SE_21 = False

                    if black_knights_inf[i][0] - 1 == black_occupation_x[j] and black_knights_inf[i][1] - 2 == black_occupation_y[j]:

                        knight_SW_21 = False

                    if black_knights_inf[i][0] - 2 == black_occupation_x[j] and black_knights_inf[i][1] - 1 == black_occupation_y[j]:

                        knight_SW_12 = False

                    if black_knights_inf[i][0] - 2 == black_occupation_x[j] and black_knights_inf[i][1] + 1 == black_occupation_y[j]:

                        knight_NW_12 = False

                    if black_knights_inf[i][0] - 1 == black_occupation_x[j] and black_knights_inf[i][1] + 2 == black_occupation_y[j]:

                        knight_NW_21 = False

                if knight_NE_21 == True:

                    legal_moves.append(get_notation("N", black_knights_inf[i][0], black_knights_inf[i][1], black_knights_inf[i][0] + 1, black_knights_inf[i][1] + 2, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_NE_12 == True:

                    legal_moves.append(get_notation("N", black_knights_inf[i][0], black_knights_inf[i][1], black_knights_inf[i][0] + 2, black_knights_inf[i][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_SE_12 == True:

                    legal_moves.append(get_notation("N", black_knights_inf[i][0], black_knights_inf[i][1], black_knights_inf[i][0] + 2, black_knights_inf[i][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_SE_21 == True:

                    legal_moves.append(get_notation("N", black_knights_inf[i][0], black_knights_inf[i][1], black_knights_inf[i][0] + 1, black_knights_inf[i][1] - 2, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_SW_21 == True:

                    legal_moves.append(get_notation("N", black_knights_inf[i][0], black_knights_inf[i][1], black_knights_inf[i][0] - 1, black_knights_inf[i][1] - 2, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_SW_12 == True:

                    legal_moves.append(get_notation("N", black_knights_inf[i][0], black_knights_inf[i][1], black_knights_inf[i][0] - 2, black_knights_inf[i][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_NW_12 == True:

                    legal_moves.append(get_notation("N", black_knights_inf[i][0], black_knights_inf[i][1], black_knights_inf[i][0] - 2, black_knights_inf[i][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                if knight_NW_21 == True:

                    legal_moves.append(get_notation("N", black_knights_inf[i][0], black_knights_inf[i][1], black_knights_inf[i][0] - 1, black_knights_inf[i][1] + 2, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

        for i in range(0, 10):

            if black_rooks_inf[i][2] == True:

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
                    
                    if black_rooks_inf[i][0] - j < 0:

                        for move in move_list:

                            if move[5] == "W" and int(move[7]) >= j:

                                rook_moves[move] = False

                    if black_rooks_inf[i][1] - j < 0:

                        for move in move_list:

                            if move[5] == "S" and int(move[7]) >= j:

                                rook_moves[move] = False

                    if black_rooks_inf[i][0] + j > 7:

                        for move in move_list:

                            if move[5] == "E" and int(move[7]) >= j:

                                rook_moves[move] = False

                    if black_rooks_inf[i][1] + j > 7:

                        for move in move_list:

                            if move[5] == "N" and int(move[7]) >= j:

                                rook_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(black_occupation_x)):

                        if black_rooks_inf[i][0] == black_occupation_x[k] and black_rooks_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "N" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        elif black_rooks_inf[i][0] + j == black_occupation_x[k] and black_rooks_inf[i][1] == black_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "E" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        elif black_rooks_inf[i][0] == black_occupation_x[k] and black_rooks_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "S" and int(move[7]) >= j:

                                    rook_moves[move] = False

                        elif black_rooks_inf[i][0] - j == black_occupation_x[k] and black_rooks_inf[i][1] == black_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "W" and int(move[7]) >= j:

                                    rook_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(white_occupation_x)):

                        if black_rooks_inf[i][0] == white_occupation_x[k] and black_rooks_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "N" and int(move[7]) > j:

                                    rook_moves[move] = False

                        elif black_rooks_inf[i][0] + j == white_occupation_x[k] and black_rooks_inf[i][1] == white_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "E" and int(move[7]) > j:

                                    rook_moves[move] = False

                        elif black_rooks_inf[i][0] == white_occupation_x[k] and black_rooks_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "S" and int(move[7]) > j:

                                    rook_moves[move] = False

                        elif black_rooks_inf[i][0] - j == white_occupation_x[k] and black_rooks_inf[i][1] == white_occupation_y[k]:

                            for move in move_list:

                                if move[5] == "W" and int(move[7]) > j:

                                    rook_moves[move] = False

                for move in move_list:

                    if rook_moves[move] == True:

                        if move[5] == "N":
                        
                            legal_moves.append(get_notation("R", black_rooks_inf[i][0], black_rooks_inf[i][1], black_rooks_inf[i][0], black_rooks_inf[i][1] + int(move[7]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[5] == "E":
                        
                            legal_moves.append(get_notation("R", black_rooks_inf[i][0], black_rooks_inf[i][1], black_rooks_inf[i][0] + int(move[7]), black_rooks_inf[i][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[5] == "S":
                        
                            legal_moves.append(get_notation("R", black_rooks_inf[i][0], black_rooks_inf[i][1], black_rooks_inf[i][0], black_rooks_inf[i][1] - int(move[7]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[5] == "W":
                        
                            legal_moves.append(get_notation("R", black_rooks_inf[i][0], black_rooks_inf[i][1], black_rooks_inf[i][0] - int(move[7]), black_rooks_inf[i][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

        for i in range(0, 9):

            if black_queens_inf[i][2] == True:

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
                    
                    if black_queens_inf[i][0] - j < 0:

                        for move in move_list:

                            if move[6] == "W" or move[7] == "W":

                                if move[7] == "_":

                                    if int(move[8]) >= j:

                                        queen_moves[move] = False

                                elif int(move[9]) >= j:

                                    queen_moves[move] = False

                    if black_queens_inf[i][1] - j < 0:

                        for move in move_list:

                            if move[6] == "S":

                                if move[7] == "_":

                                    if int(move[8]) >= j:

                                        queen_moves[move] = False

                                elif int(move[9]) >= j:

                                    queen_moves[move] = False

                    if black_queens_inf[i][0] + j > 7:

                        for move in move_list:

                            if move[6] == "E" or move[7] == "E":

                                if move[7] == "_":

                                    if int(move[8]) >= j:

                                        queen_moves[move] = False

                                elif int(move[9]) >= j:

                                    queen_moves[move] = False

                    if black_queens_inf[i][1] + j > 7:

                        for move in move_list:

                            if move[6] == "N":

                                if move[7] == "_":

                                    if int(move[8]) >= j:

                                        queen_moves[move] = False

                                elif int(move[9]) >= j:

                                    queen_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(black_occupation_x)):

                        if black_queens_inf[i][0] == black_occupation_x[k] and black_queens_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "_" and int(move[8]) >= j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] + j == black_occupation_x[k] and black_queens_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "E" and int(move[9]) >= j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] + j == black_occupation_x[k] and black_queens_inf[i][1] == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "E" and move[7] == "_" and int(move[8]) >= j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] + j == black_occupation_x[k] and black_queens_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "E" and int(move[9]) >= j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] == black_occupation_x[k] and black_queens_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "_" and int(move[8]) >= j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] - j == black_occupation_x[k] and black_queens_inf[i][1] - j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "W" and int(move[9]) >= j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] - j == black_occupation_x[k] and black_queens_inf[i][1] == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "W" and move[7] == "_" and int(move[8]) >= j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] - j == black_occupation_x[k] and black_queens_inf[i][1] + j == black_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "W" and int(move[9]) >= j:

                                    queen_moves[move] = False

                for j in range(1, 8):

                    for k in range(0, len(white_occupation_x)):

                        if black_queens_inf[i][0] == white_occupation_x[k] and black_queens_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "_" and int(move[8]) > j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] + j == white_occupation_x[k] and black_queens_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "E" and int(move[9]) > j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] + j == white_occupation_x[k] and black_queens_inf[i][1] == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "E" and move[7] == "_" and int(move[8]) > j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] + j == white_occupation_x[k] and black_queens_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "E" and int(move[9]) > j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] == white_occupation_x[k] and black_queens_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "_" and int(move[8]) > j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] - j == white_occupation_x[k] and black_queens_inf[i][1] - j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "S" and move[7] == "W" and int(move[9]) > j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] - j == white_occupation_x[k] and black_queens_inf[i][1] == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "W" and move[7] == "_" and int(move[8]) > j:

                                    queen_moves[move] = False

                        elif black_queens_inf[i][0] - j == white_occupation_x[k] and black_queens_inf[i][1] + j == white_occupation_y[k]:

                            for move in move_list:

                                if move[6] == "N" and move[7] == "W" and int(move[9]) > j:

                                    queen_moves[move] = False

                for move in move_list:

                    if queen_moves[move] == True:

                        if move[6] == "N" and move[7] == "_":
                        
                            legal_moves.append(get_notation("Q", black_queens_inf[i][0], black_queens_inf[i][1], black_queens_inf[i][0], black_queens_inf[i][1] + int(move[8]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "N" and move[7] == "E":
                        
                            legal_moves.append(get_notation("Q", black_queens_inf[i][0], black_queens_inf[i][1], black_queens_inf[i][0] + int(move[9]), black_queens_inf[i][1] + int(move[9]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "E" and move[7] == "_":
                        
                            legal_moves.append(get_notation("Q", black_queens_inf[i][0], black_queens_inf[i][1], black_queens_inf[i][0] + int(move[8]), black_queens_inf[i][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "S" and move[7] == "E":
                        
                            legal_moves.append(get_notation("Q", black_queens_inf[i][0], black_queens_inf[i][1], black_queens_inf[i][0] + int(move[9]), black_queens_inf[i][1] - int(move[9]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "S" and move[7] == "_":
                        
                            legal_moves.append(get_notation("Q", black_queens_inf[i][0], black_queens_inf[i][1], black_queens_inf[i][0], black_queens_inf[i][1] - int(move[8]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "S" and move[7] == "W":
                        
                            legal_moves.append(get_notation("Q", black_queens_inf[i][0], black_queens_inf[i][1], black_queens_inf[i][0] - int(move[9]), black_queens_inf[i][1] - int(move[9]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "W" and move[7] == "_":
                        
                            legal_moves.append(get_notation("Q", black_queens_inf[i][0], black_queens_inf[i][1], black_queens_inf[i][0] - int(move[8]), black_queens_inf[i][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                        elif move[6] == "N" and move[7] == "W":
                        
                            legal_moves.append(get_notation("Q", black_queens_inf[i][0], black_queens_inf[i][1], black_queens_inf[i][0] - int(move[9]), black_queens_inf[i][1] + int(move[9]), white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

        if black_king_inf[0][2] == True:

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
                    
            if black_king_inf[0][0] - 1 < 0:

                for move in move_list:

                    if move[5] == "W" or move[6] == "W":

                        king_moves[move] = False

            if black_king_inf[0][1] - 1 < 0:

                for move in move_list:

                    if move[5] == "S":

                        king_moves[move] = False

            if black_king_inf[0][0] + 1 > 7:

                for move in move_list:

                    if move[5] == "E" or move[6] == "E":

                        king_moves[move] = False

            if black_king_inf[0][1] + 1 > 7:

                for move in move_list:

                    if move[5] == "N":

                        king_moves[move] = False

            for i in range(0, len(black_occupation_x)):

                if black_king_inf[0][0] == black_occupation_x[i] and black_king_inf[0][1] + 1 == black_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "N" and move[6] == "_":

                            king_moves[move] = False

                elif black_king_inf[0][0] + 1 == black_occupation_x[i] and black_king_inf[0][1] + 1 == black_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "N" and move[6] == "E":

                            king_moves[move] = False

                elif black_king_inf[0][0] + 1 == black_occupation_x[i] and black_king_inf[0][1] == black_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "E" and move[6] == "_":

                            king_moves[move] = False

                elif black_king_inf[0][0] + 1 == black_occupation_x[i] and black_king_inf[0][1] - 1 == black_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "S" and move[6] == "E":

                            king_moves[move] = False

                elif black_king_inf[0][0] == black_occupation_x[i] and black_king_inf[0][1] - 1 == black_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "S" and move[6] == "_":

                            king_moves[move] = False

                elif black_king_inf[0][0] - 1 == black_occupation_x[i] and black_king_inf[0][1] - 1 == black_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "S" and move[6] == "W":

                            king_moves[move] = False

                elif black_king_inf[0][0] - 1 == black_occupation_x[i] and black_king_inf[0][1] == black_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "W" and move[6] == "_":

                            king_moves[move] = False

                elif black_king_inf[0][0] - 1 == black_occupation_x[i] and black_king_inf[0][1] + 1 == black_occupation_y[i]:

                    for move in move_list:

                        if move[5] == "N" and move[6] == "W":

                            king_moves[move] = False

            for move in move_list:

                if king_moves[move] == True:

                    if move[5] == "N" and move[6] == "_":
                        
                        legal_moves.append(get_notation("K", black_king_inf[0][0], black_king_inf[0][1], black_king_inf[0][0], black_king_inf[0][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "N" and move[6] == "E":
                        
                        legal_moves.append(get_notation("K", black_king_inf[0][0], black_king_inf[0][1], black_king_inf[0][0] + 1, black_king_inf[0][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "E" and move[6] == "_":
                        
                        legal_moves.append(get_notation("K", black_king_inf[0][0], black_king_inf[0][1], black_king_inf[0][0] + 1, black_king_inf[0][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "S" and move[6] == "E":
                        
                        legal_moves.append(get_notation("K", black_king_inf[0][0], black_king_inf[0][1], black_king_inf[0][0] + 1, black_king_inf[0][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "S" and move[6] == "_":
                        
                        legal_moves.append(get_notation("K", black_king_inf[0][0], black_king_inf[0][1], black_king_inf[0][0], black_king_inf[0][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "S" and move[6] == "W":
                        
                        legal_moves.append(get_notation("K", black_king_inf[0][0], black_king_inf[0][1], black_king_inf[0][0] - 1, black_king_inf[0][1] - 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "W" and move[6] == "_":
                        
                        legal_moves.append(get_notation("K", black_king_inf[0][0], black_king_inf[0][1], black_king_inf[0][0] - 1, black_king_inf[0][1], white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

                    elif move[5] == "N" and move[6] == "W":
                        
                        legal_moves.append(get_notation("K", black_king_inf[0][0], black_king_inf[0][1], black_king_inf[0][0] - 1, black_king_inf[0][1] + 1, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y))

        if black_king_inf[0][2] == True and black_king_inf[0][3] == True:

            move_list = ["O-O", "O-O-O"]

            king_moves = {
                "O-O" : True,
                "O-O-O" : True,
                }

            for i in range(0, len(white_occupation_x)):

                if black_king_inf[0][0] + 2 == white_occupation_x[i] and black_king_inf[0][1] == white_occupation_y[i]:

                    king_moves["O-O"] = False

                elif black_king_inf[0][0] + 1 == white_occupation_x[i] and black_king_inf[0][1] == white_occupation_y[i]:

                    king_moves["O-O"] = False

                if black_king_inf[0][0] - 3 == white_occupation_x[i] and black_king_inf[0][1] == white_occupation_y[i]:

                    king_moves["O-O-O"] = False

                elif black_king_inf[0][0] - 2 == white_occupation_x[i] and black_king_inf[0][1] == white_occupation_y[i]:

                    king_moves["O-O-O"] = False

                elif black_king_inf[0][0] - 1 == white_occupation_x[i] and black_king_inf[0][1] == white_occupation_y[i]:

                    king_moves["O-O-O"] = False

            for i in range(0, len(black_occupation_x)):

                if black_king_inf[0][0] + 2 == black_occupation_x[i] and black_king_inf[0][1] == black_occupation_y[i]:

                    king_moves["O-O"] = False

                elif black_king_inf[0][0] + 1 == black_occupation_x[i] and black_king_inf[0][1] == black_occupation_y[i]:

                    king_moves["O-O"] = False

                if black_king_inf[0][0] - 3 == black_occupation_x[i] and black_king_inf[0][1] == black_occupation_y[i]:

                    king_moves["O-O-O"] = False

                elif black_king_inf[0][0] - 2 == black_occupation_x[i] and black_king_inf[0][1] == black_occupation_y[i]:

                    king_moves["O-O-O"] = False

                elif black_king_inf[0][0] - 1 == black_occupation_x[i] and black_king_inf[0][1] == black_occupation_y[i]:

                    king_moves["O-O-O"] = False

            for i in range(0, 2):

                if black_rooks_inf[i][2] == False or black_rooks_inf[i][3] == False:

                    if i == 0:

                        king_moves["O-O-O"] = False

                    elif i == 1:

                        king_moves["O-O"] = False

            for move in move_list:

                if king_moves[move] == True:

                    legal_moves.append(move)

    return legal_moves
    
def check_checks(legal_moves, white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf, white_turn):

    moves = deepcopy(legal_moves)

    white_short_castle_through_check_check = False
    white_long_castle_through_check_check = False
    black_short_castle_through_check_check = False
    black_long_castle_through_check_check = False

    for move in moves:

        white_pawns = deepcopy(white_pawns_inf)
        white_bishops = deepcopy(white_bishops_inf)
        white_knights = deepcopy(white_knights_inf)
        white_rooks = deepcopy(white_rooks_inf)
        white_queens = deepcopy(white_queens_inf)
        white_king = deepcopy(white_king_inf)

        black_pawns = deepcopy(black_pawns_inf)
        black_bishops = deepcopy(black_bishops_inf)
        black_knights = deepcopy(black_knights_inf)
        black_rooks = deepcopy(black_rooks_inf)
        black_queens = deepcopy(black_queens_inf)
        black_king = deepcopy(black_king_inf)

        notation_val, take = convert_to_easy_notation(move)

        if notation_val == "Ke1f1" and white_turn == True:

            white_short_castle_through_check_check = True

        if notation_val == "Ke1d1" and white_turn == True:

            white_long_castle_through_check_check = True

        if notation_val == "Ke8f8" and white_turn == False:

            black_short_castle_through_check_check = True

        if notation_val == "Ke8d8" and white_turn == False:

            black_long_castle_through_check_check = True

        if notation_val[0] == "B":

            fromx = get_column_char(notation_val[1])
            fromy = int(notation_val[2]) - 1

            tox = get_column_char(notation_val[3])
            toy = int(notation_val[4]) - 1

            if white_turn == True:

                for i in range(0, 10):

                    if white_bishops[i][2] == True and white_bishops[i][0] == fromx and white_bishops[i][1] == fromy:
                            
                        white_bishops[i][0] = tox
                        white_bishops[i][1] = toy

            else:

                for i in range(0, 10):

                    if black_bishops[i][2] == True and black_bishops[i][0] == fromx and black_bishops[i][1] == fromy:
                            
                        black_bishops[i][0] = tox
                        black_bishops[i][1] = toy

        elif notation_val[0] == "N":

            fromx = get_column_char(notation_val[1])
            fromy = int(notation_val[2]) - 1

            tox = get_column_char(notation_val[3])
            toy = int(notation_val[4]) - 1

            if white_turn == True:

                for i in range(0, 10):

                    if white_knights[i][2] == True and white_knights[i][0] == fromx and white_knights[i][1] == fromy:
                            
                        white_knights[i][0] = tox
                        white_knights[i][1] = toy

            else:

                for i in range(0, 10):

                    if black_knights[i][2] == True and black_knights[i][0] == fromx and black_knights[i][1] == fromy:
                            
                        black_knights[i][0] = tox
                        black_knights[i][1] = toy

        elif notation_val[0] == "R":

            fromx = get_column_char(notation_val[1])
            fromy = int(notation_val[2]) - 1

            tox = get_column_char(notation_val[3])
            toy = int(notation_val[4]) - 1

            if white_turn == True:

                for i in range(0, 10):

                    if white_rooks[i][2] == True and white_rooks[i][0] == fromx and white_rooks[i][1] == fromy:
                            
                        white_rooks[i][0] = tox
                        white_rooks[i][1] = toy
                        white_rooks[i][3] = False

            else:

                for i in range(0, 10):

                    if black_rooks[i][2] == True and black_rooks[i][0] == fromx and black_rooks[i][1] == fromy:
                            
                        black_rooks[i][0] = tox
                        black_rooks[i][1] = toy
                        black_rooks[i][3] = False

        elif notation_val[0] == "Q":

            fromx = get_column_char(notation_val[1])
            fromy = int(notation_val[2]) - 1

            tox = get_column_char(notation_val[3])
            toy = int(notation_val[4]) - 1

            if white_turn == True:

                for i in range(0, 9):

                    if white_queens[i][2] == True and white_queens[i][0] == fromx and white_queens[i][1] == fromy:
                            
                        white_queens[i][0] = tox
                        white_queens[i][1] = toy

            else:

                for i in range(0, 9):

                    if black_queens[i][2] == True and black_queens[i][0] == fromx and black_queens[i][1] == fromy:
                            
                        black_queens[i][0] = tox
                        black_queens[i][1] = toy

        elif notation_val[0] == "K":

            fromx = get_column_char(notation_val[1])
            fromy = int(notation_val[2]) - 1

            tox = get_column_char(notation_val[3])
            toy = int(notation_val[4]) - 1

            if white_turn == True:

                if white_king[0][2] == True and white_king[0][0] == fromx and white_king[0][1] == fromy:
                            
                    white_king[0][0] = tox
                    white_king[0][1] = toy
                    white_king[0][3] = False

            else:

                if black_king[0][2] == True and black_king[0][0] == fromx and black_king[0][1] == fromy:
                            
                    black_king[0][0] = tox
                    black_king[0][1] = toy
                    black_king[0][3] = False

        elif notation_val[0] == "O":

            if white_turn == True:

                white_king[0][3] = False

                if notation_val == "O-O":

                    white_rooks[1][3] = False

                    white_king[0][0] = 6
                    white_king[0][1] = 0

                    for i in range(0, 2):

                        if white_rooks[i][0] == 7:
                    
                            white_rooks[i][0] = 5
                            white_rooks[i][1] = 0

                elif notation_val == "O-O-O":

                    white_rooks[0][3] = False

                    white_king[0][0] = 2
                    white_king[0][1] = 0

                    for i in range(0, 2):

                        if white_rooks[i][0] == 0:
                    
                            white_rooks[i][0] = 3
                            white_rooks[i][1] = 0
                            
            else:

                black_king[0][3] = False

                if notation_val == "O-O":

                    black_rooks[1][3] = False

                    black_king[0][0] = 6
                    black_king[0][1] = 7

                    for i in range(0, 2):

                        if black_rooks[i][0] == 7:
                    
                            black_rooks[i][0] = 5
                            black_rooks[i][1] = 7

                elif notation_val == "O-O-O":

                    black_rooks[0][3] = False

                    black_king[0][0] = 2
                    black_king[0][1] = 7

                    for i in range(0, 2):

                        if black_rooks[i][0] == 0:
                    
                            black_rooks[i][0] = 3
                            black_rooks[i][1] = 7

        else:

            if True:

                if notation_val[-2] == "=":

                    tox = get_column_char(notation_val[-4])
                    toy = int(notation_val[-3]) - 1

                else:
                    
                    tox = get_column_char(notation_val[-2])
                    toy = int(notation_val[-1]) - 1

                if take == True:

                    if notation_val[-2] == "=":

                        fromx = get_column_char(notation_val[-5])

                    else:

                        fromx = get_column_char(notation_val[-3])

                    if white_turn == True:
                            
                        fromy = toy - 1

                    else:

                        fromy = toy + 1

                else:

                    fromx = tox

                    if white_turn == True:

                        if toy == 3:

                            fromy = toy - 2

                            for i in range(0, 8):

                                if white_pawns[i][2] == True and white_pawns[i][0] == fromx and white_pawns[i][1] == toy - 1:

                                    fromy = toy - 1

                        else:

                            fromy = toy - 1

                    else:

                        if toy == 4:

                            fromy = toy + 2

                            for i in range(0, 8):

                                if black_pawns[i][2] == True and black_pawns[i][0] == fromx and black_pawns[i][1] == toy + 1:

                                    fromy = toy + 1

                        else:

                            fromy = toy + 1

                if white_turn == True:

                    for i in range(0, 8):
                        
                        if white_pawns[i][2] == True and white_pawns[i][0] == fromx and white_pawns[i][1] == fromy:

                            if toy == 7:

                                white_pawns[i][2] = False

                                if notation_val[-1] == "Q":

                                    promotion_complete = False

                                    for i in range(1, 9):

                                        if white_queens[i][2] == False and promotion_complete == False:

                                            promotion_complete = True

                                            white_queens[i][0] = tox
                                            white_queens[i][1] = toy
                                            white_queens[i][2] = True

                                elif notation_val[-1] == "R":

                                    promotion_complete = False

                                    for i in range(2, 10):

                                        if white_rooks[i][2] == False and promotion_complete == False:

                                            promotion_complete = True

                                            white_rooks[i][0] = tox
                                            white_rooks[i][1] = toy
                                            white_rooks[i][2] = True
                                            white_rooks[i][3] = False

                                elif notation_val[-1] == "B":

                                    promotion_complete = False

                                    for i in range(2, 10):

                                        if white_bishops[i][2] == False and promotion_complete == False:

                                            promotion_complete = True

                                            white_bishops[i][0] = tox
                                            white_bishops[i][1] = toy
                                            white_bishops[i][2] = True

                                elif notation_val[-1] == "N":

                                    promotion_complete = False

                                    for i in range(2, 10):

                                        if white_knights[i][2] == False and promotion_complete == False:

                                            promotion_complete = True

                                            white_knights[i][0] = tox
                                            white_knights[i][1] = toy
                                            white_knights[i][2] = True

                            else:
                            
                                white_pawns[i][0] = tox
                                white_pawns[i][1] = toy
                                white_pawns[i][3] = False

                else:

                    for i in range(0, 8):

                        if black_pawns[i][2] == True and black_pawns[i][0] == fromx and black_pawns[i][1] == fromy:

                            if toy == 0:

                                black_pawns[i][2] = False

                                if notation_val[-1] == "Q":

                                    promotion_complete = False

                                    for i in range(1, 9):

                                        if black_queens[i][2] == False and promotion_complete == False:

                                            promotion_complete = True

                                            black_queens[i][0] = tox
                                            black_queens[i][1] = toy
                                            black_queens[i][2] = True

                                elif notation_val[-1] == "R":

                                    promotion_complete = False

                                    for i in range(2, 10):

                                        if black_rooks[i][2] == False and promotion_complete == False:

                                            promotion_complete = True

                                            black_rooks[i][0] = tox
                                            black_rooks[i][1] = toy
                                            black_rooks[i][2] = True
                                            black_rooks[i][3] = False

                                elif notation_val[-1] == "B":

                                    promotion_complete = False

                                    for i in range(2, 10):

                                        if black_bishops[i][2] == False and promotion_complete == False:

                                            promotion_complete = True

                                            black_bishops[i][0] = tox
                                            black_bishops[i][1] = toy
                                            black_bishops[i][2] = True

                                elif notation_val[-1] == "N":

                                    promotion_complete = False

                                    for i in range(2, 10):

                                        if black_knights[i][2] == False and promotion_complete == False:

                                            promotion_complete = True

                                            black_knights[i][0] = tox
                                            black_knights[i][1] = toy
                                            black_knights[i][2] = True

                            else:
                            
                                black_pawns[i][0] = tox
                                black_pawns[i][1] = toy
                                black_pawns[i][3] = False
                            
        if take == True:

            piece_taken = False

            if white_turn == True:

                for i in range(0, 8):

                    if black_pawns[i][2] == True and black_pawns[i][0] == tox and black_pawns[i][1] == toy:

                        black_pawns[i][2] = False

                        piece_taken = True

                for i in range(0, 10):

                    if black_bishops[i][2] == True and black_bishops[i][0] == tox and black_bishops[i][1] == toy:

                        black_bishops[i][2] = False

                        piece_taken = True

                for i in range(0, 10):

                    if black_knights[i][2] == True and black_knights[i][0] == tox and black_knights[i][1] == toy:

                        black_knights[i][2] = False

                        piece_taken = True

                for i in range(0, 10):

                    if black_rooks[i][2] == True and black_rooks[i][0] == tox and black_rooks[i][1] == toy:

                        black_rooks[i][2] = False

                        piece_taken = True

                for i in range(0, 9):

                    if black_queens[i][2] == True and black_queens[i][0] == tox and black_queens[i][1] == toy:

                        black_queens[i][2] = False

                        piece_taken = True

                if piece_taken == False:

                    for i in range(0, 8):

                        if black_pawns[i][2] == True and black_pawns[i][0] == tox and black_pawns[i][1] == toy - 1:

                            black_pawns[i][2] = False
                            
            else:

                for i in range(0, 8):

                    if white_pawns[i][2] == True and white_pawns[i][0] == tox and white_pawns[i][1] == toy:

                        white_pawns[i][2] = False

                        piece_taken = True

                for i in range(0, 10):

                    if white_bishops[i][2] == True and white_bishops[i][0] == tox and white_bishops[i][1] == toy:

                        white_bishops[i][2] = False

                        piece_taken = True

                for i in range(0, 10):

                    if white_knights[i][2] == True and white_knights[i][0] == tox and white_knights[i][1] == toy:

                        white_knights[i][2] = False

                        piece_taken = True

                for i in range(0, 10):

                    if white_rooks[i][2] == True and white_rooks[i][0] == tox and white_rooks[i][1] == toy:

                        white_rooks[i][2] = False

                        piece_taken = True

                for i in range(0, 9):

                    if white_queens[i][2] == True and white_queens[i][0] == tox and white_queens[i][1] == toy:

                        white_queens[i][2] = False

                        piece_taken = True

                if piece_taken == False:

                    for i in range(0, 8):

                        if white_pawns[i][2] == True and white_pawns[i][0] == tox and white_pawns[i][1] == toy + 1:

                            white_pawns[i][2] = False

        white_occ_x = []
        white_occ_y = []
        black_occ_x = []
        black_occ_y = []

        for i in range(0, 8):

            if white_pawns[i][2] == True:

                white_occ_x.append(white_pawns[i][0])
                white_occ_y.append(white_pawns[i][1])

        for i in range(0, 10):

            if white_knights[i][2] == True:

                white_occ_x.append(white_knights[i][0])
                white_occ_y.append(white_knights[i][1])

        for i in range(0, 10):

            if white_bishops[i][2] == True:

                white_occ_x.append(white_bishops[i][0])
                white_occ_y.append(white_bishops[i][1])

        for i in range(0, 10):

            if white_rooks[i][2] == True:

                white_occ_x.append(white_rooks[i][0])
                white_occ_y.append(white_rooks[i][1])

        for i in range(0, 9):

            if white_queens[i][2] == True:

                white_occ_x.append(white_queens[i][0])
                white_occ_y.append(white_queens[i][1])

        if white_king[0][2] == True:

            white_occ_x.append(white_king[0][0])
            white_occ_y.append(white_king[0][1])

        for i in range(0, 8):

            if black_pawns[i][2] == True:

                black_occ_x.append(black_pawns[i][0])
                black_occ_y.append(black_pawns[i][1])

        for i in range(0, 10):

            if black_knights[i][2] == True:

                black_occ_x.append(black_knights[i][0])
                black_occ_y.append(black_knights[i][1])
                
        for i in range(0, 10):

            if black_bishops[i][2] == True:

                black_occ_x.append(black_bishops[i][0])
                black_occ_y.append(black_bishops[i][1])

        for i in range(0, 10):

            if black_rooks[i][2] == True:

                black_occ_x.append(black_rooks[i][0])
                black_occ_y.append(black_rooks[i][1])

        for i in range(0, 9):

            if black_queens[i][2] == True:

                black_occ_x.append(black_queens[i][0])
                black_occ_y.append(black_queens[i][1])

        if black_king[0][2] == True:

            black_occ_x.append(black_king[0][0])
            black_occ_y.append(black_king[0][1])

        if white_turn == True:

            for i in range(0, 8):

                if white_king[0][0] + 1 == black_pawns[i][0] and white_king[0][1] + 1 == black_pawns[i][1] and black_pawns[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif white_king[0][0] - 1 == black_pawns[i][0] and white_king[0][1] + 1 == black_pawns[i][1] and black_pawns[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)
                    
            for i in range(0, 10):

                if white_king[0][0] + 1 == black_knights[i][0] and white_king[0][1] + 2 == black_knights[i][1] and black_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif white_king[0][0] + 2 == black_knights[i][0] and white_king[0][1] + 1 == black_knights[i][1] and black_knights[i][2] == True:
                    
                    if move in legal_moves:

                        legal_moves.remove(move)

                elif white_king[0][0] + 2 == black_knights[i][0] and white_king[0][1] - 1 == black_knights[i][1] and black_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif white_king[0][0] + 1 == black_knights[i][0] and white_king[0][1] - 2 == black_knights[i][1] and black_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif white_king[0][0] - 1 == black_knights[i][0] and white_king[0][1] - 2 == black_knights[i][1] and black_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif white_king[0][0] - 2 == black_knights[i][0] and white_king[0][1] - 1 == black_knights[i][1] and black_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif white_king[0][0] - 2 == black_knights[i][0] and white_king[0][1] + 1 == black_knights[i][1] and black_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif white_king[0][0] - 1 == black_knights[i][0] and white_king[0][1] + 2 == black_knights[i][1] and black_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

            for i in range(0, 10):

                remove = True

                if black_bishops[i][2] == True and abs(black_bishops[i][0] - white_king[0][0]) == abs(black_bishops[i][1] - white_king[0][1]):

                    if black_bishops[i][0] > white_king[0][0]:

                        if black_bishops[i][1] > white_king[0][1]:

                            for j in range(1, abs(black_bishops[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] + j and white_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] + j and black_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(black_bishops[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] + j and white_occ_y[k] == white_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] + j and black_occ_y[k] == white_king[0][1] - j:

                                        remove = False
                            
                    else:

                        if black_bishops[i][1] > white_king[0][1]:

                            for j in range(1, abs(black_bishops[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] - j and white_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] - j and black_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(black_bishops[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] - j and white_occ_y[k] == white_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] - j and black_occ_y[k] == white_king[0][1] - j:

                                        remove = False
                                        
                    if remove == True and move in legal_moves:

                        legal_moves.remove(move)

            for i in range(0, 10):

                remove = True

                if black_rooks[i][2] == True:

                    if black_rooks[i][0] == white_king[0][0]:

                        if black_rooks[i][1] > white_king[0][1]:

                            for j in range(1, abs(black_rooks[i][1] - white_king[0][1])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] and white_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] and black_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(black_rooks[i][1] - white_king[0][1])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] and white_occ_y[k] == white_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] and black_occ_y[k] == white_king[0][1] - j:

                                        remove = False

                        if remove == True and move in legal_moves:

                            legal_moves.remove(move)

                    elif black_rooks[i][1] == white_king[0][1]:

                        if black_rooks[i][0] > white_king[0][0]:

                            for j in range(1, abs(black_rooks[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] + j and white_occ_y[k] == white_king[0][1]:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] + j and black_occ_y[k] == white_king[0][1]:

                                        remove = False

                        else:

                            for j in range(1, abs(black_rooks[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] - j and white_occ_y[k] == white_king[0][1]:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] - j and black_occ_y[k] == white_king[0][1]:

                                        remove = False

                        if remove == True and move in legal_moves:

                            legal_moves.remove(move)

            for i in range(0, 9):

                remove = True

                if black_queens[i][2] == True and abs(black_queens[i][0] - white_king[0][0]) == abs(black_queens[i][1] - white_king[0][1]):

                    if black_queens[i][0] > white_king[0][0]:

                        if black_queens[i][1] > white_king[0][1]:

                            for j in range(1, abs(black_queens[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] + j and white_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] + j and black_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(black_queens[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] + j and white_occ_y[k] == white_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] + j and black_occ_y[k] == white_king[0][1] - j:

                                        remove = False
                            
                    else:

                        if black_queens[i][1] > white_king[0][1]:

                            for j in range(1, abs(black_queens[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] - j and white_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] - j and black_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(black_queens[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] - j and white_occ_y[k] == white_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] - j and black_occ_y[k] == white_king[0][1] - j:

                                        remove = False
                                        
                    if remove == True and move in legal_moves:

                        legal_moves.remove(move)

                remove = True

                if black_queens[i][2] == True:

                    if black_queens[i][0] == white_king[0][0]:

                        if black_queens[i][1] > white_king[0][1]:

                            for j in range(1, abs(black_queens[i][1] - white_king[0][1])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] and white_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] and black_occ_y[k] == white_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(black_queens[i][1] - white_king[0][1])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] and white_occ_y[k] == white_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] and black_occ_y[k] == white_king[0][1] - j:

                                        remove = False

                        if remove == True and move in legal_moves:

                            legal_moves.remove(move)

                    elif black_queens[i][1] == white_king[0][1]:

                        if black_queens[i][0] > white_king[0][0]:

                            for j in range(1, abs(black_queens[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] + j and white_occ_y[k] == white_king[0][1]:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] + j and black_occ_y[k] == white_king[0][1]:

                                        remove = False

                        else:

                            for j in range(1, abs(black_queens[i][0] - white_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == white_king[0][0] - j and white_occ_y[k] == white_king[0][1]:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == white_king[0][0] - j and black_occ_y[k] == white_king[0][1]:

                                        remove = False

                        if remove == True and move in legal_moves:

                            legal_moves.remove(move)

            if abs(black_king[0][0] - white_king[0][0]) <= 1 and abs(black_king[0][1] - white_king[0][1]) <= 1:

                if move in legal_moves:

                    legal_moves.remove(move)

        else:

            for i in range(0, 8):

                if black_king[0][0] + 1 == white_pawns[i][0] and black_king[0][1] - 1 == white_pawns[i][1] and white_pawns[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif black_king[0][0] - 1 == white_pawns[i][0] and black_king[0][1] - 1 == white_pawns[i][1] and white_pawns[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)
                    
            for i in range(0, 10):

                if black_king[0][0] + 1 == white_knights[i][0] and black_king[0][1] + 2 == white_knights[i][1] and white_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif black_king[0][0] + 2 == white_knights[i][0] and black_king[0][1] + 1 == white_knights[i][1] and white_knights[i][2] == True:
                    
                    if move in legal_moves:

                        legal_moves.remove(move)

                elif black_king[0][0] + 2 == white_knights[i][0] and black_king[0][1] - 1 == white_knights[i][1] and white_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif black_king[0][0] + 1 == white_knights[i][0] and black_king[0][1] - 2 == white_knights[i][1] and white_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif black_king[0][0] - 1 == white_knights[i][0] and black_king[0][1] - 2 == white_knights[i][1] and white_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif black_king[0][0] - 2 == white_knights[i][0] and black_king[0][1] - 1 == white_knights[i][1] and white_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif black_king[0][0] - 2 == white_knights[i][0] and black_king[0][1] + 1 == white_knights[i][1] and white_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

                elif black_king[0][0] - 1 == white_knights[i][0] and black_king[0][1] + 2 == white_knights[i][1] and white_knights[i][2] == True:

                    if move in legal_moves:

                        legal_moves.remove(move)

            for i in range(0, 10):

                remove = True

                if white_bishops[i][2] == True and abs(white_bishops[i][0] - black_king[0][0]) == abs(white_bishops[i][1] - black_king[0][1]):

                    if white_bishops[i][0] > black_king[0][0]:

                        if white_bishops[i][1] > black_king[0][1]:

                            for j in range(1, abs(white_bishops[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] + j and white_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] + j and black_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(white_bishops[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] + j and white_occ_y[k] == black_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] + j and black_occ_y[k] == black_king[0][1] - j:

                                        remove = False
                            
                    else:

                        if white_bishops[i][1] > black_king[0][1]:

                            for j in range(1, abs(white_bishops[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] - j and white_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] - j and black_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(white_bishops[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] - j and white_occ_y[k] == black_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] - j and black_occ_y[k] == black_king[0][1] - j:

                                        remove = False
                                        
                    if remove == True and move in legal_moves:

                        legal_moves.remove(move)

            for i in range(0, 10):

                remove = True

                if white_rooks[i][2] == True:

                    if white_rooks[i][0] == black_king[0][0]:

                        if white_rooks[i][1] > black_king[0][1]:

                            for j in range(1, abs(white_rooks[i][1] - black_king[0][1])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] and white_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] and black_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(white_rooks[i][1] - black_king[0][1])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] and white_occ_y[k] == black_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] and black_occ_y[k] == black_king[0][1] - j:

                                        remove = False

                        if remove == True and move in legal_moves:

                            legal_moves.remove(move)

                    elif white_rooks[i][1] == black_king[0][1]:

                        if white_rooks[i][0] > black_king[0][0]:

                            for j in range(1, abs(white_rooks[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] + j and white_occ_y[k] == black_king[0][1]:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] + j and black_occ_y[k] == black_king[0][1]:

                                        remove = False

                        else:

                            for j in range(1, abs(white_rooks[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] - j and white_occ_y[k] == black_king[0][1]:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] - j and black_occ_y[k] == black_king[0][1]:

                                        remove = False

                        if remove == True and move in legal_moves:

                            legal_moves.remove(move)

            for i in range(0, 9):

                remove = True

                if white_queens[i][2] == True and abs(white_queens[i][0] - black_king[0][0]) == abs(white_queens[i][1] - black_king[0][1]):

                    if white_queens[i][0] > black_king[0][0]:

                        if white_queens[i][1] > black_king[0][1]:

                            for j in range(1, abs(white_queens[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] + j and white_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] + j and black_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(white_queens[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] + j and white_occ_y[k] == black_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] + j and black_occ_y[k] == black_king[0][1] - j:

                                        remove = False
                            
                    else:

                        if white_queens[i][1] > black_king[0][1]:

                            for j in range(1, abs(white_queens[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] - j and white_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] - j and black_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(white_queens[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] - j and white_occ_y[k] == black_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] - j and black_occ_y[k] == black_king[0][1] - j:

                                        remove = False
                                        
                    if remove == True and move in legal_moves:

                        legal_moves.remove(move)

                remove = True

                if white_queens[i][2] == True:

                    if white_queens[i][0] == black_king[0][0]:

                        if white_queens[i][1] > black_king[0][1]:

                            for j in range(1, abs(white_queens[i][1] - black_king[0][1])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] and white_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] and black_occ_y[k] == black_king[0][1] + j:

                                        remove = False

                        else:

                            for j in range(1, abs(white_queens[i][1] - black_king[0][1])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] and white_occ_y[k] == black_king[0][1] - j:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] and black_occ_y[k] == black_king[0][1] - j:

                                        remove = False

                        if remove == True and move in legal_moves:

                            legal_moves.remove(move)

                    elif white_queens[i][1] == black_king[0][1]:

                        if white_queens[i][0] > black_king[0][0]:

                            for j in range(1, abs(white_queens[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] + j and white_occ_y[k] == black_king[0][1]:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] + j and black_occ_y[k] == black_king[0][1]:

                                        remove = False

                        else:

                            for j in range(1, abs(white_queens[i][0] - black_king[0][0])):

                                for k in range(0, len(white_occ_x)):

                                    if white_occ_x[k] == black_king[0][0] - j and white_occ_y[k] == black_king[0][1]:

                                        remove = False

                                for k in range(0, len(black_occ_x)):

                                    if black_occ_x[k] == black_king[0][0] - j and black_occ_y[k] == black_king[0][1]:

                                        remove = False

                        if remove == True and move in legal_moves:

                            legal_moves.remove(move)

            if abs(white_king[0][0] - black_king[0][0]) <= 1 and abs(white_king[0][1] - black_king[0][1]) <= 1:

                if move in legal_moves:

                    legal_moves.remove(move)

        if white_short_castle_through_check_check == True:

            white_short_castle_through_check_check = False

            if move not in legal_moves:

                if "O-O" in legal_moves:

                    legal_moves.remove("O-O")

        elif white_long_castle_through_check_check == True:

            white_long_castle_through_check_check = False

            if move not in legal_moves:

                if "O-O-O" in legal_moves:

                    legal_moves.remove("O-O-O")

        elif black_short_castle_through_check_check == True:

            black_short_castle_through_check_check = False

            if move not in legal_moves:

                if "O-O" in legal_moves:

                    legal_moves.remove("O-O")

        elif black_long_castle_through_check_check == True:

            black_long_castle_through_check_check = False

            if move not in legal_moves:

                if "O-O-O" in legal_moves:

                    legal_moves.remove("O-O-O")

    return legal_moves
                    
def convert_to_easy_notation(notation_val):

    take = False

    if notation_val[-1] == "+":
        
        notation_val = notation_val.replace("+", "")

    for character in notation_val:

        if character == "x":
            
            take = True
            notation_val = notation_val.replace("x", "")

    return notation_val, take

def move_piece(notation_val, take, white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf):

    en_passant_x_y = [8, 8]
    half_moves += 1

    if white_turn == False:

        turn_num += 1

    if notation_val[0] == "B":

        from_x = get_column_char(notation_val[1])
        from_y = int(notation_val[2]) - 1

        to_x = get_column_char(notation_val[3])
        to_y = int(notation_val[4]) - 1

        if white_turn == True:

            for i in range(0, 10):

                if white_bishops_inf[i][2] == True and white_bishops_inf[i][0] == from_x and white_bishops_inf[i][1] == from_y:
                    
                    white_bishops_inf[i][0] = to_x
                    white_bishops_inf[i][1] = to_y

        else:

            for i in range(0, 10):

                if black_bishops_inf[i][2] == True and black_bishops_inf[i][0] == from_x and black_bishops_inf[i][1] == from_y:
                    
                    black_bishops_inf[i][0] = to_x
                    black_bishops_inf[i][1] = to_y

    elif notation_val[0] == "N":

        from_x = get_column_char(notation_val[1])
        from_y = int(notation_val[2]) - 1

        to_x = get_column_char(notation_val[3])
        to_y = int(notation_val[4]) - 1

        if white_turn == True:

            for i in range(0, 10):

                if white_knights_inf[i][2] == True and white_knights_inf[i][0] == from_x and white_knights_inf[i][1] == from_y:
                    
                    white_knights_inf[i][0] = to_x
                    white_knights_inf[i][1] = to_y

        else:

            for i in range(0, 10):

                if black_knights_inf[i][2] == True and black_knights_inf[i][0] == from_x and black_knights_inf[i][1] == from_y:
                    
                    black_knights_inf[i][0] = to_x
                    black_knights_inf[i][1] = to_y

    elif notation_val[0] == "R":

        from_x = get_column_char(notation_val[1])
        from_y = int(notation_val[2]) - 1

        to_x = get_column_char(notation_val[3])
        to_y = int(notation_val[4]) - 1

        if white_turn == True:

            for i in range(0, 10):

                if white_rooks_inf[i][2] == True and white_rooks_inf[i][0] == from_x and white_rooks_inf[i][1] == from_y:
                    
                    white_rooks_inf[i][0] = to_x
                    white_rooks_inf[i][1] = to_y
                    white_rooks_inf[i][3] = False

        else:

            for i in range(0, 10):

                if black_rooks_inf[i][2] == True and black_rooks_inf[i][0] == from_x and black_rooks_inf[i][1] == from_y:
                    
                    black_rooks_inf[i][0] = to_x
                    black_rooks_inf[i][1] = to_y
                    black_rooks_inf[i][3] = False

    elif notation_val[0] == "Q":

        from_x = get_column_char(notation_val[1])
        from_y = int(notation_val[2]) - 1

        to_x = get_column_char(notation_val[3])
        to_y = int(notation_val[4]) - 1

        if white_turn == True:

            for i in range(0, 9):

                if white_queens_inf[i][2] == True and white_queens_inf[i][0] == from_x and white_queens_inf[i][1] == from_y:
                    
                    white_queens_inf[i][0] = to_x
                    white_queens_inf[i][1] = to_y

        else:

            for i in range(0, 9):

                if black_queens_inf[i][2] == True and black_queens_inf[i][0] == from_x and black_queens_inf[i][1] == from_y:
                    
                    black_queens_inf[i][0] = to_x
                    black_queens_inf[i][1] = to_y

    elif notation_val[0] == "K":

        from_x = get_column_char(notation_val[1])
        from_y = int(notation_val[2]) - 1

        to_x = get_column_char(notation_val[3])
        to_y = int(notation_val[4]) - 1

        if white_turn == True:

            if white_king_inf[0][2] == True and white_king_inf[0][0] == from_x and white_king_inf[0][1] == from_y:
                    
                white_king_inf[0][0] = to_x
                white_king_inf[0][1] = to_y
                white_king_inf[0][3] = False

        else:

            if black_king_inf[0][2] == True and black_king_inf[0][0] == from_x and black_king_inf[0][1] == from_y:
                    
                black_king_inf[0][0] = to_x
                black_king_inf[0][1] = to_y
                black_king_inf[0][3] = False

    elif notation_val[0] == "O":

        if white_turn == True:

            white_king_inf[0][3] = False

            if notation_val == "O-O":

                white_rooks_inf[1][3] = False

                white_king_inf[0][0] = 6
                white_king_inf[0][1] = 0

                for i in range(0, 2):

                    if white_rooks_inf[i][0] == 7:
                
                        white_rooks_inf[i][0] = 5
                        white_rooks_inf[i][1] = 0

            elif notation_val == "O-O-O":

                white_rooks_inf[0][3] = False

                white_king_inf[0][0] = 2
                white_king_inf[0][1] = 0

                for i in range(0, 2):

                    if white_rooks_inf[i][0] == 0:
                
                        white_rooks_inf[i][0] = 3
                        white_rooks_inf[i][1] = 0
                        
        else:

            black_king_inf[0][3] = False

            if notation_val == "O-O":

                black_rooks_inf[1][3] = False

                black_king_inf[0][0] = 6
                black_king_inf[0][1] = 7

                for i in range(0, 2):

                    if black_rooks_inf[i][0] == 7:
                
                        black_rooks_inf[i][0] = 5
                        black_rooks_inf[i][1] = 7

            elif notation_val == "O-O-O":

                black_rooks_inf[0][3] = False

                black_king_inf[0][0] = 2
                black_king_inf[0][1] = 7

                for i in range(0, 2):

                    if black_rooks_inf[i][0] == 0:
                
                        black_rooks_inf[i][0] = 3
                        black_rooks_inf[i][1] = 7

    else:

        half_moves = 0

        repetition_draw_file_write = open("repetition_draw_file.txt", "w")
        repetition_draw_file_write.write("")
        repetition_draw_file_write.close()

        if notation_val[-2] == "=":

            to_x = get_column_char(notation_val[-4])
            to_y = int(notation_val[-3]) - 1

        else:
        
            to_x = get_column_char(notation_val[-2])
            to_y = int(notation_val[-1]) - 1

        if take == True:

            if notation_val[-2] == "=":

                from_x = get_column_char(notation_val[-5])

            else:

                from_x = get_column_char(notation_val[-3])

            if white_turn == True:
                
                from_y = to_y - 1

            else:

                from_y = to_y + 1
        else:

            from_x = to_x

            if white_turn == True:

                if to_y == 3:

                    from_y = to_y - 2

                    for i in range(0, 8):

                        if white_pawns_inf[i][2] == True and white_pawns_inf[i][0] == from_x and white_pawns_inf[i][1] == to_y - 1:

                            from_y = to_y - 1

                else:

                    from_y = to_y - 1

            else:

                if to_y == 4:

                    from_y = to_y + 2

                    for i in range(0, 8):

                        if black_pawns_inf[i][2] == True and black_pawns_inf[i][0] == from_x and black_pawns_inf[i][1] == to_y + 1:

                            from_y = to_y + 1

                else:

                    from_y = to_y + 1

        if white_turn == True:

            for i in range(0, 8):

                if white_pawns_inf[i][2] == True and white_pawns_inf[i][0] == from_x and white_pawns_inf[i][1] == from_y:
                    
                    if to_y == 7:

                        white_pawns_inf[i][2] = False

                        if notation_val[-1] == "Q":

                            promotion_complete = False

                            for i in range(1, 9):

                                if white_queens_inf[i][2] == False and promotion_complete == False:

                                    promotion_complete = True

                                    white_queens_inf[i][0] = to_x
                                    white_queens_inf[i][1] = to_y
                                    white_queens_inf[i][2] = True

                        elif notation_val[-1] == "R":

                            promotion_complete = False

                            for i in range(2, 10):

                                if white_rooks_inf[i][2] == False and promotion_complete == False:

                                    promotion_complete = True

                                    white_rooks_inf[i][0] = to_x
                                    white_rooks_inf[i][1] = to_y
                                    white_rooks_inf[i][2] = True
                                    white_rooks_inf[i][3] = False

                        elif notation_val[-1] == "B":

                            promotion_complete = False

                            for i in range(2, 10):

                                if white_bishops_inf[i][2] == False and promotion_complete == False:

                                    promotion_complete = True

                                    white_bishops_inf[i][0] = to_x
                                    white_bishops_inf[i][1] = to_y
                                    white_bishops_inf[i][2] = True

                        elif notation_val[-1] == "N":

                            promotion_complete = False

                            for i in range(2, 10):

                                if white_knights_inf[i][2] == False and promotion_complete == False:

                                    promotion_complete = True

                                    white_knights_inf[i][0] = to_x
                                    white_knights_inf[i][1] = to_y
                                    white_knights_inf[i][2] = True

                    else:

                        white_pawns_inf[i][0] = to_x
                        white_pawns_inf[i][1] = to_y  
                        white_pawns_inf[i][3] = False

                        if to_y - from_y == 2:

                            en_passant_x_y = [to_x, to_y]

        else:

            for i in range(0, 8):

                if black_pawns_inf[i][2] == True and black_pawns_inf[i][0] == from_x and black_pawns_inf[i][1] == from_y:

                    if to_y == 0:

                        black_pawns_inf[i][2] = False

                        if notation_val[-1] == "Q":

                            promotion_complete = False

                            for i in range(1, 9):

                                if black_queens_inf[i][2] == False and promotion_complete == False:

                                    promotion_complete = True

                                    black_queens_inf[i][0] = to_x
                                    black_queens_inf[i][1] = to_y
                                    black_queens_inf[i][2] = True

                        elif notation_val[-1] == "R":

                            promotion_complete = False

                            for i in range(2, 10):

                                if black_rooks_inf[i][2] == False and promotion_complete == False:

                                    promotion_complete = True

                                    black_rooks_inf[i][0] = to_x
                                    black_rooks_inf[i][1] = to_y
                                    black_rooks_inf[i][2] = True
                                    black_rooks_inf[i][3] = False

                        elif notation_val[-1] == "B":

                            promotion_complete = False

                            for i in range(2, 10):

                                if black_bishops_inf[i][2] == False and promotion_complete == False:

                                    promotion_complete = True

                                    black_bishops_inf[i][0] = to_x
                                    black_bishops_inf[i][1] = to_y
                                    black_bishops_inf[i][2] = True

                        elif notation_val[-1] == "N":

                            promotion_complete = False

                            for i in range(2, 10):

                                if black_knights_inf[i][2] == False and promotion_complete == False:

                                    promotion_complete = True

                                    black_knights_inf[i][0] = to_x
                                    black_knights_inf[i][1] = to_y
                                    black_knights_inf[i][2] = True
                
                    else:

                        black_pawns_inf[i][0] = to_x
                        black_pawns_inf[i][1] = to_y                                
                        black_pawns_inf[i][3] = False

                        if from_y - to_y == 2:

                            en_passant_x_y = [to_x, to_y]

    if take == True:

        half_moves = 0

        repetition_draw_file_write = open("repetition_draw_file.txt", "w")
        repetition_draw_file_write.write("")
        repetition_draw_file_write.close()

        peice_taken = False

        if white_turn == True:

            for i in range(0, 8):

                if black_pawns_inf[i][2] == True and black_pawns_inf[i][0] == to_x and black_pawns_inf[i][1] == to_y:

                    black_pawns_inf[i][2] = False

                    peice_taken = True

            for i in range(0, 10):

                if black_bishops_inf[i][2] == True and black_bishops_inf[i][0] == to_x and black_bishops_inf[i][1] == to_y:

                    black_bishops_inf[i][2] = False

                    peice_taken = True

            for i in range(0, 10):

                if black_knights_inf[i][2] == True and black_knights_inf[i][0] == to_x and black_knights_inf[i][1] == to_y:

                    black_knights_inf[i][2] = False

                    peice_taken = True

            for i in range(0, 10):

                if black_rooks_inf[i][2] == True and black_rooks_inf[i][0] == to_x and black_rooks_inf[i][1] == to_y:

                    black_rooks_inf[i][2] = False

                    peice_taken = True

            for i in range(0, 9):

                if black_queens_inf[i][2] == True and black_queens_inf[i][0] == to_x and black_queens_inf[i][1] == to_y:

                    black_queens_inf[i][2] = False

                    peice_taken = True

            if peice_taken == False:

                for i in range(0, 8):

                    if black_pawns_inf[i][2] == True and black_pawns_inf[i][0] == to_x and black_pawns_inf[i][1] == to_y - 1:

                        black_pawns_inf[i][2] = False
                    
        else:

            for i in range(0, 8):

                if white_pawns_inf[i][2] == True and white_pawns_inf[i][0] == to_x and white_pawns_inf[i][1] == to_y:

                    white_pawns_inf[i][2] = False

                    peice_taken = True

            for i in range(0, 10):

                if white_bishops_inf[i][2] == True and white_bishops_inf[i][0] == to_x and white_bishops_inf[i][1] == to_y:

                    white_bishops_inf[i][2] = False

                    peice_taken = True

            for i in range(0, 10):

                if white_knights_inf[i][2] == True and white_knights_inf[i][0] == to_x and white_knights_inf[i][1] == to_y:

                    white_knights_inf[i][2] = False

                    peice_taken = True

            for i in range(0, 10):

                if white_rooks_inf[i][2] == True and white_rooks_inf[i][0] == to_x and white_rooks_inf[i][1] == to_y:

                    white_rooks_inf[i][2] = False

                    peice_taken = True

            for i in range(0, 9):

                if white_queens_inf[i][2] == True and white_queens_inf[i][0] == to_x and white_queens_inf[i][1] == to_y:

                    white_queens_inf[i][2] = False

                    peice_taken = True

            if peice_taken == False:

                for i in range(0, 8):

                    if white_pawns_inf[i][2] == True and white_pawns_inf[i][0] == to_x and white_pawns_inf[i][1] == to_y + 1:

                        white_pawns_inf[i][2] = False

    return white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf, en_passant_x_y, half_moves, turn_num
                            
def stale_check_mate(white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf):

    checkmate = False

    if white_turn == True:

        for i in range(0, 8):

            if checkmate == False and white_king_inf[0][0] + 1 == black_pawns_inf[i][0] and white_king_inf[0][1] + 1 == black_pawns_inf[i][1] and black_pawns_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and white_king_inf[0][0] - 1 == black_pawns_inf[i][0] and white_king_inf[0][1] + 1 == black_pawns_inf[i][1] and black_pawns_inf[i][2] == True:

                checkmate = True
                
        for i in range(0, 10):

            if checkmate == False and white_king_inf[0][0] + 1 == black_knights_inf[i][0] and white_king_inf[0][1] + 2 == black_knights_inf[i][1] and black_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and white_king_inf[0][0] + 2 == black_knights_inf[i][0] and white_king_inf[0][1] + 1 == black_knights_inf[i][1] and black_knights_inf[i][2] == True:
                
                checkmate = True

            elif checkmate == False and white_king_inf[0][0] + 2 == black_knights_inf[i][0] and white_king_inf[0][1] - 1 == black_knights_inf[i][1] and black_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and white_king_inf[0][0] + 1 == black_knights_inf[i][0] and white_king_inf[0][1] - 2 == black_knights_inf[i][1] and black_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and white_king_inf[0][0] - 1 == black_knights_inf[i][0] and white_king_inf[0][1] - 2 == black_knights_inf[i][1] and black_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and white_king_inf[0][0] - 2 == black_knights_inf[i][0] and white_king_inf[0][1] - 1 == black_knights_inf[i][1] and black_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and white_king_inf[0][0] - 2 == black_knights_inf[i][0] and white_king_inf[0][1] + 1 == black_knights_inf[i][1] and black_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and white_king_inf[0][0] - 1 == black_knights_inf[i][0] and white_king_inf[0][1] + 2 == black_knights_inf[i][1] and black_knights_inf[i][2] == True:

                checkmate = True

        for i in range(0, 10):

            remove = True

            if checkmate == False and black_bishops_inf[i][2] == True and abs(black_bishops_inf[i][0] - white_king_inf[0][0]) == abs(black_bishops_inf[i][1] - white_king_inf[0][1]):

                if black_bishops_inf[i][0] > white_king_inf[0][0]:

                    if black_bishops_inf[i][1] > white_king_inf[0][1]:

                        for j in range(1, abs(black_bishops_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] + j and white_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] + j and black_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(black_bishops_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] + j and white_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] + j and black_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False
                        
                else:

                    if black_bishops_inf[i][1] > white_king_inf[0][1]:

                        for j in range(1, abs(black_bishops_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] - j and white_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] - j and black_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(black_bishops_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] - j and white_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] - j and black_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False
                                    
                if remove == True:

                    checkmate = True

        for i in range(0, 10):

            remove = True

            if checkmate == False and black_rooks_inf[i][2] == True:

                if black_rooks_inf[i][0] == white_king_inf[0][0]:

                    if black_rooks_inf[i][1] > white_king_inf[0][1]:

                        for j in range(1, abs(black_rooks_inf[i][1] - white_king_inf[0][1])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] and white_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] and black_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(black_rooks_inf[i][1] - white_king_inf[0][1])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] and white_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] and black_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False

                    if remove == True:

                        checkmate = True

                elif black_rooks_inf[i][1] == white_king_inf[0][1]:

                    if black_rooks_inf[i][0] > white_king_inf[0][0]:

                        for j in range(1, abs(black_rooks_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] + j and white_occupation_y[k] == white_king_inf[0][1]:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] + j and black_occupation_y[k] == white_king_inf[0][1]:

                                    remove = False

                    else:

                        for j in range(1, abs(black_rooks_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] - j and white_occupation_y[k] == white_king_inf[0][1]:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] - j and black_occupation_y[k] == white_king_inf[0][1]:

                                    remove = False

                    if remove == True:

                        checkmate = True

        for i in range(0, 9):

            remove = True

            if checkmate == False and black_queens_inf[i][2] == True and abs(black_queens_inf[i][0] - white_king_inf[0][0]) == abs(black_queens_inf[i][1] - white_king_inf[0][1]):

                if black_queens_inf[i][0] > white_king_inf[0][0]:

                    if black_queens_inf[i][1] > white_king_inf[0][1]:

                        for j in range(1, abs(black_queens_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] + j and white_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] + j and black_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(black_queens_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] + j and white_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] + j and black_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False
                        
                else:

                    if black_queens_inf[i][1] > white_king_inf[0][1]:

                        for j in range(1, abs(black_queens_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] - j and white_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] - j and black_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(black_queens_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] - j and white_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] - j and black_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False
                                    
                if remove == True:

                    checkmate = True

            remove = True

            if checkmate == False and black_queens_inf[i][2] == True:

                if black_queens_inf[i][0] == white_king_inf[0][0]:

                    if black_queens_inf[i][1] > white_king_inf[0][1]:

                        for j in range(1, abs(black_queens_inf[i][1] - white_king_inf[0][1])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] and white_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] and black_occupation_y[k] == white_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(black_queens_inf[i][1] - white_king_inf[0][1])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] and white_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] and black_occupation_y[k] == white_king_inf[0][1] - j:

                                    remove = False

                    if remove == True:

                        checkmate = True

                elif black_queens_inf[i][1] == white_king_inf[0][1]:

                    if black_queens_inf[i][0] > white_king_inf[0][0]:

                        for j in range(1, abs(black_queens_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] + j and white_occupation_y[k] == white_king_inf[0][1]:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] + j and black_occupation_y[k] == white_king_inf[0][1]:

                                    remove = False

                    else:

                        for j in range(1, abs(black_queens_inf[i][0] - white_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == white_king_inf[0][0] - j and white_occupation_y[k] == white_king_inf[0][1]:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == white_king_inf[0][0] - j and black_occupation_y[k] == white_king_inf[0][1]:

                                    remove = False

                    if remove == True:

                        checkmate = True

    else:

        for i in range(0, 8):

            if checkmate == False and black_king_inf[0][0] + 1 == white_pawns_inf[i][0] and black_king_inf[0][1] - 1 == white_pawns_inf[i][1] and white_pawns_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and black_king_inf[0][0] - 1 == white_pawns_inf[i][0] and black_king_inf[0][1] - 1 == white_pawns_inf[i][1] and white_pawns_inf[i][2] == True:

                checkmate = True
                
        for i in range(0, 10):

            if checkmate == False and black_king_inf[0][0] + 1 == white_knights_inf[i][0] and black_king_inf[0][1] + 2 == white_knights_inf[i][1] and white_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and black_king_inf[0][0] + 2 == white_knights_inf[i][0] and black_king_inf[0][1] + 1 == white_knights_inf[i][1] and white_knights_inf[i][2] == True:
                
                checkmate = True

            elif checkmate == False and black_king_inf[0][0] + 2 == white_knights_inf[i][0] and black_king_inf[0][1] - 1 == white_knights_inf[i][1] and white_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and black_king_inf[0][0] + 1 == white_knights_inf[i][0] and black_king_inf[0][1] - 2 == white_knights_inf[i][1] and white_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and black_king_inf[0][0] - 1 == white_knights_inf[i][0] and black_king_inf[0][1] - 2 == white_knights_inf[i][1] and white_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and black_king_inf[0][0] - 2 == white_knights_inf[i][0] and black_king_inf[0][1] - 1 == white_knights_inf[i][1] and white_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and black_king_inf[0][0] - 2 == white_knights_inf[i][0] and black_king_inf[0][1] + 1 == white_knights_inf[i][1] and white_knights_inf[i][2] == True:

                checkmate = True

            elif checkmate == False and black_king_inf[0][0] - 1 == white_knights_inf[i][0] and black_king_inf[0][1] + 2 == white_knights_inf[i][1] and white_knights_inf[i][2] == True:

                checkmate = True

        for i in range(0, 10):

            remove = True

            if checkmate == False and white_bishops_inf[i][2] == True and abs(white_bishops_inf[i][0] - black_king_inf[0][0]) == abs(white_bishops_inf[i][1] - black_king_inf[0][1]):

                if white_bishops_inf[i][0] > black_king_inf[0][0]:

                    if white_bishops_inf[i][1] > black_king_inf[0][1]:

                        for j in range(1, abs(white_bishops_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] + j and white_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] + j and black_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(white_bishops_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] + j and white_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] + j and black_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False
                        
                else:

                    if white_bishops_inf[i][1] > black_king_inf[0][1]:

                        for j in range(1, abs(white_bishops_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] - j and white_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] - j and black_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(white_bishops_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] - j and white_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] - j and black_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False
                                    
                if remove == True:

                    checkmate = True

        for i in range(0, 10):

            remove = True

            if checkmate == False and white_rooks_inf[i][2] == True:

                if white_rooks_inf[i][0] == black_king_inf[0][0]:

                    if white_rooks_inf[i][1] > black_king_inf[0][1]:

                        for j in range(1, abs(white_rooks_inf[i][1] - black_king_inf[0][1])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] and white_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] and black_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(white_rooks_inf[i][1] - black_king_inf[0][1])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] and white_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] and black_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False

                    if remove == True:

                        checkmate = True

                elif white_rooks_inf[i][1] == black_king_inf[0][1]:

                    if white_rooks_inf[i][0] > black_king_inf[0][0]:

                        for j in range(1, abs(white_rooks_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] + j and white_occupation_y[k] == black_king_inf[0][1]:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] + j and black_occupation_y[k] == black_king_inf[0][1]:

                                    remove = False

                    else:

                        for j in range(1, abs(white_rooks_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] - j and white_occupation_y[k] == black_king_inf[0][1]:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] - j and black_occupation_y[k] == black_king_inf[0][1]:

                                    remove = False

                    if remove == True:

                        checkmate = True

        for i in range(0, 9):

            remove = True

            if checkmate == False and white_queens_inf[i][2] == True and abs(white_queens_inf[i][0] - black_king_inf[0][0]) == abs(white_queens_inf[i][1] - black_king_inf[0][1]):

                if white_queens_inf[i][0] > black_king_inf[0][0]:

                    if white_queens_inf[i][1] > black_king_inf[0][1]:

                        for j in range(1, abs(white_queens_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] + j and white_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] + j and black_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(white_queens_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] + j and white_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] + j and black_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False
                        
                else:

                    if white_queens_inf[i][1] > black_king_inf[0][1]:

                        for j in range(1, abs(white_queens_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] - j and white_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] - j and black_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(white_queens_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] - j and white_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] - j and black_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False
                                    
                if remove == True:

                    checkmate = True

            remove = True

            if checkmate == False and white_queens_inf[i][2] == True:

                if white_queens_inf[i][0] == black_king_inf[0][0]:

                    if white_queens_inf[i][1] > black_king_inf[0][1]:

                        for j in range(1, abs(white_queens_inf[i][1] - black_king_inf[0][1])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] and white_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] and black_occupation_y[k] == black_king_inf[0][1] + j:

                                    remove = False

                    else:

                        for j in range(1, abs(white_queens_inf[i][1] - black_king_inf[0][1])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] and white_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] and black_occupation_y[k] == black_king_inf[0][1] - j:

                                    remove = False

                    if remove == True:

                        checkmate = True

                elif white_queens_inf[i][1] == black_king_inf[0][1]:

                    if white_queens_inf[i][0] > black_king_inf[0][0]:

                        for j in range(1, abs(white_queens_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] + j and white_occupation_y[k] == black_king_inf[0][1]:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] + j and black_occupation_y[k] == black_king_inf[0][1]:

                                    remove = False

                    else:

                        for j in range(1, abs(white_queens_inf[i][0] - black_king_inf[0][0])):

                            for k in range(0, len(white_occupation_x)):

                                if white_occupation_x[k] == black_king_inf[0][0] - j and white_occupation_y[k] == black_king_inf[0][1]:

                                    remove = False

                            for k in range(0, len(black_occupation_x)):

                                if black_occupation_x[k] == black_king_inf[0][0] - j and black_occupation_y[k] == black_king_inf[0][1]:

                                    remove = False

                    if remove == True:

                        checkmate = True

    return checkmate

def find_piece_name(x, y, white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf):

    found = False

    for i in range(0, 8):

        if white_pawns_inf[i][2] == True and white_pawns_inf[i][0] == x and white_pawns_inf[i][1] == y:

            found = True

            return "P"

    for i in range(0, 10):

        if white_bishops_inf[i][2] == True and white_bishops_inf[i][0] == x and white_bishops_inf[i][1] == y:

            found = True

            return "B"

    for i in range(0, 10):

        if white_knights_inf[i][2] == True and white_knights_inf[i][0] == x and white_knights_inf[i][1] == y:

            found = True

            return "N"

    for i in range(0, 10):

        if white_rooks_inf[i][2] == True and white_rooks_inf[i][0] == x and white_rooks_inf[i][1] == y:

            found = True

            return "R"

    for i in range(0, 9):

        if white_queens_inf[i][2] == True and white_queens_inf[i][0] == x and white_queens_inf[i][1] == y:

            found = True

            return "Q"

    if white_king_inf[0][2] == True and white_king_inf[0][0] == x and white_king_inf[0][1] == y:

        found = True

        return "K"

    for i in range(0, 8):

        if black_pawns_inf[i][2] == True and black_pawns_inf[i][0] == x and black_pawns_inf[i][1] == y:

            found = True

            return "P"

    for i in range(0, 10):

        if black_bishops_inf[i][2] == True and black_bishops_inf[i][0] == x and black_bishops_inf[i][1] == y:

            found = True

            return "B"

    for i in range(0, 10):

        if black_knights_inf[i][2] == True and black_knights_inf[i][0] == x and black_knights_inf[i][1] == y:

            found = True

            return "N"

    for i in range(0, 10):

        if black_rooks_inf[i][2] == True and black_rooks_inf[i][0] == x and black_rooks_inf[i][1] == y:

            found = True

            return "R"

    for i in range(0, 9):

        if black_queens_inf[i][2] == True and black_queens_inf[i][0] == x and black_queens_inf[i][1] == y:

            found = True

            return "Q"

    if black_king_inf[0][2] == True and black_king_inf[0][0] == x and black_king_inf[0][1] == y:

        found = True

        return "K"

    if found == False:

        return "none"

def no_moves(white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf):

    check_mate = stale_check_mate(white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf)

    if check_mate == True:

        if white_turn == True:

            print("Black wins by Checkmate!")

        else:

            print("White wins by Checkmate!")

    else:

        print("It's a draw by stalemate!")

    return check_mate

def check_draw_by_insufficient_material(white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf):

    keep_checking_for_draw = True

    white_minor_pieces_num = 0
    black_minor_pieces_num = 0

    if keep_checking_for_draw == True:

        for i in range(0, 8):

            if white_pawns_inf[i][2] == True:

                keep_checking_for_draw = False

                break

    if keep_checking_for_draw == True:

        for i in range(0, 8):

            if black_pawns_inf[i][2] == True:

                keep_checking_for_draw = False

                break

    if keep_checking_for_draw == True:

        for i in range(0, 9):

            if white_queens_inf[i][2] == True:

                keep_checking_for_draw = False

                break

    if keep_checking_for_draw == True:

        for i in range(0, 9):

            if black_queens_inf[i][2] == True:

                keep_checking_for_draw = False

                break

    if keep_checking_for_draw == True:

        for i in range(0, 10):

            if white_rooks_inf[i][2] == True:

                keep_checking_for_draw = False

                break

    if keep_checking_for_draw == True:

        for i in range(0, 10):

            if black_rooks_inf[i][2] == True:

                keep_checking_for_draw = False

                break

    if keep_checking_for_draw == True:

        for i in range(0, 8):

            if white_bishops_inf[i][2] == True:

                white_minor_pieces_num += 1

    if keep_checking_for_draw == True:

        for i in range(0, 8):

            if black_bishops_inf[i][2] == True:

                black_minor_pieces_num += 1

    if keep_checking_for_draw == True:

        for i in range(0, 8):

            if white_knights_inf[i][2] == True:

                white_minor_pieces_num += 1

    if keep_checking_for_draw == True:

        for i in range(0, 8):

            if black_knights_inf[i][2] == True:

                black_minor_pieces_num += 1

    if keep_checking_for_draw == True:

        if white_minor_pieces_num >= 2:

            keep_checking_for_draw = False

        if black_minor_pieces_num >= 2:

            keep_checking_for_draw = False

    if keep_checking_for_draw == True:

        game_over = True

        return True

    else:

        return False

def get_notation(piece, from_x, from_y, to_x, to_y, white_turn, white_occupation_x, white_occupation_y, black_occupation_x, black_occupation_y):

    notation_val = "error"

    capture = False

    if piece == "P":

        if to_y == 7 or to_y == 0:

            if to_x == from_x and (to_y == from_y + 1 or to_y == from_y - 1 or to_y == from_y + 2 or to_y == from_y - 2):
                
                notation_val = get_column(to_x) + get_row(to_y) + "="

            elif (to_x == from_x + 1 or to_x == from_x - 1) and (to_y == from_y + 1 or to_y == from_y - 1):

                notation_val = get_column(from_x) + "x" + get_column(to_x) + get_row(to_y) + "="

        else:

            if to_x == from_x and (to_y == from_y + 1 or to_y == from_y - 1 or to_y == from_y + 2 or to_y == from_y - 2):
                
                notation_val = get_column(to_x) + get_row(to_y)

            elif (to_x == from_x + 1 or to_x == from_x - 1) and (to_y == from_y + 1 or to_y == from_y - 1):

                notation_val = get_column(from_x) + "x" + get_column(to_x) + get_row(to_y)

    else:

        if white_turn == True:

            for i in range(0, len(black_occupation_x)):

                if to_x == black_occupation_x[i] and to_y == black_occupation_y[i]:

                    capture = True

        else:

            for i in range(0, len(white_occupation_x)):

                if to_x == white_occupation_x[i] and to_y == white_occupation_y[i]:

                    capture = True

        if capture == True:
                    
            notation_val = piece + get_column(from_x) + get_row(from_y) + "x" + get_column(to_x) + get_row(to_y)

        else:

            notation_val = piece + get_column(from_x) + get_row(from_y) + get_column(to_x) + get_row(to_y)

    return notation_val

def get_column(x):
    
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

def get_column_char(x):
    
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

def get_row(y):

    for i in range(0, 8):

        if y == i:

            return str(i + 1)

    if y != 0 and y != 1 and y != 2 and y != 3 and y != 4 and y != 5 and y != 6 and y != 7:

        return "9"

def create_fen_position(white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf):

    fen = "11111111/11111111/11111111/11111111/11111111/11111111/11111111/11111111 w KQkq - - -"

    pos = 83

    fen = fen[:pos] + str(turn_num) + fen[pos + 1:]

    pos = 81

    fen = fen[:pos] + str(half_moves) + fen[pos + 1:]

    if en_passant_x_y[0] != 8 and en_passant_x_y[1] != 8:

        pos = 79

        if white_turn == True:

            fen = fen[:pos] + get_column(en_passant_x_y[0]) + get_row(en_passant_x_y[1] + 1) + fen[pos + 1:]

        else:

            fen = fen[:pos] + get_column(en_passant_x_y[0]) + get_row(en_passant_x_y[1] - 1) + fen[pos + 1:]

    if black_king_inf[0][3] == True:

        black_queenside_castling = False
        black_kingside_castling = False

        for i in range(0, 10):

            if black_rooks_inf[i][2] == True and black_rooks_inf[i][3] == True and black_rooks_inf[i][0] == 0 and black_rooks_inf[i][1] == 7:

                black_queenside_castling = True

            if black_rooks_inf[i][2] == True and black_rooks_inf[i][3] == True and black_rooks_inf[i][0] == 7 and black_rooks_inf[i][1] == 7:

                black_kingside_castling = True

        if black_queenside_castling == False:

            pos = 77

            fen = fen[:pos] + fen[pos + 1:]

        if black_kingside_castling == False:

            pos = 76

            fen = fen[:pos] + fen[pos + 1:]

    else:

        pos = 76

        fen = fen[:pos] + fen[pos + 2:]

    if white_king_inf[0][3] == True:

        white_queenside_castling = False
        white_kingside_castling = False

        for i in range(0, 10):

            if white_rooks_inf[i][2] == True and white_rooks_inf[i][3] == True and white_rooks_inf[i][0] == 0 and white_rooks_inf[i][1] == 0:

                white_queenside_castling = True

            if white_rooks_inf[i][2] == True and white_rooks_inf[i][3] == True and white_rooks_inf[i][0] == 7 and white_rooks_inf[i][1] == 0:

                white_kingside_castling = True

        if white_queenside_castling == False:

            pos = 75

            fen = fen[:pos] + fen[pos + 1:]

        if white_kingside_castling == False:

            pos = 74

            fen = fen[:pos] + fen[pos + 1:]

    else:

        pos = 74

        if fen[76] == " ":

            fen = fen[:pos] + "-" + fen[pos + 2:]

        else:

            fen = fen[:pos] + fen[pos + 2:]

    pos = 72

    if white_turn == True:

        fen = fen[:pos] + "w" + fen[pos + 1:]

    else:

        fen = fen[:pos] + "b" + fen[pos + 1:]

    for i in range(0, 8):

        if white_pawns_inf[i][2] == True:

            pos = white_pawns_inf[i][0] + ((7 - white_pawns_inf[i][1]) * 9)

            fen = fen[:pos] + "P" + fen[pos + 1:]

    for i in range(0, 10):

        if white_bishops_inf[i][2] == True:

            pos = white_bishops_inf[i][0] + ((7 - white_bishops_inf[i][1]) * 9)

            fen = fen[:pos] + "B" + fen[pos + 1:]

    for i in range(0, 10):

        if white_knights_inf[i][2] == True:

            pos = white_knights_inf[i][0] + ((7 - white_knights_inf[i][1]) * 9)

            fen = fen[:pos] + "N" + fen[pos + 1:]

    for i in range(0, 10):

        if white_rooks_inf[i][2] == True:

            pos = white_rooks_inf[i][0] + ((7 - white_rooks_inf[i][1]) * 9)

            fen = fen[:pos] + "R" + fen[pos + 1:]

    for i in range(0, 9):

        if white_queens_inf[i][2] == True:

            pos = white_queens_inf[i][0] + ((7 - white_queens_inf[i][1]) * 9)

            fen = fen[:pos] + "Q" + fen[pos + 1:]

    if white_king_inf[0][2] == True:

        pos = white_king_inf[0][0] + ((7 - white_king_inf[0][1]) * 9)

        fen = fen[:pos] + "K" + fen[pos + 1:]

    for i in range(0, 8):

        if black_pawns_inf[i][2] == True:

            pos = black_pawns_inf[i][0] + ((7 - black_pawns_inf[i][1]) * 9)

            fen = fen[:pos] + "p" + fen[pos + 1:]

    for i in range(0, 10):

        if black_bishops_inf[i][2] == True:

            pos = black_bishops_inf[i][0] + ((7 - black_bishops_inf[i][1]) * 9)

            fen = fen[:pos] + "b" + fen[pos + 1:]

    for i in range(0, 10):

        if black_knights_inf[i][2] == True:

            pos = black_knights_inf[i][0] + ((7 - black_knights_inf[i][1]) * 9)

            fen = fen[:pos] + "n" + fen[pos + 1:]

    for i in range(0, 10):

        if black_rooks_inf[i][2] == True:

            pos = black_rooks_inf[i][0] + ((7 - black_rooks_inf[i][1]) * 9)

            fen = fen[:pos] + "r" + fen[pos + 1:]

    for i in range(0, 9):

        if black_queens_inf[i][2] == True:

            pos = black_queens_inf[i][0] + ((7 - black_queens_inf[i][1]) * 9)

            fen = fen[:pos] + "q" + fen[pos + 1:]

    if black_king_inf[0][2] == True:

        pos = black_king_inf[0][0] + ((7 - black_king_inf[0][1]) * 9)

        fen = fen[:pos] + "k" + fen[pos + 1:]
        
    pos = 0

    while fen[pos] != " ":

        if (fen[pos] == "1" or fen[pos] == "2" or fen[pos] == "3" or fen[pos] == "4" or fen[pos] == "5" or fen[pos] == "6" or fen[pos] == "7") and fen[pos + 1] == "1":

            fen = fen[:pos] + str(int(fen[pos]) + int(fen[pos + 1])) + fen[pos + 2:]

        else:

            pos += 1

    return fen

def load_fen_position(fen):

    white_pawns_inf = [[0, 1, False, False], [1, 1, False, False], [2, 1, False, False], [3, 1, False, False], [4, 1, False, False], [5, 1, False, False], [6, 1, False, False], [7, 1, False, False]]
    white_bishops_inf = [[2, 0, False], [5, 0, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False]]
    white_knights_inf = [[1, 0, False], [6, 0, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False]]
    white_rooks_inf = [[0, 0, False, False], [7, 0, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False]]
    white_queens_inf = [[3, 0, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False]]
    white_king_inf = [[4, 0, False, False]]

    black_pawns_inf = [[0, 6, False, False], [1, 6, False, False], [2, 6, False, False], [3, 6, False, False], [4, 6, False, False], [5, 6, False, False], [6, 6, False, False], [7, 6, False, False]]
    black_bishops_inf = [[2, 7, False], [5, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False]]
    black_knights_inf = [[6, 7, False], [1, 7, False], [6, 3, False], [0, 3, False], [2, 0, False], [2, 6, False], [6, 2, False], [0, 2, False], [0, 7, False], [0, 7, False]]
    black_rooks_inf = [[0, 7, False, False], [7, 7, False, False], [2, 0, False, False], [4, 6, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False], [0, 7, False, False]]
    black_queens_inf = [[3, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False], [0, 7, False]]
    black_king_inf = [[4, 7, False, False]]

    en_passant_x_y = [8, 8]

    fen_stage = 0
    x = 0
    y = 7

    half_move_chars = ""
    turn_num_chars = ""

    for char in fen:

        if char == " ":

            fen_stage += 1

        elif fen_stage == 0:

            if char == "/":

                x = -1
                y -= 1

            elif char.isnumeric():

                x += int(char) - 1

            elif char == "P":

                count = 0

                while count <= 7:

                    if white_pawns_inf[count][2] == False:

                        white_pawns_inf[count][0] = x
                        white_pawns_inf[count][1] = y
                        white_pawns_inf[count][2] = True

                        if y == 1:

                            white_pawns_inf[count][3] = True

                        break

                    else:

                        count += 1

            elif char == "B":

                count = 0

                while count <= 9:

                    if white_bishops_inf[count][2] == False:

                        white_bishops_inf[count][0] = x
                        white_bishops_inf[count][1] = y
                        white_bishops_inf[count][2] = True

                        break

                    else:

                        count += 1

            elif char == "N":

                count = 0

                while count <= 9:

                    if white_knights_inf[count][2] == False:

                        white_knights_inf[count][0] = x
                        white_knights_inf[count][1] = y
                        white_knights_inf[count][2] = True

                        break

                    else:

                        count += 1

            elif char == "R":

                count = 0

                while count <= 9:

                    if white_rooks_inf[count][2] == False:

                        white_rooks_inf[count][0] = x
                        white_rooks_inf[count][1] = y
                        white_rooks_inf[count][2] = True

                        break

                    else:

                        count += 1

            elif char == "Q":

                count = 0

                while count <= 8:

                    if white_queens_inf[count][2] == False:

                        white_queens_inf[count][0] = x
                        white_queens_inf[count][1] = y
                        white_queens_inf[count][2] = True

                        break

                    else:

                        count += 1

            elif char == "K":

                if white_king_inf[0][2] == False:

                    white_king_inf[0][0] = x
                    white_king_inf[0][1] = y
                    white_king_inf[0][2] = True

            elif char == "p":

                count = 0

                while count <= 7:

                    if black_pawns_inf[count][2] == False:

                        black_pawns_inf[count][0] = x
                        black_pawns_inf[count][1] = y
                        black_pawns_inf[count][2] = True

                        if y == 6:

                            black_pawns_inf[count][3] = True

                        break

                    else:

                        count += 1

            elif char == "b":

                count = 0

                while count <= 9:

                    if black_bishops_inf[count][2] == False:

                        black_bishops_inf[count][0] = x
                        black_bishops_inf[count][1] = y
                        black_bishops_inf[count][2] = True

                        break

                    else:

                        count += 1

            elif char == "n":

                count = 0

                while count <= 9:

                    if black_knights_inf[count][2] == False:

                        black_knights_inf[count][0] = x
                        black_knights_inf[count][1] = y
                        black_knights_inf[count][2] = True

                        break

                    else:

                        count += 1

            elif char == "r":

                count = 0

                while count <= 9:

                    if black_rooks_inf[count][2] == False:

                        black_rooks_inf[count][0] = x
                        black_rooks_inf[count][1] = y
                        black_rooks_inf[count][2] = True

                        break

                    else:

                        count += 1

            elif char == "q":

                count = 0

                while count <= 8:

                    if black_queens_inf[count][2] == False:

                        black_queens_inf[count][0] = x
                        black_queens_inf[count][1] = y
                        black_queens_inf[count][2] = True

                        break

                    else:

                        count += 1

            elif char == "k":

                if black_king_inf[0][2] == False:

                    black_king_inf[0][0] = x
                    black_king_inf[0][1] = y
                    black_king_inf[0][2] = True

            x += 1

        elif fen_stage == 1:

            if char == "w":

                white_turn = True

            elif char == "b":

                white_turn = False

        elif fen_stage == 2:

            if char == "K":

                white_king_inf[0][3] = True

                for i in range(0, 10):

                    if white_rooks_inf[i][2] == True and white_rooks_inf[i][0] == 7 and white_rooks_inf[i][1] == 0:

                        white_rooks_inf[i][3] = True

            elif char == "Q":

                white_king_inf[0][3] = True

                for i in range(0, 10):

                    if white_rooks_inf[i][2] == True and white_rooks_inf[i][0] == 0 and white_rooks_inf[i][1] == 0:

                        white_rooks_inf[i][3] = True

            elif char == "k":

                black_king_inf[0][3] = True

                for i in range(0, 10):

                    if black_rooks_inf[i][2] == True and black_rooks_inf[i][0] == 7 and black_rooks_inf[i][1] == 7:

                        black_rooks_inf[i][3] = True

            elif char == "q":

                black_king_inf[0][3] = True

                for i in range(0, 10):

                    if black_rooks_inf[i][2] == True and black_rooks_inf[i][0] == 0 and black_rooks_inf[i][1] == 7:

                        black_rooks_inf[i][3] = True

        elif fen_stage == 3:

            if char.isnumeric():

                if white_turn == True:

                    en_passant_x_y[1] = int(char) - 2

                else:

                    en_passant_x_y[1] = int(char)

            else:

                en_passant_x_y[0] = get_column_char(char)

        elif fen_stage == 4:

            if char.isnumeric():

                half_move_chars = half_move_chars + char

                half_moves = int(half_move_chars)

        elif fen_stage == 5:

            if char.isnumeric():

                turn_num_chars = turn_num_chars + char

                turn_num = int(turn_num_chars)

    return white_pawns_inf, white_bishops_inf, white_knights_inf, white_rooks_inf, white_queens_inf, white_king_inf, black_pawns_inf, black_bishops_inf, black_knights_inf, black_rooks_inf, black_queens_inf, black_king_inf, white_turn, en_passant_x_y, half_moves, turn_num

def save_notation_for_repetition(directory):

    draw_by_repetition = False

    fen = create_fen_position()
    
    fen = fen[:fen.find(" ")]
    
    repetition_draw_file_append = open(f"{directory}/repetition_draw_file.txt", "a")
    repetition_draw_file_append.write(fen + "\n")
    repetition_draw_file_append.close()

    repeat_num = 0

    repetition_draw_file_read = open(f"{directory}/repetition_draw_file.txt", "r")

    for line in repetition_draw_file_read:

        if line == fen + "\n":

            repeat_num += 1

    repetition_draw_file_read.close()

    if repeat_num >= 3:

        draw_by_repetition = True

    return draw_by_repetition
