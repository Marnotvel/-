class Player:
    def __init__(self, name):
        self.name = name
        self.words_used = []

    def word_count(self):
        '''получение количества слов'''
        return len(self.words_used)

    def adding_word(self, answer):
        '''добавление слова в словарь'''
        self.words_used.append(answer)

    def usage_check(self, answer):
        '''проверка использования слова до этого'''
        return answer in self.words_used

    def __repr__(self):
        return self.name
