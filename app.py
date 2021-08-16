import time
import random
import pickle
import game_loader
from form import Form
from player import Player

games = game_loader.load()
running = True

guest = Player('Guest')
current_player = guest
players = [] # Guest will automatically added here with load_save()

def play():
    global guest, current_player

    games_title = [game.title for game in games]
    games_title.append('Random')
    games_title.append('Back')

    print('')
    print('Wins: {}, Loses: {}'.format(current_player.score['wins'], current_player.score['loses']))

    game_menu = Form('Games', games_title)
    game_menu_input = game_menu.ask()

    game_chosen = None

    if game_menu_input['choice'] == 'Random':
        game_chosen = random.choice(games)
    elif game_menu_input['choice'] == 'Back':
        return
    else:
        game_chosen = games[game_menu_input['index'] - 1]

    game = None

    if game_chosen.title == 'Tic-Tac-Toe':
        game = game_chosen(current_player, players)
    else:
        game = game_chosen(current_player)

    print('')
    print('----------{}----------'.format(game.title))
    print('')
    game.run()
    print('')
    print('----------' + '-' * len(game.title) + '----------')
    print('')

    time.sleep(2)

    if game.won:
        print('Wow you won, GG\'s!\n')
    else:
        print('You lost, but you did your best\n')

    time.sleep(2)

def create_player():
    global current_player, players

    def repeated(name):
        for player in players:
            if player.name == name:
                return True
        
        return False

    print('')
    print('----------Player Creation----------')

    while True:
        name = input('Name: ')

        # Checks so name doesn't get repeated
        if repeated(name):
            print('That name unfortunately exists already. Please choose another!')
            continue

        print('Creating...')

        new_player = Player(name)

        current_player = new_player
        players.append(new_player)

        save_save(log=False)

        print('-----------------------------------')
        
        break

def switch_player():
    global current_player

    choices = []

    for player in players:
        choices.append(player.name)

    choices.append('Back')

    switch_player_menu = Form('Switch Player', choices)
    switch_player_menu_input = switch_player_menu.ask()

    if switch_player_menu_input['choice'] == 'Back':
        print('')
        return

    player_chosen = None

    for player in players:
        if player.name == switch_player_menu_input['choice']:
            player_chosen = player
            break

    current_player = player_chosen
    print('Switched to {}\n'.format(current_player.name))

    time.sleep(0.5)

def delete_player():
    global players, current_player

    choices = []

    for player in players:
        if player.name == 'Guest':
            continue

        choices.append(player.name)

    choices.append('Back')

    delete_player_menu = Form('Delete Player', choices)
    delete_player_menu_input = delete_player_menu.ask()

    if delete_player_menu_input['choice'] == 'Back':
        print('')
        return

    for player in players:
        if player.name == delete_player_menu_input['choice']:
            are_you_sure = input('Are you sure you want to delete "{}". All progress will be lost! (y/n): '.format(player.name)).lower()

            if are_you_sure == 'y' or are_you_sure == 'yes':
                print('Deleting player...\n')
                players.remove(player)

                current_player = guest

                break

    save_save(log=False)

    time.sleep(0.5)

def quit():
    global running

    print('')
    save_save()
    print('Peace out!')

    running = False

def save_save(log = True):
    global players

    if log:
        print('Saving...')

    with open('save.db', 'wb') as f:
        # Removes guest from players, so it doesn't get saved
        for player in players:
            if player.name == 'Guest':
                players.remove(player)

        pickle.dump(players, f)

def load_save():
    global players

    save = None

    try:
        with open('save.db', 'rb') as f:
            save = pickle.load(f)
    except FileNotFoundError:
        print('\nSave file isn\'t found! Creating...\n')
        save_save(log=False)

        with open('save.db', 'rb') as save:
            save = pickle.load(save)

    players = save
    players.insert(0, guest) # Guest should always be at the beginning of the list

def main():
    global running

    print('\nAre you bored and ready to play?')
    time.sleep(2)
    print('\nI welcome you to Unbored Game!\nA game that makes you unbored\n')
    time.sleep(2)
    
    while running:
        print('Player: {}'.format(current_player.name))

        menu = Form('Menu', ['Play', 'Create Player', 'Switch Player', 'Delete Player', 'About', 'Quit'])
        menu_input = menu.ask()
        index = menu_input['index']

        if index == 1:
            play()
        elif index == 2:
            create_player()
        elif index == 3:
            switch_player()
        elif index == 4:
            delete_player()
        elif index == 5:
            print('\nThis is a game that makes you unbored.')
            print('Reason why this is made is because the developer was bored')
            print('because of no wifi.\n')
            
            time.sleep(4)
        elif index == 6:
            quit()
        else:
            print('\nInvalid input! Please try again\n')
            time.sleep(0.5)

if __name__ == '__main__':
    load_save()

    try:
        main()
    except KeyboardInterrupt:
        print('')
        quit()
