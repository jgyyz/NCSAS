# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yrd/eric_workspace/chap09/payment/paymentdlg.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PaymentDlg(object):
    def setupUi(self, PaymentDlg):
        PaymentDlg.setObjectName("PaymentDlg")
        PaymentDlg.resize(399, 276)
        self.gridlayout = QtWidgets.QGridLayout(PaymentDlg)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(PaymentDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.NoButton|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(381, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(PaymentDlg)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.tab)
        self.hboxlayout.setContentsMargins(9, 9, 9, 9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.paidCheckBox = QtWidgets.QCheckBox(self.tab)
        self.paidCheckBox.setObjectName("paidCheckBox")
        self.hboxlayout.addWidget(self.paidCheckBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridlayout1 = QtWidgets.QGridLayout(self.tab_2)
        self.gridlayout1.setContentsMargins(9, 9, 9, 9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")
        self.sortCodeLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.sortCodeLineEdit.setObjectName("sortCodeLineEdit")
        self.gridlayout1.addWidget(self.sortCodeLineEdit, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridlayout1.addWidget(self.label_8, 1, 2, 1, 1)
        self.bankLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.bankLineEdit.setObjectName("bankLineEdit")
        self.gridlayout1.addWidget(self.bankLineEdit, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridlayout1.addWidget(self.label_7, 0, 2, 1, 1)
        self.accountNumLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.accountNumLineEdit.setObjectName("accountNumLineEdit")
        self.gridlayout1.addWidget(self.accountNumLineEdit, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridlayout1.addWidget(self.label_6, 1, 0, 1, 1)
        self.checkNumLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.checkNumLineEdit.setObjectName("checkNumLineEdit")
        self.gridlayout1.addWidget(self.checkNumLineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridlayout1.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridlayout2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridlayout2.setContentsMargins(9, 9, 9, 9)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")
        self.creditCardLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.creditCardLineEdit.setObjectName("creditCardLineEdit")
        self.gridlayout2.addWidget(self.creditCardLineEdit, 0, 1, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.gridlayout2.addWidget(self.label_11, 0, 0, 1, 1)
        self.expiryDateEdit = QtWidgets.QDateEdit(self.tab_3)
        self.expiryDateEdit.setAlignment(QtCore.Qt.AlignRight)
        self.expiryDateEdit.setObjectName("expiryDateEdit")
        self.gridlayout2.addWidget(self.expiryDateEdit, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.gridlayout2.addWidget(self.label_10, 1, 2, 1, 1)
        self.validFromDateEdit = QtWidgets.QDateEdit(self.tab_3)
        self.validFromDateEdit.setAlignment(QtCore.Qt.AlignRight)
        self.validFromDateEdit.setObjectName("validFromDateEdit")
        self.gridlayout2.addWidget(self.validFromDateEdit, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.gridlayout2.addWidget(self.label_9, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridlayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridlayout3 = QtWidgets.QGridLayout()
        self.gridlayout3.setContentsMargins(0, 0, 0, 0)
        self.gridlayout3.setSpacing(6)
        self.gridlayout3.setObjectName("gridlayout3")
        self.label_3 = QtWidgets.QLabel(PaymentDlg)
        self.label_3.setObjectName("label_3")
        self.gridlayout3.addWidget(self.label_3, 0, 2, 1, 1)
        self.amountSpinBox = QtWidgets.QDoubleSpinBox(PaymentDlg)
        self.amountSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.amountSpinBox.setMaximum(999999.0)
        self.amountSpinBox.setObjectName("amountSpinBox")
        self.gridlayout3.addWidget(self.amountSpinBox, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(PaymentDlg)
        self.label.setObjectName("label")
        self.gridlayout3.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(PaymentDlg)
        self.label_5.setObjectName("label_5")
        self.gridlayout3.addWidget(self.label_5, 1, 0, 1, 1)
        self.surnameLineEdit = QtWidgets.QLineEdit(PaymentDlg)
        self.surnameLineEdit.setObjectName("surnameLineEdit")
        self.gridlayout3.addWidget(self.surnameLineEdit, 0, 3, 1, 1)
        self.forenameLineEdit = QtWidgets.QLineEdit(PaymentDlg)
        self.forenameLineEdit.setObjectName("forenameLineEdit")
        self.gridlayout3.addWidget(self.forenameLineEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(PaymentDlg)
        self.label_4.setObjectName("label_4")
        self.gridlayout3.addWidget(self.label_4, 1, 2, 1, 1)
        self.invoiceNumSpinBox = QtWidgets.QSpinBox(PaymentDlg)
        self.invoiceNumSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.invoiceNumSpinBox.setMaximum(999999999)
        self.invoiceNumSpinBox.setMinimum(1000000)
        self.invoiceNumSpinBox.setProperty("value", 1000000)
        self.invoiceNumSpinBox.setObjectName("invoiceNumSpinBox")
        self.gridlayout3.addWidget(self.invoiceNumSpinBox, 1, 1, 1, 1)
        self.gridlayout.addLayout(self.gridlayout3, 0, 0, 1, 1)
        self.label_8.setBuddy(self.sortCodeLineEdit)
        self.label_7.setBuddy(self.bankLineEdit)
        self.label_6.setBuddy(self.accountNumLineEdit)
        self.label_2.setBuddy(self.checkNumLineEdit)
        self.label_11.setBuddy(self.creditCardLineEdit)
        self.label_10.setBuddy(self.expiryDateEdit)
        self.label_9.setBuddy(self.validFromDateEdit)
        self.label_3.setBuddy(self.surnameLineEdit)
        self.label.setBuddy(self.forenameLineEdit)
        self.label_5.setBuddy(self.invoiceNumSpinBox)
        self.label_4.setBuddy(self.amountSpinBox)

        self.retranslateUi(PaymentDlg)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(PaymentDlg.accept)
        self.buttonBox.rejected.connect(PaymentDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(PaymentDlg)
        PaymentDlg.setTabOrder(self.forenameLineEdit, self.surnameLineEdit)
        PaymentDlg.setTabOrder(self.surnameLineEdit, self.invoiceNumSpinBox)
        PaymentDlg.setTabOrder(self.invoiceNumSpinBox, self.amountSpinBox)
        PaymentDlg.setTabOrder(self.amountSpinBox, self.tabWidget)
        PaymentDlg.setTabOrder(self.tabWidget, self.paidCheckBox)
        PaymentDlg.setTabOrder(self.paidCheckBox, self.checkNumLineEdit)
        PaymentDlg.setTabOrder(self.checkNumLineEdit, self.accountNumLineEdit)
        PaymentDlg.setTabOrder(self.accountNumLineEdit, self.bankLineEdit)
        PaymentDlg.setTabOrder(self.bankLineEdit, self.sortCodeLineEdit)
        PaymentDlg.setTabOrder(self.sortCodeLineEdit, self.creditCardLineEdit)
        PaymentDlg.setTabOrder(self.creditCardLineEdit, self.validFromDateEdit)
        PaymentDlg.setTabOrder(self.validFromDateEdit, self.expiryDateEdit)

    def retranslateUi(self, PaymentDlg):
        _translate = QtCore.QCoreApplication.translate
        PaymentDlg.setWindowTitle(_translate("PaymentDlg", "Payment Form"))
        self.paidCheckBox.setText(_translate("PaymentDlg", "&Paid"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PaymentDlg", "Cas&h"))
        self.label_8.setText(_translate("PaymentDlg", "S&ort Code:"))
        self.label_7.setText(_translate("PaymentDlg", "&Bank:"))
        self.label_6.setText(_translate("PaymentDlg", "A&ccount No.:"))
        self.label_2.setText(_translate("PaymentDlg", "Check &No.:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PaymentDlg", "Chec&k"))
        self.label_11.setText(_translate("PaymentDlg", "&Number:"))
        self.expiryDateEdit.setDisplayFormat(_translate("PaymentDlg", "MMM yyyy"))
        self.label_10.setText(_translate("PaymentDlg", "E&xpiry Date"))
        self.validFromDateEdit.setDisplayFormat(_translate("PaymentDlg", "MMM yyyy"))
        self.label_9.setText(_translate("PaymentDlg", "&Valid From:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("PaymentDlg", "Credit Car&d"))
        self.label_3.setText(_translate("PaymentDlg", "&Surname:"))
        self.amountSpinBox.setPrefix(_translate("PaymentDlg", "$ "))
        self.label.setText(_translate("PaymentDlg", "&Forename:"))
        self.label_5.setText(_translate("PaymentDlg", "&Invoice No.:"))
        self.label_4.setText(_translate("PaymentDlg", "&Amount:"))

# -*- coding: utf-8 -*-

"""
Module implementing PaymentDlg.
"""

from PyQt5.QtCore import pyqtSlot,QDate
from PyQt5.QtWidgets import QDialog,QApplication,QDialogButtonBox
import sys
# from Ui_paymentdlg import Ui_PaymentDlg


class PaymentDlg(QDialog, Ui_PaymentDlg):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(PaymentDlg, self).__init__(parent)
        self.setupUi(self)
        for lineEdit in (self.forenameLineEdit, self.surnameLineEdit,
                         self.checkNumLineEdit, self.accountNumLineEdit,
                         self.bankLineEdit, self.sortCodeLineEdit,
                         self.creditCardLineEdit):
            lineEdit.textEdited.connect(self.updateUi)
        for dateEdit in (self.validFromDateEdit, self.expiryDateEdit):
            dateEdit.dateChanged.connect(self.updateUi)
        self.paidCheckBox.clicked.connect(self.updateUi)
        self.updateUi()
        self.forenameLineEdit.setFocus()

    def updateUi(self):
        today = QDate.currentDate()
        enable = (self.forenameLineEdit.text() and
                       self.surnameLineEdit.text())
        if enable:
            enable = (self.paidCheckBox.isChecked() or
                  (self.checkNumLineEdit.text() and
                        self.accountNumLineEdit.text() and
                        self.bankLineEdit.text() and
                        self.sortCodeLineEdit.text()) or
                  (self.creditCardLineEdit.text() and
                   self.validFromDateEdit.date() <= today and
                   self.expiryDateEdit.date() >= today))
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(bool(enable))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = PaymentDlg()
    form.show()
    app.exec_()
    print("test")