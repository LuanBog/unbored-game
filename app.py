import time
import random
import games
from form import Form

games = [games.Hangman, games.Rps]

running = True

def play():
    games_title = [game.title for game in games]
    games_title.append('Random')

    game_menu = Form('Games', games_title)
    game_menu_input = game_menu.ask()

    game_chosen = None

    if game_menu_input['choice'] == 'Random':
        game_chosen = random.choice(games)()
    else:
        game_chosen = games[game_menu_input['index'] - 1]()

    print('')
    print('----------{}----------'.format(game_chosen.title))
    print('')
    game_chosen.run()
    print('')
    print('----------' + '-' * len(game_chosen.title) + '----------')
    print('')

    time.sleep(2)

    if game_chosen.won:
        print('Wow you won, GG\'s!\n')
    else:
        print('Awww, you did your best\n')

    time.sleep(2)

def quit():
    global running

    print('\nPeace out!')
    running = False

def main():
    global running

    print('\nAre you bored and ready to play?')
    time.sleep(2)
    print('\nI welcome you to Unbored Game!\nA game that makes you unbored')
    time.sleep(2)
    
    while running:
        menu = Form('Menu', ['Play', 'About', 'Quit'])
        menu_input = menu.ask()

        if menu_input['index'] == 1:
            play()
        elif menu_input['index'] == 2:
            print('\nThis is a game that makes you unbored.')
            print('Reason why this is made is because the developer was bored')
            print('because of no wifi.\n')
            
            time.sleep(4)
        elif menu_input['index'] == 3:
            quit()
        else:
            print('\nInvalid input! Please try again\n')
            time.sleep(0.5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('')
        quit()
