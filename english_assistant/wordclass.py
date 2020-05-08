class Word:
    """ 单词类 记录英文,中文,熟练度  """

    def __init__(self, english_meaning: str, chinese_meaning: str, proficiency: float = 0.0):
        self.english_meaning: str = english_meaning
        self.chinese_meaning: str = chinese_meaning
        self.proficiency = proficiency

    def __lt__(self, other):
        return self.proficiency < other.proficiency

    def __repr__(self):
        return ' "' + self.english_meaning + '"  "' + self.chinese_meaning + '"  ' + str(self.proficiency)

    def show(self):
        return self.english_meaning, self.chinese_meaning


if __name__ == '__main__':
    pass
