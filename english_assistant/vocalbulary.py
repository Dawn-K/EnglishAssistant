# -*- coding:utf-8 -*-
import json
import os
from wordclass import Word
from wordlist import WordList
from wordpool import WordPool
from typing import List


# 总词库,里面包含若干清单
class Vacalbulary:
    def __init__(self):
        # 应该每次从文件中读取单词清单,而不是一股脑存在内存里,只同时存一个

        # 测试
        self.word_list_names: List[str] = []
        self.load_word_list_name()
        self.word_list: WordList = None
        self.word_pool: WordPool = WordPool('all_word.json')

    def load_word_list_name(self):
        """
        载入已经存在的清单的名字
        :return:
        """
        self.word_list_names.clear()
        for maindir, subdir, all_file in os.walk('../wordlist'):
            for filename in all_file:
                apath = os.path.join(maindir, filename)

                # *.wl 表示清单文件
                if apath.endswith('.wl'):
                    self.word_list_names.append(apath)

    def creat_new_list(self, word_list_name: str) -> bool:
        """
        新建清单并创建配套的文件
        :param word_list_name:
        :return: 是否创建成功
        """
        if word_list_name in self.word_list_names:
            return False
        self.word_list_names.append(word_list_name)
        f = open('../wordlist/' + word_list_name + '.wl', "w", encoding="utf-8")
        f.write('{}')
        f.close()
        return True

    def load_word_list(self, word_list_name: str):
        """
        保存当前清单,切换到新的清单
        :param word_list_name:
        :return:
        """
        if self.word_list is not None:
            self.word_list.write_list('../wordlist/' + self.word_list.name + '.wl')
        self.word_list = WordList(word_list_name, '../wordlist/' + word_list_name + '.wl')

    def save_current_list(self):
        """
        保存当前的清单
        """
        self.word_list.write_list('../wordlist/' + self.word_list.name + '.wl')

    def save_dict(self):
        """
        保存当前词库
        """
        self.word_pool.write2file('all_word.json')

    def get_front_word(self) -> Word:
        """
        获取最小熟练度的单词
        :return:
        """
        return self.word_list.get_min_proficiency_word(self.word_pool)

    def change_proficiency(self, english_meaning: str, _choice: str):
        """
        修改单词熟练度
        :param english_meaning:
        :param _choice:
        :return:
        """
        self.word_list.change_word_proficiency(english_meaning, _choice, self.word_pool)

    def add_word(self, english_meaning: str):
        assert self.word_list is not None
        if not self.word_pool.has(english_meaning):
            return
        self.word_list.add_word(english_meaning)

    def remove_word(self, english_meaning: str):
        assert self.word_list is not None
        if not self.word_pool.has(english_meaning):
            return
        self.word_list.remove_word(english_meaning)


"""
v = Vacalbulary()
v.creat_new_list('GG')
v.load_word_list('important_word')
word_name = v.get_front_word()
v.change_proficiency(word_name, 'remember')
v.change_proficiency(word_name, 'blurry')
v.change_proficiency(word_name, 'forget')
v.save_current_list()
v.save_dict()
"""

if __name__ == "__main__":
    # 以下是测试代码
    v = Vacalbulary()
    v.creat_new_list('GG')
    v.load_word_list('important_word')
    flag = True
    v.word_list.add_many_words(['your', 'but', 'latter'])
    while flag:
        print(v.get_front_word())
        v.word_pool.show()
        choice = input()
        word_name = v.get_front_word().english_meaning
        if choice == '1':
            v.change_proficiency(word_name, 'remember')
        elif choice == '2':
            v.change_proficiency(word_name, 'blurry')
        elif choice == '3':
            v.change_proficiency(word_name, 'forget')
        else:
            flag = False
    v.save_current_list()
    v.save_dict()
