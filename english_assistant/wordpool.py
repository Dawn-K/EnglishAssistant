# -*- coding:utf-8 -*-
"""
@author: DawnK
@file: wordpool.py
@time: 2020/5/6 14:35
@desc:
"""
import json
from wordclass import Word
from typing import List, Dict, Set


class WordPool:
    """ 单词库,清单每次从单词库中寻找单词 """

    def __init__(self, file_path: str = None):
        self.words: Dict[str, Word] = {}

        # 文件导入
        # raw_dict = {}
        if file_path is None:
            return
        with open(file_path, "r", encoding='utf-8') as load_f:
            raw_dict = json.load(load_f)
        for english_meaning in raw_dict:
            cur_tuple = raw_dict[english_meaning]
            self.words[english_meaning] = Word(english_meaning, cur_tuple[0], cur_tuple[1])

    def get_word(self, english_meaning: str) -> Word:
        return self.words[english_meaning]

    def has(self, english_meaning: str) -> bool:
        return english_meaning in self.words.keys()

    def add_word(self, english_meaning: str, chinese_meaning: str, proficiency: float = 0.0) -> bool:
        if english_meaning not in self.words.keys():
            self.words[english_meaning] = Word(english_meaning, chinese_meaning, proficiency)
            return True
        else:
            return False

    def remove_word(self, english_meaning: str) -> bool:

        if self.words[english_meaning] is not None:
            self.words.pop(english_meaning)
            return True
        else:
            return False

    # def fix_word(self, english_meaning: str) -> bool:
    #     pass

    def read_from_file(self, file_name: str) -> bool:
        try:
            input_file = open(file_name, 'r', encoding='utf-8')
            for line in input_file.readline():
                json.loads(line)
                # self.add_word()
                pass
            input_file.close()
            return True
        except IOError:
            print("File is not accessible.")
            return False

    def write2file(self, file_name: str):
        cur_dict = {}
        for english_meaning in self.words:
            cur_dict[english_meaning] = tuple([self.words[english_meaning].chinese_meaning,
                                               self.words[english_meaning].proficiency])
        with open(file_name, "w", encoding='utf-8') as dump_f:
            json.dump(cur_dict, dump_f)

    def change_word_proficiency(self, english_meaning: str, change_value: float):
        self.words[english_meaning].proficiency += change_value

    def show(self):
        print(self.words)
