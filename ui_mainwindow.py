# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(692, 513)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_43 = QLabel(self.centralwidget)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout.addWidget(self.label_43, 0, 0, 1, 1)

        self.Fecha_general_lineEdit = QLineEdit(self.centralwidget)
        self.Fecha_general_lineEdit.setObjectName(u"Fecha_general_lineEdit")

        self.gridLayout.addWidget(self.Fecha_general_lineEdit, 0, 1, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_6 = QGridLayout(self.tab_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget_6 = QTabWidget(self.tab_7)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tab_26 = QWidget()
        self.tab_26.setObjectName(u"tab_26")
        self.gridLayout_29 = QGridLayout(self.tab_26)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_46 = QLabel(self.tab_26)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_29.addWidget(self.label_46, 0, 0, 1, 1)

        self.idventa_vent_reg_lineEdit = QLineEdit(self.tab_26)
        self.idventa_vent_reg_lineEdit.setObjectName(u"idventa_vent_reg_lineEdit")

        self.gridLayout_29.addWidget(self.idventa_vent_reg_lineEdit, 0, 1, 1, 1)

        self.label_49 = QLabel(self.tab_26)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_29.addWidget(self.label_49, 0, 2, 1, 1)

        self.fecha_vent_reg_lineEdit = QLineEdit(self.tab_26)
        self.fecha_vent_reg_lineEdit.setObjectName(u"fecha_vent_reg_lineEdit")

        self.gridLayout_29.addWidget(self.fecha_vent_reg_lineEdit, 0, 3, 1, 2)

        self.label_50 = QLabel(self.tab_26)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_29.addWidget(self.label_50, 0, 5, 1, 1)

        self.subtotal_vent_reg_lineEdit = QLineEdit(self.tab_26)
        self.subtotal_vent_reg_lineEdit.setObjectName(u"subtotal_vent_reg_lineEdit")

        self.gridLayout_29.addWidget(self.subtotal_vent_reg_lineEdit, 0, 6, 1, 1)

        self.label_51 = QLabel(self.tab_26)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_29.addWidget(self.label_51, 0, 7, 1, 1)

        self.iva_vent_reg_lineEdit = QLineEdit(self.tab_26)
        self.iva_vent_reg_lineEdit.setObjectName(u"iva_vent_reg_lineEdit")

        self.gridLayout_29.addWidget(self.iva_vent_reg_lineEdit, 0, 8, 1, 1)

        self.label_52 = QLabel(self.tab_26)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_29.addWidget(self.label_52, 0, 9, 1, 1)

        self.total_vent_reg_lineEdit = QLineEdit(self.tab_26)
        self.total_vent_reg_lineEdit.setObjectName(u"total_vent_reg_lineEdit")

        self.gridLayout_29.addWidget(self.total_vent_reg_lineEdit, 0, 10, 1, 1)

        self.groupBox_9 = QGroupBox(self.tab_26)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_23 = QGridLayout(self.groupBox_9)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.idproducto_venta_reg_lineEdit = QLineEdit(self.groupBox_9)
        self.idproducto_venta_reg_lineEdit.setObjectName(u"idproducto_venta_reg_lineEdit")

        self.gridLayout_23.addWidget(self.idproducto_venta_reg_lineEdit, 6, 1, 1, 1)

        self.idcliente_venta_reg_lineEdit = QLineEdit(self.groupBox_9)
        self.idcliente_venta_reg_lineEdit.setObjectName(u"idcliente_venta_reg_lineEdit")

        self.gridLayout_23.addWidget(self.idcliente_venta_reg_lineEdit, 3, 1, 1, 1)

        self.label_34 = QLabel(self.groupBox_9)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_23.addWidget(self.label_34, 7, 0, 1, 1)

        self.label_37 = QLabel(self.groupBox_9)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_23.addWidget(self.label_37, 9, 0, 1, 1)

        self.label_35 = QLabel(self.groupBox_9)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_23.addWidget(self.label_35, 2, 0, 1, 1)

        self.venta_registrar_pushButton = QPushButton(self.groupBox_9)
        self.venta_registrar_pushButton.setObjectName(u"venta_registrar_pushButton")

        self.gridLayout_23.addWidget(self.venta_registrar_pushButton, 10, 0, 1, 2)

        self.label_36 = QLabel(self.groupBox_9)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_23.addWidget(self.label_36, 3, 0, 1, 1)

        self.label_33 = QLabel(self.groupBox_9)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_23.addWidget(self.label_33, 6, 0, 1, 1)

        self.pago_venta_reg_lineEdit = QLineEdit(self.groupBox_9)
        self.pago_venta_reg_lineEdit.setObjectName(u"pago_venta_reg_lineEdit")

        self.gridLayout_23.addWidget(self.pago_venta_reg_lineEdit, 9, 1, 1, 1)

        self.cantidadproducto_venta_reg_spinBox = QSpinBox(self.groupBox_9)
        self.cantidadproducto_venta_reg_spinBox.setObjectName(u"cantidadproducto_venta_reg_spinBox")
        self.cantidadproducto_venta_reg_spinBox.setMaximum(99999)

        self.gridLayout_23.addWidget(self.cantidadproducto_venta_reg_spinBox, 7, 1, 1, 1)

        self.idempleado_venta_reg_lineEdit = QLineEdit(self.groupBox_9)
        self.idempleado_venta_reg_lineEdit.setObjectName(u"idempleado_venta_reg_lineEdit")

        self.gridLayout_23.addWidget(self.idempleado_venta_reg_lineEdit, 2, 1, 1, 1)

        self.venta_agregar_pushButton = QPushButton(self.groupBox_9)
        self.venta_agregar_pushButton.setObjectName(u"venta_agregar_pushButton")

        self.gridLayout_23.addWidget(self.venta_agregar_pushButton, 8, 0, 1, 2)


        self.gridLayout_29.addWidget(self.groupBox_9, 1, 0, 1, 4)

        self.tabla_general_most = QTableWidget(self.tab_26)
        self.tabla_general_most.setObjectName(u"tabla_general_most")

        self.gridLayout_29.addWidget(self.tabla_general_most, 1, 4, 1, 7)

        self.tabWidget_6.addTab(self.tab_26, "")
        self.tab_27 = QWidget()
        self.tab_27.setObjectName(u"tab_27")
        self.gridLayout_24 = QGridLayout(self.tab_27)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.tabla_venta_cons = QTableWidget(self.tab_27)
        self.tabla_venta_cons.setObjectName(u"tabla_venta_cons")

        self.gridLayout_24.addWidget(self.tabla_venta_cons, 0, 0, 1, 2)

        self.id_venta_cons_lineEdit = QLineEdit(self.tab_27)
        self.id_venta_cons_lineEdit.setObjectName(u"id_venta_cons_lineEdit")

        self.gridLayout_24.addWidget(self.id_venta_cons_lineEdit, 1, 0, 1, 1)

        self.venta_consultar_pushButton = QPushButton(self.tab_27)
        self.venta_consultar_pushButton.setObjectName(u"venta_consultar_pushButton")

        self.gridLayout_24.addWidget(self.venta_consultar_pushButton, 1, 1, 1, 1)

        self.tabWidget_6.addTab(self.tab_27, "")

        self.gridLayout_6.addWidget(self.tabWidget_6, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 201, 201))
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_9.addWidget(self.label_2, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_9.addWidget(self.label, 2, 0, 1, 1)

        self.telefono_empleado_reg_lineEdit_2 = QLineEdit(self.groupBox)
        self.telefono_empleado_reg_lineEdit_2.setObjectName(u"telefono_empleado_reg_lineEdit_2")
        self.telefono_empleado_reg_lineEdit_2.setMaxLength(10)

        self.gridLayout_9.addWidget(self.telefono_empleado_reg_lineEdit_2, 3, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_9.addWidget(self.label_3, 4, 0, 1, 1)

        self.status_empleado_reg_spinBox = QSpinBox(self.groupBox)
        self.status_empleado_reg_spinBox.setObjectName(u"status_empleado_reg_spinBox")
        self.status_empleado_reg_spinBox.setMaximum(1)

        self.gridLayout_9.addWidget(self.status_empleado_reg_spinBox, 4, 1, 1, 1)

        self.nombre_empleado_reg_lineEdit = QLineEdit(self.groupBox)
        self.nombre_empleado_reg_lineEdit.setObjectName(u"nombre_empleado_reg_lineEdit")
        self.nombre_empleado_reg_lineEdit.setMaxLength(35)

        self.gridLayout_9.addWidget(self.nombre_empleado_reg_lineEdit, 2, 1, 1, 1)

        self.empleado_registrar_pushButton = QPushButton(self.groupBox)
        self.empleado_registrar_pushButton.setObjectName(u"empleado_registrar_pushButton")

        self.gridLayout_9.addWidget(self.empleado_registrar_pushButton, 5, 0, 1, 2)

        self.idempleado_reg_lineEdit = QLineEdit(self.groupBox)
        self.idempleado_reg_lineEdit.setObjectName(u"idempleado_reg_lineEdit")

        self.gridLayout_9.addWidget(self.idempleado_reg_lineEdit, 0, 1, 1, 1)

        self.label_53 = QLabel(self.groupBox)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_9.addWidget(self.label_53, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_32 = QGridLayout(self.tab_5)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.groupBox_2 = QGroupBox(self.tab_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_10 = QGridLayout(self.groupBox_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_10.addWidget(self.label_6, 2, 0, 1, 1)

        self.nombre_empleado_mod_lineEdit = QLineEdit(self.groupBox_2)
        self.nombre_empleado_mod_lineEdit.setObjectName(u"nombre_empleado_mod_lineEdit")

        self.gridLayout_10.addWidget(self.nombre_empleado_mod_lineEdit, 1, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_10.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_10.addWidget(self.label_5, 1, 0, 1, 1)

        self.telefono_empleado_mod_lineEdit = QLineEdit(self.groupBox_2)
        self.telefono_empleado_mod_lineEdit.setObjectName(u"telefono_empleado_mod_lineEdit")
        self.telefono_empleado_mod_lineEdit.setMaxLength(10)

        self.gridLayout_10.addWidget(self.telefono_empleado_mod_lineEdit, 2, 1, 1, 1)

        self.id_empleado_mod_lineEdit = QLineEdit(self.groupBox_2)
        self.id_empleado_mod_lineEdit.setObjectName(u"id_empleado_mod_lineEdit")

        self.gridLayout_10.addWidget(self.id_empleado_mod_lineEdit, 0, 1, 1, 1)

        self.empleado_modificar_pushButton = QPushButton(self.groupBox_2)
        self.empleado_modificar_pushButton.setObjectName(u"empleado_modificar_pushButton")

        self.gridLayout_10.addWidget(self.empleado_modificar_pushButton, 4, 1, 1, 1)

        self.status_empleado_mod_spinBox = QSpinBox(self.groupBox_2)
        self.status_empleado_mod_spinBox.setObjectName(u"status_empleado_mod_spinBox")
        self.status_empleado_mod_spinBox.setMaximum(1)

        self.gridLayout_10.addWidget(self.status_empleado_mod_spinBox, 3, 1, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tabla_empleado_mod_general_most = QTableWidget(self.tab_5)
        self.tabla_empleado_mod_general_most.setObjectName(u"tabla_empleado_mod_general_most")

        self.gridLayout_32.addWidget(self.tabla_empleado_mod_general_most, 0, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_11 = QGridLayout(self.tab_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tabla_empleado_cons = QTableWidget(self.tab_10)
        self.tabla_empleado_cons.setObjectName(u"tabla_empleado_cons")

        self.gridLayout_11.addWidget(self.tabla_empleado_cons, 0, 0, 1, 2)

        self.id_empleado_cons_lineEdit = QLineEdit(self.tab_10)
        self.id_empleado_cons_lineEdit.setObjectName(u"id_empleado_cons_lineEdit")

        self.gridLayout_11.addWidget(self.id_empleado_cons_lineEdit, 1, 0, 1, 1)

        self.empleado_consultar_pushButton = QPushButton(self.tab_10)
        self.empleado_consultar_pushButton.setObjectName(u"empleado_consultar_pushButton")

        self.gridLayout_11.addWidget(self.empleado_consultar_pushButton, 1, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_12 = QGridLayout(self.tab_11)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.tabla_empleado_most = QTableWidget(self.tab_11)
        self.tabla_empleado_most.setObjectName(u"tabla_empleado_most")

        self.gridLayout_12.addWidget(self.tabla_empleado_most, 0, 0, 1, 1)

        self.empleado_mostrar_pushButton = QPushButton(self.tab_11)
        self.empleado_mostrar_pushButton.setObjectName(u"empleado_mostrar_pushButton")

        self.gridLayout_12.addWidget(self.empleado_mostrar_pushButton, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_11, "")

        self.gridLayout_3.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget_3 = QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.formLayout = QFormLayout(self.tab_12)
        self.formLayout.setObjectName(u"formLayout")
        self.groupBox_3 = QGroupBox(self.tab_12)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_13 = QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_13.addWidget(self.label_10, 3, 0, 1, 1)

        self.direccion_cliente_reg_lineEdit = QLineEdit(self.groupBox_3)
        self.direccion_cliente_reg_lineEdit.setObjectName(u"direccion_cliente_reg_lineEdit")

        self.gridLayout_13.addWidget(self.direccion_cliente_reg_lineEdit, 2, 1, 1, 1)

        self.cliente_registrar_pushButton = QPushButton(self.groupBox_3)
        self.cliente_registrar_pushButton.setObjectName(u"cliente_registrar_pushButton")

        self.gridLayout_13.addWidget(self.cliente_registrar_pushButton, 4, 0, 1, 2)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_13.addWidget(self.label_8, 1, 0, 1, 1)

        self.puntos_cliente_reg_lineEdit = QLineEdit(self.groupBox_3)
        self.puntos_cliente_reg_lineEdit.setObjectName(u"puntos_cliente_reg_lineEdit")
        self.puntos_cliente_reg_lineEdit.setMaxLength(8)

        self.gridLayout_13.addWidget(self.puntos_cliente_reg_lineEdit, 3, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_13.addWidget(self.label_9, 2, 0, 1, 1)

        self.nombre_cliente_reg_lineEdit = QLineEdit(self.groupBox_3)
        self.nombre_cliente_reg_lineEdit.setObjectName(u"nombre_cliente_reg_lineEdit")

        self.gridLayout_13.addWidget(self.nombre_cliente_reg_lineEdit, 1, 1, 1, 1)

        self.label_54 = QLabel(self.groupBox_3)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_13.addWidget(self.label_54, 0, 0, 1, 1)

        self.idcliente_reg_lineEdit = QLineEdit(self.groupBox_3)
        self.idcliente_reg_lineEdit.setObjectName(u"idcliente_reg_lineEdit")

        self.gridLayout_13.addWidget(self.idcliente_reg_lineEdit, 0, 1, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.groupBox_3)

        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_33 = QGridLayout(self.tab_13)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.groupBox_4 = QGroupBox(self.tab_13)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_14 = QGridLayout(self.groupBox_4)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.cliente_modificar_pushButton = QPushButton(self.groupBox_4)
        self.cliente_modificar_pushButton.setObjectName(u"cliente_modificar_pushButton")

        self.gridLayout_14.addWidget(self.cliente_modificar_pushButton, 5, 1, 1, 2)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_14.addWidget(self.label_13, 3, 0, 1, 2)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_14.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_14.addWidget(self.label_12, 2, 0, 1, 2)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_14.addWidget(self.label_14, 4, 0, 1, 2)

        self.nombre_cliente_mod_lineEdit = QLineEdit(self.groupBox_4)
        self.nombre_cliente_mod_lineEdit.setObjectName(u"nombre_cliente_mod_lineEdit")
        self.nombre_cliente_mod_lineEdit.setMaxLength(45)

        self.gridLayout_14.addWidget(self.nombre_cliente_mod_lineEdit, 2, 2, 1, 1)

        self.direccion_cliente_mod_lineEdit = QLineEdit(self.groupBox_4)
        self.direccion_cliente_mod_lineEdit.setObjectName(u"direccion_cliente_mod_lineEdit")
        self.direccion_cliente_mod_lineEdit.setMaxLength(150)

        self.gridLayout_14.addWidget(self.direccion_cliente_mod_lineEdit, 3, 2, 1, 1)

        self.puntos_cliente_mod_lineEdit = QLineEdit(self.groupBox_4)
        self.puntos_cliente_mod_lineEdit.setObjectName(u"puntos_cliente_mod_lineEdit")
        self.puntos_cliente_mod_lineEdit.setMaxLength(8)

        self.gridLayout_14.addWidget(self.puntos_cliente_mod_lineEdit, 4, 2, 1, 1)

        self.id_cliente_mod_lineEdit = QLineEdit(self.groupBox_4)
        self.id_cliente_mod_lineEdit.setObjectName(u"id_cliente_mod_lineEdit")

        self.gridLayout_14.addWidget(self.id_cliente_mod_lineEdit, 0, 2, 1, 1)


        self.gridLayout_33.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.tabla_cliente_mod_general_most = QTableWidget(self.tab_13)
        self.tabla_cliente_mod_general_most.setObjectName(u"tabla_cliente_mod_general_most")

        self.gridLayout_33.addWidget(self.tabla_cliente_mod_general_most, 0, 1, 1, 1)

        self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_15 = QGridLayout(self.tab_14)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.tabla_cliente_cons = QTableWidget(self.tab_14)
        self.tabla_cliente_cons.setObjectName(u"tabla_cliente_cons")

        self.gridLayout_15.addWidget(self.tabla_cliente_cons, 0, 0, 1, 2)

        self.id_cliente_cons_lineEdit = QLineEdit(self.tab_14)
        self.id_cliente_cons_lineEdit.setObjectName(u"id_cliente_cons_lineEdit")

        self.gridLayout_15.addWidget(self.id_cliente_cons_lineEdit, 1, 0, 1, 1)

        self.cliente_consultar_pushButton = QPushButton(self.tab_14)
        self.cliente_consultar_pushButton.setObjectName(u"cliente_consultar_pushButton")

        self.gridLayout_15.addWidget(self.cliente_consultar_pushButton, 1, 1, 1, 1)

        self.tabWidget_3.addTab(self.tab_14, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.formLayout_2 = QFormLayout(self.tab_15)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.tabla_cliente_most = QTableWidget(self.tab_15)
        self.tabla_cliente_most.setObjectName(u"tabla_cliente_most")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.tabla_cliente_most)

        self.cliente_mostrar_pushButton = QPushButton(self.tab_15)
        self.cliente_mostrar_pushButton.setObjectName(u"cliente_mostrar_pushButton")

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.cliente_mostrar_pushButton)

        self.tabWidget_3.addTab(self.tab_15, "")

        self.gridLayout_2.addWidget(self.tabWidget_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget_4 = QTabWidget(self.tab_3)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.groupBox_5 = QGroupBox(self.tab_18)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 10, 191, 151))
        self.formLayout_3 = QFormLayout(self.groupBox_5)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.nombre_proveedor_reg_lineEdit = QLineEdit(self.groupBox_5)
        self.nombre_proveedor_reg_lineEdit.setObjectName(u"nombre_proveedor_reg_lineEdit")
        self.nombre_proveedor_reg_lineEdit.setMaxLength(35)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.nombre_proveedor_reg_lineEdit)

        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_16)

        self.telefono_proveedor_reg_lineEdit = QLineEdit(self.groupBox_5)
        self.telefono_proveedor_reg_lineEdit.setObjectName(u"telefono_proveedor_reg_lineEdit")
        self.telefono_proveedor_reg_lineEdit.setMaxLength(10)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.telefono_proveedor_reg_lineEdit)

        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_17)

        self.celular_proveedor_reg_lineEdit = QLineEdit(self.groupBox_5)
        self.celular_proveedor_reg_lineEdit.setObjectName(u"celular_proveedor_reg_lineEdit")
        self.celular_proveedor_reg_lineEdit.setMaxLength(10)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.celular_proveedor_reg_lineEdit)

        self.proveedor_registrar_pushButton = QPushButton(self.groupBox_5)
        self.proveedor_registrar_pushButton.setObjectName(u"proveedor_registrar_pushButton")

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.proveedor_registrar_pushButton)

        self.label_56 = QLabel(self.groupBox_5)
        self.label_56.setObjectName(u"label_56")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_56)

        self.idproveedor_reg_lineEdit_2 = QLineEdit(self.groupBox_5)
        self.idproveedor_reg_lineEdit_2.setObjectName(u"idproveedor_reg_lineEdit_2")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.idproveedor_reg_lineEdit_2)

        self.tabWidget_4.addTab(self.tab_18, "")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.gridLayout_34 = QGridLayout(self.tab_19)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.groupBox_6 = QGroupBox(self.tab_19)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_16 = QGridLayout(self.groupBox_6)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_20 = QLabel(self.groupBox_6)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_16.addWidget(self.label_20, 2, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_16.addWidget(self.label_18, 0, 0, 1, 1)

        self.celular_proveedor_mod_lineEdit = QLineEdit(self.groupBox_6)
        self.celular_proveedor_mod_lineEdit.setObjectName(u"celular_proveedor_mod_lineEdit")
        self.celular_proveedor_mod_lineEdit.setMaxLength(10)

        self.gridLayout_16.addWidget(self.celular_proveedor_mod_lineEdit, 3, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_6)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_16.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_6)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_16.addWidget(self.label_21, 3, 0, 1, 1)

        self.id_proveedor_mod_lineEdit = QLineEdit(self.groupBox_6)
        self.id_proveedor_mod_lineEdit.setObjectName(u"id_proveedor_mod_lineEdit")

        self.gridLayout_16.addWidget(self.id_proveedor_mod_lineEdit, 0, 1, 1, 1)

        self.nombre_proveedor_mod_lineEdit = QLineEdit(self.groupBox_6)
        self.nombre_proveedor_mod_lineEdit.setObjectName(u"nombre_proveedor_mod_lineEdit")

        self.gridLayout_16.addWidget(self.nombre_proveedor_mod_lineEdit, 1, 1, 1, 1)

        self.proveedor_modificar_pushButton = QPushButton(self.groupBox_6)
        self.proveedor_modificar_pushButton.setObjectName(u"proveedor_modificar_pushButton")

        self.gridLayout_16.addWidget(self.proveedor_modificar_pushButton, 4, 1, 1, 1)

        self.telefono_proveedor_mod_lineEdit = QLineEdit(self.groupBox_6)
        self.telefono_proveedor_mod_lineEdit.setObjectName(u"telefono_proveedor_mod_lineEdit")
        self.telefono_proveedor_mod_lineEdit.setMaxLength(10)

        self.gridLayout_16.addWidget(self.telefono_proveedor_mod_lineEdit, 2, 1, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.tabla_proveedor_mod_general_most = QTableWidget(self.tab_19)
        self.tabla_proveedor_mod_general_most.setObjectName(u"tabla_proveedor_mod_general_most")

        self.gridLayout_34.addWidget(self.tabla_proveedor_mod_general_most, 0, 1, 1, 1)

        self.tabWidget_4.addTab(self.tab_19, "")
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.gridLayout_17 = QGridLayout(self.tab_20)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tabla_proveedor_cons = QTableWidget(self.tab_20)
        self.tabla_proveedor_cons.setObjectName(u"tabla_proveedor_cons")

        self.gridLayout_17.addWidget(self.tabla_proveedor_cons, 0, 0, 1, 2)

        self.id_proveedor_cons_lineEdit = QLineEdit(self.tab_20)
        self.id_proveedor_cons_lineEdit.setObjectName(u"id_proveedor_cons_lineEdit")

        self.gridLayout_17.addWidget(self.id_proveedor_cons_lineEdit, 1, 0, 1, 1)

        self.provvedor_consultar_pushButton = QPushButton(self.tab_20)
        self.provvedor_consultar_pushButton.setObjectName(u"provvedor_consultar_pushButton")

        self.gridLayout_17.addWidget(self.provvedor_consultar_pushButton, 1, 1, 1, 1)

        self.tabWidget_4.addTab(self.tab_20, "")
        self.tab_21 = QWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.gridLayout_18 = QGridLayout(self.tab_21)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.tabla_proveedor_most = QTableWidget(self.tab_21)
        self.tabla_proveedor_most.setObjectName(u"tabla_proveedor_most")

        self.gridLayout_18.addWidget(self.tabla_proveedor_most, 0, 0, 1, 1)

        self.proveedor_mostrar_pushButton = QPushButton(self.tab_21)
        self.proveedor_mostrar_pushButton.setObjectName(u"proveedor_mostrar_pushButton")

        self.gridLayout_18.addWidget(self.proveedor_mostrar_pushButton, 1, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_21, "")

        self.gridLayout_4.addWidget(self.tabWidget_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_5 = QGridLayout(self.tab_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget_5 = QTabWidget(self.tab_6)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.gridLayout_36 = QGridLayout(self.tab_22)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.groupBox_7 = QGroupBox(self.tab_22)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_19 = QGridLayout(self.groupBox_7)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.idprovee_producto_reg_lineEdit = QLineEdit(self.groupBox_7)
        self.idprovee_producto_reg_lineEdit.setObjectName(u"idprovee_producto_reg_lineEdit")

        self.gridLayout_19.addWidget(self.idprovee_producto_reg_lineEdit, 4, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_7)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_19.addWidget(self.label_24, 3, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_7)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_19.addWidget(self.label_23, 2, 0, 1, 1)

        self.preciovent_producto_reg_lineEdit = QLineEdit(self.groupBox_7)
        self.preciovent_producto_reg_lineEdit.setObjectName(u"preciovent_producto_reg_lineEdit")

        self.gridLayout_19.addWidget(self.preciovent_producto_reg_lineEdit, 3, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_7)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_19.addWidget(self.label_25, 4, 0, 1, 1)

        self.preciocomp_producto_reg_lineEdit = QLineEdit(self.groupBox_7)
        self.preciocomp_producto_reg_lineEdit.setObjectName(u"preciocomp_producto_reg_lineEdit")

        self.gridLayout_19.addWidget(self.preciocomp_producto_reg_lineEdit, 2, 1, 1, 1)

        self.nombre_producto_reg_lineEdit = QLineEdit(self.groupBox_7)
        self.nombre_producto_reg_lineEdit.setObjectName(u"nombre_producto_reg_lineEdit")
        self.nombre_producto_reg_lineEdit.setMaxLength(45)

        self.gridLayout_19.addWidget(self.nombre_producto_reg_lineEdit, 1, 1, 1, 1)

        self.producto_registrar_pushButton = QPushButton(self.groupBox_7)
        self.producto_registrar_pushButton.setObjectName(u"producto_registrar_pushButton")

        self.gridLayout_19.addWidget(self.producto_registrar_pushButton, 6, 0, 1, 2)

        self.cantidad_producto_reg_lineEdit = QLineEdit(self.groupBox_7)
        self.cantidad_producto_reg_lineEdit.setObjectName(u"cantidad_producto_reg_lineEdit")
        self.cantidad_producto_reg_lineEdit.setMaxLength(5)

        self.gridLayout_19.addWidget(self.cantidad_producto_reg_lineEdit, 5, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_7)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_19.addWidget(self.label_22, 1, 0, 1, 1)

        self.label_26 = QLabel(self.groupBox_7)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_19.addWidget(self.label_26, 5, 0, 1, 1)

        self.label_55 = QLabel(self.groupBox_7)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_19.addWidget(self.label_55, 0, 0, 1, 1)

        self.idproducto_reg_lineEdit = QLineEdit(self.groupBox_7)
        self.idproducto_reg_lineEdit.setObjectName(u"idproducto_reg_lineEdit")

        self.gridLayout_19.addWidget(self.idproducto_reg_lineEdit, 0, 1, 1, 1)


        self.gridLayout_36.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.tabla_producto_reg_general_most = QTableWidget(self.tab_22)
        self.tabla_producto_reg_general_most.setObjectName(u"tabla_producto_reg_general_most")

        self.gridLayout_36.addWidget(self.tabla_producto_reg_general_most, 0, 1, 1, 1)

        self.tabWidget_5.addTab(self.tab_22, "")
        self.tab_24 = QWidget()
        self.tab_24.setObjectName(u"tab_24")
        self.gridLayout_35 = QGridLayout(self.tab_24)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.groupBox_8 = QGroupBox(self.tab_24)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_20 = QGridLayout(self.groupBox_8)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.idprovee_producto_mod_lineEdit = QLineEdit(self.groupBox_8)
        self.idprovee_producto_mod_lineEdit.setObjectName(u"idprovee_producto_mod_lineEdit")

        self.gridLayout_20.addWidget(self.idprovee_producto_mod_lineEdit, 4, 1, 1, 1)

        self.label_31 = QLabel(self.groupBox_8)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_20.addWidget(self.label_31, 4, 0, 1, 1)

        self.preciocomp_producto_mod_lineEdit = QLineEdit(self.groupBox_8)
        self.preciocomp_producto_mod_lineEdit.setObjectName(u"preciocomp_producto_mod_lineEdit")

        self.gridLayout_20.addWidget(self.preciocomp_producto_mod_lineEdit, 2, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox_8)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_20.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox_8)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_20.addWidget(self.label_32, 5, 0, 1, 1)

        self.label_30 = QLabel(self.groupBox_8)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_20.addWidget(self.label_30, 3, 0, 1, 1)

        self.id_product_mod_lineEdit = QLineEdit(self.groupBox_8)
        self.id_product_mod_lineEdit.setObjectName(u"id_product_mod_lineEdit")

        self.gridLayout_20.addWidget(self.id_product_mod_lineEdit, 0, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_8)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_20.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_28 = QLabel(self.groupBox_8)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_20.addWidget(self.label_28, 1, 0, 1, 1)

        self.preciovent_producto_mod_lineEdit = QLineEdit(self.groupBox_8)
        self.preciovent_producto_mod_lineEdit.setObjectName(u"preciovent_producto_mod_lineEdit")

        self.gridLayout_20.addWidget(self.preciovent_producto_mod_lineEdit, 3, 1, 1, 1)

        self.nombre_producto_mod_lineEdit = QLineEdit(self.groupBox_8)
        self.nombre_producto_mod_lineEdit.setObjectName(u"nombre_producto_mod_lineEdit")

        self.gridLayout_20.addWidget(self.nombre_producto_mod_lineEdit, 1, 1, 1, 1)

        self.cantidad_producto_mod_lineEdit = QLineEdit(self.groupBox_8)
        self.cantidad_producto_mod_lineEdit.setObjectName(u"cantidad_producto_mod_lineEdit")
        self.cantidad_producto_mod_lineEdit.setMaxLength(5)

        self.gridLayout_20.addWidget(self.cantidad_producto_mod_lineEdit, 5, 1, 1, 1)

        self.producto_modificar_pushButton = QPushButton(self.groupBox_8)
        self.producto_modificar_pushButton.setObjectName(u"producto_modificar_pushButton")

        self.gridLayout_20.addWidget(self.producto_modificar_pushButton, 6, 0, 1, 2)


        self.gridLayout_35.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.tabla_producto_mod_general_most = QTableWidget(self.tab_24)
        self.tabla_producto_mod_general_most.setObjectName(u"tabla_producto_mod_general_most")

        self.gridLayout_35.addWidget(self.tabla_producto_mod_general_most, 0, 1, 1, 1)

        self.tabWidget_5.addTab(self.tab_24, "")
        self.tab_23 = QWidget()
        self.tab_23.setObjectName(u"tab_23")
        self.gridLayout_21 = QGridLayout(self.tab_23)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.tabla_producto_cons = QTableWidget(self.tab_23)
        self.tabla_producto_cons.setObjectName(u"tabla_producto_cons")

        self.gridLayout_21.addWidget(self.tabla_producto_cons, 0, 0, 1, 2)

        self.id_producto_cons_lineEdit = QLineEdit(self.tab_23)
        self.id_producto_cons_lineEdit.setObjectName(u"id_producto_cons_lineEdit")

        self.gridLayout_21.addWidget(self.id_producto_cons_lineEdit, 1, 0, 1, 1)

        self.producto_consultar_pushButton = QPushButton(self.tab_23)
        self.producto_consultar_pushButton.setObjectName(u"producto_consultar_pushButton")

        self.gridLayout_21.addWidget(self.producto_consultar_pushButton, 1, 1, 1, 1)

        self.tabWidget_5.addTab(self.tab_23, "")
        self.tab_25 = QWidget()
        self.tab_25.setObjectName(u"tab_25")
        self.gridLayout_22 = QGridLayout(self.tab_25)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.tabla_producto_most = QTableWidget(self.tab_25)
        self.tabla_producto_most.setObjectName(u"tabla_producto_most")

        self.gridLayout_22.addWidget(self.tabla_producto_most, 0, 0, 1, 1)

        self.producto_mostrar_pushButton = QPushButton(self.tab_25)
        self.producto_mostrar_pushButton.setObjectName(u"producto_mostrar_pushButton")

        self.gridLayout_22.addWidget(self.producto_mostrar_pushButton, 1, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_25, "")

        self.gridLayout_5.addWidget(self.tabWidget_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_7 = QGridLayout(self.tab_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tabWidget_7 = QTabWidget(self.tab_8)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tab_28 = QWidget()
        self.tab_28.setObjectName(u"tab_28")
        self.gridLayout_30 = QGridLayout(self.tab_28)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.groupBox_10 = QGroupBox(self.tab_28)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_25 = QGridLayout(self.groupBox_10)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.cantidad_producto_detalledevolucion_reg_lineEdit = QLineEdit(self.groupBox_10)
        self.cantidad_producto_detalledevolucion_reg_lineEdit.setObjectName(u"cantidad_producto_detalledevolucion_reg_lineEdit")
        self.cantidad_producto_detalledevolucion_reg_lineEdit.setMaxLength(5)

        self.gridLayout_25.addWidget(self.cantidad_producto_detalledevolucion_reg_lineEdit, 6, 1, 1, 1)

        self.codigoempleado_devolucion_reg_lineEdit = QLineEdit(self.groupBox_10)
        self.codigoempleado_devolucion_reg_lineEdit.setObjectName(u"codigoempleado_devolucion_reg_lineEdit")

        self.gridLayout_25.addWidget(self.codigoempleado_devolucion_reg_lineEdit, 3, 1, 1, 1)

        self.label_40 = QLabel(self.groupBox_10)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_25.addWidget(self.label_40, 1, 0, 1, 1)

        self.id_devolucion_detalledevolucion_reg_lineEdit = QLineEdit(self.groupBox_10)
        self.id_devolucion_detalledevolucion_reg_lineEdit.setObjectName(u"id_devolucion_detalledevolucion_reg_lineEdit")

        self.gridLayout_25.addWidget(self.id_devolucion_detalledevolucion_reg_lineEdit, 1, 1, 1, 1)

        self.label_38 = QLabel(self.groupBox_10)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_25.addWidget(self.label_38, 2, 0, 1, 1)

        self.id_producto_detalledevolucion_reg_lineEdit = QLineEdit(self.groupBox_10)
        self.id_producto_detalledevolucion_reg_lineEdit.setObjectName(u"id_producto_detalledevolucion_reg_lineEdit")

        self.gridLayout_25.addWidget(self.id_producto_detalledevolucion_reg_lineEdit, 4, 1, 1, 1)

        self.devolucion_registrar_pushButton = QPushButton(self.groupBox_10)
        self.devolucion_registrar_pushButton.setObjectName(u"devolucion_registrar_pushButton")

        self.gridLayout_25.addWidget(self.devolucion_registrar_pushButton, 8, 0, 1, 2)

        self.codigoventa_devolucion_reg_lineEdit = QLineEdit(self.groupBox_10)
        self.codigoventa_devolucion_reg_lineEdit.setObjectName(u"codigoventa_devolucion_reg_lineEdit")

        self.gridLayout_25.addWidget(self.codigoventa_devolucion_reg_lineEdit, 2, 1, 1, 1)

        self.label_45 = QLabel(self.groupBox_10)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_25.addWidget(self.label_45, 6, 0, 1, 1)

        self.label_39 = QLabel(self.groupBox_10)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_25.addWidget(self.label_39, 3, 0, 1, 1)

        self.label_44 = QLabel(self.groupBox_10)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_25.addWidget(self.label_44, 4, 0, 1, 1)

        self.devolucion_agregar_pushButton = QPushButton(self.groupBox_10)
        self.devolucion_agregar_pushButton.setObjectName(u"devolucion_agregar_pushButton")

        self.gridLayout_25.addWidget(self.devolucion_agregar_pushButton, 7, 0, 1, 2)


        self.gridLayout_30.addWidget(self.groupBox_10, 0, 0, 1, 1)

        self.tabla_devolucion_reg_general_most = QTableWidget(self.tab_28)
        self.tabla_devolucion_reg_general_most.setObjectName(u"tabla_devolucion_reg_general_most")

        self.gridLayout_30.addWidget(self.tabla_devolucion_reg_general_most, 0, 1, 1, 1)

        self.tabWidget_7.addTab(self.tab_28, "")
        self.tab_29 = QWidget()
        self.tab_29.setObjectName(u"tab_29")
        self.gridLayout_26 = QGridLayout(self.tab_29)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.tabla_devolucion_cons = QTableWidget(self.tab_29)
        self.tabla_devolucion_cons.setObjectName(u"tabla_devolucion_cons")

        self.gridLayout_26.addWidget(self.tabla_devolucion_cons, 0, 0, 1, 2)

        self.id_devolucion_cons_lineEdit = QLineEdit(self.tab_29)
        self.id_devolucion_cons_lineEdit.setObjectName(u"id_devolucion_cons_lineEdit")

        self.gridLayout_26.addWidget(self.id_devolucion_cons_lineEdit, 1, 0, 1, 1)

        self.devolucion_consultar_pushButton = QPushButton(self.tab_29)
        self.devolucion_consultar_pushButton.setObjectName(u"devolucion_consultar_pushButton")

        self.gridLayout_26.addWidget(self.devolucion_consultar_pushButton, 1, 1, 1, 1)

        self.tabWidget_7.addTab(self.tab_29, "")

        self.gridLayout_7.addWidget(self.tabWidget_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_8 = QGridLayout(self.tab_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tabWidget_8 = QTabWidget(self.tab_9)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tab_30 = QWidget()
        self.tab_30.setObjectName(u"tab_30")
        self.gridLayout_31 = QGridLayout(self.tab_30)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.groupBox_11 = QGroupBox(self.tab_30)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_27 = QGridLayout(self.groupBox_11)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.cantidad_compras_reg_lineEdit = QLineEdit(self.groupBox_11)
        self.cantidad_compras_reg_lineEdit.setObjectName(u"cantidad_compras_reg_lineEdit")
        self.cantidad_compras_reg_lineEdit.setMaxLength(5)

        self.gridLayout_27.addWidget(self.cantidad_compras_reg_lineEdit, 4, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox_11)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_27.addWidget(self.label_41, 1, 0, 1, 1)

        self.label_48 = QLabel(self.groupBox_11)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_27.addWidget(self.label_48, 3, 0, 1, 1)

        self.id_producto_pedido_detalle_reg_lineEdit = QLineEdit(self.groupBox_11)
        self.id_producto_pedido_detalle_reg_lineEdit.setObjectName(u"id_producto_pedido_detalle_reg_lineEdit")

        self.gridLayout_27.addWidget(self.id_producto_pedido_detalle_reg_lineEdit, 3, 1, 1, 1)

        self.label_57 = QLabel(self.groupBox_11)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_27.addWidget(self.label_57, 0, 0, 1, 1)

        self.compras_registrar_pushButton = QPushButton(self.groupBox_11)
        self.compras_registrar_pushButton.setObjectName(u"compras_registrar_pushButton")

        self.gridLayout_27.addWidget(self.compras_registrar_pushButton, 6, 0, 1, 2)

        self.idproveedor_compras_reg_lineEdit = QLineEdit(self.groupBox_11)
        self.idproveedor_compras_reg_lineEdit.setObjectName(u"idproveedor_compras_reg_lineEdit")

        self.gridLayout_27.addWidget(self.idproveedor_compras_reg_lineEdit, 1, 1, 1, 1)

        self.label_42 = QLabel(self.groupBox_11)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_27.addWidget(self.label_42, 4, 0, 1, 1)

        self.idpedido_compras_reg_lineEdit = QLineEdit(self.groupBox_11)
        self.idpedido_compras_reg_lineEdit.setObjectName(u"idpedido_compras_reg_lineEdit")

        self.gridLayout_27.addWidget(self.idpedido_compras_reg_lineEdit, 0, 1, 1, 1)

        self.compras_agregar_pushButton = QPushButton(self.groupBox_11)
        self.compras_agregar_pushButton.setObjectName(u"compras_agregar_pushButton")

        self.gridLayout_27.addWidget(self.compras_agregar_pushButton, 5, 0, 1, 2)


        self.gridLayout_31.addWidget(self.groupBox_11, 0, 0, 1, 1)

        self.tabla_pedidos_reg_general_most = QTableWidget(self.tab_30)
        self.tabla_pedidos_reg_general_most.setObjectName(u"tabla_pedidos_reg_general_most")

        self.gridLayout_31.addWidget(self.tabla_pedidos_reg_general_most, 0, 1, 1, 1)

        self.tabWidget_8.addTab(self.tab_30, "")
        self.tab_31 = QWidget()
        self.tab_31.setObjectName(u"tab_31")
        self.gridLayout_28 = QGridLayout(self.tab_31)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.tabla_compras_cons = QTableWidget(self.tab_31)
        self.tabla_compras_cons.setObjectName(u"tabla_compras_cons")

        self.gridLayout_28.addWidget(self.tabla_compras_cons, 0, 0, 1, 2)

        self.id_compras_cons_lineEdit = QLineEdit(self.tab_31)
        self.id_compras_cons_lineEdit.setObjectName(u"id_compras_cons_lineEdit")

        self.gridLayout_28.addWidget(self.id_compras_cons_lineEdit, 1, 0, 1, 1)

        self.compras_consultar_pushButton = QPushButton(self.tab_31)
        self.compras_consultar_pushButton.setObjectName(u"compras_consultar_pushButton")

        self.gridLayout_28.addWidget(self.compras_consultar_pushButton, 1, 1, 1, 1)

        self.tabWidget_8.addTab(self.tab_31, "")

        self.gridLayout_8.addWidget(self.tabWidget_8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_9, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 692, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Id Venta", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"SUBTOTAL", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"IVA", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"TOTAL", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Venta", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Cantidad producto", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Precio producto", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Id empleado", None))
        self.venta_registrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Id cliente", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Id producto", None))
        self.venta_agregar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_26), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.venta_consultar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_27), QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Venta", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Empleado", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.empleado_registrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Id empleado", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Empleado", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Id Empleado", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.empleado_modificar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.empleado_consultar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.empleado_mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Empleado", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.cliente_registrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Direccion", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Id cliente", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.cliente_modificar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Direccion", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.cliente_consultar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.cliente_mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Proveedor", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Celular", None))
        self.proveedor_registrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Id proveedor", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_18), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Proveedor", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Id proveedor", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Celular", None))
        self.proveedor_modificar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_19), QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.provvedor_consultar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_20), QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.proveedor_mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_21), QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Proveedor", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Precio Venta", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Precio Compra", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Id Proveedor", None))
        self.producto_registrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"registrar", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Id producto", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_22), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Id proveedor", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Id producto", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Precio Venta", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Precio Compra", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.producto_modificar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_24), QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.producto_consultar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_23), QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.producto_mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_25), QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Producto", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Devolucion", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Id devolucion", None))
        self.id_devolucion_detalledevolucion_reg_lineEdit.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Id Venta", None))
        self.devolucion_registrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Cantidad Producto", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Id Empleado", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Id Producto", None))
        self.devolucion_agregar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_28), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.devolucion_consultar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_29), QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Devolucion", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Pedido", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Id Proveedor", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Id producto", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Id pedido", None))
        self.compras_registrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.compras_agregar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_30), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.compras_consultar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_31), QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Pedidos", None))
    # retranslateUi

