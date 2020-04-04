# -*- coding: utf-8 -*-
'''
程序思想：
有两个本地语音库，美音库Speech_US，英音库Speech_US
调用有道api，获取语音MP3，存入对应的语音库中

主要接口：
word_pronounce()  单词发音
multi_thread_download() 单词发音的批量多线程下载
'''
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import os
from playsound import playsound


class pronounciation():
    def __init__(self, type=0, word='hellow'):
        '''
        调用youdao API
        type = 0：美音
        type = 1：英音

        判断当前目录下是否存在两个语音库的目录
        如果不存在，创建
        '''
        word = word.lower()  # 小写
        self._type = type  # 发音方式
        self._word = word  # 单词

        # 文件根目录
        self._dirRoot = os.path.dirname(os.path.abspath(__file__))

        if 0 == self._type:
            self._dir_speech = os.path.join(self._dirRoot+'/..', 'Speech_US')  # 美音库
        else:
            self._dir_speech = os.path.join(self._dirRoot+'/..', 'Speech_EN')  # 英音库

        # 判断是否存在美音库
        print(os.path)
        if not os.path.exists('../Speech_US'):
            # 不存在，就创建
            os.makedirs('../Speech_US')
        # 判断是否存在英音库
        if not os.path.exists('../Speech_EN'):
            # 不存在，就创建
            os.makedirs('../Speech_EN')

    def word_input(self, word_and_type):
        '''
        测试使用  单词的输入  形如 [（word，type）,（word，type）,（word，type）]的list
        '''
        word = 'hello'
        print('input word \nEnds with a #')
        while word != '#':
            word = input('word: ')
            if word == '#':
                break
            type = input('type( US(0) or EN(1) or both(2) ): ')
            if type == '1':
                t = 1
            elif type == '0':
                t = 0
            else:
                t = 2
            word_and_type.append((word, t))

    def print_wordlist(self, word_and_type):
        for cur in word_and_type:
            print('word: ' + cur[0] + ' type: ' + str(cur[1]))

    def down(self, w_t):
        '''
        下载单词的MP3
        判断语音库中是否有对应的MP3
        如果没有就下载
        '''
        word = w_t[0].lower()
        type = w_t[1]
        dir_speech = self._get_dir_speech(type)
        tmp = self._get_mp3_file_path(word, type, dir_speech)[0]
        filePath = self._get_mp3_file_path(word, type, dir_speech)[1]
        fileName = self._get_mp3_file_path(word, type, dir_speech)[2]
        if tmp is False:
            cur_url = self._getURL(word, type)
            # 组合URL
            # 调用下载程序，下载到目标文件夹
            # print('不存在 %s.mp3 文件\n将URL:\n' % word, self._url, '\n下载到:\n', self._filePath)
            # 下载到目标地址
            print('%s.mp3 正在下载\n' % fileName)
            urllib.request.urlretrieve(cur_url, filename=filePath)
            print('%s.mp3 下载完成\n' % fileName)
        else:
            print('已经存在 %s.mp3, 不需要下载' % fileName)

        # 返回声音文件路径
        return filePath

    def _getURL(self, word, type):
        '''
        私有函数，生成发音的目标URL
        http://dict.youdao.com/dictvoice?type=0&audio=
        '''
        url = r'http://dict.youdao.com/dictvoice?type=' + str(
            type) + r'&audio=' + word
        return url

    def _get_mp3_file_path(self, word, type, dir_speech):
        '''
        获取单词的MP3本地文件路径
        如果有MP3文件，返回路径(绝对路径)
        如果没有，返回None
        '''
        word = word.lower()  # 小写
        # print('word: '+self._word+' type: '+str(self._type)+'\n')
        if type == 0:
            fileName = word + '_US.mp3'
        else:
            fileName = word + '_EN.mp3'
        filePath = os.path.join(dir_speech, fileName)

        # 判断是否存在这个MP3文件
        if os.path.exists(filePath):
            # 存在这个mp3
            return (True, filePath, fileName)
        else:
            # 不存在这个MP3，返回none
            return (False, filePath, fileName)

    def _get_dir_speech(self, type):  # 返回MP3文件的上一级绝对路径
        if 0 == type:
            dir_speech = os.path.join(self._dirRoot+'/..', 'Speech_US')  # 美音库
        else:
            dir_speech = os.path.join(self._dirRoot+'/..', 'Speech_EN')  # 英音库
        return dir_speech

    def word_pronounce(self, w_t=('hello', 0)):
        '''
        实现 单词发音
        如果单词发音已经下载，直接发音
        如果尚未下载，将进行下载，并发音

        输入参数为一个二元组
        第一个参数：单词
        第二个参数：单词发音类别（0：美音  1：英音  2：函数内重新判断 <对应美音，英音全都下载了的情况> ）
        '''
        self._word = w_t[0]
        self._type = w_t[1]
        if w_t[1] == 2:
            print('US(0) or EN(1): ')
            self._type = input()
        dir_speech = self._get_dir_speech(self._type)
        tmp = self._get_mp3_file_path(self._word, self._type, dir_speech)
        if tmp[0] is False:
            print("该单词尚未下载\n")
            print("即将下载\n")
            self.down(w_t)
            self.word_pronounce(w_t)
        else:
            playsound(tmp[1])

    def multi_thread_download(self, word_and_type, num=9):
        '''
        函数实现多线程批量单词发音下载功能
        输入参数包括两部分
        1.一个由二元组组成的list   二元粗参数 ：第一个参数：单词
                                             第二个参数：单词发音类别（0：美音  1：英音  2：美音，英音全都下载 ）
          形如 [（word，type）,（word，type）,（word，type）]的list
        2.线程池大小   默认为9 可以不输入
          最佳线程池大小 2N+1 （N为电脑cpu个数）
        '''
        # 多线程实现参考 https://www.jb51.net/article/170571.htm
        pool = ThreadPoolExecutor(num)  # 线程池的大小
        for cur_w_t in word_and_type:
            if cur_w_t[1] == 2:
                new1_w_t = (cur_w_t[0], 0)
                new2_w_t = (cur_w_t[0], 1)
                word_and_type.append(new1_w_t)
                word_and_type.append(new2_w_t)
                continue
            pool.submit(self.down, cur_w_t)

'''
if __name__ == "__main__":
    word_and_type = []
    ss = pronounciation()
    ss.word_input(word_and_type)  # 输入函数 供测试使用
    ss.multi_thread_download(word_and_type)
    ss.word_pronounce(('Lebron', 0))
'''