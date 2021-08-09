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

# This function is used to update the score when the current_player's score is updated. Because it doesn't naturally update when you update current_player's score
# def update_players_score():
#     global players

#     for player in players:
#         if player.name == current_player.name:
#             player.score = current_player.score

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
        game_chosen = random.choice(games)(current_player)
    elif game_menu_input['choice'] == 'Back':
        return
    else:
        game_chosen = games[game_menu_input['index'] - 1](current_player)

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
        print('You lost, but you did your best\n')

    # update_players_score()

    time.sleep(2)

def quit():
    global running

    print('')
    save_save()
    print('Peace out!')
    running = False

def save_save():
    global players

    print('Saving...')

    with open('save.db', 'wb') as save:
        # Removes guest from players, so it doesn't get saved
        for player in players:
            if player.name == 'Guest':
                players.remove(player)

        pickle.dump(players, save)

def load_save():
    global players

    save = None

    try:
        with open('save.db', 'rb') as save:
            save = pickle.load(save)
    except FileNotFoundError:
        print('\nSave file isn\'t found! Creating...\n')
        save_save()

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
    load_save()

    try:
        main()
    except KeyboardInterrupt:
        print('')
        quit()
