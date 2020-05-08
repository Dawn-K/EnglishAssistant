from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from vocalbulary import Vacalbulary
import translate
from rssreader import rss_moduel
from pronounce import pronounciation
import json

v = Vacalbulary()
v.load_word_list('important_word')
r1 = rss_moduel()
ss = pronounciation()


class Ui_Form_search(object):  # 搜索单词界面
    def setupUi(self, Form):
        Form.setObjectName("查询单词")
        Form.resize(980, 667)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/0.png")))
        self.setPalette(palette)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(700, 150, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                      "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.word_edit = QtWidgets.QLineEdit(Form)  # 搜索单词文本框
        self.word_edit.setGeometry(QtCore.QRect(270, 150, 171, 41))
        self.word_edit.setObjectName("word_edit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(520, 150, 101, 41))
        self.comboBox.setStyleSheet("QComboBox{color:rgb(125,125,125)}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.display_word = QtWidgets.QTextEdit(Form)  # 显示单词的意思、词性文本框
        self.display_word.setGeometry(QtCore.QRect(270, 250, 541, 311))
        self.display_word.setObjectName("display_word")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 371, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 130, 121, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 230, 121, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 330, 121, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 430, 121, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 530, 121, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_3.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_4.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.pushButton_5.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.pushButton_6.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        # 单词发音
        self.us_pro = QtWidgets.QPushButton(Form)
        self.us_pro.setGeometry(QtCore.QRect(520, 200, 40, 40))
        self.us_pro.setObjectName("us_pro")
        self.uk_pro = QtWidgets.QPushButton(Form)
        self.uk_pro.setGeometry(QtCore.QRect(570, 200, 40, 40))
        self.uk_pro.setObjectName("uk_pro")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.search_click)
        self.pushButton_2.clicked.connect(self.inerface_search)
        self.pushButton_3.clicked.connect(self.interface_word)
        self.pushButton_4.clicked.connect(self.interface_RSS)
        self.pushButton_5.clicked.connect(self.interface_library)
        self.pushButton_6.clicked.connect(self.interface_center)
        self.us_pro.clicked.connect(self.us_click)
        self.uk_pro.clicked.connect(self.uk_click)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "搜索"))
        self.us_pro.setText(_translate("Form", "US"))
        self.uk_pro.setText(_translate("Form", "UK"))
        self.comboBox.setItemText(0, _translate("Form", "有道翻译"))
        self.comboBox.setItemText(1, _translate("Form", "百度翻译"))
        self.comboBox.setItemText(2, _translate("Form", "谷歌翻译"))
        self.label.setText(_translate("Form", "请输入单词"))
        self.label_2.setText(_translate("Form", "欢迎来到英语辅助学习系统"))
        self.pushButton_2.setText(_translate("Form", "在线搜索"))
        self.pushButton_3.setText(_translate("Form", "背单词"))
        self.pushButton_4.setText(_translate("Form", "RSS信息"))
        self.pushButton_5.setText(_translate("Form", "词库"))
        self.pushButton_6.setText(_translate("Form", "个人中心"))
        self.label_3.setText(_translate("Form", "翻译结果"))

    def us_click(self):
        word = self.word_edit.text()
        if word == '':
            return
        ss.word_pronounce((word, 0))

    def uk_click(self):
        word = self.word_edit.text()
        if word == '':
            return
        ss.word_pronounce((word, 1))

    def search_click(self):
        str = self.word_edit.text()
        self.display_word.setText(translate.Tran(str, self.comboBox.currentText()))

    def inerface_search(self):
        self.hide()
        self.s = search_ui()
        self.s.show()

    def interface_word(self):
        self.hide()
        self.s = word_ui()
        self.s.show()

    def interface_RSS(self):
        self.hide()
        self.s = RSS_ui()
        self.s.show()

    def interface_library(self):
        self.hide()
        self.s = library_ui()
        self.s.show()

    def interface_center(self):
        self.hide()
        self.s = center_ui()
        self.s.show()


class Ui_Form_word(object):  # 背单词界面
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(980, 667)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/0.png")))
        self.setPalette(palette)
        self.word_line = QtWidgets.QLineEdit(Form)  # 展示单词文本框
        self.word_line.setText(v.get_front_word().english_meaning)
        self.word_line.setGeometry(QtCore.QRect(270, 150, 541, 41))
        self.word_line.setObjectName("word_line")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.display_text = QtWidgets.QTextEdit(Form)  # 展示单词信息文本框
        self.display_text.setText('\n'.join(v.get_front_word().chinese_meaning.split('\t')))
        self.display_text.setGeometry(QtCore.QRect(270, 250, 541, 311))
        self.display_text.setObjectName("display_text")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 371, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 130, 121, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 230, 121, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 330, 121, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 430, 121, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 530, 121, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_3.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_4.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.pushButton_5.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.pushButton_6.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(840, 280, 101, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(840, 370, 101, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(840, 450, 101, 51))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_7.setStyleSheet("QPushButton{border-image: url(img/3-2.png)}"
                                        "QPushButton:hover{border-image: url(img/3-1.png)}")
        self.pushButton_8.setStyleSheet("QPushButton{border-image: url(img/3-2.png)}"
                                        "QPushButton:hover{border-image: url(img/3-1.png)}")
        self.pushButton_9.setStyleSheet("QPushButton{border-image: url(img/3-2.png)}"
                                        "QPushButton:hover{border-image: url(img/3-1.png)}")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.inerface_search)
        self.pushButton_3.clicked.connect(self.interface_word)
        self.pushButton_4.clicked.connect(self.interface_RSS)
        self.pushButton_5.clicked.connect(self.interface_library)
        self.pushButton_6.clicked.connect(self.interface_center)
        self.pushButton_7.clicked.connect(self.word_familar)
        self.pushButton_8.clicked.connect(self.word_vague)
        self.pushButton_9.clicked.connect(self.word_forget)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "单词"))
        self.label_2.setText(_translate("Form", "欢迎来到英语辅助学习系统"))
        self.pushButton_2.setText(_translate("Form", "在线搜索"))
        self.pushButton_3.setText(_translate("Form", "背单词"))
        self.pushButton_4.setText(_translate("Form", "RSS信息"))
        self.pushButton_5.setText(_translate("Form", "词库"))
        self.pushButton_6.setText(_translate("Form", "个人中心"))
        self.label_3.setText(_translate("Form", "单词信息"))
        self.pushButton_7.setText(_translate("Form", "熟悉"))
        self.pushButton_8.setText(_translate("Form", "模糊"))
        self.pushButton_9.setText(_translate("Form", "忘记"))

    def word_familar(self):  # 熟悉 动作触发
        v.change_proficiency(v.get_front_word().english_meaning, 'remember')
        self.word_line.setText(v.get_front_word().english_meaning)
        self.display_text.setText('\n'.join(v.get_front_word().chinese_meaning.split('\t')))

    def word_vague(self):  # 模糊动作触发
        v.change_proficiency(v.get_front_word().english_meaning, 'blurry')
        self.word_line.setText(v.get_front_word().english_meaning)
        self.display_text.setText('\n'.join(v.get_front_word().chinese_meaning.split('\t')))

    def word_forget(self):  # 忘记动作触发
        v.change_proficiency(v.get_front_word().english_meaning, 'forget')
        self.word_line.setText(v.get_front_word().english_meaning)
        self.display_text.setText('\n'.join(v.get_front_word().chinese_meaning.split('\t')))

    def inerface_search(self):
        self.hide()
        self.s = search_ui()
        self.s.show()

    def interface_word(self):
        self.hide()
        self.s = word_ui()
        self.s.show()

    def interface_RSS(self):
        self.hide()
        self.s = RSS_ui()
        self.s.show()

    def interface_library(self):
        self.hide()
        self.s = library_ui()
        self.s.show()

    def interface_center(self):
        self.hide()
        self.s = center_ui()
        self.s.show()


class Ui_Form_library(object):  # 词库界面
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(980, 667)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/0.png")))
        self.setPalette(palette)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(440, 120, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 371, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # 绘制左侧菜单栏
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 130, 121, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 230, 121, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 330, 121, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 430, 121, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 530, 121, 61))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 120, 101, 41))  # 添加单词
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 310, 101, 41))  # 添加清单
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(310, 120, 101, 41))  # 修改单词
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(450, 310, 101, 41))  # 删除单词
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(310, 310, 101, 41))  # 修改清单
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_2.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_3.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_4.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.pushButton_5.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_6.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.pushButton.setStyleSheet("QPushButton{border-image: url(img/4-2.png)}"
                                      "QPushButton:hover{border-image: url(img/4-1.png)}")
        self.pushButton_7.setStyleSheet("QPushButton{border-image: url(img/4-2.png)}"
                                        "QPushButton:hover{border-image: url(img/4-1.png)}")
        self.pushButton_8.setStyleSheet("QPushButton{border-image: url(img/4-2.png)}"
                                        "QPushButton:hover{border-image: url(img/4-1.png)}")
        self.pushButton_9.setStyleSheet("QPushButton{border-image: url(img/4-2.png)}"
                                        "QPushButton:hover{border-image: url(img/4-1.png)}")

        self.pushButton_10.setStyleSheet("QPushButton{border-image: url(img/4-2.png)}"
                                         "QPushButton:hover{border-image: url(img/4-1.png)}")

        self.pushButton_11.setStyleSheet("QPushButton{border-image: url(img/4-2.png)}"
                                         "QPushButton:hover{border-image: url(img/4-1.png)}")
        self.word_Browser = QtWidgets.QLineEdit(Form)  # 浏览单词的文本框
        self.word_Browser.setGeometry(QtCore.QRect(180, 170, 751, 121))
        self.word_Browser.setObjectName("word_Browser")
        self.list_1 = QtWidgets.QTextBrowser(Form)  # 清单一
        self.list_1.setGeometry(QtCore.QRect(240, 390, 691, 31))
        self.list_1.setObjectName("list_1")
        self.list_1.setText(' '.join(v.word_list.show()))  # 设置清单一初始值
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 390, 51, 31))
        self.label.setObjectName("label")
        self.list_2 = QtWidgets.QTextBrowser(Form)  # 清单二
        self.list_2.setGeometry(QtCore.QRect(240, 440, 691, 31))
        self.list_2.setObjectName("list_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 440, 51, 31))
        self.label_3.setObjectName("label_3")
        self.list_3 = QtWidgets.QTextBrowser(Form)
        self.list_3.setGeometry(QtCore.QRect(240, 490, 691, 31))
        self.list_3.setObjectName("list_3")  # 清单三
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(170, 490, 51, 31))
        self.label_4.setObjectName("label_4")
        self.list_4 = QtWidgets.QTextBrowser(Form)  # 清单四
        self.list_4.setGeometry(QtCore.QRect(240, 540, 691, 31))
        self.list_4.setObjectName("list_1")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(170, 540, 51, 31))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.delete_word)
        self.pushButton_2.clicked.connect(self.inerface_search)
        self.pushButton_3.clicked.connect(self.interface_word)
        self.pushButton_4.clicked.connect(self.interface_RSS)
        self.pushButton_5.clicked.connect(self.interface_library)
        self.pushButton_6.clicked.connect(self.interface_center)
        self.pushButton_7.clicked.connect(self.add_word)
        self.pushButton_9.clicked.connect(self.change_word)
        self.pushButton_8.clicked.connect(self.add_list)
        self.pushButton_11.clicked.connect(self.change_list)
        self.pushButton_10.clicked.connect(self.delete_list)
        self.idx = 0

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "删除单词"))
        self.label_2.setText(_translate("Form", "欢迎来到英语辅助学习系统"))
        self.pushButton_2.setText(_translate("Form", "在线搜索"))
        self.pushButton_3.setText(_translate("Form", "背单词"))
        self.pushButton_4.setText(_translate("Form", "RSS信息"))
        self.pushButton_5.setText(_translate("Form", "词库"))
        self.pushButton_6.setText(_translate("Form", "个人中心"))
        self.pushButton_7.setText(_translate("Form", "添加单词"))
        self.pushButton_8.setText(_translate("Form", "添加清单"))
        self.pushButton_9.setText(_translate("Form", "修改单词"))
        self.pushButton_10.setText(_translate("Form", "删除清单"))
        self.pushButton_11.setText(_translate("Form", "修改清单"))
        self.label.setText(_translate("Form", "清单一"))
        self.label_3.setText(_translate("Form", "清单二"))
        self.label_4.setText(_translate("Form", "清单三"))
        self.label_5.setText(_translate("Form", "清单四"))

    def inerface_search(self):
        self.hide()
        self.s = search_ui()
        self.s.show()

    def interface_word(self):
        self.hide()
        self.s = word_ui()
        self.s.show()

    def interface_RSS(self):
        self.hide()
        self.s = RSS_ui()
        self.s.show()

    def interface_library(self):
        self.hide()
        self.s = library_ui()
        self.s.show()

    def interface_center(self):
        self.hide()
        self.s = center_ui()
        self.s.show()

    def add_word(self):  # 添加单词
        name = self.word_Browser.text()
        if name == '' or name in v.word_list.word_list:
            self.word_Browser.setText('添加单词失败: ' + name + '为空或已存在')
        else:
            v.add_word(name)
            self.word_Browser.setText('添加单词成功: ' + name)

    def change_word(self):  # 改单词
        names = self.word_Browser.text()
        arr = names.split(' ')
        if len(arr) != 2:
            self.word_Browser.setText('请输入两个单词,以空格分隔,分别是原单词和新单词')
        else:
            v.remove_word(arr[0])
            v.add_word(arr[1])
            self.word_Browser.setText('修改成功')

    def delete_word(self):  # 删除单词
        name = self.word_Browser.text()
        if name == '' or name not in v.word_list.word_list:
            self.word_Browser.setText('删除单词失败: ' + name + '不存在')
        else:
            v.remove_word(name)
            self.word_Browser.setText('删除单词成功: ' + name)

    def add_list(self):  # 添加清单
        name = self.word_Browser.text()
        if name == '':
            name = 'list_' + str(self.idx)
            self.idx += 1
        v.creat_new_list(name)
        self.word_Browser.setText('已添加清单: ' + name)

    def change_list(self):  # 改清单
        name = self.word_Browser.text()
        if name == '' or name not in v.word_list_names:
            self.word_Browser.setText('切换清单失败: ' + name + '不存在')
        else:
            v.load_word_list(name)
            self.word_Browser.setText('切换清单成功: ' + name)

    def delete_list(self):  # 删除清单
        name = self.word_Browser.text()
        if name == '' or name not in v.word_list_names:
            self.word_Browser.setText('删除清单失败: ' + name + '不存在')
        else:
            # v.load_word_list(name)
            v.word_list_names.remove(name)
            self.word_Browser.setText('删除清单成功: ' + name)


class Ui_Form_RSS(object):  # 管理RSS界面
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(980, 667)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/0.png")))
        self.setPalette(palette)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 371, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 130, 121, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 230, 121, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 330, 121, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 430, 121, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 530, 121, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_3.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_4.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.pushButton_5.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_6.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(230, 110, 251, 31))
        self.comboBox.setStyleSheet("QComboBox{color:rgb(125,125,125)}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.rss_op_lineEdit = QtWidgets.QLineEdit(Form)
        self.rss_op_lineEdit.setGeometry(QtCore.QRect(690, 200, 200, 31))  # 输入框
        self.rss_op_lineEdit.setObjectName("lineEdit")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(380, 190, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 110, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(230, 250, 481, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText('\n'.join(r1.get_all_rss_link()))  # 设置RSS所有的源
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(790, 260, 101, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(790, 340, 101, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(790, 420, 101, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                      "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_7.setStyleSheet("QPushButton{border-image: url(img/3-2.png)}"
                                        "QPushButton:hover{border-image: url(img/3-1.png)}")

        self.pushButton_8.setStyleSheet("QPushButton{border-image: url(img/3-2.png)}"
                                        "QPushButton:hover{border-image: url(img/3-1.png)}")
        self.pushButton_9.setStyleSheet("QPushButton{border-image: url(img/3-2.png)}"
                                        "QPushButton:hover{border-image: url(img/3-1.png)}")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.inerface_search)
        self.pushButton_3.clicked.connect(self.interface_word)
        self.pushButton_4.clicked.connect(self.interface_RSS)
        self.pushButton_5.clicked.connect(self.interface_library)
        self.pushButton_6.clicked.connect(self.interface_center)
        self.pushButton_7.clicked.connect(self.add_subscribe)
        self.pushButton_8.clicked.connect(self.change_subscribe)
        self.pushButton_9.clicked.connect(self.delete_subscribe)
        self.pushButton.clicked.connect(self.rss_choice)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "欢迎来到英语辅助学习系统"))
        self.pushButton_2.setText(_translate("Form", "在线搜索"))
        self.pushButton_3.setText(_translate("Form", "背单词"))
        self.pushButton_4.setText(_translate("Form", "RSS信息"))
        self.pushButton_5.setText(_translate("Form", "词库"))
        self.pushButton_6.setText(_translate("Form", "个人中心"))
        self.comboBox.setItemText(0, _translate("Form", "管理RSS信息源"))
        self.comboBox.setItemText(1, _translate("Form", "阅读RSS信息源"))
        self.label.setText(_translate("Form", "管理RSS信息源"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_7.setText(_translate("Form", "添加订阅"))
        self.pushButton_8.setText(_translate("Form", "修改订阅"))
        self.pushButton_9.setText(_translate("Form", "删除订阅"))

    def inerface_search(self):
        self.hide()
        self.s = search_ui()
        self.s.show()

    def interface_word(self):
        self.hide()
        self.s = word_ui()
        self.s.show()

    def interface_RSS(self):
        self.hide()
        self.s = RSS_ui()
        self.s.show()

    def interface_library(self):
        self.hide()
        self.s = library_ui()
        self.s.show()

    def interface_center(self):
        self.hide()
        self.s = center_ui()
        self.s.show()

    def change_subscribe(self):  # 改变订阅
        feedurl_arr = self.rss_op_lineEdit.text().split(' ')
        if len(feedurl_arr) != 2:
            QMessageBox.information(self,
                                    "警告",
                                    "请在框中输入两个url,中间以空格分隔",
                                    QMessageBox.Yes | QMessageBox.No)
        else:
            if feedurl_arr[0] not in r1.rss_map.keys():
                QMessageBox.information(self,
                                        "警告",
                                        "第一个链接不存在",
                                        QMessageBox.Yes | QMessageBox.No)
            else:
                r1.alter_rss_source(feedurl_arr[0], feedurl_arr[1])
        self.textBrowser.setText('\n'.join(r1.get_all_rss_link()))

    def delete_subscribe(self):  # 删除订阅
        feedurl = self.rss_op_lineEdit.text()
        if feedurl not in r1.rss_map.keys():
            QMessageBox.information(self,
                                    "警告",
                                    "链接不存在",
                                    QMessageBox.Yes | QMessageBox.No)
            return
        r1.del_rss_source(feedurl)
        self.textBrowser.setText('\n'.join(r1.get_all_rss_link()))

    def add_subscribe(self):  # 添加订阅
        feedurl = self.rss_op_lineEdit.text()
        if feedurl == "":
            return
        r1.add_rss_source(feedurl)
        self.textBrowser.setText('\n'.join(r1.get_all_rss_link()))

    def rss_choice(self):
        # 做一个判断跳转页面
        if self.comboBox.currentText() == "管理RSS信息源":
            self.hide()
            self.s = RSS_ui()
            self.s.show()
        if self.comboBox.currentText() == "阅读RSS信息源":
            self.hide()
            self.s = RSS1_ui()
            self.s.show()


class Ui_Form_RSS1(object):  # 阅读RSS界面
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(976, 666)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/0.png")))
        self.setPalette(palette)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 230, 121, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(230, 110, 251, 31))
        self.comboBox.setStyleSheet("QComboBox{color:rgb(125,125,125)}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 530, 121, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.RSS_Browser = QtWidgets.QTextBrowser(Form)  # RSS展示
        self.RSS_Browser.setGeometry(QtCore.QRect(230, 250, 481, 291))
        self.RSS_Browser.setObjectName("RSS_Browser")
        self.RSS_Browser.setText(r1.get_rss_source())
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 130, 121, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(380, 190, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 430, 121, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 110, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 330, 121, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 371, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_3.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_4.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.pushButton_5.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_6.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                      "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.inerface_search)
        self.pushButton_3.clicked.connect(self.interface_word)
        self.pushButton_4.clicked.connect(self.interface_RSS)
        self.pushButton_5.clicked.connect(self.interface_library)
        self.pushButton_6.clicked.connect(self.interface_center)
        self.pushButton.clicked.connect(self.rss_choice)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "背单词"))
        self.comboBox.setItemText(0, _translate("Form", "管理RSS信息源"))
        self.comboBox.setItemText(1, _translate("Form", "阅读RSS信息源"))
        self.pushButton_6.setText(_translate("Form", "个人中心"))
        self.pushButton_2.setText(_translate("Form", "在线搜索"))
        self.label.setText(_translate("Form", "阅读RSS"))
        self.pushButton_5.setText(_translate("Form", "词库"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_4.setText(_translate("Form", "RSS信息"))
        self.label_2.setText(_translate("Form", "欢迎来到英语辅助学习系统"))

    def inerface_search(self):
        self.hide()
        self.s = search_ui()
        self.s.show()

    def interface_word(self):
        self.hide()
        self.s = word_ui()
        self.s.show()

    def interface_RSS(self):
        self.hide()
        self.s = RSS_ui()
        self.s.show()

    def interface_library(self):
        self.hide()
        self.s = library_ui()
        self.s.show()

    def interface_center(self):
        self.hide()
        self.s = center_ui()
        self.s.show()

    def rss_choice(self):
        # 做一个判断跳转页面
        if self.comboBox.currentText() == "管理RSS信息源":
            self.hide()
            self.s = RSS_ui()
            self.s.show()
        if self.comboBox.currentText() == "阅读RSS信息源":
            self.hide()
            self.s = RSS1_ui()
            self.s.show()


class Ui_Form_center(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(980, 667)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/0.png")))
        self.setPalette(palette)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 371, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 130, 121, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 230, 121, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 330, 121, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 430, 121, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 530, 121, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_3.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_4.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")

        self.pushButton_5.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.pushButton_6.setStyleSheet("QPushButton{border-image: url(img/2-2.png)}"
                                        "QPushButton:hover{border-image: url(img/2-1.png)}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(500, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(440, 140, 201, 41))  # 昵称
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 210, 201, 41))  # 姓名
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(330, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 280, 201, 41))  # 电话
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(330, 280, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 350, 201, 41))  # 邮箱
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(330, 350, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 430, 201, 41))  # 学校
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(330, 430, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(500, 510, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{border-image: url(img/4-2.png)}"
                                      "QPushButton:hover{border-image: url(img/4-1.png)}")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.inerface_search)
        self.pushButton_3.clicked.connect(self.interface_word)
        self.pushButton_4.clicked.connect(self.interface_RSS)
        self.pushButton_5.clicked.connect(self.interface_library)
        self.pushButton_6.clicked.connect(self.interface_center)
        self.pushButton.clicked.connect(self.conserve_info)

        # 读取信息文件,填充表单
        f = open('information', 'r', encoding='utf-8')
        info_dic = json.load(f)
        self.lineEdit.setText(info_dic['id'])
        self.lineEdit_2.setText(info_dic['name'])
        self.lineEdit_3.setText(info_dic['telephone'])
        self.lineEdit_4.setText(info_dic['email'])
        self.lineEdit_5.setText(info_dic['school'])

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "欢迎来到英语辅助学习系统"))
        self.pushButton_2.setText(_translate("Form", "在线搜索"))
        self.pushButton_3.setText(_translate("Form", "背单词"))
        self.pushButton_4.setText(_translate("Form", "RSS信息"))
        self.pushButton_5.setText(_translate("Form", "词库"))
        self.pushButton_6.setText(_translate("Form", "个人中心"))
        self.label.setText(_translate("Form", "个人信息"))
        self.label_3.setText(_translate("Form", "昵称"))
        self.label_4.setText(_translate("Form", "姓名"))
        self.label_5.setText(_translate("Form", "电话"))
        self.label_6.setText(_translate("Form", "邮箱"))
        self.label_7.setText(_translate("Form", "就读学校"))
        self.pushButton.setText(_translate("Form", "保存"))

    def inerface_search(self):
        self.hide()
        self.s = search_ui()
        self.s.show()

    def interface_word(self):
        self.hide()
        self.s = word_ui()
        self.s.show()

    def interface_RSS(self):
        self.hide()
        self.s = RSS_ui()
        self.s.show()

    def interface_library(self):
        self.hide()
        self.s = library_ui()
        self.s.show()

    def interface_center(self):
        self.hide()
        self.s = center_ui()
        self.s.show()

    def conserve_info(self):  # 保存信息
        f = open('information', 'w', encoding='utf-8')
        info_dic = {'id': self.lineEdit.text(), 'name': self.lineEdit_2.text(), 'telephone': self.lineEdit_3.text(),
                    'email': self.lineEdit_4.text(), 'school': self.lineEdit_5.text()}
        json.dump(info_dic, f)


class search_ui(QWidget, Ui_Form_search):
    def __init__(self, parent=None):
        super(search_ui, self).__init__(parent)
        wnd = self.setupUi(self)


class word_ui(QWidget, Ui_Form_word):
    def __init__(self, parent=None):
        super(word_ui, self).__init__(parent)
        wnd = self.setupUi(self)


class library_ui(QWidget, Ui_Form_library):
    def __init__(self, parent=None):
        super(library_ui, self).__init__(parent)
        wnd = self.setupUi(self)


class RSS_ui(QWidget, Ui_Form_RSS):
    def __init__(self, parent=None):
        super(RSS_ui, self).__init__(parent)
        wnd = self.setupUi(self)


class RSS1_ui(QWidget, Ui_Form_RSS1):
    def __init__(self, parent=None):
        super(RSS1_ui, self).__init__(parent)
        wnd = self.setupUi(self)


class center_ui(QWidget, Ui_Form_center):
    def __init__(self, parent=None):
        super(center_ui, self).__init__(parent)
        wnd = self.setupUi(self)
