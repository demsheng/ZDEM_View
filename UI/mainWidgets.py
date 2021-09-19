# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWidgets.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
from PyQt5 import QtGui

import imageio
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, QFile, pyqtSignal, QBuffer, QByteArray
from PyQt5.QtGui import QMovie


class Ui_mainWidgets(object):
    """
    工作绘图区类
    """

    def __init__(self, parent=None, myUi=None):
        self.parent = parent
        self.myUi = myUi
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.parent)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0,0,0,0)
        # self.mainWidgets_vlayout = QtWidgets.QVBoxLayout(self.parent)
        # self.mainWidgets_vlayout.setObjectName("mainWidgets_vlayout")
        # 文件选择区
        self.select_horizontalLayout = QtWidgets.QHBoxLayout()
        self.select_horizontalLayout.setObjectName("select_horizontalLayout")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        #font.setWeight(50)
        self.label = QtWidgets.QLabel(self.parent)
        self.label.setObjectName("label")
        self.label.setText('选择文件')
        self.label.setFont(font)
        self.select_horizontalLayout.addWidget(self.label)
        self.select_comBox = QtWidgets.QComboBox(self.parent)
        self.select_comBox.setObjectName("comboBox")
        self.select_comBox.setMinimumWidth(200)
        self.select_comBox.currentIndexChanged.connect(self.selectionChange)
        self.select_horizontalLayout.addWidget(self.select_comBox)
        self.select_horizontalLayout.setContentsMargins(1,1,1,1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.select_horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.select_horizontalLayout)
        # 绘图区
        self.canvas_verticalLayout = QtWidgets.QVBoxLayout()
        self.canvas_verticalLayout.setObjectName("canvas_verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.parent)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        # self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        
        # self.tabWidget.setUpdatesEnabled(True)
        self.tabWidget.setTabsClosable(True)  # 设置tab页可关闭
        self.tabWidget.tabCloseRequested.connect(self.closeTab)  # 为tab关闭动作连接函数
        self.canvas_verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.canvas_verticalLayout)
        QtCore.QMetaObject.connectSlotsByName(self.parent)

    def retranslateUi(self, mainWidgets):
        _translate = QtCore.QCoreApplication.translate
        mainWidgets.setWindowTitle(_translate("mainWidgets", "Form"))

    def nextPage(self):
        nowIndex = self.tabWidget.currentIndex()
        self.tabWidget.setCurrentIndex(nowIndex + 1)
        print("当前为第" + str(nowIndex) + "页")

    def previousPage(self):
        nowIndex = self.tabWidget.currentIndex()
        self.tabWidget.setCurrentIndex(nowIndex - 1)
        print("当前为第" + str(nowIndex) + "页")

    def selectionChange(self):
        nowIndex = self.select_comBox.currentIndex()
        self.tabWidget.setCurrentIndex(nowIndex)

    def compose_gif_2(self):
        gifThread = gif_thread(self)
        gifThread.gifData_signal.connect(self.playGif)
        gifThread.start()

    def compose_gif(self):
        # XXX:生成gif前先检查是否保存了图片
        jpgPath_List = []
        jpgList = os.listdir("./temp save files")
        for jpgName in jpgList:
            absolutePath = os.path.join("./temp save files/", jpgName)
            jpgPath_List.append(absolutePath)
        gif_images = []
        for path in jpgPath_List:
            gif_images.append(imageio.imread(path))
        imageio.mimsave("./temp save files/test.gif", gif_images, fps=2)
        self.gif = QMovie('./temp save files/test.gif')
        # tabwidget增加一页
        gif_tab = QtWidgets.QWidget()
        gif_tab.setObjectName('gif_tab')
        self.tabWidget.addTab(gif_tab, 'GIF')
        scrollArea_layout = QtWidgets.QVBoxLayout(gif_tab)
        scrollArea_layout.setObjectName('scrollArea_layout')
        gifTab_scrollArea = QtWidgets.QScrollArea(gif_tab)
        scrollArea_layout.addWidget(gifTab_scrollArea)
        gif_verticalLAYOUT = QtWidgets.QVBoxLayout(gifTab_scrollArea)
        gif_verticalLAYOUT.setObjectName('gif_verticalLAYOUT')
        self.gifLabel = QtWidgets.QLabel(gifTab_scrollArea)
        self.gifLabel.setObjectName('gifLabel')
        gif_verticalLAYOUT.addWidget(self.gifLabel)
        self.tabWidget.setCurrentWidget(gif_tab)  # 设置当前页为gif播放tab
        self.gifLabel.setMovie(self.gif)
        self.gif.start()
        self.gifLabel.show()

    def play_gif(self, gif_data):
        self.buffer = QBuffer()
        self.buffer.setData(gif_data)
        self.newGif = QMovie()
        self.newGif.setCacheMode(self.newGif.CacheAll)
        self.newGif.setDevice(self.buffer)
        self.gifLabel.setMovie(self.newGif)
        self.newGif.start()
        self.gifLabel.show()

    def pauseGif(self):
        self.gif.setPaused(True)

    def playGif(self):
        self.gif.setPaused(False)

    def closeTab(self, currentIndex):
        currentQWidget = self.tabWidget.widget(currentIndex)
        currentQWidget.deleteLater()
        self.tabWidget.removeTab(currentIndex)


class gif_thread(QThread):
    """
    gif线程类
    """
    gifData_signal = pyqtSignal(QByteArray)

    def __init__(self, mainWidgetObj):
        super(gif_thread, self).__init__()
        self.mainWidgetObj = mainWidgetObj

    def run(self):
        jpgPath_List = []
        jpgList = os.listdir(".\\temp save files")
        for jpgName in jpgList:
            absolutePath = os.path.join("/temp save files\\", jpgName)
            jpgPath_List.append(absolutePath)
        gif_images = []
        for path in jpgPath_List:
            gif_images.append(imageio.imread(path))
        imageio.mimsave("./temp save files/test.gif", gif_images, fps=2)
        f = QFile("./temp save files/test.gif")
        f.open(f.ReadOnly)
        self.gifData_signal.emit(f.readAll())
        f.close()
        # self.gif = QMovie('./temp save files/test.gif')
        # self.mainWidgetObj.gifLabel.setMovie(self.gif)
        # self.gif.start()
        # self.mainWidgetObj.gifLabel.show()
