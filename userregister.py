# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userregisteration.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registration(object):
    def setupUi(self, registration):
        registration.setObjectName("registration")
        registration.resize(752, 513)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/register_login_signup_icon_219991.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        registration.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(registration)
        self.frame.setGeometry(QtCore.QRect(10, 10, 731, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/Your paragraph text (3).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(310, 150, 391, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_username = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_username.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_username)
        self.Line_username = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Line_username.setObjectName("Line_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Line_username)
        self.label_password = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_password.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.Line_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Line_password.setObjectName("Line_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Line_password)
        self.label_passwordagain = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_passwordagain.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_passwordagain.setFont(font)
        self.label_passwordagain.setObjectName("label_passwordagain")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_passwordagain)
        self.Line_passwordcomfire = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Line_passwordcomfire.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Line_passwordcomfire.setObjectName("Line_passwordcomfire")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Line_passwordcomfire)
        self.label_email = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_email.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_email)
        self.Line_email = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Line_email.setObjectName("Line_email")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Line_email)
        self.label_code = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_code.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_code.setFont(font)
        self.label_code.setObjectName("label_code")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_code)
        self.codeimage = QtWidgets.QLabel(self.formLayoutWidget)
        self.codeimage.setText("")
        self.codeimage.setObjectName("codeimage")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.codeimage)
        self.register_but = QtWidgets.QPushButton(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.register_but.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.register_but.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/smartphone_mobile_phone_online_registration_check_mark_checked_approved_done_icon_175516.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.register_but.setIcon(icon1)
        self.register_but.setObjectName("register_but")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.register_but)
        self.Cancel_but = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_but.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/receipt_cancel_icon_177356.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cancel_but.setIcon(icon2)
        self.Cancel_but.setFlat(False)
        self.Cancel_but.setObjectName("Cancel_but")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Cancel_but)
        self.Linecode = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Linecode.setObjectName("Linecode")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Linecode)
        self.tool_refrash = QtWidgets.QToolButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tool_refrash.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/1491313940-repeat_82991.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tool_refrash.setIcon(icon3)
        self.tool_refrash.setObjectName("tool_refrash")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.tool_refrash)
        self.displayline3 = QtWidgets.QFrame(self.frame)
        self.displayline3.setGeometry(QtCore.QRect(20, 450, 691, 16))
        self.displayline3.setLineWidth(2)
        self.displayline3.setFrameShape(QtWidgets.QFrame.HLine)
        self.displayline3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.displayline3.setObjectName("displayline3")
        self.img = QtWidgets.QLabel(self.frame)
        self.img.setGeometry(QtCore.QRect(30, 160, 261, 211))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/3d-casual-life-blockchain-technologies.png"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.titke = QtWidgets.QLabel(self.frame)
        self.titke.setGeometry(QtCore.QRect(270, 30, 211, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.titke.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("PT Bold Dusky")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.titke.setFont(font)
        self.titke.setObjectName("titke")
        self.displayline2 = QtWidgets.QFrame(self.frame)
        self.displayline2.setGeometry(QtCore.QRect(290, 160, 20, 191))
        self.displayline2.setFrameShape(QtWidgets.QFrame.VLine)
        self.displayline2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.displayline2.setObjectName("displayline2")
        self.displayline1 = QtWidgets.QFrame(self.frame)
        self.displayline1.setGeometry(QtCore.QRect(10, 60, 701, 16))
        self.displayline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.displayline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.displayline1.setObjectName("displayline1")

        self.retranslateUi(registration)
        QtCore.QMetaObject.connectSlotsByName(registration)

    def retranslateUi(self, registration):
        _translate = QtCore.QCoreApplication.translate
        registration.setWindowTitle(_translate("registration", "System registration interface"))
        self.label_username.setText(_translate("registration", "USERANME"))
        self.Line_username.setPlaceholderText(_translate("registration", "Enter your username（len > 15）"))
        self.label_password.setText(_translate("registration", "PASSWORD"))
        self.Line_password.setPlaceholderText(_translate("registration", "Enter your password(Include 1aA)"))
        self.label_passwordagain.setText(_translate("registration", "Confirm Password"))
        self.Line_passwordcomfire.setPlaceholderText(_translate("registration", "Confirm your password"))
        self.label_email.setText(_translate("registration", "EMAIL"))
        self.Line_email.setPlaceholderText(_translate("registration", "Enter your  email address"))
        self.label_code.setText(_translate("registration", "Verification Code"))
        self.register_but.setText(_translate("registration", "REGISTER"))
        self.Cancel_but.setText(_translate("registration", "CANCEL"))
        self.Linecode.setPlaceholderText(_translate("registration", "Enter the code"))
        self.tool_refrash.setText(_translate("registration", "\\"))
        self.titke.setText(_translate("registration", "New User Registration"))
