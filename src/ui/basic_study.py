# Form implementation generated from reading ui file 'basic_study.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BasicStudy(object):
    def setupUi(self, BasicStudy):
        BasicStudy.setObjectName("BasicStudy")
        BasicStudy.resize(1000, 600)
        self.pushButton_before = QtWidgets.QPushButton(parent=BasicStudy)
        self.pushButton_before.setGeometry(QtCore.QRect(40, 250, 100, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_before.setFont(font)
        self.pushButton_before.setObjectName("pushButton_before")
        self.pushButton_after = QtWidgets.QPushButton(parent=BasicStudy)
        self.pushButton_after.setGeometry(QtCore.QRect(860, 250, 100, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_after.setFont(font)
        self.pushButton_after.setObjectName("pushButton_after")
        self.pushButton_main = QtWidgets.QPushButton(parent=BasicStudy)
        self.pushButton_main.setGeometry(QtCore.QRect(400, 540, 200, 41))
        self.pushButton_main.setObjectName("pushButton_main")
        self.label_eng = QtWidgets.QLabel(parent=BasicStudy)
        self.label_eng.setGeometry(QtCore.QRect(320, 221, 251, 51))
        self.label_eng.setText("")
        self.label_eng.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_eng.setObjectName("label_eng")
        self.label_kor = QtWidgets.QLabel(parent=BasicStudy)
        self.label_kor.setGeometry(QtCore.QRect(350, 230, 300, 100))
        self.label_kor.setText("")
        self.label_kor.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_kor.setObjectName("label_kor")
        self.line = QtWidgets.QFrame(parent=BasicStudy)
        self.line.setGeometry(QtCore.QRect(140, 20, 20, 550))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=BasicStudy)
        self.line_2.setGeometry(QtCore.QRect(840, 20, 20, 550))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(BasicStudy)
        QtCore.QMetaObject.connectSlotsByName(BasicStudy)

    def retranslateUi(self, BasicStudy):
        _translate = QtCore.QCoreApplication.translate
        BasicStudy.setWindowTitle(_translate("BasicStudy", "Form"))
        self.pushButton_before.setText(_translate("BasicStudy", "이전"))
        self.pushButton_after.setText(_translate("BasicStudy", "다음"))
        self.pushButton_main.setText(_translate("BasicStudy", "홈으로"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BasicStudy = QtWidgets.QWidget()
    ui = Ui_BasicStudy()
    ui.setupUi(BasicStudy)
    BasicStudy.show()
    sys.exit(app.exec())