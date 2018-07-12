# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from app import App
import re
import time

class Ui_MainWindow(object):
    def __init__(self):
        self.app = App()

        # tab setup
        self.selectedTable = ""
        self.setupTextCol_def = "text"
        self.setupClassCol_def = "clas"
        self.setupTextCol = "text"
        self.setupClassCol = "clas"
        self.exceptCol = []

        # tab fix word
        # self.fixWord_db = "sentiment_analysis"
        self.fixWord_cols = ['id','word','word_fix']
        self.fixWord_fixtable = "fix_word"
        self.fixWord_indexData = None
        self.fixWord_idData = 0

        # tab evaluation
        self.evaluation_doPreprocessing = True
        self.evaluation_doFeatureSelection = False
        self.evaluation_numFeatureToRetain = 0
        self.evaluation_thresholdFeatureIgnore = 0
        self.eval_time = 0

        # tab training
        self.preprocessing_time = 0
        self.vsmFeature = None
        self.vsm = None
        self.model = None
        self.trainingFold_def = 10
        self.training_total_data = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_setup = QtWidgets.QWidget()
        self.tab_setup.setObjectName("tab_setup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_setup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.pushButton_setup_next = QtWidgets.QPushButton(self.tab_setup)
        self.pushButton_setup_next.setObjectName("pushButton_setup_next")
        self.gridLayout_3.addWidget(self.pushButton_setup_next, 2, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_setup)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_setup_except_col = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_setup_except_col.setObjectName("lineEdit_setup_except_col")
        self.gridLayout_6.addWidget(self.lineEdit_setup_except_col, 2, 1, 1, 1)
        self.lineEdit_setup_clas_col = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_setup_clas_col.setObjectName("lineEdit_setup_clas_col")
        self.gridLayout_6.addWidget(self.lineEdit_setup_clas_col, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 2, 0, 1, 1)
        self.lineEdit_setup_text_col = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_setup_text_col.setObjectName("lineEdit_setup_text_col")
        self.gridLayout_6.addWidget(self.lineEdit_setup_text_col, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem2, 3, 1, 1, 1)
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.lineEdit_setup_except_col.raise_()
        self.lineEdit_setup_clas_col.raise_()
        self.lineEdit_setup_text_col.raise_()
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.tab_setup)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_setup_table = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_setup_table.setObjectName("comboBox_setup_table")
        self.gridLayout_4.addWidget(self.comboBox_setup_table, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_setup_db = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_setup_db.setObjectName("lineEdit_setup_db")
        self.gridLayout_4.addWidget(self.lineEdit_setup_db, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 6, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_setup_password = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_setup_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_setup_password.setObjectName("lineEdit_setup_password")
        self.gridLayout_4.addWidget(self.lineEdit_setup_password, 2, 1, 1, 1)
        self.lineEdit_setup_host = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_setup_host.setText("")
        self.lineEdit_setup_host.setObjectName("lineEdit_setup_host")
        self.gridLayout_4.addWidget(self.lineEdit_setup_host, 0, 1, 1, 1)
        self.lineEdit_setup_user = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_setup_user.setObjectName("lineEdit_setup_user")
        self.gridLayout_4.addWidget(self.lineEdit_setup_user, 1, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 0, 1, 1)
        self.pushButton_setup_connect = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_setup_connect.setObjectName("pushButton_setup_connect")
        self.gridLayout_5.addWidget(self.pushButton_setup_connect, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 4, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.label_setup_status_connect = QtWidgets.QLabel(self.groupBox)
        self.label_setup_status_connect.setObjectName("label_setup_status_connect")
        self.horizontalLayout.addWidget(self.label_setup_status_connect)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout_4.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_setup, "")
        self.tab_fix_word = QtWidgets.QWidget()
        self.tab_fix_word.setObjectName("tab_fix_word")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_fix_word)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.tableWidget_fixword = QtWidgets.QTableWidget(self.tab_fix_word)
        self.tableWidget_fixword.setObjectName("tableWidget_fixword")
        self.tableWidget_fixword.setColumnCount(0)
        self.tableWidget_fixword.setRowCount(0)
        self.gridLayout_10.addWidget(self.tableWidget_fixword, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_10, 0, 2, 4, 3)
        self.pushButton_fixword_next = QtWidgets.QPushButton(self.tab_fix_word)
        self.pushButton_fixword_next.setObjectName("pushButton_fixword_next")
        self.gridLayout_7.addWidget(self.pushButton_fixword_next, 4, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem7, 4, 2, 1, 1)
        self.pushButton_fixword_save = QtWidgets.QPushButton(self.tab_fix_word)
        self.pushButton_fixword_save.setObjectName("pushButton_fixword_save")
        self.gridLayout_7.addWidget(self.pushButton_fixword_save, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem8, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_fix_word)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_fix_word)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEdit_fixword_word = QtWidgets.QLineEdit(self.tab_fix_word)
        self.lineEdit_fixword_word.setReadOnly(True)
        self.lineEdit_fixword_word.setPlaceholderText("")
        self.lineEdit_fixword_word.setObjectName("lineEdit_fixword_word")
        self.gridLayout_7.addWidget(self.lineEdit_fixword_word, 0, 1, 1, 1)
        self.lineEdit_fixword_wordfix = QtWidgets.QLineEdit(self.tab_fix_word)
        self.lineEdit_fixword_wordfix.setObjectName("lineEdit_fixword_wordfix")
        self.gridLayout_7.addWidget(self.lineEdit_fixword_wordfix, 1, 1, 1, 1)
        self.pushButton_fixword_back = QtWidgets.QPushButton(self.tab_fix_word)
        self.pushButton_fixword_back.setObjectName("pushButton_fixword_back")
        self.gridLayout_7.addWidget(self.pushButton_fixword_back, 4, 3, 1, 1)
        self.tabWidget.addTab(self.tab_fix_word, "")
        self.tab_evaluation = QtWidgets.QWidget()
        self.tab_evaluation.setObjectName("tab_evaluation")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_evaluation)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.groupBox_evaluation = QtWidgets.QGroupBox(self.tab_evaluation)
        self.groupBox_evaluation.setObjectName("groupBox_evaluation")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_evaluation)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_15.setObjectName("label_15")
        self.gridLayout_14.addWidget(self.label_15, 2, 0, 1, 1)
        self.lineEdit_evaluation_folds = QtWidgets.QLineEdit(self.groupBox_evaluation)
        self.lineEdit_evaluation_folds.setObjectName("lineEdit_evaluation_folds")
        self.gridLayout_14.addWidget(self.lineEdit_evaluation_folds, 2, 1, 1, 1)
        self.pushButton_evaluation_start_kfold = QtWidgets.QPushButton(self.groupBox_evaluation)
        self.pushButton_evaluation_start_kfold.setObjectName("pushButton_evaluation_start_kfold")
        self.gridLayout_14.addWidget(self.pushButton_evaluation_start_kfold, 2, 2, 1, 1)
        self.label_evaluation_status = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_evaluation_status.setObjectName("label_evaluation_status")
        self.gridLayout_14.addWidget(self.label_evaluation_status, 3, 0, 1, 4)
        self.label_14 = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_14.setObjectName("label_14")
        self.gridLayout_14.addWidget(self.label_14, 1, 0, 1, 3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem9, 1, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem10, 1, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem11, 1, 5, 1, 1)
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.label_47 = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_47.setObjectName("label_47")
        self.gridLayout_27.addWidget(self.label_47, 0, 1, 1, 1)
        self.label_evaluation_recall = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_evaluation_recall.setObjectName("label_evaluation_recall")
        self.gridLayout_27.addWidget(self.label_evaluation_recall, 0, 2, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_42.setObjectName("label_42")
        self.gridLayout_27.addWidget(self.label_42, 0, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_27.addItem(spacerItem12, 0, 3, 1, 1)
        self.gridLayout_24.addLayout(self.gridLayout_27, 0, 2, 1, 1)
        self.gridLayout_26 = QtWidgets.QGridLayout()
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.label_evaluation_precision = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_evaluation_precision.setObjectName("label_evaluation_precision")
        self.gridLayout_26.addWidget(self.label_evaluation_precision, 0, 2, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_45.setObjectName("label_45")
        self.gridLayout_26.addWidget(self.label_45, 0, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_39.setObjectName("label_39")
        self.gridLayout_26.addWidget(self.label_39, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem13, 0, 3, 1, 1)
        self.gridLayout_24.addLayout(self.gridLayout_26, 0, 1, 1, 1)
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.label_21 = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_21.setObjectName("label_21")
        self.gridLayout_25.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_44.setObjectName("label_44")
        self.gridLayout_25.addWidget(self.label_44, 0, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_20.setObjectName("label_20")
        self.gridLayout_25.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_evaluation_accuration = QtWidgets.QLabel(self.groupBox_evaluation)
        self.label_evaluation_accuration.setObjectName("label_evaluation_accuration")
        self.gridLayout_25.addWidget(self.label_evaluation_accuration, 0, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem14, 0, 4, 1, 1)
        self.gridLayout_24.addLayout(self.gridLayout_25, 0, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_24, 2, 3, 1, 3)
        self.gridLayout_13.addLayout(self.gridLayout_14, 0, 0, 1, 2)
        self.plainTextEdit_evaluation_log = QtWidgets.QPlainTextEdit(self.groupBox_evaluation)
        self.plainTextEdit_evaluation_log.setObjectName("plainTextEdit_evaluation_log")
        self.gridLayout_13.addWidget(self.plainTextEdit_evaluation_log, 1, 0, 1, 2)
        self.gridLayout_11.addWidget(self.groupBox_evaluation, 1, 0, 1, 3)
        self.pushButton_evaluation_next = QtWidgets.QPushButton(self.tab_evaluation)
        self.pushButton_evaluation_next.setObjectName("pushButton_evaluation_next")
        self.gridLayout_11.addWidget(self.pushButton_evaluation_next, 2, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem15, 2, 0, 1, 1)
        self.pushButton_evaluation_back = QtWidgets.QPushButton(self.tab_evaluation)
        self.pushButton_evaluation_back.setObjectName("pushButton_evaluation_back")
        self.gridLayout_11.addWidget(self.pushButton_evaluation_back, 2, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_evaluation)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.radioButton_evaluation_nb = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_evaluation_nb.setObjectName("radioButton_evaluation_nb")
        self.gridLayout_23.addWidget(self.radioButton_evaluation_nb, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_23.addWidget(self.label_19, 0, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem16, 2, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_23, 0, 4, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.radioButton_evaluation_nopreprocessing = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_evaluation_nopreprocessing.setObjectName("radioButton_evaluation_nopreprocessing")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_evaluation_nopreprocessing)
        self.gridLayout_19.addWidget(self.radioButton_evaluation_nopreprocessing, 1, 0, 1, 1)
        self.radioButton_evaluation_withpreprocessing = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_evaluation_withpreprocessing.setObjectName("radioButton_evaluation_withpreprocessing")
        self.buttonGroup.addButton(self.radioButton_evaluation_withpreprocessing)
        self.gridLayout_19.addWidget(self.radioButton_evaluation_withpreprocessing, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_19.addWidget(self.label_17, 0, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem17, 3, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_19, 0, 1, 1, 1)
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.radioButton_evaluation_featureselection_ig = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_evaluation_featureselection_ig.setObjectName("radioButton_evaluation_featureselection_ig")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_evaluation_featureselection_ig)
        self.gridLayout_20.addWidget(self.radioButton_evaluation_featureselection_ig, 2, 0, 1, 1)
        self.radioButton_evaluation_nofeatureselection = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_evaluation_nofeatureselection.setObjectName("radioButton_evaluation_nofeatureselection")
        self.buttonGroup_2.addButton(self.radioButton_evaluation_nofeatureselection)
        self.gridLayout_20.addWidget(self.radioButton_evaluation_nofeatureselection, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_20.addWidget(self.label_18, 0, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_20.addItem(spacerItem18, 3, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_20, 0, 2, 1, 1)
        self.lineEdit_evaluation_number_of_feature = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_evaluation_number_of_feature.setObjectName("lineEdit_evaluation_number_of_feature")
        self.gridLayout_12.addWidget(self.lineEdit_evaluation_number_of_feature, 1, 2, 1, 2)
        self.lineEdit_evaluation_threshold_of_feature = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_evaluation_threshold_of_feature.setObjectName("lineEdit_evaluation_threshold_of_feature")
        self.gridLayout_12.addWidget(self.lineEdit_evaluation_threshold_of_feature, 2, 2, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_12.addWidget(self.label_13, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_12.addWidget(self.label_11, 1, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem19, 1, 4, 1, 1)
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem20, 0, 0, 1, 1)
        self.pushButton_evaluation_start_pre = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_evaluation_start_pre.setObjectName("pushButton_evaluation_start_pre")
        self.gridLayout_22.addWidget(self.pushButton_evaluation_start_pre, 0, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem21, 0, 2, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_22, 3, 1, 1, 4)
        self.progressBar_evaluation_progress_pre = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar_evaluation_progress_pre.setProperty("value", 0)
        self.progressBar_evaluation_progress_pre.setObjectName("progressBar_evaluation_progress_pre")
        self.gridLayout_12.addWidget(self.progressBar_evaluation_progress_pre, 4, 1, 1, 4)
        self.gridLayout_11.addWidget(self.groupBox_3, 0, 0, 1, 3)
        self.tabWidget.addTab(self.tab_evaluation, "")
        self.tab_training = QtWidgets.QWidget()
        self.tab_training.setObjectName("tab_training")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_training)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.pushButton_training_back = QtWidgets.QPushButton(self.tab_training)
        self.pushButton_training_back.setObjectName("pushButton_training_back")
        self.gridLayout_15.addWidget(self.pushButton_training_back, 2, 1, 1, 1)
        self.pushButton_training_analys = QtWidgets.QPushButton(self.tab_training)
        self.pushButton_training_analys.setObjectName("pushButton_training_analys")
        self.gridLayout_15.addWidget(self.pushButton_training_analys, 2, 2, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem22, 2, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_training)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem23, 5, 4, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox_5)
        self.label_34.setObjectName("label_34")
        self.gridLayout_16.addWidget(self.label_34, 6, 4, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_5)
        self.label_25.setObjectName("label_25")
        self.gridLayout_16.addWidget(self.label_25, 3, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_5)
        self.label_23.setObjectName("label_23")
        self.gridLayout_16.addWidget(self.label_23, 4, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_5)
        self.label_24.setObjectName("label_24")
        self.gridLayout_16.addWidget(self.label_24, 5, 0, 1, 1)
        self.label_training_total_data = QtWidgets.QLabel(self.groupBox_5)
        self.label_training_total_data.setObjectName("label_training_total_data")
        self.gridLayout_16.addWidget(self.label_training_total_data, 4, 3, 1, 1)
        self.label_training_total_feature = QtWidgets.QLabel(self.groupBox_5)
        self.label_training_total_feature.setObjectName("label_training_total_feature")
        self.gridLayout_16.addWidget(self.label_training_total_feature, 5, 3, 1, 1)
        self.label_training_time = QtWidgets.QLabel(self.groupBox_5)
        self.label_training_time.setObjectName("label_training_time")
        self.gridLayout_16.addWidget(self.label_training_time, 6, 3, 1, 1)
        self.label_training_total_class = QtWidgets.QLabel(self.groupBox_5)
        self.label_training_total_class.setObjectName("label_training_total_class")
        self.gridLayout_16.addWidget(self.label_training_total_class, 3, 3, 1, 1)
        self.label_training_data_perclass = QtWidgets.QLabel(self.groupBox_5)
        self.label_training_data_perclass.setText("")
        self.label_training_data_perclass.setObjectName("label_training_data_perclass")
        self.gridLayout_16.addWidget(self.label_training_data_perclass, 4, 4, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem24)
        self.pushButton_training = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_training.setObjectName("pushButton_training")
        self.horizontalLayout_2.addWidget(self.pushButton_training)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem25)
        self.gridLayout_16.addLayout(self.horizontalLayout_2, 0, 0, 1, 8)
        self.label_training_status = QtWidgets.QLabel(self.groupBox_5)
        self.label_training_status.setText("")
        self.label_training_status.setObjectName("label_training_status")
        self.gridLayout_16.addWidget(self.label_training_status, 2, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_5)
        self.label_26.setObjectName("label_26")
        self.gridLayout_16.addWidget(self.label_26, 6, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_5)
        self.label_27.setObjectName("label_27")
        self.gridLayout_16.addWidget(self.label_27, 3, 2, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_5)
        self.label_28.setObjectName("label_28")
        self.gridLayout_16.addWidget(self.label_28, 4, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_5)
        self.label_30.setObjectName("label_30")
        self.gridLayout_16.addWidget(self.label_30, 6, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_5)
        self.label_29.setObjectName("label_29")
        self.gridLayout_16.addWidget(self.label_29, 5, 2, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem26, 5, 6, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem27, 5, 5, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_5, 0, 0, 1, 3)
        self.groupBox_training_eval = QtWidgets.QGroupBox(self.tab_training)
        self.groupBox_training_eval.setObjectName("groupBox_training_eval")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_training_eval)
        self.gridLayout_17.setObjectName("gridLayout_17")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem28, 0, 1, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_40 = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_40.setObjectName("label_40")
        self.gridLayout_18.addWidget(self.label_40, 0, 0, 1, 1)
        self.label_training_recall = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_training_recall.setObjectName("label_training_recall")
        self.gridLayout_18.addWidget(self.label_training_recall, 0, 1, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem29, 0, 2, 1, 1)
        self.tableWidget_training_features = QtWidgets.QTableWidget(self.groupBox_training_eval)
        self.tableWidget_training_features.setObjectName("tableWidget_training_features")
        self.tableWidget_training_features.setColumnCount(0)
        self.tableWidget_training_features.setRowCount(0)
        self.gridLayout_18.addWidget(self.tableWidget_training_features, 1, 0, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem30, 0, 3, 1, 1)
        self.tableWidget_training_vsm = QtWidgets.QTableWidget(self.groupBox_training_eval)
        self.tableWidget_training_vsm.setObjectName("tableWidget_training_vsm")
        self.tableWidget_training_vsm.setColumnCount(0)
        self.tableWidget_training_vsm.setRowCount(0)
        self.gridLayout_18.addWidget(self.tableWidget_training_vsm, 1, 1, 1, 3)
        self.gridLayout_17.addLayout(self.gridLayout_18, 1, 0, 1, 5)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_31 = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_31.setObjectName("label_31")
        self.gridLayout_8.addWidget(self.label_31, 0, 0, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_54.setObjectName("label_54")
        self.gridLayout_8.addWidget(self.label_54, 1, 4, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_53.setObjectName("label_53")
        self.gridLayout_8.addWidget(self.label_53, 1, 3, 1, 1)
        self.label_training_reduction = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_training_reduction.setObjectName("label_training_reduction")
        self.gridLayout_8.addWidget(self.label_training_reduction, 1, 5, 1, 1)
        self.label_training_feature_before = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_training_feature_before.setObjectName("label_training_feature_before")
        self.gridLayout_8.addWidget(self.label_training_feature_before, 0, 2, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_50.setObjectName("label_50")
        self.gridLayout_8.addWidget(self.label_50, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_22.setObjectName("label_22")
        self.gridLayout_8.addWidget(self.label_22, 0, 1, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_51.setObjectName("label_51")
        self.gridLayout_8.addWidget(self.label_51, 1, 1, 1, 1)
        self.label_training_feature = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_training_feature.setObjectName("label_training_feature")
        self.gridLayout_8.addWidget(self.label_training_feature, 1, 2, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_56.setObjectName("label_56")
        self.gridLayout_8.addWidget(self.label_56, 1, 6, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem31, 0, 2, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem32, 0, 3, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem33, 0, 4, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lineEdit_training_sentence = QtWidgets.QLineEdit(self.groupBox_training_eval)
        self.lineEdit_training_sentence.setObjectName("lineEdit_training_sentence")
        self.gridLayout_9.addWidget(self.lineEdit_training_sentence, 1, 0, 1, 1)
        self.pushButton_training_test_sentence = QtWidgets.QPushButton(self.groupBox_training_eval)
        self.pushButton_training_test_sentence.setObjectName("pushButton_training_test_sentence")
        self.gridLayout_9.addWidget(self.pushButton_training_test_sentence, 1, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_35.setObjectName("label_35")
        self.gridLayout_9.addWidget(self.label_35, 0, 0, 1, 1)
        self.label_training_result_test_sentence = QtWidgets.QLabel(self.groupBox_training_eval)
        self.label_training_result_test_sentence.setText("")
        self.label_training_result_test_sentence.setObjectName("label_training_result_test_sentence")
        self.gridLayout_9.addWidget(self.label_training_result_test_sentence, 2, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_9, 2, 0, 1, 5)
        self.gridLayout_15.addWidget(self.groupBox_training_eval, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab_training, "")
        self.tab_analysis = QtWidgets.QWidget()
        self.tab_analysis.setObjectName("tab_analysis")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_analysis)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget.addTab(self.tab_analysis, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setupDefault()
        self.connectAction()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sentiment Analysis"))
        self.pushButton_setup_next.setText(_translate("MainWindow", "Next"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Additional"))
        self.lineEdit_setup_except_col.setToolTip(_translate("MainWindow", "<html><head/><body><p>Column that not neccesary for process, eg : id column.</p></body></html>"))
        self.lineEdit_setup_except_col.setPlaceholderText(_translate("MainWindow", "seperate with comma (,)"))
        self.lineEdit_setup_clas_col.setToolTip(_translate("MainWindow", "<html><head/><body><p>Class column of data. Default : clas</p></body></html>"))
        self.lineEdit_setup_clas_col.setPlaceholderText(_translate("MainWindow", "default : clas"))
        self.label_7.setText(_translate("MainWindow", "Class column"))
        self.label_6.setText(_translate("MainWindow", "Text column"))
        self.label_8.setText(_translate("MainWindow", "Exceptional Column"))
        self.lineEdit_setup_text_col.setToolTip(_translate("MainWindow", "<html><head/><body><p>Column for text to be process. Default : text</p></body></html>"))
        self.lineEdit_setup_text_col.setPlaceholderText(_translate("MainWindow", "default : text"))
        self.groupBox.setTitle(_translate("MainWindow", "Data source"))
        self.label.setText(_translate("MainWindow", "Host"))
        self.label_2.setText(_translate("MainWindow", "User"))
        self.label_4.setText(_translate("MainWindow", "Database"))
        self.lineEdit_setup_db.setToolTip(_translate("MainWindow", "<html><head/><body><p>Database to use</p></body></html>"))
        self.lineEdit_setup_db.setPlaceholderText(_translate("MainWindow", "eg : training_db"))
        self.label_5.setText(_translate("MainWindow", "Table for training data"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.lineEdit_setup_password.setToolTip(_translate("MainWindow", "<html><head/><body><p>User password</p></body></html>"))
        self.lineEdit_setup_password.setPlaceholderText(_translate("MainWindow", "password"))
        self.lineEdit_setup_host.setToolTip(_translate("MainWindow", "<html><head/><body><p>Host of database server</p></body></html>"))
        self.lineEdit_setup_host.setPlaceholderText(_translate("MainWindow", "eg : localhost"))
        self.lineEdit_setup_user.setToolTip(_translate("MainWindow", "<html><head/><body><p>Database user</p></body></html>"))
        self.lineEdit_setup_user.setPlaceholderText(_translate("MainWindow", "eg : root"))
        self.pushButton_setup_connect.setText(_translate("MainWindow", "Connect"))
        self.label_12.setText(_translate("MainWindow", "Status :"))
        self.label_setup_status_connect.setText(_translate("MainWindow", "Disconnected"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_setup), _translate("MainWindow", "Setup"))
        self.pushButton_fixword_next.setText(_translate("MainWindow", "Next"))
        self.pushButton_fixword_save.setText(_translate("MainWindow", "Save"))
        self.label_9.setText(_translate("MainWindow", "Word"))
        self.label_10.setText(_translate("MainWindow", "Word fix"))
        self.lineEdit_fixword_wordfix.setToolTip(_translate("MainWindow", "Word fix"))
        self.pushButton_fixword_back.setText(_translate("MainWindow", "Back"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fix_word), _translate("MainWindow", "Fix word"))
        self.groupBox_evaluation.setTitle(_translate("MainWindow", "Evaluation"))
        self.label_15.setText(_translate("MainWindow", "Folds"))
        self.lineEdit_evaluation_folds.setPlaceholderText(_translate("MainWindow", "default : 10"))
        self.pushButton_evaluation_start_kfold.setText(_translate("MainWindow", "Start"))
        self.label_evaluation_status.setText(_translate("MainWindow", "-"))
        self.label_14.setText(_translate("MainWindow", "K-Fold Cross Validation"))
        self.label_47.setText(_translate("MainWindow", ":"))
        self.label_evaluation_recall.setText(_translate("MainWindow", "0"))
        self.label_42.setText(_translate("MainWindow", "Recall"))
        self.label_evaluation_precision.setText(_translate("MainWindow", "0"))
        self.label_45.setText(_translate("MainWindow", ":"))
        self.label_39.setText(_translate("MainWindow", "Precision"))
        self.label_21.setText(_translate("MainWindow", "Accuration"))
        self.label_44.setText(_translate("MainWindow", "%"))
        self.label_20.setText(_translate("MainWindow", ":"))
        self.label_evaluation_accuration.setText(_translate("MainWindow", "0"))
        self.pushButton_evaluation_next.setText(_translate("MainWindow", "Next"))
        self.pushButton_evaluation_back.setText(_translate("MainWindow", "Back"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Setting"))
        self.radioButton_evaluation_nb.setText(_translate("MainWindow", "Naive Bayes"))
        self.label_19.setText(_translate("MainWindow", "Classifier"))
        self.radioButton_evaluation_nopreprocessing.setToolTip(_translate("MainWindow", "<html><head/><body><p>Will only remove symbol and lower case the text.</p></body></html>"))
        self.radioButton_evaluation_nopreprocessing.setText(_translate("MainWindow", "No preprocessing"))
        self.radioButton_evaluation_withpreprocessing.setToolTip(_translate("MainWindow", "<html><head/><body><p>Remove symbols, case folding, remove stopword, and do stemming.</p><p><br/></p></body></html>"))
        self.radioButton_evaluation_withpreprocessing.setText(_translate("MainWindow", "Preprocessing"))
        self.label_17.setText(_translate("MainWindow", "Preprocessing"))
        self.radioButton_evaluation_featureselection_ig.setToolTip(_translate("MainWindow", "<html><head/><body><p>Perform a feature selection.</p></body></html>"))
        self.radioButton_evaluation_featureselection_ig.setText(_translate("MainWindow", "Information Gain (IG)"))
        self.radioButton_evaluation_nofeatureselection.setToolTip(_translate("MainWindow", "<html><head/><body><p>No feature selection process.</p></body></html>"))
        self.radioButton_evaluation_nofeatureselection.setText(_translate("MainWindow", "No feature selection"))
        self.label_18.setText(_translate("MainWindow", "Feature Selection"))
        self.lineEdit_evaluation_number_of_feature.setToolTip(_translate("MainWindow", "<html><head/><body><p>Number of feature taken.</p></body></html>"))
        self.lineEdit_evaluation_number_of_feature.setPlaceholderText(_translate("MainWindow", "default : 0, all feature selected"))
        self.lineEdit_evaluation_threshold_of_feature.setToolTip(_translate("MainWindow", "<html><head/><body><p>Threshold feature to be taken, if below threshold then feature will be removed.</p></body></html>"))
        self.lineEdit_evaluation_threshold_of_feature.setPlaceholderText(_translate("MainWindow", "default : -1. no threshold - all feature selected"))
        self.label_13.setText(_translate("MainWindow", "Threshold (IG)"))
        self.label_11.setText(_translate("MainWindow", "Number of feature (IG)"))
        self.pushButton_evaluation_start_pre.setText(_translate("MainWindow", "Start Preprocessing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_evaluation), _translate("MainWindow", "Evaluation"))
        self.pushButton_training_back.setText(_translate("MainWindow", "Back"))
        self.pushButton_training_analys.setText(_translate("MainWindow", "Analysis Data"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Training Classifier (Naive Bayes)"))
        self.label_34.setText(_translate("MainWindow", "second"))
        self.label_25.setText(_translate("MainWindow", "Total class"))
        self.label_23.setText(_translate("MainWindow", "Total training data"))
        self.label_24.setText(_translate("MainWindow", "Total feature processed"))
        self.label_training_total_data.setText(_translate("MainWindow", "0"))
        self.label_training_total_feature.setText(_translate("MainWindow", "0"))
        self.label_training_time.setText(_translate("MainWindow", "0"))
        self.label_training_total_class.setText(_translate("MainWindow", "0"))
        self.pushButton_training.setText(_translate("MainWindow", "Train data"))
        self.label_26.setText(_translate("MainWindow", "Time elapsed"))
        self.label_27.setText(_translate("MainWindow", ":"))
        self.label_28.setText(_translate("MainWindow", ":"))
        self.label_30.setText(_translate("MainWindow", ":"))
        self.label_29.setText(_translate("MainWindow", ":"))
        self.groupBox_training_eval.setTitle(_translate("MainWindow", "Detail"))
        self.label_40.setText(_translate("MainWindow", "Features"))
        self.label_training_recall.setText(_translate("MainWindow", "Vector Space Model"))
        self.label_31.setText(_translate("MainWindow", "Total feature before"))
        self.label_54.setText(_translate("MainWindow", ":"))
        self.label_53.setText(_translate("MainWindow", "Reduction"))
        self.label_training_reduction.setText(_translate("MainWindow", "0"))
        self.label_training_feature_before.setText(_translate("MainWindow", "0"))
        self.label_50.setText(_translate("MainWindow", "Total feature"))
        self.label_22.setText(_translate("MainWindow", ":"))
        self.label_51.setText(_translate("MainWindow", ":"))
        self.label_training_feature.setText(_translate("MainWindow", "0"))
        self.label_56.setText(_translate("MainWindow", "%"))
        self.lineEdit_training_sentence.setPlaceholderText(_translate("MainWindow", "Enter sentence here"))
        self.pushButton_training_test_sentence.setText(_translate("MainWindow", "Test sentence"))
        self.label_35.setText(_translate("MainWindow", "Sentence Test"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_training), _translate("MainWindow", "Training"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_analysis), _translate("MainWindow", "Analysis"))

    def setupDefault(self):
        self.tabWidget.setTabEnabled(1,False)
        self.tabWidget.setTabEnabled(2,False)
        self.tabWidget.setTabEnabled(3,False)
        self.tabWidget.setTabEnabled(4,False)

        # tab setup
        self.pushButton_setup_next.setEnabled(False)

        # tab fix word
        self.pushButton_fixword_next.setEnabled(False)

        # tab evaluation
        self.pushButton_evaluation_next.setEnabled(False)
        self.radioButton_evaluation_withpreprocessing.setChecked(True)
        self.radioButton_evaluation_nofeatureselection.setChecked(True)
        self.radioButton_evaluation_nb.setChecked(True)
        self.lineEdit_evaluation_number_of_feature.setEnabled(False)
        self.lineEdit_evaluation_threshold_of_feature.setEnabled(False)
        self.groupBox_evaluation.setEnabled(False)
        self.plainTextEdit_evaluation_log.setReadOnly(True)

        # tab training
        self.pushButton_training_analys.setEnabled(False)

    def connectAction(self):
        # tab setup
        regexLetterUnderscoreOnly = QtCore.QRegExp(r'^[a-zA-Z0-9\_]*$')
        validator1 = QtGui.QRegExpValidator(regexLetterUnderscoreOnly,self.lineEdit_setup_host)
        self.lineEdit_setup_host.setValidator(validator1)
        validator2 = QtGui.QRegExpValidator(regexLetterUnderscoreOnly,self.lineEdit_setup_user)
        self.lineEdit_setup_user.setValidator(validator2)
        validator3 = QtGui.QRegExpValidator(regexLetterUnderscoreOnly,self.lineEdit_setup_db)
        self.lineEdit_setup_db.setValidator(validator3)
        self.pushButton_setup_connect.clicked.connect(lambda: self.buttonConnectDb())
        self.comboBox_setup_table.currentTextChanged.connect(self.tableTrainingCheck)
        self.lineEdit_setup_text_col.keyReleaseEvent = self.setupHandleKeyReleaseText
        self.lineEdit_setup_clas_col.keyReleaseEvent = self.setupHandleKeyReleaseClass
        self.lineEdit_setup_except_col.keyReleaseEvent = self.setupHandleKeyReleaseEx
        self.pushButton_setup_next.clicked.connect(lambda: self.setupNext())

        # tab fixword
        regexLetter = QtCore.QRegExp(r'^[a-z\s]*$') #!!!!!!!!!!!!!!!!!!!!!!!!!!
        validatorWordFix = QtGui.QRegExpValidator(regexLetter,self.lineEdit_fixword_wordfix)
        self.lineEdit_fixword_wordfix.setValidator(validatorWordFix)
        self.pushButton_fixword_save.clicked.connect(self.fixWordSave)
        self.pushButton_fixword_back.clicked.connect(self.fixWordBack)
        self.pushButton_fixword_next.clicked.connect(self.fixWordNext)

        # tab evaluation
        self.radioButton_evaluation_nopreprocessing.toggled.connect(self.evalCheckNoPre)
        self.radioButton_evaluation_withpreprocessing.toggled.connect(self.evalCheckPre)
        self.radioButton_evaluation_nofeatureselection.toggled.connect(self.evalCheckNoFS)
        self.radioButton_evaluation_featureselection_ig.toggled.connect(self.evalCheckFS)
        self.radioButton_evaluation_nb.toggled.connect(self.evalCheckNB)
        regexNumber = QtCore.QRegExp(r'^[0-9]*$')
        validatorPreNum = QtGui.QRegExpValidator(regexNumber,self.lineEdit_evaluation_number_of_feature)
        self.lineEdit_evaluation_number_of_feature.setValidator(validatorPreNum)
        regexDecimal = QtCore.QRegExp(r'^[0-9]\d*(\.\d+)?$')
        validatorPreDec = QtGui.QRegExpValidator(regexDecimal,self.lineEdit_evaluation_threshold_of_feature)
        self.lineEdit_evaluation_threshold_of_feature.setValidator(validatorPreDec)
        self.pushButton_evaluation_start_pre.clicked.connect(self.evalStartPre)
        validatorNumFold = QtGui.QRegExpValidator(regexNumber,self.lineEdit_evaluation_folds)
        self.lineEdit_evaluation_folds.setValidator(validatorNumFold)
        self.pushButton_evaluation_start_kfold.clicked.connect(self.testEvalKFold)
        self.pushButton_evaluation_back.clicked.connect(self.evalBack)
        self.pushButton_evaluation_next.clicked.connect(self.evalNext)

        # tab training
        self.pushButton_training.clicked.connect(self.trainingData)
        self.pushButton_training_test_sentence.clicked.connect(self.trainingTestSentence)
        self.pushButton_training_back.clicked.connect(self.trainingBack)

# tab setup
    def buttonConnectDb(self):
        self.pushButton_setup_connect.setEnabled(False)
        self.comboBox_setup_table.clear()
        host = self.lineEdit_setup_host.text()
        user = self.lineEdit_setup_user.text()
        password = self.lineEdit_setup_password.text()
        db = self.lineEdit_setup_db.text()
        connectStatus = self.app.connectDb(host,user,password,db)
        if connectStatus['success'] == True:
            if connectStatus['tables'] != None:
                for tb in connectStatus['tables']:
                    self.comboBox_setup_table.addItem(tb[0])
        else:
            pass
        self.label_setup_status_connect.setText(connectStatus['msg'])
        self.pushButton_setup_connect.setEnabled(True)

    def setupCheckTrainingTable(self):
        if self.app.con != None:
            if self.setupTextCol and self.setupClassCol and self.setupTextCol == self.setupClassCol:
                print("Text column cannot be same as class column!")
                self.pushButton_setup_next.setEnabled(False)
                self.tabWidget.setTabEnabled(1,False)
                self.tabWidget.setTabEnabled(2,False)
                self.tabWidget.setTabEnabled(3,False)
                # self.tabWidget.setTabEnabled(4,False)
            else:
                query = "SELECT {0},{1} from {2}"
                testCol = self.app.con.queryWithError(query.format(self.setupTextCol,self.setupClassCol,self.selectedTable))
                if testCol['errorcode'] == 1054:
                    print("Table does not contain \'{0}\' or \'{1}\' column, please select another table!".format(self.setupTextCol,self.setupClassCol))
                    print("Or change column below.")
                    self.pushButton_setup_next.setEnabled(False)
                    self.tabWidget.setTabEnabled(1,False)
                    self.tabWidget.setTabEnabled(2,False)
                    self.tabWidget.setTabEnabled(3,False)
                    # self.tabWidget.setTabEnabled(4,False)
                elif testCol['errorcode'] == 0:
                    self.pushButton_setup_next.setEnabled(True)
                    print("Column text and class confirmed.")
                else:
                    print(query.format(self.setupTextCol,self.setupClassCol,self.selectedTable))
                    print("Error in check column for table. No {0}".format(testCol['errorcode']))
                    self.pushButton_setup_next.setEnabled(False)
                    self.tabWidget.setTabEnabled(1,False)
                    self.tabWidget.setTabEnabled(2,False)
                    self.tabWidget.setTabEnabled(3,False)
                    # self.tabWidget.setTabEnabled(4,False)

    def tableTrainingCheck(self,value):
        self.selectedTable = value
        self.setupCheckTrainingTable()

    def setupHandleKeyReleaseText(self,event):
        self.setupTextCol = self.lineEdit_setup_text_col.text()
        if not self.setupTextCol:
            self.setupTextCol = self.setupTextCol_def
        QtWidgets.QLineEdit.keyReleaseEvent(self.lineEdit_setup_text_col,event)
        self.setupCheckTrainingTable()

    def setupHandleKeyReleaseClass(self,event):
        self.setupClassCol = self.lineEdit_setup_clas_col.text()
        if not self.setupClassCol:
            self.setupClassCol = self.setupClassCol_def
        QtWidgets.QLineEdit.keyReleaseEvent(self.lineEdit_setup_clas_col,event)
        self.setupCheckTrainingTable()

    def setupHandleKeyReleaseEx(self,event):
        exceptCol = self.lineEdit_setup_except_col.text()
        if re.search(r'^[a-zA-Z0-9,\_]*$',exceptCol):
            # print("check to db, before it parse to list with comma separator")
            exceptCol = exceptCol.split(",")
            self.exceptCol = list(filter(None,exceptCol)) #remove empty string in list
            if self.setupTextCol in self.exceptCol or self.setupClassCol in self.exceptCol:
                self.pushButton_setup_next.setEnabled(False)
                self.tabWidget.setTabEnabled(1,False)
                self.tabWidget.setTabEnabled(2,False)
            else:
                self.pushButton_setup_next.setEnabled(True)
            # print(self.exceptCol)
            # print(len(self.exceptCol))
        else:
            print("Character contain illegal symbol, only comma (,) allowed!")
        QtWidgets.QLineEdit.keyReleaseEvent(self.lineEdit_setup_except_col,event)

    def setupNext(self):
        self.selectedTable = str(self.comboBox_setup_table.currentText())
        if self.selectedTable:
            self.pushButton_setup_next.setEnabled(False)
            self.app.setTrainingTable(self.selectedTable)
            self.app.setTextCol(self.setupTextCol)
            self.app.setClassCol(self.setupClassCol)
            self.app.setExceptionalFeature(self.exceptCol)
            qc = QtCore.QCoreApplication
            self.app.chekForUnidenChar(qc=qc)
            self.fixWordTableRefresh(self.gridLayout_10)
            self.tabWidget.setTabEnabled(1,True)
                # self.tabWidget.setTabEnabled(2,True)
            self.tabWidget.setCurrentIndex(1)
            self.pushButton_setup_next.setEnabled(True)

# tab fixword
    def fixWordTableRefresh(self,lay):
        import sip

        lay.removeWidget(self.tableWidget_fixword)
        sip.delete(self.tableWidget_fixword)
        self.tableWidget_fixword= None

        colCount = 0
        rowCount = 0
        data = None

        if self.app.con != None:
            colCount = len(self.fixWord_cols)
            cols_q = ""
            j = 0
            for i in self.fixWord_cols:
                cols_q+=i
                j+=1
                if j < colCount:
                    cols_q+=","

            query = "SELECT {0} FROM {1}"
            data = self.app.con.query(query.format(cols_q,self.fixWord_fixtable))
            rowCount = len(data)

        self.tableWidget_fixword = QtWidgets.QTableWidget(rowCount, colCount)
        self.tableWidget_fixword.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_fixword.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        vheader = QtWidgets.QHeaderView(QtCore.Qt.Vertical)
        vheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_fixword.setVerticalHeader(vheader)
        hheader = QtWidgets.QHeaderView(QtCore.Qt.Horizontal)
        hheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_fixword.setHorizontalHeader(hheader)
        self.tableWidget_fixword.setHorizontalHeaderLabels(self.fixWord_cols)

        if data != None:
            for i in range(rowCount):
                for j in range(colCount):
                    if data[i][j]:
                        itemText = str(data[i][j])
                    else:
                        itemText = ""
                    item = QtWidgets.QTableWidgetItem(itemText)
                    self.tableWidget_fixword.setItem(i, j, item)
                    QtCore.QCoreApplication.processEvents()
                QtCore.QCoreApplication.processEvents()
        self.tableWidget_fixword.doubleClicked.connect(lambda: self.fixWordgetItem(cols_q))
        lay.addWidget(self.tableWidget_fixword)
        QtCore.QCoreApplication.processEvents()

        self.pushButton_fixword_next.setEnabled(True)
        self.tabWidget.setTabEnabled(2,True)

    def fixWordgetItem(self,cols_q):

        self.fixWord_indexData = self.tableWidget_fixword.currentRow()
        self.fixWord_idData = self.tableWidget_fixword.item(self.fixWord_indexData,0).text()

        query = "SELECT {0} FROM {1} where id={2}"
        data = self.app.con.query(query.format(cols_q,self.fixWord_fixtable,self.fixWord_idData))

        self.lineEdit_fixword_word.setText(data[0][1])
        self.lineEdit_fixword_wordfix.setText(data[0][2])

    def fixWordSave(self):
        self.pushButton_fixword_save.setEnabled(False)
        if self.fixWord_idData == 0:
            print("No data selected!")
        elif not self.lineEdit_fixword_wordfix.text():
            print("Empty!")
        else:
            print("Saving ...")
            newText = self.lineEdit_fixword_wordfix.text()
            query = "UPDATE {0} set word_fix='{1}' where id={2}"
            self.app.con.queryInsert(query.format(self.fixWord_fixtable,newText,self.fixWord_idData))
            self.tableWidget_fixword.item(self.fixWord_indexData,2).setText(newText)
            self.lineEdit_fixword_word.setText("")
            self.lineEdit_fixword_wordfix.setText("")
            self.fixWord_idData = 0
            print("Saved")
        self.pushButton_fixword_save.setEnabled(True)

    def fixWordBack(self):
        self.tabWidget.setCurrentIndex(0)

    def fixWordNext(self):
        self.tabWidget.setCurrentIndex(2)

# tab evaluation
    def evalCheckNoPre(self,enabled):
        if enabled:
            self.evaluation_doPreprocessing = False
            self.groupBox_evaluation.setEnabled(False)
            self.tabWidget.setTabEnabled(3,False)
            self.pushButton_evaluation_next.setEnabled(False)

    def evalCheckPre(self,enabled):
        if enabled:
            self.evaluation_doPreprocessing = True
            self.groupBox_evaluation.setEnabled(False)
            self.tabWidget.setTabEnabled(3,False)
            self.pushButton_evaluation_next.setEnabled(False)

    def evalCheckNoFS(self,enabled):
        if enabled:
            self.evaluation_doFeatureSelection = False
            self.lineEdit_evaluation_number_of_feature.setEnabled(False)
            self.lineEdit_evaluation_threshold_of_feature.setEnabled(False)
            self.groupBox_evaluation.setEnabled(False)
            self.tabWidget.setTabEnabled(3,False)
            self.pushButton_evaluation_next.setEnabled(False)

    def evalCheckFS(self,enabled):
        if enabled:
            self.evaluation_doFeatureSelection = True
            self.lineEdit_evaluation_number_of_feature.setEnabled(True)
            self.lineEdit_evaluation_threshold_of_feature.setEnabled(True)
            self.groupBox_evaluation.setEnabled(False)
            self.tabWidget.setTabEnabled(3,False)
            self.pushButton_evaluation_next.setEnabled(False)

    def evalCheckNB(self,enabled):
        if enabled:
            pass

    def evalStartPre(self):
        self.progressBar_evaluation_progress_pre.setValue(0)
        self.pushButton_evaluation_start_pre.setEnabled(False)
        self.pushButton_evaluation_next.setEnabled(False)
        self.pushButton_evaluation_start_kfold.setEnabled(False)

        start_time = time.time()
        qc = QtCore.QCoreApplication
        self.app.preprocessingText(self.evaluation_doPreprocessing,self.progressBar_evaluation_progress_pre,qc)
        self.tabWidget.setTabEnabled(3,True)
        self.eval_time = time.time() - start_time

        self.pushButton_evaluation_start_pre.setEnabled(True)
        self.tabWidget.setTabEnabled(3,True)
        self.groupBox_evaluation.setEnabled(True)
        self.pushButton_evaluation_next.setEnabled(True)
        self.pushButton_evaluation_start_kfold.setEnabled(True)

    def testEvalKFold(self):
        self.pushButton_evaluation_start_kfold.setEnabled(False)
        self.pushButton_evaluation_start_pre.setEnabled(False)
        self.pushButton_evaluation_next.setEnabled(False)
        folds = self.lineEdit_evaluation_folds.text()
        if not folds:
            folds = self.trainingFold_def
        folds = int(folds)

        if folds > self.app.getDataTrainingCount():
            print("Folds cannot be higher as training data count!")
        elif folds < 2:
            print("Cannot only 1 fold or less!!")
        else:
            qc = QtCore.QCoreApplication
            stat = self.label_evaluation_status
            stat.setText("Starting evaluation ...")
            logdis = self.plainTextEdit_evaluation_log
            if self.evaluation_doFeatureSelection:
                if self.lineEdit_evaluation_number_of_feature.text():
                    self.evaluation_numFeatureToRetain = int(self.lineEdit_evaluation_number_of_feature.text())
                else:
                    self.evaluation_numFeatureToRetain = 0
                if self.lineEdit_evaluation_threshold_of_feature.text():
                    self.evaluation_thresholdFeatureIgnore = float(self.lineEdit_evaluation_threshold_of_feature.text())
                else:
                    self.evaluation_thresholdFeatureIgnore = 0

            eval = self.app.evalKFoldCV(self.app.getDataTrainingCount(),folds,self.evaluation_doFeatureSelection,self.evaluation_numFeatureToRetain,self.evaluation_thresholdFeatureIgnore,qc=qc,stat=stat,logdis=logdis)
            if eval is not False:
                self.label_evaluation_accuration.setText(str(eval['accuration']))
                self.label_evaluation_precision.setText(str(eval['precision']))
                self.label_evaluation_recall.setText(str(eval['recall']))
            stat.setText("Evaluation complete.")
        self.pushButton_evaluation_start_kfold.setEnabled(True)
        self.pushButton_evaluation_start_pre.setEnabled(True)
        self.pushButton_evaluation_next.setEnabled(True)

    def evalBack(self):
        self.tabWidget.setCurrentIndex(1)

    def evalNext(self):
        self.tabWidget.setCurrentIndex(3)

#tab training
    def trainingData(self):
        self.pushButton_training.setEnabled(False)
        qc = QtCore.QCoreApplication

        if self.evaluation_doFeatureSelection:
            if self.lineEdit_evaluation_number_of_feature.text():
                self.evaluation_numFeatureToRetain = self.lineEdit_evaluation_number_of_feature.text()
            else:
                self.evaluation_numFeatureToRetain = 0

            if self.lineEdit_evaluation_threshold_of_feature.text():
                self.evaluation_thresholdFeatureIgnore = self.lineEdit_evaluation_threshold_of_feature.text()
            else:
                self.evaluation_thresholdFeatureIgnore = 0
        label = self.label_training_status
        start_time = time.time()
        features = self.app.preprocessing(self.evaluation_doPreprocessing,self.evaluation_doFeatureSelection,self.evaluation_numFeatureToRetain,self.evaluation_thresholdFeatureIgnore,self.progressBar_evaluation_progress_pre,qc,label=label)
        self.preprocessing_time = (time.time() - start_time)
        self.vsm = features['vsm']
        self.label_training_status.setText("Building table ... Please wait ...")
        self.trainingFeatureTable(self.gridLayout_18,features)

        if self.vsmFeature is not None:
            start_time = time.time()
            self.label_training_status.setText("Training data ... Please wait ...")
            qc = QtCore.QCoreApplication
            qc.processEvents()
            self.model = self.app.trainingClassificator(self.vsmFeature,qc=qc)
            if self.model is not None:
                featureprocessed = self.label_training_feature.text()
                clas = self.model['clas']
                totalclas = str(len(clas))
                dataTrainingPr = self.app.getDataTrainingProperty(clas)
                self.training_total_data = dataTrainingPr['totaltrainingdata']
                totaldata = str(self.training_total_data)
                totaldataperc = dataTrainingPr['totaltrainingdataperclas']
                timeprocess = self.preprocessing_time
                # akumulasi dr preprocessing
                timeprocess = (time.time() - start_time) + timeprocess
                # timeprocess = str(timeprocess)
                self.label_training_total_class.setText(totalclas)
                self.label_training_total_data.setText(totaldata+" -> ")
                self.label_training_data_perclass.setText(totaldataperc)
                self.label_training_total_feature.setText(featureprocessed)
                self.label_training_time.setText(format(timeprocess,'.2f'))

                self.groupBox_training_eval.setEnabled(True)
                self.label_training_status.setText("Training complete.")
            else:
                self.groupBox_training_eval.setEnabled(False)
        else:
            print("No training data loaded!")
        self.pushButton_training.setEnabled(True)

    def trainingFeatureTable(self,lay,features):
        import sip

        lay.removeWidget(self.tableWidget_training_features)
        sip.delete(self.tableWidget_training_features)
        self.tableWidget_training_features= None

        lay.removeWidget(self.tableWidget_training_vsm)
        sip.delete(self.tableWidget_training_vsm)
        self.tableWidget_training_vsm= None

        colCount = 0
        rowCount = 0
        data = None
        cols = []

        vms_colCount = 0
        vms_rowCount = 0
        vms_data = None
        vms_cols = []

        if features != None:
            feature = features['vsm']['feature']
            vsm = features['vsm']['vsm']

            cols.append("original")
            cols_temp = [i for i in feature]
            cols.extend(cols_temp)
            colCount = len(cols)
            rowCount = len(feature.index)

            vms_cols = [i for i in vsm]
            vms_colCount = len(vms_cols)
            vms_rowCount = len(vsm.index)

            totalFeatureBefore = features['featurebefore']
            totalFeatureAfter = rowCount
            reduction = 0
            if totalFeatureBefore != 0:
                reduction = totalFeatureAfter/totalFeatureBefore*100
                reduction = round(100-reduction)
            # self.label_training_feature_before.setText("Creating table ... Please wait ...")

        #for table feature
        self.tableWidget_training_features = QtWidgets.QTableWidget(rowCount, colCount)
        self.tableWidget_training_features.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_training_features.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        vheader = QtWidgets.QHeaderView(QtCore.Qt.Vertical)
        vheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_training_features.setVerticalHeader(vheader)
        hheader = QtWidgets.QHeaderView(QtCore.Qt.Horizontal)
        hheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_training_features.setHorizontalHeader(hheader)

        self.tableWidget_training_features.setHorizontalHeaderLabels(cols) # !

        #for table VSM
        self.tableWidget_training_vsm = QtWidgets.QTableWidget(vms_rowCount, vms_colCount)
        self.tableWidget_training_vsm.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_training_vsm.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        vms_vheader = QtWidgets.QHeaderView(QtCore.Qt.Vertical)
        vheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_training_vsm.setVerticalHeader(vms_vheader)
        vms_hheader = QtWidgets.QHeaderView(QtCore.Qt.Horizontal)
        hheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_training_vsm.setHorizontalHeader(vms_hheader)

        self.tableWidget_training_vsm.setHorizontalHeaderLabels(vms_cols) # !


        if features != None:
            feature = features['vsm']['feature']
            oritext = features['oritext']
            vsm = features['vsm']['vsm']

            cols = [i for i in feature]

            for index,row in feature.iterrows():
                jj = 0
                item = QtWidgets.QTableWidgetItem(oritext[row[cols[0]]])
                self.tableWidget_training_features.setItem(index, jj, item)
                jj+=1
                for j in cols:
                    feat = row[j]
                    if not feat:
                        feat = ""
                    item = QtWidgets.QTableWidgetItem(str(feat))
                    self.tableWidget_training_features.setItem(index, jj, item)
                    jj+=1
                    QtCore.QCoreApplication.processEvents()
                QtCore.QCoreApplication.processEvents()

            for index,row in vsm.iterrows():
                jj = 0
                for j in vms_cols:
                    feat = row[j]
                    item = QtWidgets.QTableWidgetItem(str(feat))
                    self.tableWidget_training_vsm.setItem(index, jj, item)
                    jj+=1
                    QtCore.QCoreApplication.processEvents()
                QtCore.QCoreApplication.processEvents()

            # for button next, to process in training data
            self.label_training_feature_before.setText(str(totalFeatureBefore))
            self.label_training_feature.setText(str(totalFeatureAfter))
            self.label_training_reduction.setText(str(reduction))
            if len(vsm.index) > 0:
                self.vsmFeature = features
            else:
                print("VSM has no data!")
                self.pushButton_training_analys.setEnabled(False)
                self.tabWidget.setTabEnabled(4,False)
        else:
            self.pushButton_training_analys.setEnabled(False)
            self.tabWidget.setTabEnabled(4,False)

        lay.addWidget(self.tableWidget_training_features, 1, 0, 1, 1)
        lay.addWidget(self.tableWidget_training_vsm, 1, 1, 1, 3)

    def trainingTestSentence(self):
        self.pushButton_training_test_sentence.setEnabled(False)
        sentence = self.lineEdit_training_sentence.text()
        if sentence and self.model is not None:
            # c = self.app.classificator.classifyWithModel(self.model,sentence)
            c = self.app.evalSentence(self.model,sentence)
            self.label_training_result_test_sentence.setText("Result class : {0}".format(str(c)))
        else:
            print("No sentence or no model found!")
        self.pushButton_training_test_sentence.setEnabled(True)

    def trainingBack(self):
        self.tabWidget.setCurrentIndex(2)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
