class BasicWord:
    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def __repr__(self):
        return f"""BasicWord({self.word}, {len(self.sub_words)})"""

    def has_sub_word(self, word):
        """
        проверку введенного слова в списке допустимых подслов
         word: проверяемое слово
         :return найдино ли совподение
         """

        return word in self.sub_words

    def coutnt_sub_word(self):
        """
        подсчет количества подслов
        :return: общее количество подслов
        """
        return len(self.sub_words)

    def get_word(self):
        return self.word