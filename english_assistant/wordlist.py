# -*- coding:utf-8 -*-
"""
@author: DawnK
@file: wordlist.py
@time: 2020/5/6 14:38
@desc:
"""
import json

from typing import List, Dict, Set
from wordclass import Word
from wordpool import WordPool


class WordList:
    """  单词清单类,用户可创建多个单词清单,多个清单底层共用底层单词库 """
    """
        1. 设置名字
        2. 添加单词
        3. 批量添加单词
        4. 删除单词

    """

    def __init__(self, name: str, file_path):
        self.name = name
        self.file_path = file_path
        self.word_list: Set[str] = set()
        self.load_list(file_path)
        self.choice_value = {'remember': 1, 'blurry': 0.6, 'forget': 0.2}

    def show(self):
        return list(self.word_list)

    def load_list(self, file_path: str):
        cur_dict = {}
        with open(file_path, "r", encoding='utf-8') as load_f:
            cur_dict = json.load(load_f)

        self.word_list.clear()
        for word in cur_dict:
            self.word_list.add(word)

    def write_list(self, file_path: str):
        cur_dict = {}
        for word in self.word_list:
            cur_dict[word] = ""

        with open(file_path, "w", encoding='utf-8') as dump_f:
            json.dump(cur_dict, dump_f)

    def set_list_name(self, name: str):
        self.name = name

    def add_word(self, english_meaning: str) -> bool:
        if english_meaning not in self.word_list:
            self.word_list.add(english_meaning)
            return True
        else:
            return False

    def add_many_words(self, words: List[str]):
        for word in words:
            self.add_word(word)

    def remove_word(self, english_meaning: str) -> bool:
        if english_meaning not in self.word_list:
            return False
        else:
            self.word_list.remove(english_meaning)
            return True

    def get_min_proficiency_word(self, word_pool: WordPool) -> Word:
        """
        :return: 返回熟练度最小的单词
        """
        if len(self.word_list) == 0:
            return None
        else:
            word_arr = list(self.word_list)
            min_proficiency = word_pool.get_word(word_arr[0]).proficiency
            min_word = word_arr[0]
            for word in word_arr:
                if min_proficiency > word_pool.get_word(word).proficiency:
                    min_proficiency = word_pool.get_word(word).proficiency
                    min_word = word
        return word_pool.get_word(min_word)

    def change_word_proficiency(self, english_meaning: str, choice: str, word_pool: WordPool):
        """
        修改单词熟练度
        :param english_meaning:
        :param choice:
        :param word_pool:
        :return:
        """
        assert choice in self.choice_value.keys()
        word_pool.change_word_proficiency(english_meaning, self.choice_value[choice])
