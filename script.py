# explain game
print('==============================================================================')
print('==============================================================================')
print(' ')
print('welcome to a very rudimentary connect 4 game in python')
print('the goal of the game is to get 4 tiles in a row')
print("player 1 is 'X' and player 2 is 'O'")
print("players can enter values of 1-7 to signify which column they would like to drop their tile, press 'ender' to drop")
print(' ')
print('the author also invites you to check out his website, calday.one, feel free to send feedback to cal@calday.one!')
print('enjoy!')
print(' ')
print('==============================================================================')
print('==============================================================================')


# define the template for the 'game' object (customized data class)
class C4Model:

    def __init__(game):
        game.p1 = 'player 1'
        game.p2 = 'player 2'
        game.rows = [
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','',''],
            ['','','','','','','']
        ]

    def print_rows():
        print('here are the rows lol')