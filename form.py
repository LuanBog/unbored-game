class Form:
    invalid = {
        'index': 0,
        'choice': 'invalid'
    }

    def __init__(self, title, choices):
        self.title = title
        self.choices = choices

    def ask(self):
        choices_with_index = []

        print('----------{}----------'.format(self.title))
        for index, choice in enumerate(self.choices):
            choices_with_index.append({
                'index': index + 1,
                'choice': choice,
            })

            print('{}) {}'.format(index + 1, choice))
        print('----------' + '-' * len(self.title) + '----------')
        
        try:
            user_input = int(input('> '))
            
            if user_input < 0 or user_input > len(self.choices):
                return Form.invalid
                
            for choice in choices_with_index:
                if choice['index'] == user_input:
                    return choice
            
            return Form.invalid
        except ValueError: # Player puts in a letter
            return Form.invalid
