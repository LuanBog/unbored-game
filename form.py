class Form:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions

    def ask(self):
        print('----------{}----------'.format(self.title))
        for index, question in enumerate(self.questions):
            print('{}) {}'.format(index + 1, question))
        print('----------' + '-' * len(self.title) + '----------')
        
        user_input = int(input('> '))
        
        if user_input < 0 or user_input > len(self.questions):
            return None

        return user_input
