import time
import os
from random import randint


def make_board():# 
    board_list = []
    for i in range(9):
        board_list.append([])
        for j in range(3):
            board_list[i].append('       ')

    for i in range(9):
        if i < 3:
            board_list[6+i][1] = f'   {i+1}   '
        elif 3<= i < 6:
            board_list[i][1] = f'   {i+1}   '
        else:
            board_list[i-6][1] = f'   {i+1}   '

    return board_list

def show_board(board):
    for i in range(0,9,3):
        print('-'*25)
        print('|'+board[i][0]+'|'+board[i+1][0]+'|'+board[i+2][0]+'|')
        print('|'+board[i][1]+'|'+board[i+1][1]+'|'+board[i+2][1]+'|')
        print('|'+board[i][2]+'|'+board[i+1][2]+'|'+board[i+2][2]+'|')
    print('-'*25)

def board_change(changed_n,ox,board):
    
    board_o = ['   @   ',' @   @ ','   @   ']
    board_x = [' *   * ','   *   ',' *   * ']
    
    if ox == 'O':
        board[changed_n] = board_o
    elif ox == 'X':
        board[changed_n] = board_x
    else:
        pass

    return board

def board_lndex(changed_n,ox,index_list):
    index_list[changed_n] = ox
    return index_list

def changed_num(num):

    if num in [1,2,3]:
        num = num + 5
    elif num in [4,5,6]:
        num = num - 1
    elif num in [7,8,9]:
        num = num - 7
    else:
        pass

    return num

def gameover():
    rq = input('RETRY(r) or QUIT(q)? : ')
    while rq not in ['r','q']:
        rq = input('Choose RETRY(r) or QUIT(q) : ')
    if rq == 'r':
        return  True
    else:
        return  False


'''
-----------------------------------Start---------------------------------------
-----------------------------------Start---------------------------------------
-----------------------------------Start---------------------------------------
'''
state = True

while state:
    os.system('cls||clear')
    board = make_board()
    show_board(board)
    bot = None
    turn = 0
    result = 'nobody'
    index_list = ['','','','','','','','','']
    print('GAME START!')
    player = input('X is first player\nO is second player\n Choose X or O : ')
    while player not in ['X','O']:
        player = input('Choose X or O : ')

    if player == 'O':
        bot = 'X'
    else:
        bot = 'O'

    if player == 'O':
        os.system('cls||clear')
        show_board(board)
        turn = 1
        print(f'turn : {turn}')
        print("bot's turn...")
        time.sleep(3)
        bot_num = randint(1,9)
        changed_n = changed_num(bot_num)
        board = board_change(changed_n,bot,board)
        index_list = board_lndex(changed_n,bot,index_list)
        os.system('cls||clear')
        show_board(board)
    else:
        pass

    while turn != 9:
        turn += 1
        os.system('cls||clear')
        show_board(board)
        print('Your turn!')
        player_choose = input("Choose position : ")
        while player_choose not in ['1','2','3','4','5','6','7','8','9']:
            player_choose = input(f'{player_choose} is not a number 1 to 9\nchoose position:')

        player_num = int(player_choose)
        changed_n = changed_num(player_num)
        while index_list[changed_n] in ['O','X']:
            player_num = input('There is already Check\nChoose position : ')
            while player_num not in ['1','2','3','4','5','6','7','8','9']:
                player_num = input(f'{player_num} is not a number 1 to 9\nchoose position:')

            changed_n = changed_num(int(player_num))
        
        board = board_change(changed_n,player,board)
        index_list = board_lndex(changed_n,player,index_list)
        os.system('cls||clear')
        show_board(board)

        if (index_list[0] == index_list[1] == index_list[2] in ['O','X']) or (index_list[3] == index_list[4] == index_list[5] in ['O','X']) or (index_list[6] == index_list[7] == index_list[8] in ['O','X']) or (index_list[0] == index_list[3] == index_list[6] in ['O','X']) or (index_list[1] == index_list[4] == index_list[7] in ['O','X']) or (index_list[2] == index_list[5] == index_list[8] in ['O','X']) or (index_list[0] == index_list[4] == index_list[8] in ['O','X']) or (index_list[2] == index_list[4] == index_list[6] in ['O','X']):
            result = player
            break

        
        if turn == 9:
            result = 'DRAW'
            break

        turn += 1
        print("bot's turn...")
        time.sleep(3)
        bot_num = randint(1,9)
        changed_n = changed_num(bot_num)
        while index_list[changed_n] in ['O','X']:
            bot_num = randint(1,9)
            changed_n = changed_num(bot_num)
        
        board = board_change(changed_n,bot,board)
        index_list = board_lndex(changed_n,bot,index_list)
        os.system('cls||clear')
        show_board(board)

        if (index_list[0] == index_list[1] == index_list[2] in ['O','X']) or (index_list[3] == index_list[4] == index_list[5] in ['O','X']) or (index_list[6] == index_list[7] == index_list[8] in ['O','X']) or (index_list[0] == index_list[3] == index_list[6] in ['O','X']) or (index_list[1] == index_list[4] == index_list[7] in ['O','X']) or (index_list[2] == index_list[5] == index_list[8] in ['O','X']) or (index_list[0] == index_list[4] == index_list[8] in ['O','X']) or (index_list[2] == index_list[4] == index_list[6] in ['O','X']):
            result = bot
            break

        if turn == 9:
            result = 'DRAW'
            break

    

    if result == 'DRAW':
        print('DRAW!')
        state = gameover()
    else:
        print(f'WINNER IS {result}')
        state = gameover()
