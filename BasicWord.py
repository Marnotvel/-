class BasicWord:
    def __init__(self, word, acceptable_words):
        self.word = word
        self.acceptable_words = acceptable_words

    def examination(self, answer):
        '''проверка введенного слова в списке допустимых подслов'''
        return answer in self.acceptable_words

    def subword_counting(self):
        '''подсчет количества подслов'''
        return len(self.acceptable_words)

    def __repr__(self):
        return self.word
