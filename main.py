from gamealgorithms import *
import time


#define board of 2 dimensions with 6 rows and 7 colums to create connect 4 game
board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]


def Game_manual(board, AIdepth, Computerdepth, type):
    if type == "simple":
        print("Using Simple Algorithm ")
    else:
        print("Using Alpha-Beta Algorithm ")
    score1 = 0
    score2 = 0
    while True:
        moves = Move_Options(board)
        if (is_terminal_game(board)):
            score1 = 0
            score2 = 0
            break
        # first AI Agent play using a minmax algorithm
        make_move(board, AIdepth, AI_Agent, type)
        print_board(board)
        score1 = winning_move(board, AI_Agent)
        # after every move agent do it in board we check if it win or not
        if score1:
            break
        # second player is computer, it play randomly not using any algorithm
        # check if the board is full and no one is win so we get out of loop and the result is draw

        make_move(board, Computerdepth, Computer, type)
        print_board(board)
        score2 = winning_move(board, Computer)
        # after every move computer do it in board we check if it win or not
        if score2:
            break
    # check which one is win in game or game ended draw
    if (winning_move(board, AI_Agent)):
        print("score1= ", Get_score(board, AI_Agent))
        print("AI AGENT WON")
    elif (winning_move(board, Computer)):
        print("score2= ", Get_score(board, Computer))
        print("COMPUTER WON")
    else:
        print("DRAW")


def Game_manual2(board, depth, type):
    if type == "simple":
        print("Using Simple Algorithm ")
    else:
        print("Using Alpha-Beta Algorithm ")
    score1 = 0
    score2 = 0
    while True:
        # first AI Agent play using a minmax algorithm
        make_move(board, depth, AI_Agent, type)
        print_board(board)
        score1 = Get_score(board, AI_Agent)
        # after every move agent do it in board we check if it win or not
        if score1 == 100:
            break
        # second player is computer, it play randomly not using any algorithm
        moves = Move_Options(board)
        # check if the board is full and no one is win so we get out of loop and the result is draw
        if (len(moves) == 0):
            break
        index = int(input("enter the place: "))
        # print("Computer select randomly: ",moves[index])
        board[moves[index][0]][moves[index][1]] = Computer
        print_board(board)
        score2 = Get_score(board, Computer)
        # after every move computer do it in board we check if it win or not
        if score2 == 100:
            break
    # check which one is win in game or game ended draw
    if (score1 > 0 and score2 == 0):
        print("score1= ", score1)
        print("AI Agent win")
    elif (score2 > 0 and score1 == 0):
        print("score2= ", score2)
        print("Human win")
    else:
        print(score1, "   ", score2)
        print("DRAW")


def Game_manual_time(board, depth1,depth2, type1, type2):
    score1 = 0
    score2 = 0
    while True:
        moves = Move_Options(board)
        if (is_terminal_game(board)):
            score1 = 0
            score2 = 0
            break
        # first AI Agent play using a minmax algorithm
        start_time = time.time()

        make_move(board, depth1, AI_Agent, "simple")
        end_time = time.time()
        execution_time = (end_time - start_time)*100

        print(f"Execution time of minmax: {execution_time} milli-seconds")
        # print_board(board)
        score1 = winning_move(board, AI_Agent)
        # after every move agent do it in board we check if it win or not
        if score1:
            break
        # second player is computer, it play randomly not using any algorithm
        # check if the board is full and no one is win so we get out of loop and the result is draw

        start_time = time.time()

        make_move(board, depth1, AI_Agent, "simple")
        end_time = time.time()
        execution_time = (end_time - start_time) * 100

        print(f"Execution time of alphabeta: {execution_time} milli-seconds")
        # print_board(board)
        score2 = winning_move(board, Computer)
        # after every move computer do it in board we check if it win or not
        if score2:
            break
    # check which one is win in game or game ended draw
    if (winning_move(board, AI_Agent)):
        print("score1= ", Get_score(board, AI_Agent))
        print("AI AGENT WON")
    elif (winning_move(board, Computer)):
        print("score2= ", Get_score(board, Computer))
        print("COMPUTER WON")
    else:
        print("DRAW")


type= input("Enter Which Algorithm You Want To Use? ")
diffficulty = input("CHOOSE DIFFICULTY LEVEL:\na)Easy b)Medium c)Hard d)Human vs AI e)Test time")

if(diffficulty=='a'):
    Game_manual(board, 5,2, type)
elif (diffficulty=='b'):
    Game_manual(board, 5, 3, type)
elif (diffficulty=='c'):
    Game_manual(board, 5, 4, type)
elif (diffficulty=='d'):
    Game_manual2(board,5,type)
elif (diffficulty=='e'):
    Game_manual_time(board,1,1,"MinMax","AlphaBeta")

print_board(board)
#print(Move_Options(board))


