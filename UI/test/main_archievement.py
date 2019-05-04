# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_archievement.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# 研究成果界面(真正使用的界面)
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1126, 776)
        self.frameArchievement = QtWidgets.QFrame(Form)
        self.frameArchievement.setGeometry(QtCore.QRect(0, 0, 1121, 771))
        self.frameArchievement.setStyleSheet("")
        self.frameArchievement.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameArchievement.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameArchievement.setObjectName("frameArchievement")
        self.tabAchievements = QtWidgets.QTabWidget(self.frameArchievement)
        self.tabAchievements.setGeometry(QtCore.QRect(20, 10, 1081, 721))
        self.tabAchievements.setStyleSheet("QTabWidget {\n"
"    background: #FFF;\n"
"}")
        self.tabAchievements.setObjectName("tabAchievements")
        self.tabPreProcessed = QtWidgets.QWidget()
        self.tabPreProcessed.setObjectName("tabPreProcessed")
        self.tabBrand = QtWidgets.QTabWidget(self.tabPreProcessed)
        self.tabBrand.setGeometry(QtCore.QRect(20, 20, 1041, 661))
        self.tabBrand.setStyleSheet("QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}")
        self.tabBrand.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabBrand.setObjectName("tabBrand")
        self.tabLenovo = QtWidgets.QWidget()
        self.tabLenovo.setObjectName("tabLenovo")
        self.frameLenovo = QtWidgets.QFrame(self.tabLenovo)
        self.frameLenovo.setGeometry(QtCore.QRect(10, 10, 1011, 601))
        self.frameLenovo.setStyleSheet("QFrame {\n"
"    background: #FFFFFF;\n"
"}")
        self.frameLenovo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLenovo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLenovo.setObjectName("frameLenovo")
        self.buttonBad = QtWidgets.QPushButton(self.frameLenovo)
        self.buttonBad.setGeometry(QtCore.QRect(40, 280, 61, 151))
        self.buttonBad.setObjectName("buttonBad")
        self.stackedWidgetContent = QtWidgets.QStackedWidget(self.frameLenovo)
        self.stackedWidgetContent.setGeometry(QtCore.QRect(150, 20, 811, 561))
        self.stackedWidgetContent.setStyleSheet("")
        self.stackedWidgetContent.setObjectName("stackedWidgetContent")
        self.pagePraise = QtWidgets.QWidget()
        self.pagePraise.setObjectName("pagePraise")
        self.toolBoxPraise = QtWidgets.QToolBox(self.pagePraise)
        self.toolBoxPraise.setGeometry(QtCore.QRect(10, 30, 771, 511))
        self.toolBoxPraise.setObjectName("toolBoxPraise")
        self.pageItemComments = QtWidgets.QWidget()
        self.pageItemComments.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.pageItemComments.setObjectName("pageItemComments")
        self.tableViewComments = QtWidgets.QTableView(self.pageItemComments)
        self.tableViewComments.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewComments.setObjectName("tableViewComments")
        self.toolBoxPraise.addItem(self.pageItemComments, "")
        self.pageItemGetRid = QtWidgets.QWidget()
        self.pageItemGetRid.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.pageItemGetRid.setObjectName("pageItemGetRid")
        self.tableViewGetRid = QtWidgets.QTableView(self.pageItemGetRid)
        self.tableViewGetRid.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewGetRid.setObjectName("tableViewGetRid")
        self.toolBoxPraise.addItem(self.pageItemGetRid, "")
        self.pageItemTagWords = QtWidgets.QWidget()
        self.pageItemTagWords.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.pageItemTagWords.setObjectName("pageItemTagWords")
        self.tableViewTagWords = QtWidgets.QTableView(self.pageItemTagWords)
        self.tableViewTagWords.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewTagWords.setObjectName("tableViewTagWords")
        self.toolBoxPraise.addItem(self.pageItemTagWords, "")
        self.pageItemAttrScore = QtWidgets.QWidget()
        self.pageItemAttrScore.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.pageItemAttrScore.setObjectName("pageItemAttrScore")
        self.toolBoxPraise.addItem(self.pageItemAttrScore, "")
        self.stackedWidgetContent.addWidget(self.pagePraise)
        self.pageBad = QtWidgets.QWidget()
        self.pageBad.setObjectName("pageBad")
        self.toolBoxCotent = QtWidgets.QToolBox(self.pageBad)
        self.toolBoxCotent.setGeometry(QtCore.QRect(10, 30, 771, 511))
        self.toolBoxCotent.setObjectName("toolBoxCotent")
        self.pageItemComments_2 = QtWidgets.QWidget()
        self.pageItemComments_2.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.pageItemComments_2.setObjectName("pageItemComments_2")
        self.tableViewComments_2 = QtWidgets.QTableView(self.pageItemComments_2)
        self.tableViewComments_2.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewComments_2.setObjectName("tableViewComments_2")
        self.toolBoxCotent.addItem(self.pageItemComments_2, "")
        self.pageItemGetRid_2 = QtWidgets.QWidget()
        self.pageItemGetRid_2.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.pageItemGetRid_2.setObjectName("pageItemGetRid_2")
        self.tableViewGetRid_2 = QtWidgets.QTableView(self.pageItemGetRid_2)
        self.tableViewGetRid_2.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewGetRid_2.setObjectName("tableViewGetRid_2")
        self.toolBoxCotent.addItem(self.pageItemGetRid_2, "")
        self.pageItemTagWords_2 = QtWidgets.QWidget()
        self.pageItemTagWords_2.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.pageItemTagWords_2.setObjectName("pageItemTagWords_2")
        self.tableViewTagWords_2 = QtWidgets.QTableView(self.pageItemTagWords_2)
        self.tableViewTagWords_2.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewTagWords_2.setObjectName("tableViewTagWords_2")
        self.toolBoxCotent.addItem(self.pageItemTagWords_2, "")
        self.pageItemAttrScore_2 = QtWidgets.QWidget()
        self.pageItemAttrScore_2.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.pageItemAttrScore_2.setObjectName("pageItemAttrScore_2")
        self.toolBoxCotent.addItem(self.pageItemAttrScore_2, "")
        self.stackedWidgetContent.addWidget(self.pageBad)
        self.buttonPraise = QtWidgets.QPushButton(self.frameLenovo)
        self.buttonPraise.setGeometry(QtCore.QRect(40, 100, 61, 151))
        self.buttonPraise.setObjectName("buttonPraise")
        self.tabBrand.addTab(self.tabLenovo, "")
        self.tabHp = QtWidgets.QWidget()
        self.tabHp.setObjectName("tabHp")
        self.frameHp = QtWidgets.QFrame(self.tabHp)
        self.frameHp.setGeometry(QtCore.QRect(10, 10, 1011, 601))
        self.frameHp.setStyleSheet("QFrame {\n"
"    background: #FFFFFF;\n"
"}")
        self.frameHp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHp.setObjectName("frameHp")
        self.buttonBad_2 = QtWidgets.QPushButton(self.frameHp)
        self.buttonBad_2.setGeometry(QtCore.QRect(40, 280, 61, 151))
        self.buttonBad_2.setObjectName("buttonBad_2")
        self.stackedWidgetContent_2 = QtWidgets.QStackedWidget(self.frameHp)
        self.stackedWidgetContent_2.setGeometry(QtCore.QRect(150, 20, 811, 561))
        self.stackedWidgetContent_2.setStyleSheet("")
        self.stackedWidgetContent_2.setObjectName("stackedWidgetContent_2")
        self.pagePraise_2 = QtWidgets.QWidget()
        self.pagePraise_2.setObjectName("pagePraise_2")
        self.toolBoxPraise_2 = QtWidgets.QToolBox(self.pagePraise_2)
        self.toolBoxPraise_2.setGeometry(QtCore.QRect(10, 30, 771, 511))
        self.toolBoxPraise_2.setObjectName("toolBoxPraise_2")
        self.pageItemComments_3 = QtWidgets.QWidget()
        self.pageItemComments_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemComments_3.setObjectName("pageItemComments_3")
        self.tableViewComments_3 = QtWidgets.QTableView(self.pageItemComments_3)
        self.tableViewComments_3.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewComments_3.setObjectName("tableViewComments_3")
        self.toolBoxPraise_2.addItem(self.pageItemComments_3, "")
        self.pageItemGetRid_3 = QtWidgets.QWidget()
        self.pageItemGetRid_3.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.pageItemGetRid_3.setObjectName("pageItemGetRid_3")
        self.tableViewGetRid_3 = QtWidgets.QTableView(self.pageItemGetRid_3)
        self.tableViewGetRid_3.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewGetRid_3.setObjectName("tableViewGetRid_3")
        self.toolBoxPraise_2.addItem(self.pageItemGetRid_3, "")
        self.pageItemTagWords_3 = QtWidgets.QWidget()
        self.pageItemTagWords_3.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.pageItemTagWords_3.setObjectName("pageItemTagWords_3")
        self.tableViewTagWords_3 = QtWidgets.QTableView(self.pageItemTagWords_3)
        self.tableViewTagWords_3.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewTagWords_3.setObjectName("tableViewTagWords_3")
        self.toolBoxPraise_2.addItem(self.pageItemTagWords_3, "")
        self.pageItemAttrScore_3 = QtWidgets.QWidget()
        self.pageItemAttrScore_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemAttrScore_3.setObjectName("pageItemAttrScore_3")
        self.toolBoxPraise_2.addItem(self.pageItemAttrScore_3, "")
        self.stackedWidgetContent_2.addWidget(self.pagePraise_2)
        self.pageBad_2 = QtWidgets.QWidget()
        self.pageBad_2.setObjectName("pageBad_2")
        self.toolBoxCotent_2 = QtWidgets.QToolBox(self.pageBad_2)
        self.toolBoxCotent_2.setGeometry(QtCore.QRect(10, 30, 771, 511))
        self.toolBoxCotent_2.setObjectName("toolBoxCotent_2")
        self.pageItemComments_4 = QtWidgets.QWidget()
        self.pageItemComments_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemComments_4.setObjectName("pageItemComments_4")
        self.tableViewComments_4 = QtWidgets.QTableView(self.pageItemComments_4)
        self.tableViewComments_4.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewComments_4.setObjectName("tableViewComments_4")
        self.toolBoxCotent_2.addItem(self.pageItemComments_4, "")
        self.pageItemGetRid_4 = QtWidgets.QWidget()
        self.pageItemGetRid_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemGetRid_4.setObjectName("pageItemGetRid_4")
        self.tableViewGetRid_4 = QtWidgets.QTableView(self.pageItemGetRid_4)
        self.tableViewGetRid_4.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewGetRid_4.setObjectName("tableViewGetRid_4")
        self.toolBoxCotent_2.addItem(self.pageItemGetRid_4, "")
        self.pageItemTagWords_4 = QtWidgets.QWidget()
        self.pageItemTagWords_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemTagWords_4.setObjectName("pageItemTagWords_4")
        self.tableViewTagWords_4 = QtWidgets.QTableView(self.pageItemTagWords_4)
        self.tableViewTagWords_4.setGeometry(QtCore.QRect(0, 10, 761, 361))
        self.tableViewTagWords_4.setObjectName("tableViewTagWords_4")
        self.toolBoxCotent_2.addItem(self.pageItemTagWords_4, "")
        self.pageItemAttrScore_4 = QtWidgets.QWidget()
        self.pageItemAttrScore_4.setGeometry(QtCore.QRect(0, 0, 771, 391))
        self.pageItemAttrScore_4.setObjectName("pageItemAttrScore_4")
        self.toolBoxCotent_2.addItem(self.pageItemAttrScore_4, "")
        self.stackedWidgetContent_2.addWidget(self.pageBad_2)
        self.buttonPraise_2 = QtWidgets.QPushButton(self.frameHp)
        self.buttonPraise_2.setGeometry(QtCore.QRect(40, 100, 61, 151))
        self.buttonPraise_2.setObjectName("buttonPraise_2")
        self.tabBrand.addTab(self.tabHp, "")
        self.tabAchievements.addTab(self.tabPreProcessed, "")
        self.tabBrandComparison = QtWidgets.QWidget()
        self.tabBrandComparison.setObjectName("tabBrandComparison")
        self.tabAchievements.addTab(self.tabBrandComparison, "")
        self.tabDictionary = QtWidgets.QWidget()
        self.tabDictionary.setObjectName("tabDictionary")
        self.tabAchievements.addTab(self.tabDictionary, "")
        self.buttonReturn = QtWidgets.QPushButton(self.frameArchievement)
        self.buttonReturn.setGeometry(QtCore.QRect(1020, 740, 93, 28))
        self.buttonReturn.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"}")
        self.buttonReturn.setObjectName("buttonReturn")

        self.retranslateUi(Form)
        self.tabAchievements.setCurrentIndex(2)
        self.tabBrand.setCurrentIndex(1)
        self.stackedWidgetContent.setCurrentIndex(1)
        self.toolBoxPraise.setCurrentIndex(2)
        self.toolBoxCotent.setCurrentIndex(3)
        self.stackedWidgetContent_2.setCurrentIndex(1)
        self.toolBoxPraise_2.setCurrentIndex(2)
        self.toolBoxCotent_2.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.buttonBad.setText(_translate("Form", "差\n"
"评"))
        self.toolBoxPraise.setItemText(self.toolBoxPraise.indexOf(self.pageItemComments), _translate("Form", "原评论"))
        self.toolBoxPraise.setItemText(self.toolBoxPraise.indexOf(self.pageItemGetRid), _translate("Form", "去重"))
        self.toolBoxPraise.setItemText(self.toolBoxPraise.indexOf(self.pageItemTagWords), _translate("Form", "分词标注"))
        self.toolBoxPraise.setItemText(self.toolBoxPraise.indexOf(self.pageItemAttrScore), _translate("Form", "属性词得分"))
        self.toolBoxCotent.setItemText(self.toolBoxCotent.indexOf(self.pageItemComments_2), _translate("Form", "原评论"))
        self.toolBoxCotent.setItemText(self.toolBoxCotent.indexOf(self.pageItemGetRid_2), _translate("Form", "去重"))
        self.toolBoxCotent.setItemText(self.toolBoxCotent.indexOf(self.pageItemTagWords_2), _translate("Form", "分词标注"))
        self.toolBoxCotent.setItemText(self.toolBoxCotent.indexOf(self.pageItemAttrScore_2), _translate("Form", "属性词得分"))
        self.buttonPraise.setText(_translate("Form", "好\n"
"评"))
        self.tabBrand.setTabText(self.tabBrand.indexOf(self.tabLenovo), _translate("Form", "联想"))
        self.buttonBad_2.setText(_translate("Form", "差\n"
"评"))
        self.toolBoxPraise_2.setItemText(self.toolBoxPraise_2.indexOf(self.pageItemComments_3), _translate("Form", "原评论"))
        self.toolBoxPraise_2.setItemText(self.toolBoxPraise_2.indexOf(self.pageItemGetRid_3), _translate("Form", "去重"))
        self.toolBoxPraise_2.setItemText(self.toolBoxPraise_2.indexOf(self.pageItemTagWords_3), _translate("Form", "分词标注"))
        self.toolBoxPraise_2.setItemText(self.toolBoxPraise_2.indexOf(self.pageItemAttrScore_3), _translate("Form", "属性词得分"))
        self.toolBoxCotent_2.setItemText(self.toolBoxCotent_2.indexOf(self.pageItemComments_4), _translate("Form", "原评论"))
        self.toolBoxCotent_2.setItemText(self.toolBoxCotent_2.indexOf(self.pageItemGetRid_4), _translate("Form", "去重"))
        self.toolBoxCotent_2.setItemText(self.toolBoxCotent_2.indexOf(self.pageItemTagWords_4), _translate("Form", "分词标注"))
        self.toolBoxCotent_2.setItemText(self.toolBoxCotent_2.indexOf(self.pageItemAttrScore_4), _translate("Form", "属性词得分"))
        self.buttonPraise_2.setText(_translate("Form", "好\n"
"评"))
        self.tabBrand.setTabText(self.tabBrand.indexOf(self.tabHp), _translate("Form", "惠普"))
        self.tabAchievements.setTabText(self.tabAchievements.indexOf(self.tabPreProcessed), _translate("Form", "预处理"))
        self.tabAchievements.setTabText(self.tabAchievements.indexOf(self.tabBrandComparison), _translate("Form", "品牌对比"))
        self.tabAchievements.setTabText(self.tabAchievements.indexOf(self.tabDictionary), _translate("Form", "词典"))
        self.buttonReturn.setText(_translate("Form", "返回"))

