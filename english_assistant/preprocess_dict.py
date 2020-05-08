# -*- coding:utf-8 -*-
"""
@author: DawnK
@file: preprocess_dict.py
@time: 2020/5/7 10:31
@desc:
"""
import re, json

if __name__ == '__main__':
    word_dict = {}
    with open('word.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            arr = list(filter(None, line.rstrip('\n').split('\t')))
            if len(arr) < 6:
                continue
            if int(arr[1]) > 10:
                continue
            english_meaning = arr[3]
            chinese_meanings = ''
            for elem in arr[5].split(' '):
                chinese_meanings += re.sub(r'\d+?.', '\t', elem)
            chinese_meanings_arr = list(filter(None, chinese_meanings.split('\t')))
            chinese_meanings = '\t'.join(chinese_meanings_arr)
            # word_dict[english_meaning] = tuple([chinese_meanings, 0.0])
            word_dict[english_meaning] = ""

    with open('../wordlist/important_word.wl', "w") as dump_f:
        json.dump(word_dict, dump_f)
    print(len(word_dict))
