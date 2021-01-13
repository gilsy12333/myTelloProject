# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestureUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gestureUI(object):
    def setupUi(self, gestureUI):
        gestureUI.setObjectName("gestureUI")
        gestureUI.resize(674, 664)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(gestureUI.sizePolicy().hasHeightForWidth())
        gestureUI.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(gestureUI)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_PC_Cam_frame_show = QtWidgets.QLabel(gestureUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_PC_Cam_frame_show.sizePolicy().hasHeightForWidth())
        self.label_PC_Cam_frame_show.setSizePolicy(sizePolicy)
        self.label_PC_Cam_frame_show.setMinimumSize(QtCore.QSize(200, 200))
        self.label_PC_Cam_frame_show.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.label_PC_Cam_frame_show.setText("")
        self.label_PC_Cam_frame_show.setObjectName("label_PC_Cam_frame_show")
        self.gridLayout.addWidget(self.label_PC_Cam_frame_show, 0, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(gestureUI)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.label_is_ready = QtWidgets.QLabel(gestureUI)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        self.label_is_ready.setFont(font)
        self.label_is_ready.setObjectName("label_is_ready")
        self.gridLayout.addWidget(self.label_is_ready, 1, 1, 1, 1)
        self.textBrowser_order_already_sent = QtWidgets.QTextBrowser(gestureUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_order_already_sent.sizePolicy().hasHeightForWidth())
        self.textBrowser_order_already_sent.setSizePolicy(sizePolicy)
        self.textBrowser_order_already_sent.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        self.textBrowser_order_already_sent.setFont(font)
        self.textBrowser_order_already_sent.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_order_already_sent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser_order_already_sent.setObjectName("textBrowser_order_already_sent")
        self.gridLayout.addWidget(self.textBrowser_order_already_sent, 3, 0, 1, 2)
        self.frame = QtWidgets.QFrame(gestureUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_start_and_close = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        self.pushButton_start_and_close.setFont(font)
        self.pushButton_start_and_close.setObjectName("pushButton_start_and_close")
        self.horizontalLayout_2.addWidget(self.pushButton_start_and_close)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.dockWidget_HintHelp = QtWidgets.QDockWidget(gestureUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_HintHelp.sizePolicy().hasHeightForWidth())
        self.dockWidget_HintHelp.setSizePolicy(sizePolicy)
        self.dockWidget_HintHelp.setMinimumSize(QtCore.QSize(174, 300))
        self.dockWidget_HintHelp.setMaximumSize(QtCore.QSize(524287, 524287))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        self.dockWidget_HintHelp.setFont(font)
        self.dockWidget_HintHelp.setFloating(True)
        self.dockWidget_HintHelp.setObjectName("dockWidget_HintHelp")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background-color: Transparent;")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.dockWidget_HintHelp.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.dockWidget_HintHelp)

        self.retranslateUi(gestureUI)
        QtCore.QMetaObject.connectSlotsByName(gestureUI)

    def retranslateUi(self, gestureUI):
        _translate = QtCore.QCoreApplication.translate
        gestureUI.setWindowTitle(_translate("gestureUI", "手势控制窗口"))
        self.label_is_ready.setText(_translate("gestureUI", "就绪"))
        self.textBrowser_order_already_sent.setPlaceholderText(_translate("gestureUI", ">>"))
        self.pushButton_start_and_close.setText(_translate("gestureUI", "开始手势控制"))
        self.dockWidget_HintHelp.setWindowTitle(_translate("gestureUI", "帮助"))
        self.textBrowser_2.setHtml(_translate("gestureUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Heiti SC\',\'Heiti SC\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\'; font-weight:400;\">支持的手势如下：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\'; font-weight:400;\">双手合十：启动；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\'; font-weight:400;\">大拇指向上：起飞；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\'; font-weight:400;\">大拇指向下：降落；</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Heiti SC\'; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\'; font-weight:400;\">一/二/三/四/五/六个手指：向上/下/左/右/前/后飞20厘米；</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Heiti SC\'; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\'; font-weight:400;\">七/八个手指：顺/逆时针旋转90度；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Heiti SC\'; font-weight:400;\">九个手指：悬停；</span></p></body></html>"))