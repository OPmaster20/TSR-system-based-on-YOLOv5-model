# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editimgsform(object):
    def setupUi(self, editimgsform):
        editimgsform.setObjectName("editimgsform")
        editimgsform.resize(1104, 848)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/management_settings_cogwheel_options_icon_262697.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        editimgsform.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(editimgsform)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1081, 831))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 1081, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/Untitled design.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(490, 40, 531, 371))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(480, 30, 551, 391))
        self.graphicsView.setObjectName("graphicsView")
        self.toolsarea = QtWidgets.QTabWidget(self.frame)
        self.toolsarea.setGeometry(QtCore.QRect(20, 30, 401, 781))
        self.toolsarea.setTabPosition(QtWidgets.QTabWidget.West)
        self.toolsarea.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.toolsarea.setElideMode(QtCore.Qt.ElideNone)
        self.toolsarea.setDocumentMode(False)
        self.toolsarea.setTabsClosable(False)
        self.toolsarea.setMovable(False)
        self.toolsarea.setTabBarAutoHide(False)
        self.toolsarea.setObjectName("toolsarea")
        self.p1 = QtWidgets.QWidget()
        self.p1.setObjectName("p1")
        self.linea = QtWidgets.QFrame(self.p1)
        self.linea.setGeometry(QtCore.QRect(10, 530, 351, 31))
        self.linea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.linea.setLineWidth(2)
        self.linea.setFrameShape(QtWidgets.QFrame.HLine)
        self.linea.setObjectName("linea")
        self.line_2 = QtWidgets.QFrame(self.p1)
        self.line_2.setGeometry(QtCore.QRect(10, 320, 351, 31))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.group1 = QtWidgets.QGroupBox(self.p1)
        self.group1.setGeometry(QtCore.QRect(10, 350, 351, 181))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.group1.setFont(font)
        self.group1.setFlat(False)
        self.group1.setCheckable(False)
        self.group1.setObjectName("group1")
        self.formLayoutWidget = QtWidgets.QWidget(self.group1)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 230, 89))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labelname1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelname1.setObjectName("labelname1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelname1)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.labelname3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelname3.setObjectName("labelname3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelname3)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.confirm_but = QtWidgets.QPushButton(self.formLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/bug_danger_data_internet_malware_security_virus_icon_127084.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirm_but.setIcon(icon1)
        self.confirm_but.setDefault(True)
        self.confirm_but.setObjectName("confirm_but")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.confirm_but)
        self.group2 = QtWidgets.QGroupBox(self.p1)
        self.group2.setGeometry(QtCore.QRect(9, 560, 351, 191))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.group2.setFont(font)
        self.group2.setObjectName("group2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.group2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 171, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.check_en = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.check_en.setFont(font)
        self.check_en.setObjectName("check_en")
        self.verticalLayout.addWidget(self.check_en)
        self.check_show = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.check_show.setFont(font)
        self.check_show.setObjectName("check_show")
        self.verticalLayout.addWidget(self.check_show)
        self.saveimgs = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saveimgs.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/picture_file_image_photo_gallery_icon_219497.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveimgs.setIcon(icon2)
        self.saveimgs.setDefault(True)
        self.saveimgs.setFlat(False)
        self.saveimgs.setObjectName("saveimgs")
        self.verticalLayout.addWidget(self.saveimgs)
        self.recover = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.recover.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/1491313940-repeat_82991.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recover.setIcon(icon3)
        self.recover.setDefault(True)
        self.recover.setObjectName("recover")
        self.verticalLayout.addWidget(self.recover)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.group2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 40, 151, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.exit_but = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.exit_but.setIcon(icon3)
        self.exit_but.setDefault(True)
        self.exit_but.setObjectName("exit_but")
        self.verticalLayout_2.addWidget(self.exit_but)
        self.groupBox = QtWidgets.QGroupBox(self.p1)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 351, 271))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 311, 41))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.setting1 = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.setting1.setTracking(True)
        self.setting1.setOrientation(QtCore.Qt.Horizontal)
        self.setting1.setInvertedAppearance(False)
        self.setting1.setInvertedControls(False)
        self.setting1.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.setting1.setTickInterval(10)
        self.setting1.setObjectName("setting1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.setting1)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 80, 201, 80))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.labelname2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.labelname2.setObjectName("labelname2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelname2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.formLayoutWidget_3)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setObjectName("lcdNumber")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lcdNumber)
        self.confirm_but2 = QtWidgets.QPushButton(self.formLayoutWidget_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/setting_balance_equalizer_icon_152217.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirm_but2.setIcon(icon4)
        self.confirm_but2.setDefault(True)
        self.confirm_but2.setObjectName("confirm_but2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.confirm_but2)
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(20, 180, 311, 31))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.dilatingSlider = QtWidgets.QSlider(self.formLayoutWidget_4)
        self.dilatingSlider.setOrientation(QtCore.Qt.Horizontal)
        self.dilatingSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.dilatingSlider.setObjectName("dilatingSlider")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.dilatingSlider)
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(20, 220, 217, 41))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_3.setObjectName("label_3")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.formLayoutWidget_5)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lcdNumber_2)
        self.confirm_but3 = QtWidgets.QPushButton(self.groupBox)
        self.confirm_but3.setGeometry(QtCore.QRect(240, 220, 93, 28))
        self.confirm_but3.setObjectName("confirm_but3")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/picture_photo_image_icon_131252.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolsarea.addTab(self.p1, icon5, "")
        self.p2 = QtWidgets.QWidget()
        self.p2.setObjectName("p2")
        self.settingsdock = QtWidgets.QDockWidget(self.p2)
        self.settingsdock.setGeometry(QtCore.QRect(10, 10, 351, 761))
        self.settingsdock.setFloating(False)
        self.settingsdock.setObjectName("settingsdock")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.toolgroup1 = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.toolgroup1.setGeometry(QtCore.QRect(10, 10, 331, 181))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.toolgroup1.setFont(font)
        self.toolgroup1.setFlat(True)
        self.toolgroup1.setCheckable(False)
        self.toolgroup1.setObjectName("toolgroup1")
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.toolgroup1)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(10, 30, 301, 151))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_4.setObjectName("label_4")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.imgnameline = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        self.imgnameline.setReadOnly(True)
        self.imgnameline.setObjectName("imgnameline")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.imgnameline)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_5.setObjectName("label_5")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.pathline = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.pathline.setText("")
        self.pathline.setObjectName("pathline")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pathline)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_6.setObjectName("label_6")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.heightline = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.heightline.setText("")
        self.heightline.setObjectName("heightline")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.heightline)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_7.setObjectName("label_7")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.widthline = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.widthline.setText("")
        self.widthline.setObjectName("widthline")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.widthline)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_8.setObjectName("label_8")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.resolutionline = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.resolutionline.setText("")
        self.resolutionline.setObjectName("resolutionline")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.resolutionline)
        self.toolgroup2 = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.toolgroup2.setGeometry(QtCore.QRect(10, 240, 331, 181))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolgroup2.setFont(font)
        self.toolgroup2.setFlat(True)
        self.toolgroup2.setObjectName("toolgroup2")
        self.formLayoutWidget_7 = QtWidgets.QWidget(self.toolgroup2)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(10, 30, 301, 141))
        self.formLayoutWidget_7.setObjectName("formLayoutWidget_7")
        self.formLayout_7 = QtWidgets.QFormLayout(self.formLayoutWidget_7)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.label_9.setObjectName("label_9")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.savenameline = QtWidgets.QLineEdit(self.formLayoutWidget_7)
        self.savenameline.setReadOnly(True)
        self.savenameline.setObjectName("savenameline")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.savenameline)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.label_10.setObjectName("label_10")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.filetypeline = QtWidgets.QLineEdit(self.formLayoutWidget_7)
        self.filetypeline.setReadOnly(True)
        self.filetypeline.setObjectName("filetypeline")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.filetypeline)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.label_11.setObjectName("label_11")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.originalnameline = QtWidgets.QLineEdit(self.formLayoutWidget_7)
        self.originalnameline.setReadOnly(True)
        self.originalnameline.setObjectName("originalnameline")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.originalnameline)
        self.revise_but = QtWidgets.QPushButton(self.formLayoutWidget_7)
        self.revise_but.setDefault(True)
        self.revise_but.setFlat(False)
        self.revise_but.setObjectName("revise_but")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.revise_but)
        self.saveset_but = QtWidgets.QPushButton(self.formLayoutWidget_7)
        self.saveset_but.setObjectName("saveset_but")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.saveset_but)
        self.line_3 = QtWidgets.QFrame(self.dockWidgetContents)
        self.line_3.setGeometry(QtCore.QRect(10, 220, 331, 20))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.toolgroup3 = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.toolgroup3.setGeometry(QtCore.QRect(10, 440, 331, 291))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolgroup3.setFont(font)
        self.toolgroup3.setObjectName("toolgroup3")
        self.listWidget = QtWidgets.QListWidget(self.toolgroup3)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 311, 231))
        self.listWidget.setObjectName("listWidget")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.toolgroup3)
        self.lcdNumber_3.setGeometry(QtCore.QRect(10, 260, 64, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.settingsdock.setWidget(self.dockWidgetContents)
        self.toolsarea.addTab(self.p2, "")
        self.p3 = QtWidgets.QWidget()
        self.p3.setObjectName("p3")
        self.ad_dock = QtWidgets.QDockWidget(self.p3)
        self.ad_dock.setGeometry(QtCore.QRect(10, 10, 351, 731))
        self.ad_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.ad_dock.setObjectName("ad_dock")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 331, 471))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_8 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_8.setGeometry(QtCore.QRect(10, 30, 311, 161))
        self.formLayoutWidget_8.setObjectName("formLayoutWidget_8")
        self.formLayout_8 = QtWidgets.QFormLayout(self.formLayoutWidget_8)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.formLayout_8.setObjectName("formLayout_8")
        self.check1 = QtWidgets.QCheckBox(self.formLayoutWidget_8)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/icons8-depth-effect-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check1.setIcon(icon6)
        self.check1.setObjectName("check1")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.check1)
        self.check2 = QtWidgets.QCheckBox(self.formLayoutWidget_8)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/icons8-buy-for-cash-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check2.setIcon(icon7)
        self.check2.setObjectName("check2")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.check2)
        self.check3 = QtWidgets.QCheckBox(self.formLayoutWidget_8)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/icons8-aspect-ratio-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check3.setIcon(icon8)
        self.check3.setObjectName("check3")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.check3)
        self.check4 = QtWidgets.QCheckBox(self.formLayoutWidget_8)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/icons8-depth-effect-48 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check4.setIcon(icon9)
        self.check4.setObjectName("check4")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.check4)
        self.check5 = QtWidgets.QCheckBox(self.formLayoutWidget_8)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/icons8-normal-screen-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check5.setIcon(icon10)
        self.check5.setObjectName("check5")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.check5)
        self.formLayoutWidget_9 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_9.setGeometry(QtCore.QRect(10, 190, 311, 80))
        self.formLayoutWidget_9.setObjectName("formLayoutWidget_9")
        self.formLayout_9 = QtWidgets.QFormLayout(self.formLayoutWidget_9)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_9)
        self.label_12.setObjectName("label_12")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.numberofimgs = QtWidgets.QSpinBox(self.formLayoutWidget_9)
        self.numberofimgs.setWrapping(False)
        self.numberofimgs.setFrame(True)
        self.numberofimgs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numberofimgs.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.numberofimgs.setAccelerated(False)
        self.numberofimgs.setObjectName("numberofimgs")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numberofimgs)
        self.cleanbut = QtWidgets.QPushButton(self.formLayoutWidget_9)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/icons8-time-lapse-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cleanbut.setIcon(icon11)
        self.cleanbut.setObjectName("cleanbut")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cleanbut)
        self.confirmbut = QtWidgets.QPushButton(self.formLayoutWidget_9)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/icons8-transitions-browser-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirmbut.setIcon(icon12)
        self.confirmbut.setObjectName("confirmbut")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.confirmbut)
        self.line_6 = QtWidgets.QFrame(self.groupBox_2)
        self.line_6.setGeometry(QtCore.QRect(10, 280, 311, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 300, 311, 112))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.pathframe = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        self.pathframe.setReadOnly(True)
        self.pathframe.setObjectName("pathframe")
        self.verticalLayout_3.addWidget(self.pathframe)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 410, 181, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.confirm_pressed = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/icons8-bursts-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirm_pressed.setIcon(icon13)
        self.confirm_pressed.setObjectName("confirm_pressed")
        self.horizontalLayout.addWidget(self.confirm_pressed)
        self.tools = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.tools.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/icons8-wire-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tools.setIcon(icon14)
        self.tools.setObjectName("tools")
        self.horizontalLayout.addWidget(self.tools)
        self.ad_dock.setWidget(self.dockWidgetContents_2)
        self.toolsarea.addTab(self.p3, "")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(430, 30, 21, 791))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.originalarea = QtWidgets.QLabel(self.frame)
        self.originalarea.setGeometry(QtCore.QRect(480, 460, 381, 271))
        self.originalarea.setText("")
        self.originalarea.setObjectName("originalarea")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(480, 430, 551, 16))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(870, 450, 20, 341))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label.raise_()
        self.graphicsView.raise_()
        self.toolsarea.raise_()
        self.line.raise_()
        self.label_2.raise_()
        self.originalarea.raise_()
        self.line_4.raise_()
        self.line_5.raise_()

        self.retranslateUi(editimgsform)
        self.toolsarea.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(editimgsform)

    def retranslateUi(self, editimgsform):
        _translate = QtCore.QCoreApplication.translate
        editimgsform.setWindowTitle(_translate("editimgsform", "Edit images"))
        self.group1.setTitle(_translate("editimgsform", "Smoothing Images"))
        self.labelname1.setText(_translate("editimgsform", "Smoothing parameter"))
        self.labelname3.setText(_translate("editimgsform", "Smooth Mode"))
        self.confirm_but.setText(_translate("editimgsform", "CONFIRM"))
        self.group2.setTitle(_translate("editimgsform", "Other Editing Settings"))
        self.check_en.setText(_translate("editimgsform", "Image Enhancement"))
        self.check_show.setText(_translate("editimgsform", "Show original image"))
        self.saveimgs.setText(_translate("editimgsform", "SAVE"))
        self.recover.setText(_translate("editimgsform", "RECOVER"))
        self.exit_but.setText(_translate("editimgsform", "EXIT"))
        self.groupBox.setTitle(_translate("editimgsform", "Eroding and Dilating"))
        self.labelname2.setText(_translate("editimgsform", "Erosion parameters"))
        self.confirm_but2.setText(_translate("editimgsform", "CONFIRM"))
        self.label_3.setText(_translate("editimgsform", "Expansion Parameters"))
        self.confirm_but3.setText(_translate("editimgsform", "CONFIRM"))
        self.toolsarea.setTabText(self.toolsarea.indexOf(self.p1), _translate("editimgsform", "Basics"))
        self.settingsdock.setWindowTitle(_translate("editimgsform", "Edit Settings"))
        self.toolgroup1.setTitle(_translate("editimgsform", "Image information"))
        self.label_4.setText(_translate("editimgsform", "Image Name"))
        self.label_5.setText(_translate("editimgsform", "Image path"))
        self.label_6.setText(_translate("editimgsform", "Height"))
        self.label_7.setText(_translate("editimgsform", "Width"))
        self.label_8.setText(_translate("editimgsform", "Resolution"))
        self.toolgroup2.setTitle(_translate("editimgsform", "Other settings"))
        self.label_9.setText(_translate("editimgsform", "Default save name"))
        self.label_10.setText(_translate("editimgsform", "Default save file type"))
        self.label_11.setText(_translate("editimgsform", "Original saved file name"))
        self.revise_but.setText(_translate("editimgsform", "REVISE"))
        self.saveset_but.setText(_translate("editimgsform", "SAVE"))
        self.toolgroup3.setTitle(_translate("editimgsform", "Historical images"))
        self.toolsarea.setTabText(self.toolsarea.indexOf(self.p2), _translate("editimgsform", "Site"))
        self.ad_dock.setWindowTitle(_translate("editimgsform", "Automated advanced image editing"))
        self.groupBox_2.setTitle(_translate("editimgsform", "Automatic image preprocessing"))
        self.check1.setText(_translate("editimgsform", "Add Erosion"))
        self.check2.setText(_translate("editimgsform", "Add Smoothing"))
        self.check3.setText(_translate("editimgsform", "Adding a Linear Filter"))
        self.check4.setText(_translate("editimgsform", "Add Expansion"))
        self.check5.setText(_translate("editimgsform", "Adding geometric transformations"))
        self.label_12.setText(_translate("editimgsform", "Number of generated images"))
        self.cleanbut.setText(_translate("editimgsform", "CLEAN"))
        self.confirmbut.setText(_translate("editimgsform", "CONFIRM"))
        self.label_13.setText(_translate("editimgsform", "Generate the save path of the image"))
        self.confirm_pressed.setText(_translate("editimgsform", "CONFIRM"))
        self.toolsarea.setTabText(self.toolsarea.indexOf(self.p3), _translate("editimgsform", "Advanced"))
