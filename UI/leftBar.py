

import os
from matplotlib.ticker import FuncFormatter, MultipleLocator

from model.Thread import PlotThread
import numpy as np

from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt


class leftBar():
    toolsBox_page_style = ("QWidget {"
                            "background-color: #ebf5ff;"
                            "}")


    def __init__(self,leftFrame,myUi):
        self.leftFrame = leftFrame
        self.myUi = myUi
        self.leftFrame.setMaximumWidth(350)
        self.leftFrame_HLayout = QtWidgets.QHBoxLayout(self.leftFrame)
        self.leftFrame_HLayout.setSpacing(0)  
        self.leftFrame_HLayout.setContentsMargins(0,0,0,0) 
        self.leftFrame_HLayout.setAlignment(QtCore.Qt.AlignCenter)     
        self.left_list_widget = QtWidgets.QListWidget(self.leftFrame)
        self.left_stacked_widget = QtWidgets.QStackedWidget(self.leftFrame)
        self.left_stacked_widget.setContentsMargins(0,0,0,0)
        self.leftFrame_HLayout.addWidget(self.left_list_widget)
        self.leftFrame_HLayout.addWidget(self.left_stacked_widget)
        QtCore.QMetaObject.connectSlotsByName(self.leftFrame)
        # init 
        self.init_list_widget()
        self.init_dataView()
        self.init_dataLog()
        self.init_paramWidgets()
        self.init_export()
        self.retranslateUi()
        #
        self.left_list_widget.setCurrentRow(0)






    def init_list_widget(self):
        self.left_list_widget.setFrameShape(QtWidgets.QListWidget.NoFrame) # 去除边框
        self.left_list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 隐藏滚动条
        self.left_list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # 字体
        font_1 = QtGui.QFont()
        font_1.setFamily("黑体")
        font_1.setPointSize(12)
        font_1.setBold(False)
        self.left_list_widget.setFont(font_1)
        #
        dataView_icon = QtGui.QIcon()
        dataView_icon.addPixmap(QtGui.QPixmap("./icons/dataView.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dataView_item = QtWidgets.QListWidgetItem(dataView_icon,'文件管理',self.left_list_widget)
        self.dataView_item.setSizeHint(QSize(30,60))
        self.dataView_item.setTextAlignment(QtCore.Qt.AlignCenter)
        #
        dataLog_icon = QtGui.QIcon()
        dataLog_icon.addPixmap(QtGui.QPixmap("./icons/dataLog.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dataLog_item = QtWidgets.QListWidgetItem(dataLog_icon,'数据信息',self.left_list_widget)
        self.dataLog_item.setSizeHint(QSize(30,60))
        self.dataLog_item.setTextAlignment(QtCore.Qt.AlignCenter)
        #
        param_icon = QtGui.QIcon()
        param_icon.addPixmap(QtGui.QPixmap("./icons/figureParam.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.param_item = QtWidgets.QListWidgetItem(param_icon,'图像参数',self.left_list_widget)
        self.param_item.setSizeHint(QSize(30,60))
        self.param_item.setTextAlignment(QtCore.Qt.AlignCenter)
        #
        export_icon = QtGui.QIcon()
        export_icon.addPixmap(QtGui.QPixmap("./icons/save.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_item = QtWidgets.QListWidgetItem(export_icon,'导出',self.left_list_widget)
        self.export_item.setSizeHint(QSize(30,60))
        self.export_item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.export_item.whatsThis()
        # 添加点击事件
        self.left_list_widget.itemClicked.connect(self.item_clicked)

    def init_dataView(self):

        self.left_stacked_widget.addWidget(self.myUi.dataViewFrame)
        self.left_stacked_widget.setMaximumWidth(230)

    def init_dataLog(self):
        self.export_frame = QtWidgets.QFrame()
        self.export_frame.setMaximumWidth(230)
        self.export_frame.setMinimumWidth(230)
        self.export_frame.setObjectName("export_frame")
        self.dataLog_verticalLayout = QtWidgets.QVBoxLayout(self.export_frame)
        self.dataLog_verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.dataLog_verticalLayout.setObjectName("dataLog_verticalLayout")
        self.label_dataText = QtWidgets.QLabel(self.export_frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_dataText.setFont(font)
        self.label_dataText.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dataText.setObjectName("label_dataText")
        self.dataLog_verticalLayout.addWidget(self.label_dataText)
        self.textBrowser_data = QtWidgets.QTextBrowser(self.export_frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_data.setFont(font)
        self.textBrowser_data.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_data.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser_data.setObjectName("textBrowser_data")
        self.dataLog_verticalLayout.addWidget(self.textBrowser_data)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dataLog_verticalLayout.addItem(spacerItem)
        # 添加
        self.left_stacked_widget.addWidget(self.export_frame)

    def init_paramWidgets(self):
        self.param_widget = QtWidgets.QWidget()
        self.param_widget.setObjectName("param_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.param_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(1,1,1,1)
        self.label_paramTitle = QtWidgets.QLabel(self.param_widget)
        self.label_paramTitle.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_paramTitle.setFont(font)
        self.label_paramTitle.setObjectName("label_paramTitle")
        self.verticalLayout.addWidget(self.label_paramTitle)
        self.toolBox_figureParam = QtWidgets.QToolBox(self.param_widget)
        self.toolBox_figureParam.setFont(font)
        # self.toolBox_figureParam.setMaximumWidth(480)
        self.toolBox_figureParam.setToolTip("")
        self.toolBox_figureParam.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBox_figureParam.setObjectName("toolBox_figureParam")
        self.tools_move = QtWidgets.QWidget()
        self.tools_move.setStyleSheet(self.toolsBox_page_style)
        # self.tools_move.setGeometry(QtCore.QRect(0, 0, 301, 372))
        self.tools_move.setToolTip("")
        self.tools_move.setWhatsThis("")
        self.tools_move.setAccessibleDescription("")
        self.tools_move.setAutoFillBackground(True)
        self.tools_move.setObjectName("tools_move")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tools_move)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_xmove = QtWidgets.QLineEdit(self.tools_move)
        self.lineEdit_xmove.setObjectName("lineEdit_xmove")
        # self.lineEdit_xmove.setText()
        self.gridLayout_5.addWidget(self.lineEdit_xmove, 0, 1, 1, 1)
        self.label_ymove = QtWidgets.QLabel(self.tools_move)
        self.label_ymove.setObjectName("label_ymove")
        self.gridLayout_5.addWidget(self.label_ymove, 1, 0, 1, 1)
        self.label_xmove = QtWidgets.QLabel(self.tools_move)
        self.label_xmove.setToolTip("")
        self.label_xmove.setObjectName("label_xmove")
        self.gridLayout_5.addWidget(self.label_xmove, 0, 0, 1, 1)
        self.lineEdit_ymove = QtWidgets.QLineEdit(self.tools_move)
        self.lineEdit_ymove.setObjectName("lineEdit_ymove")
        self.gridLayout_5.addWidget(self.lineEdit_ymove, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 2, 1, 1, 1)
        self.toolBox_figureParam.addItem(self.tools_move, "")
        self.page_axisRange = QtWidgets.QWidget()
        self.page_axisRange.setObjectName("page_axisRange")
        self.page_axisRange.setStyleSheet(self.toolsBox_page_style)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_axisRange)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.yminLabel = QtWidgets.QLabel(self.page_axisRange)
        self.yminLabel.setObjectName("yminLabel")
        self.gridLayout_3.addWidget(self.yminLabel, 2, 0, 1, 1)
        self.xmax_lineEdit = QtWidgets.QLineEdit(self.page_axisRange)
        self.xmax_lineEdit.setObjectName("xmax_lineEdit")
        self.gridLayout_3.addWidget(self.xmax_lineEdit, 1, 1, 1, 1)
        self.xmaxLabel = QtWidgets.QLabel(self.page_axisRange)
        self.xmaxLabel.setObjectName("xmaxLabel")
        self.gridLayout_3.addWidget(self.xmaxLabel, 1, 0, 1, 1)
        self.xminLabel = QtWidgets.QLabel(self.page_axisRange)
        self.xminLabel.setObjectName("xminLabel")
        self.gridLayout_3.addWidget(self.xminLabel, 0, 0, 1, 1)
        self.xmin_lineEdit = QtWidgets.QLineEdit(self.page_axisRange)
        self.xmin_lineEdit.setObjectName("xmin_lineEdit")
        self.gridLayout_3.addWidget(self.xmin_lineEdit, 0, 1, 1, 1)
        self.ymaxLabel = QtWidgets.QLabel(self.page_axisRange)
        self.ymaxLabel.setObjectName("ymaxLabel")
        self.gridLayout_3.addWidget(self.ymaxLabel, 3, 0, 1, 1)
        self.ymin_lineEdit = QtWidgets.QLineEdit(self.page_axisRange)
        self.ymin_lineEdit.setObjectName("ymin_lineEdit")
        self.gridLayout_3.addWidget(self.ymin_lineEdit, 2, 1, 1, 1)
        self.ymax_lineEdit = QtWidgets.QLineEdit(self.page_axisRange)
        self.ymax_lineEdit.setObjectName("ymax_lineEdit")
        self.gridLayout_3.addWidget(self.ymax_lineEdit, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 4, 0, 1, 1)
        self.toolBox_figureParam.addItem(self.page_axisRange, "")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.page.setStyleSheet(self.toolsBox_page_style)
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.Button_plotPoint = QtWidgets.QRadioButton(self.page)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/plotPoint.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_plotPoint.setIcon(icon1)
        self.Button_plotPoint.setObjectName("Button_plotPoint")
        self.gridLayout_10.addWidget(self.Button_plotPoint, 1, 0, 1, 1)
        self.Button_plotCircle = QtWidgets.QRadioButton(self.page)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/plot.ico"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_plotCircle.setIcon(icon2)
        self.Button_plotCircle.setObjectName("Button_plotCircle")
        self.gridLayout_10.addWidget(self.Button_plotCircle, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem3, 2, 0, 1, 1)
        self.toolBox_figureParam.addItem(self.page, "")
        self.tools_plotWall = QtWidgets.QWidget()
        self.tools_plotWall.setGeometry(QtCore.QRect(0, 0, 301, 372))
        self.tools_plotWall.setObjectName("tools_plotWall")
        self.tools_plotWall.setStyleSheet(self.toolsBox_page_style)
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tools_plotWall)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.SpinBox_lineSize = QtWidgets.QDoubleSpinBox(self.tools_plotWall)
        self.SpinBox_lineSize.setFrame(True)
        self.SpinBox_lineSize.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SpinBox_lineSize.setSingleStep(0.1)
        self.SpinBox_lineSize.setProperty("value", 0.8)
        self.SpinBox_lineSize.setObjectName("SpinBox_lineSize")
        self.gridLayout_9.addWidget(self.SpinBox_lineSize, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem4, 5, 1, 1, 1)
        self.label_lineSize = QtWidgets.QLabel(self.tools_plotWall)
        self.label_lineSize.setObjectName("label_lineSize")
        self.gridLayout_9.addWidget(self.label_lineSize, 1, 0, 1, 1)
        self.checkBox_plotWall = QtWidgets.QCheckBox(self.tools_plotWall)
        self.checkBox_plotWall.setMaximumSize(QtCore.QSize(100, 16777215))
        self.checkBox_plotWall.setChecked(True)
        self.checkBox_plotWall.setObjectName("checkBox_plotWall")
        self.gridLayout_9.addWidget(self.checkBox_plotWall, 0, 0, 1, 1)
        self.toolBox_figureParam.addItem(self.tools_plotWall, "")
        self.page_color = QtWidgets.QWidget()
        self.page_color.setStyleSheet(self.toolsBox_page_style)
        self.page_color.setGeometry(QtCore.QRect(0, 0, 301, 372))
        self.page_color.setObjectName("page_color")
        self.gridLayout = QtWidgets.QGridLayout(self.page_color)
        self.gridLayout.setObjectName("gridLayout")
        self.label_color = QtWidgets.QLabel(self.page_color)
        self.label_color.setObjectName("label_color")
        self.gridLayout.addWidget(self.label_color, 0, 0, 1, 1)
        self.comboBox_color = QtWidgets.QComboBox(self.page_color)
        self.comboBox_color.setObjectName("comboBox_color")
        self.comboBox_color.addItem("")
        self.gridLayout.addWidget(self.comboBox_color, 0, 1, 1, 1)
        self.Button_importColor = QtWidgets.QPushButton(self.page_color)
        self.Button_importColor.setObjectName("Button_importColor")
        self.gridLayout.addWidget(self.Button_importColor, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        self.toolBox_figureParam.addItem(self.page_color, "")
        self.page_figureTitle = QtWidgets.QWidget()
        self.page_figureTitle.setStyleSheet(self.toolsBox_page_style)
        self.page_figureTitle.setObjectName("page_figureTitle")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_figureTitle)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_title = QtWidgets.QLineEdit(self.page_figureTitle)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.gridLayout_2.addWidget(self.lineEdit_title, 0, 1, 1, 1)
        self.fontComboBox_titleFont = QtWidgets.QFontComboBox(
            self.page_figureTitle)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fontComboBox_titleFont.sizePolicy().hasHeightForWidth())
        self.fontComboBox_titleFont.setSizePolicy(sizePolicy)
        self.fontComboBox_titleFont.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fontComboBox_titleFont.setObjectName("fontComboBox_titleFont")
        self.gridLayout_2.addWidget(self.fontComboBox_titleFont, 1, 1, 1, 1)
        self.label_titleFont = QtWidgets.QLabel(self.page_figureTitle)
        self.label_titleFont.setObjectName("label_titleFont")
        self.gridLayout_2.addWidget(self.label_titleFont, 1, 0, 1, 1)
        self.label_titleFontSize = QtWidgets.QLabel(self.page_figureTitle)
        self.label_titleFontSize.setObjectName("label_titleFontSize")
        self.gridLayout_2.addWidget(self.label_titleFontSize, 2, 0, 1, 1)
        self.label_title = QtWidgets.QLabel(self.page_figureTitle)
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 0, 0, 1, 1)
        self.spinBox_title = QtWidgets.QSpinBox(self.page_figureTitle)
        self.spinBox_title.setPrefix("")
        self.spinBox_title.setSingleStep(1)
        self.spinBox_title.setProperty("value", 12)
        self.spinBox_title.setObjectName("spinBox_title")
        self.gridLayout_2.addWidget(self.spinBox_title, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 3, 1, 1, 1)
        self.toolBox_figureParam.addItem(self.page_figureTitle, "")
        self.page_axisTick = QtWidgets.QWidget()
        self.page_axisTick.setStyleSheet(self.toolsBox_page_style)
        self.page_axisTick.setObjectName("page_axisTick")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_axisTick)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_yName = QtWidgets.QLabel(self.page_axisTick)
        self.label_yName.setObjectName("label_yName")
        self.gridLayout_6.addWidget(self.label_yName, 4, 0, 1, 1)
        self.spinBox_xTickSize = QtWidgets.QSpinBox(self.page_axisTick)
        self.spinBox_xTickSize.setPrefix("")
        self.spinBox_xTickSize.setSingleStep(1)
        self.spinBox_xTickSize.setProperty("value", 9)
        self.spinBox_xTickSize.setObjectName("spinBox_xTickSize")
        self.gridLayout_6.addWidget(self.spinBox_xTickSize, 2, 1, 1, 1)
        self.label_xName = QtWidgets.QLabel(self.page_axisTick)
        self.label_xName.setObjectName("label_xName")
        self.gridLayout_6.addWidget(self.label_xName, 0, 0, 1, 1)
        self.label_xTickFont = QtWidgets.QLabel(self.page_axisTick)
        self.label_xTickFont.setObjectName("label_xTickFont")
        self.gridLayout_6.addWidget(self.label_xTickFont, 1, 0, 1, 1)
        self.label_yTickSize = QtWidgets.QLabel(self.page_axisTick)
        self.label_yTickSize.setObjectName("label_yTickSize")
        self.gridLayout_6.addWidget(self.label_yTickSize, 6, 0, 1, 1)
        self.label_yTickFont = QtWidgets.QLabel(self.page_axisTick)
        self.label_yTickFont.setObjectName("label_yTickFont")
        self.gridLayout_6.addWidget(self.label_yTickFont, 5, 0, 1, 1)
        self.label_minorTickInterval = QtWidgets.QLabel(self.page_axisTick)
        self.label_minorTickInterval.setObjectName("label_minorTickInterval")
        self.gridLayout_6.addWidget(self.label_minorTickInterval, 10, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.page_axisTick)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_6.addWidget(self.line_2, 7, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.page_axisTick)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_6.addWidget(self.line, 3, 0, 1, 2)
        self.lineEdit_xName = QtWidgets.QLineEdit(self.page_axisTick)
        self.lineEdit_xName.setObjectName("lineEdit_xName")
        self.gridLayout_6.addWidget(self.lineEdit_xName, 0, 1, 1, 1)
        self.label_mainTickInterval = QtWidgets.QLabel(self.page_axisTick)
        self.label_mainTickInterval.setObjectName("label_mainTickInterval")
        self.gridLayout_6.addWidget(self.label_mainTickInterval, 8, 0, 1, 2)
        self.lineEdit_yName = QtWidgets.QLineEdit(self.page_axisTick)
        self.lineEdit_yName.setObjectName("lineEdit_yName")
        self.gridLayout_6.addWidget(self.lineEdit_yName, 4, 1, 1, 1)
        self.label_xTickSzie = QtWidgets.QLabel(self.page_axisTick)
        self.label_xTickSzie.setObjectName("label_xTickSzie")
        self.gridLayout_6.addWidget(self.label_xTickSzie, 2, 0, 1, 1)
        self.spinBox_yTickSize = QtWidgets.QSpinBox(self.page_axisTick)
        self.spinBox_yTickSize.setPrefix("")
        self.spinBox_yTickSize.setSingleStep(1)
        self.spinBox_yTickSize.setProperty("value", 9)
        self.spinBox_yTickSize.setObjectName("spinBox_yTickSize")
        self.gridLayout_6.addWidget(self.spinBox_yTickSize, 6, 1, 1, 1)
        self.fontComboBox_yTick = QtWidgets.QFontComboBox(self.page_axisTick)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fontComboBox_yTick.sizePolicy().hasHeightForWidth())
        self.fontComboBox_yTick.setSizePolicy(sizePolicy)
        self.fontComboBox_yTick.setMaximumSize(QtCore.QSize(220, 16777215))
        self.fontComboBox_yTick.setObjectName("fontComboBox_yTick")
        self.gridLayout_6.addWidget(self.fontComboBox_yTick, 5, 1, 1, 1)
        self.fontComboBox_xTick = QtWidgets.QFontComboBox(self.page_axisTick)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fontComboBox_xTick.sizePolicy().hasHeightForWidth())
        self.fontComboBox_xTick.setSizePolicy(sizePolicy)
        self.fontComboBox_xTick.setMaximumSize(QtCore.QSize(220, 16777215))
        self.fontComboBox_xTick.setObjectName("fontComboBox_xTick")
        self.gridLayout_6.addWidget(self.fontComboBox_xTick, 1, 1, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem7, 12, 0, 1, 1)
        self.lineEdit_mainTickInterval = QtWidgets.QLineEdit(
            self.page_axisTick)
        self.lineEdit_mainTickInterval.setMaximumSize(
            QtCore.QSize(200, 16777215))
        self.lineEdit_mainTickInterval.setObjectName(
            "lineEdit_mainTickInterval")
        self.gridLayout_6.addWidget(self.lineEdit_mainTickInterval, 9, 0, 1, 2)
        self.lineEdit_minorTickInterval = QtWidgets.QLineEdit(
            self.page_axisTick)
        self.lineEdit_minorTickInterval.setMaximumSize(
            QtCore.QSize(200, 16777215))
        self.lineEdit_minorTickInterval.setObjectName(
            "lineEdit_minorTickInterval")
        self.gridLayout_6.addWidget(
            self.lineEdit_minorTickInterval, 11, 0, 1, 2)
        self.toolBox_figureParam.addItem(self.page_axisTick, "")
        self.page_showAxis = QtWidgets.QWidget()
        self.page_showAxis.setStyleSheet(self.toolsBox_page_style)
        self.page_showAxis.setObjectName("page_showAxis")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_showAxis)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.checkBox_top = QtWidgets.QCheckBox(self.page_showAxis)
        self.checkBox_top.setChecked(True)
        self.checkBox_top.setObjectName("checkBox_top")
        self.gridLayout_7.addWidget(self.checkBox_top, 0, 0, 1, 1)
        self.checkBox_bottom = QtWidgets.QCheckBox(self.page_showAxis)
        self.checkBox_bottom.setChecked(True)
        self.checkBox_bottom.setObjectName("checkBox_bottom")
        self.gridLayout_7.addWidget(self.checkBox_bottom, 0, 1, 1, 1)
        self.checkBox_left = QtWidgets.QCheckBox(self.page_showAxis)
        self.checkBox_left.setChecked(True)
        self.checkBox_left.setObjectName("checkBox_left")
        self.gridLayout_7.addWidget(self.checkBox_left, 1, 0, 1, 1)
        self.checkBox_right = QtWidgets.QCheckBox(self.page_showAxis)
        self.checkBox_right.setChecked(True)
        self.checkBox_right.setObjectName("checkBox_right")
        self.gridLayout_7.addWidget(self.checkBox_right, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem8, 2, 0, 1, 1)
        self.toolBox_figureParam.addItem(self.page_showAxis, "")
        self.page_units = QtWidgets.QWidget()
        self.page_units.setStyleSheet(self.toolsBox_page_style)
        self.page_units.setObjectName("page_units")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_units)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.comboBox_units = QtWidgets.QComboBox(self.page_units)
        self.comboBox_units.setObjectName("comboBox_units")
        self.comboBox_units.addItem("")
        self.comboBox_units.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_units, 0, 1, 1, 1)
        self.label_units = QtWidgets.QLabel(self.page_units)
        self.label_units.setObjectName("label_units")
        self.gridLayout_8.addWidget(self.label_units, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem9, 1, 0, 1, 1)
        self.toolBox_figureParam.addItem(self.page_units, "")
        self.verticalLayout.addWidget(self.toolBox_figureParam)
        # 重绘功能
        self.reDraw_buttton = QtWidgets.QPushButton(
            QtGui.QIcon("./icons/reDraw.png"), '重新绘图', self.param_widget)
        self.reDraw_action = QtWidgets.QAction(self.param_widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/reDraw.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reDraw_action.setIcon(icon)
        self.reDraw_action.setText('重新绘图')
        self.reDraw_action.setObjectName("reDraw_action")
        self.reDraw_buttton.addAction(self.reDraw_action)
        self.reDraw_buttton.setFont(font)
        # self.reDraw_buttton.setMaximumWidth(200)
        # 重置参数功能
        self.reSet_button = QtWidgets.QPushButton(
            QtGui.QIcon("./icons/reSet.png"), '重置参数', self.param_widget)
        self.reSet_action = QtWidgets.QAction(self.param_widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/reSet.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reSet_action.setIcon(icon2)
        self.reSet_action.setText('重新绘图')
        self.reSet_action.setObjectName("reSet_action")
        self.reSet_button.addAction(self.reSet_action)
        self.reSet_button.setFont(font)

        self.verticalLayout.addWidget(self.reSet_button)
        self.verticalLayout.addWidget(self.reDraw_buttton)

        spacerItem10 = QtWidgets.QSpacerItem(
            20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem10)
        self.toolBox_figureParam.layout().setSpacing(1)
        self.left_stacked_widget.addWidget(self.param_widget)

    def init_export(self):
        self.export_widget = QtWidgets.QWidget()
        self.export_widget.setMaximumWidth(230)
        self.export_widget.setObjectName("export_widget")
        icon4 = QtGui.QIcon()
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        icon4.addPixmap(QtGui.QPixmap("./icons/save.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # 为导出页添加控件
        self.vLayout_export = QtWidgets.QVBoxLayout(self.export_widget)
        self.vLayout_export.setObjectName("vLayout_export")
        self.saveAll_button = QtWidgets.QPushButton(
            QtGui.QIcon("./icons/save.ico"), '保存全部图片', self.export_widget)
        self.saveAll_button.setFont(font)
        self.vLayout_export.addWidget(self.saveAll_button)
        self.left_stacked_widget.addWidget(self.export_widget)

    def item_clicked(self):
        item = self.left_list_widget.selectedItems()[0]
        if item.text() == '文件管理':
            self.switch_dataView()
        elif (item.text() == '数据信息'):
            self.switch_dataLog()
        elif item.text() == '图像参数':
            self.switch_paramWidget()
        else:
            self.switch_export()

    def switch_dataView(self):
        self.left_stacked_widget.setCurrentWidget(self.myUi.dataViewFrame)
        self.leftFrame.setMaximumWidth(350)
        self.leftFrame.setMinimumWidth(350)


    def switch_dataLog(self):
        self.left_stacked_widget.setCurrentWidget(self.export_frame)
        self.leftFrame.setMaximumWidth(350)
        self.leftFrame.setMinimumWidth(350)


    def switch_paramWidget(self):
        self.left_stacked_widget.setCurrentWidget(self.param_widget)
        self.left_stacked_widget.setMinimumWidth(380)
        self.left_stacked_widget.setMaximumWidth(380)
        self.leftFrame.setMaximumWidth(500)
        self.leftFrame.setMinimumWidth(500)

    def switch_export(self):
        self.left_stacked_widget.setCurrentWidget(self.export_widget)
        self.leftFrame.setMaximumWidth(350)
        self.leftFrame.setMinimumWidth(350)


    def getParam(self):

        # 默认参数表
        paramList = []
        xMove = None
        yMove = None
        xMin = 0.0
        xMax = 0.0
        yMin = 0.0
        yMax = 0.0
        ballStyle = ''
        isPlotWall = True
        wallLineSize = 0.8
        colorStyle = 'ZDEMColor'
        titleText = ''
        titleTextFontSize = 12
        xText = ''
        xTextFontSize = 9
        yText = ''
        yTextFontSize = 9
        mainTickInterval = 10000.0
        minorTickInterval = 1000.0
        isShowTop = True
        isShowBottom = True
        isShowLeft = True
        isShowRight = True
        unit = 1000
        # 坐标偏移量
        if self.lineEdit_xmove.text() != '':
            xMove = float(self.lineEdit_xmove.text())
        if self.lineEdit_ymove.text() != '':
            yMove = float(self.lineEdit_ymove.text())
        # 坐标轴范围
        xMin = float(self.xmin_lineEdit.text())
        xMax = float(self.xmax_lineEdit.text())
        yMin = float(self.ymin_lineEdit.text())
        yMax = float(self.ymax_lineEdit.text())
        # 颗粒
        if (self.Button_plotCircle.isChecked() == True) & (self.Button_plotPoint.isChecked() == False):
            ballStyle = 'circle'
        if (self.Button_plotCircle.isChecked() == False) & (self.Button_plotPoint.isChecked() == True):
            ballStyle = 'point'
        if (self.Button_plotCircle.isChecked() == True) & (self.Button_plotPoint.isChecked() == True):
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, '警告', '请选择颗粒样式')
            msg_box.exec_()
        if (self.Button_plotCircle.isChecked() == False) & (self.Button_plotPoint.isChecked() == False):
            msg_box1 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, '警告', '请选择颗粒样式')
            msg_box1.exec_()
        # 墙
        isPlotWall = self.checkBox_plotWall.isChecked()  # 返回值为bool
        wallLineSize = self.SpinBox_lineSize.value()
        # 颜色设置
        if (self.comboBox_color.currentText() == 'ZDEM默认颜色'):
            colorStyle = 'ZDEMColor'
        # 图名  ！！！！暂时未实现自定义字体样式功能，x、y轴too
        titleText = self.lineEdit_title.text()
        titleTextFontSize = self.spinBox_title.value()
        # 轴标签
        xText = self.lineEdit_xName.text()
        xTextFontSize = self.spinBox_xTickSize.value()
        yText = self.lineEdit_yName.text()
        yTextFontSize = self.spinBox_yTickSize.value()
        if self.lineEdit_mainTickInterval.text() != '':
            mainTickInterval = float(self.lineEdit_mainTickInterval.text())
        if self.lineEdit_minorTickInterval.text() != '':
            minorTickInterval = float(self.lineEdit_minorTickInterval.text())
        # 是否显示坐标轴
        isShowTop = self.checkBox_top.isChecked()  # bool
        isShowBottom = self.checkBox_bottom.isChecked()
        isShowLeft = self.checkBox_left.isChecked()
        isShowRight = self.checkBox_right.isChecked()
        # 单位
        if self.comboBox_units.currentText() == 'km':
            unit = 1000
        if self.comboBox_units.currentText() == 'm':
            unit = 1
        # 将得到的参数存放到参数表
        paramList.append(xMove)
        paramList.append(yMove)
        paramList.append(xMin)
        paramList.append(xMax)
        paramList.append(yMin)
        paramList.append(yMax)
        paramList.append(ballStyle)
        paramList.append(isPlotWall)
        paramList.append(wallLineSize)
        paramList.append(colorStyle)
        paramList.append(titleText)
        paramList.append(titleTextFontSize)
        paramList.append(xText)
        paramList.append(xTextFontSize)
        paramList.append(yText)
        paramList.append(yTextFontSize)
        paramList.append(mainTickInterval)
        paramList.append(minorTickInterval)
        paramList.append(isShowTop)
        paramList.append(isShowBottom)
        paramList.append(isShowLeft)
        paramList.append(isShowRight)
        paramList.append(unit)
        return paramList

    def reDraw(self):

        self.paramList = self.getParam()
        if self.paramList[6] == '':
            return False
        self.mplWidgetList = self.myUi.dataView.mplWidget_list
        self.list_select_files = self.myUi.dataView.list_select_files
        self.absulotePathList = self.myUi.dataView.absulotePathList
        if (self.paramList[0] is None) and (self.paramList[1] is None) and (self.paramList[7] == True) and (self.paramList[8] == 0.8):
            self.reDraw_axis()
        else:
            for i in range(len(self.list_select_files)):  # 循环创建多个线程对象，添加到线程池
                PlotALLThread = PlotThread(
                    self.mplWidgetList[i], self.absulotePathList[i], self.myUi, i, paramList=self.paramList)
                PlotALLThread.plotObj_test.updata_canvas_signal.connect(
                    self.myUi.dataView.updataCanvas)
                PlotALLThread.plotObj_test.begin_plot_signal.connect(
                    self.myUi.dataView.beginPlot_labelupdata)
                self.myUi.dataView.poolManager.addThread(
                    PlotALLThread)  # 添加到线程池
                PlotALLThread.autoDelete()  # 线程执行完毕自动删除
            self.myUi.dataView.poolManager.start()  # 所有的绘图子线程已经添加到线程池，start开启执行
            self.myUi.ProgressBar.statusLabel.setText("绘图中，请稍后...")

    def reDraw_axis(self):
        for i in range(len(self.list_select_files)):
            # 设置 x轴、y轴范围
            self.mplWidgetList[i].qCanvas.axes.set_xlim(
                self.paramList[2], self.paramList[3])
            self.mplWidgetList[i].qCanvas.axes.set_ylim(
                self.paramList[4], self.paramList[5])
            # 单位

            def unitsformat(x, pos):
                return '{:n}'.format(x / self.paramList[22])
            xmajorformatter = FuncFormatter(unitsformat)
            self.mplWidgetList[i].qCanvas.axes.xaxis.set_major_formatter(
                xmajorformatter)
            ymajorformatter = FuncFormatter(unitsformat)
            self.mplWidgetList[i].qCanvas.axes.yaxis.set_major_formatter(
                ymajorformatter)
            # 修改主刻度
            xmajorLocator = MultipleLocator(
                self.paramList[16])  # 将x主刻度标签设置为20的倍数
            # xmajorFormatter = FormatStrFormatter('%5.1f')  # 设置x轴标签文本的格式
            ymajorLocator = MultipleLocator(
                self.paramList[16])  # 将y轴主刻度标签设置为0.5的倍数
            # ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
            # 设置主刻度标签的位置,标签文本的格式
            self.mplWidgetList[i].qCanvas.axes.xaxis.set_major_locator(
                xmajorLocator)
            # self.canvasObj.qCanvas.axes.xaxis.set_major_formatter(xmajorFormatter)
            self.mplWidgetList[i].qCanvas.axes.yaxis.set_major_locator(
                ymajorLocator)
            # self.canvasObj.qCanvas.axes.yaxis.set_major_formatter(ymajorFormatter)
            # 修改次刻度
            xminorLocator = MultipleLocator(self.paramList[17])
            yminorLocator = MultipleLocator(self.paramList[17])
            self.mplWidgetList[i].qCanvas.axes.xaxis.set_minor_locator(
                xminorLocator)
            self.mplWidgetList[i].qCanvas.axes.yaxis.set_minor_locator(
                yminorLocator)
            # 设置标签label的字体大小
            self.mplWidgetList[i].qCanvas.axes.tick_params(
                axis='x', labelsize=self.paramList[13])
            self.mplWidgetList[i].qCanvas.axes.tick_params(
                axis='y', labelsize=self.paramList[15])
            # 坐标轴边框显示/隐藏
            self.mplWidgetList[i].qCanvas.axes.spines['top'].set_visible(
                self.paramList[18])
            self.mplWidgetList[i].qCanvas.axes.spines['right'].set_visible(
                self.paramList[21])
            self.mplWidgetList[i].qCanvas.axes.spines['bottom'].set_visible(
                self.paramList[19])
            self.mplWidgetList[i].qCanvas.axes.spines['left'].set_visible(
                self.paramList[20])
            # 计算图片尺寸
            wi = self.paramList[3] - self.paramList[2]
            hi = self.paramList[5] - self.paramList[4]
            wcm = 14
            winch = wcm/2.54
            hinch = (winch+0.1)/wi*hi
            self.mplWidgetList[i].qCanvas.figs.set_size_inches(
                w=winch, h=hinch)
            self.mplWidgetList[i].qCanvas.figs.canvas.draw()
            # 画布刷新self.figs.canvas
            self.mplWidgetList[i].qCanvas.figs.canvas.flush_events()

    def saveAll(self):
        """

        :return:
        """
        QCanvas_list = []
        QCanvas_list = self.myUi.dataView.QCanvas_list
        num = len(self.myUi.dataView.list_select_files)
        for i in range(num):
            QCanvas_list[i].saveFig()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.label_dataText.setText(_translate("self.siderBarWidget", "数据信息"))

        self.label_paramTitle.setText(
            _translate("self.siderBarWidget", "图像参数"))
        self.tools_move.setStatusTip(_translate("self.siderBarWidget", ")"))
        self.tools_move.setAccessibleName(
            _translate("self.siderBarWidget", ")"))
        self.lineEdit_xmove.setToolTip(_translate(
            "self.siderBarWidget", "设置坐标沿X轴的偏移量，单位(m)"))
        self.label_ymove.setText(_translate("self.siderBarWidget", "Y轴"))
        self.label_xmove.setText(_translate("self.siderBarWidget", "X轴"))
        self.lineEdit_ymove.setToolTip(_translate(
            "self.siderBarWidget", "设置坐标沿Y轴的偏移量，单位(m)"))
        self.toolBox_figureParam.setItemText(self.toolBox_figureParam.indexOf(
            self.tools_move), _translate("self.siderBarWidget", "坐标偏移量"))
        self.yminLabel.setText(_translate("self.siderBarWidget", "Y轴最小值"))
        self.xmax_lineEdit.setToolTip(
            _translate("self.siderBarWidget", "单位(m)"))
        self.xmaxLabel.setText(_translate("self.siderBarWidget", "X轴最大值"))
        self.xminLabel.setText(_translate("self.siderBarWidget", "X轴最小值"))
        self.xmin_lineEdit.setToolTip(
            _translate("self.siderBarWidget", "单位(m)"))
        self.ymaxLabel.setText(_translate("self.siderBarWidget", "Y轴最大值"))
        self.toolBox_figureParam.setItemText(self.toolBox_figureParam.indexOf(
            self.page_axisRange), _translate("self.siderBarWidget", "坐标轴范围"))
        self.Button_plotPoint.setText(_translate("self.siderBarWidget", "散点"))
        self.Button_plotCircle.setText(
            _translate("self.siderBarWidget", "二维圆"))
        self.toolBox_figureParam.setItemText(self.toolBox_figureParam.indexOf(
            self.page), _translate("self.siderBarWidget", "颗粒"))
        self.label_lineSize.setText(_translate("self.siderBarWidget", "线条粗细"))
        self.checkBox_plotWall.setText(
            _translate("self.siderBarWidget", "绘制墙体"))
        self.toolBox_figureParam.setItemText(self.toolBox_figureParam.indexOf(
            self.tools_plotWall), _translate("self.siderBarWidget", "墙"))
        self.label_color.setText(_translate("self.siderBarWidget", "颜色设置"))
        self.comboBox_color.setItemText(
            0, _translate("self.siderBarWidget", "ZDEM默认颜色"))
        self.Button_importColor.setText(
            _translate("self.siderBarWidget", "导入其他"))
        self.toolBox_figureParam.setItemText(self.toolBox_figureParam.indexOf(
            self.page_color), _translate("self.siderBarWidget", "颜色设置"))
        self.label_titleFont.setText(_translate("self.siderBarWidget", "字体"))
        self.label_titleFontSize.setText(
            _translate("self.siderBarWidget", "大小"))
        self.label_title.setText(_translate("self.siderBarWidget", "图名"))
        self.toolBox_figureParam.setItemText(self.toolBox_figureParam.indexOf(
            self.page_figureTitle), _translate("self.siderBarWidget", "图名"))
        self.label_yName.setText(_translate("self.siderBarWidget", "Y轴名"))
        self.label_xName.setText(_translate("self.siderBarWidget", "X轴名"))
        self.label_xTickFont.setText(_translate("self.siderBarWidget", "字体"))
        self.label_yTickSize.setText(_translate("self.siderBarWidget", "大小"))
        self.label_yTickFont.setText(_translate("self.siderBarWidget", "字体"))
        self.label_minorTickInterval.setText(
            _translate("self.siderBarWidget", "次坐标刻度间隔"))
        self.label_mainTickInterval.setText(
            _translate("self.siderBarWidget", "主坐标刻度间隔"))
        self.label_xTickSzie.setText(_translate("self.siderBarWidget", "大小"))
        self.lineEdit_mainTickInterval.setText(
            _translate("self.siderBarWidget", "10000.0"))
        self.lineEdit_minorTickInterval.setText(
            _translate("self.siderBarWidget", "1000.0"))
        self.toolBox_figureParam.setItemText(self.toolBox_figureParam.indexOf(
            self.page_axisTick), _translate("self.siderBarWidget", "轴标签"))
        self.checkBox_top.setText(_translate("self.siderBarWidget", "Top"))
        self.checkBox_bottom.setText(
            _translate("self.siderBarWidget", "Bottom"))
        self.checkBox_left.setText(_translate("self.siderBarWidget", "Left"))
        self.checkBox_right.setText(_translate("self.siderBarWidget", "Right"))
        self.toolBox_figureParam.setItemText(self.toolBox_figureParam.indexOf(
            self.page_showAxis), _translate("self.siderBarWidget", "显示/隐藏坐标轴"))
        self.comboBox_units.setItemText(
            0, _translate("self.siderBarWidget", "km"))
        self.comboBox_units.setItemText(
            1, _translate("self.siderBarWidget", "m"))
        self.label_units.setText(_translate("self.siderBarWidget", "单位"))
        self.toolBox_figureParam.setItemText(self.toolBox_figureParam.indexOf(
            self.page_units), _translate("self.siderBarWidget", "单位"))
        # caohshu
        self.reDraw_buttton.clicked.connect(self.reDraw)
        self.saveAll_button.clicked.connect(self.saveAll)
