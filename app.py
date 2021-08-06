import time
from form import Form

running = True

def main():
    global running

    print('\nAre you bored and ready to play?')
    time.sleep(2)
    print('\nI welcome you to Unbored Game!\nA game that makes you unbored')
    time.sleep(2)
    
    while running:
        menu = Form('Menu', ['Play', 'About', 'Quit'])
        user_input = menu.ask()

        if user_input == 1:
            pass
        elif user_input == 2:
            print('\nThis is a game that makes you unbored.')
            print('Reason why this is made is because the developer was bored')
            print('because of no wifi.\n')
            
            time.sleep(4)
        elif user_input == 3:
            print('\nPeace out!')
            running = False
        else:
            print('\nInvalid input! Please try again\n')
            time.sleep(0.5)

if __name__ == '__main__':
    main()
