import time
import random
import pickle
import game_loader
from form import Form

games = game_loader.load()

score = {
    'wins': 0,
    'loses': 0
}

running = True

def play():
    global score

    games_title = [game.title for game in games]
    games_title.append('Random')
    games_title.append('Back')

    print('')
    print('Wins: {}, Loses: {}'.format(score['wins'], score['loses']))

    game_menu = Form('Games', games_title)
    game_menu_input = game_menu.ask()

    game_chosen = None

    if game_menu_input['choice'] == 'Random':
        game_chosen = random.choice(games)()
    elif game_menu_input['choice'] == 'Back':
        return
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
        score['wins'] += 1
    else:
        print('You lost, but you did your best\n')
        score['loses'] += 1

    time.sleep(2)

def quit():
    global running

    print('\nPeace out!')
    save_save()
    running = False

def save_save():
    with open('save.db', 'wb') as save:
        pickle.dump(score, save)

def load_save():
    try:
        with open('save.db', 'rb') as save:
            return pickle.load(save)
    except FileNotFoundError:
        print('\nSave file isn\'t found! Creating...\n')
        save_save()

        with open('save.db', 'rb') as save:
            return pickle.load(save)

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
    save = load_save()
    
    if save:
        score = save

    try:
        main()
    except KeyboardInterrupt:
        print('')
        quit()
