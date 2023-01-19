from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox,QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
import dulceria_con
from pathlib import Path
from gestor_producto import Gestor_Producto
from produto import Producto_venta

import datetime 
import mysql.connector
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator

#pyside2-uic mainwindow.ui para pasar de .ui a python
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.articulo1=dulceria_con.Articulos()
        self.productos_list=Gestor_Producto()
        self.productos_lista=[]
        self.cantidades_lista=[]
        self.precios_lista=[]
        self.producto_pedido=[]
        self.cantidadespedido_lista=[]
        self.producto_devolucion=[]
        self.cantidadedevolucion_lista=[]
        
        self.subtotal=0
        self.iva=0
        self.total=0
        self.VALIDADOR_NUMEROS="[0-9]+"
        current_time = datetime.datetime.now() 
        self.id_cliente_bool=False
        self.id_empleado_bool=False
        self.id_proveedor_bool=False
        self.id_proveedor_prod_bool=False
        self.id_producto_bool=False
        self.id_venta_devolucion_bool=False
        self.id_empleado_devolucion_bool=False
        self.id_producto_devolucion_bool=False
        self.id_proveedor_pedidos_bool=False
        self.id_producto_pedidos_bool=False
        self.id_empleado_venta_bool=False
        self.id_cliente_venta_bool=False
        self.id_producto_venta_bool=False
        self.id_proveedor_pedidos_producto_bool=False
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.empleado_registrar_pushButton.clicked.connect(self.registrar_empleado)
        self.ui.cliente_registrar_pushButton.clicked.connect(self.registrar_cliente)
        self.ui.proveedor_registrar_pushButton.clicked.connect(self.registrar_proveedor)
        self.ui.producto_registrar_pushButton.clicked.connect(self.registrar_producto)
        self.ui.venta_registrar_pushButton.clicked.connect(self.registrar_venta)
        self.ui.devolucion_registrar_pushButton.clicked.connect(self.registrar_devolucion)
        self.ui.compras_registrar_pushButton.clicked.connect(self.registrar_compras)
        self.ui.empleado_modificar_pushButton.clicked.connect(self.modificar_empleado)
        self.ui.cliente_modificar_pushButton.clicked.connect(self.modificar_cliente)
        self.ui.proveedor_modificar_pushButton.clicked.connect(self.modificar_proveedor)
        self.ui.producto_modificar_pushButton.clicked.connect(self.modificar_producto)
        self.ui.empleado_consultar_pushButton.clicked.connect(self.consultar_empleado)
        self.ui.empleado_mostrar_pushButton.clicked.connect(self.mostrar_empleado)
        self.ui.cliente_consultar_pushButton.clicked.connect(self.consultar_cliente)
        self.ui.cliente_mostrar_pushButton.clicked.connect(self.mostrar_cliente)
        self.ui.provvedor_consultar_pushButton.clicked.connect(self.consultar_proveedor)
        self.ui.proveedor_mostrar_pushButton.clicked.connect(self.mostrar_proveedor)
        self.ui.producto_consultar_pushButton.clicked.connect(self.consultar_producto)
        self.ui.producto_mostrar_pushButton.clicked.connect(self.mostrar_producto)
        self.ui.venta_consultar_pushButton.clicked.connect(self.consultar_venta)
        self.ui.devolucion_consultar_pushButton.clicked.connect(self.consultar_devolucion)
        self.ui.compras_consultar_pushButton.clicked.connect(self.consultar_pedido)
        self.ui.compras_registrar_pushButton.clicked.connect(self.registrar_pedido)
        self.ui.venta_agregar_pushButton.clicked.connect(self.agregar_producto_a_gestor)
        self.ui.compras_agregar_pushButton.clicked.connect(self.agregar_pedido_a_gestor)
        self.ui.devolucion_agregar_pushButton.clicked.connect(self.agregar_devolucion_a_gestor)
        
        """
        self.ui.idempleado_venta_reg_lineEdit.returnPressed.connect(self.consultar_empleado_venta)
        self.ui.idcliente_venta_reg_lineEdit.returnPressed.connect(self.consultar_cliente_venta)
        self.ui.idproducto_venta_reg_lineEdit.returnPressed.connect(self.consultar_producto_venta)

        """
        
        self.ui.idempleado_venta_reg_lineEdit.textChanged.connect(self.consultar_empleado_venta)
        self.ui.idcliente_venta_reg_lineEdit.textChanged.connect(self.consultar_cliente_venta)
        self.ui.idproducto_venta_reg_lineEdit.textChanged.connect(self.consultar_producto_venta)
        #self.ui.cantidadproducto_venta_reg_spinBox.textChanged.connect(self.mostrar_productos_reg_venta)
        self.ui.id_empleado_mod_lineEdit.textChanged.connect(self.consultar_empleado_mod)
        self.ui.id_cliente_mod_lineEdit.textChanged.connect(self.consultar_cliente_mod)
        self.ui.id_proveedor_mod_lineEdit.textChanged.connect(self.consultar_proveedor_mod)
        self.ui.idprovee_producto_reg_lineEdit.textChanged.connect(self.consultar_proveedor_reg_producto)
        self.ui.id_product_mod_lineEdit.textChanged.connect(self.consultar_producto_mod)
        self.ui.idprovee_producto_mod_lineEdit.textChanged.connect(self.consultar_proveedor_producto_mod)
        self.ui.codigoventa_devolucion_reg_lineEdit.textChanged.connect(self.consultar_venta_devolucion_reg)
        self.ui.id_producto_detalledevolucion_reg_lineEdit.textChanged.connect(self.consultar_producto_devolucion_reg)
        self.ui.codigoempleado_devolucion_reg_lineEdit.textChanged.connect(self.consultar_empleado_devolucion_reg)
        self.ui.idproveedor_compras_reg_lineEdit.textChanged.connect(self.consultar_proveedor_pedidos_reg)
        self.ui.id_producto_pedido_detalle_reg_lineEdit.textChanged.connect(self.consultar_producto_pedidos_reg)
        
        #self.ui.cantidadproducto_venta_reg_spinBox.textChanged.connect()
        
        

        self.ui.idempleado_venta_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.idcliente_venta_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))

        self.ui.idventa_vent_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.idproducto_venta_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_venta_cons_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.nombre_empleado_reg_lineEdit.setValidator(QRegExpValidator(QRegExp("[a-z^A-Z^ ]+")))
        self.ui.telefono_empleado_reg_lineEdit_2.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))

        self.ui.id_empleado_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.nombre_empleado_mod_lineEdit.setValidator(QRegExpValidator(QRegExp("[a-z^A-Z^ ]+")))
        self.ui.telefono_empleado_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_empleado_cons_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))

        self.ui.nombre_cliente_reg_lineEdit.setValidator(QRegExpValidator(QRegExp("[a-z^A-Z^ ]+")))
        self.ui.direccion_cliente_reg_lineEdit.setValidator(QRegExpValidator(QRegExp("[a-z^A-Z^0-9^ ]+")))
        self.ui.puntos_cliente_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_cliente_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.nombre_cliente_mod_lineEdit.setValidator(QRegExpValidator(QRegExp("[a-z^A-Z^ ]+")))
        self.ui.direccion_cliente_mod_lineEdit.setValidator(QRegExpValidator(QRegExp("[a-z^A-Z^0-9^ ]+")))
        self.ui.puntos_cliente_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_cliente_cons_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))

        self.ui.nombre_proveedor_reg_lineEdit.setValidator(QRegExpValidator(QRegExp("[a-z^A-Z^ ]+")))
        self.ui.telefono_proveedor_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.celular_proveedor_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_proveedor_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.nombre_proveedor_mod_lineEdit.setValidator(QRegExpValidator(QRegExp("[a-z^A-Z^ ]+")))
        self.ui.telefono_proveedor_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.celular_proveedor_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_proveedor_cons_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))

        self.ui.nombre_producto_reg_lineEdit.setValidator(QRegExpValidator(QRegExp("[a-z^A-Z^ ]+")))
        self.ui.preciovent_producto_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.idprovee_producto_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.preciocomp_producto_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.cantidad_producto_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_product_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.nombre_producto_mod_lineEdit.setValidator(QRegExpValidator(QRegExp("[a-z^A-Z^ ]+")))
        self.ui.preciocomp_producto_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.preciovent_producto_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.idprovee_producto_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.cantidad_producto_mod_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_producto_cons_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))

        self.ui.codigoventa_devolucion_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.codigoempleado_devolucion_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        #self.ui.id_devolucion_detalledevolucion_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_producto_detalledevolucion_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.cantidad_producto_detalledevolucion_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_devolucion_cons_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))

        self.ui.idproveedor_compras_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        #self.ui.id_pedido_pedido_detalle_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_producto_pedido_detalle_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.cantidad_compras_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        #self.ui.producto_compras_detalles_reg_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
        self.ui.id_compras_cons_lineEdit.setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))

        self.ui.fecha_vent_reg_lineEdit.setReadOnly(True)
        self.ui.fecha_vent_reg_lineEdit.setPlaceholderText(str(current_time.day)+'/'+str(current_time.month)+'/'+str(current_time.year))

        self.ui.idventa_vent_reg_lineEdit.setReadOnly(True)
        self.ui.subtotal_vent_reg_lineEdit.setReadOnly(True)
        self.ui.iva_vent_reg_lineEdit.setReadOnly(True)
        self.ui.total_vent_reg_lineEdit.setReadOnly(True)

        self.ui.pago_venta_reg_lineEdit.setReadOnly(True)

        self.ui.idempleado_reg_lineEdit.setReadOnly(True)
        self.ui.idcliente_reg_lineEdit.setReadOnly(True)
        self.ui.idproveedor_reg_lineEdit_2.setReadOnly(True)
        self.ui.idproducto_reg_lineEdit.setReadOnly(True)
        self.ui.id_devolucion_detalledevolucion_reg_lineEdit.setReadOnly(True)
        self.ui.idpedido_compras_reg_lineEdit.setReadOnly(True)

        self.ui.Fecha_general_lineEdit.setReadOnly(True)
        self.ui.Fecha_general_lineEdit.setPlaceholderText(str(current_time.day)+'/'+str(current_time.month)+'/'+str(current_time.year))
        self.actulizar_id_venta_reg()
        self.actulizar_id_empleado_reg()
        self.actulizar_id_cliente_reg()
        self.actulizar_id_proveedor_reg()
        self.actulizar_id_producto_reg()
        self.actulizar_id_devolucion_reg()
        self.actulizar_id_pedido_reg()
        #setValidator(QRegExpValidator(QRegExp('[a-zA-Z\d\S]+')))
        #setValidator(QRegExpValidator(QRegExp(self.VALIDADOR_NUMEROS)))
    """
    @Slot()
    def agregar_cantidad_prod_reg_venta(self,cantidad_llevar):
        self.producto1.reg_cantidad(cantidad_llevar)
        #self.productos_list.editar_cantidad_producto(cantidad_llevar)
    """
    @Slot()
    def agregar_pedido_a_gestor(self):
        self.id_cantidad_detalles_pedido_reg=self.ui.cantidad_compras_reg_lineEdit.text()
        self.id_proveedor_pedido=self.ui.idproveedor_compras_reg_lineEdit.text()
        self.id_producto_detalles_pedido_reg=self.ui.id_producto_pedido_detalle_reg_lineEdit.text()
        resultados= self.articulo1.consulta_proveedor()
        resultados2=self.articulo1.consulta_producto_proveedor_pedido(self.id_proveedor_pedido)
     
        for idPROD,nobrePROD,precioc,preciov,cantidad,idPROV2 in resultados2:
                
            if idPROD == self.id_producto_detalles_pedido_reg and idPROV2==self.id_proveedor_pedido:
                print("Es e¿correcto")
                self.id_proveedor_pedidos_producto_bool=True
                break

        print(self.id_proveedor_pedidos_producto_bool)
        if self.id_proveedor_pedidos_bool==True and self.id_producto_pedidos_bool==True and self.id_cantidad_detalles_pedido_reg !="" and self.id_cantidad_detalles_pedido_reg !="0" :#and self.id_proveedor_pedidos_producto_bool==True:
            
            self.producto_pedido.append(self.id_producto_detalles_pedido_reg)
            self.cantidadespedido_lista.append(self.id_cantidad_detalles_pedido_reg)
            self.mostrar_productos_reg_pedido()
            QMessageBox.information(
                    self,
                    "Agregado",
                    f'Se a agregado el producto a la lista.'
                    )
        if self.id_proveedor_pedidos_bool==False:
            QMessageBox.warning(
                        self,
                        "Id proveedor",
                        f'Id proveedor incorrecto, no encontrado.'
                        )
        if self.id_producto_pedidos_bool==False:
            QMessageBox.warning(
                        self,
                        "Id producto",
                        f'Id producto incorrecto, no encontrado.'
                        )
        if self.id_cantidad_detalles_pedido_reg == "0":
            QMessageBox.warning(
                        self,
                        "Cantidad",
                        f'Ingrese una cantidad correcta.'
                        )
        if self.id_cantidad_detalles_pedido_reg == "":
            QMessageBox.warning(
                        self,
                        "Cantidad",
                        f'Ingrese una cantidad correcta.'
                        )
        """if self.id_proveedor_pedidos_producto_bool==False:
            QMessageBox.warning(
                        self,
                        "Producto y proveedor",
                        f'El producto y proveedor no coenciden, este proveedor no surte el producto..'
                        )
            """
    @Slot()
    def agregar_devolucion_a_gestor(self):
        
        self.id_cantidad_detalles_devolucion_reg=self.ui.cantidad_producto_detalledevolucion_reg_lineEdit.text()
        #condicion=self.coencide_devolucion()
        #print(condicion)
        if self.id_venta_devolucion_bool == True and self.id_empleado_devolucion_bool == True  and self.id_producto_devolucion_bool == True and self.id_cantidad_detalles_devolucion_reg!="" and self.id_cantidad_detalles_devolucion_reg!="0"   :
            self.id_producto_detalles_devolucion_reg=self.ui.id_producto_detalledevolucion_reg_lineEdit.text()
            #self.coencide_ventadev_detalleventa=False
            #self.coencide_productodev_detalleventa=False
            
            self.producto_devolucion.append(self.id_producto_detalles_devolucion_reg)
            self.cantidadedevolucion_lista.append(self.id_cantidad_detalles_devolucion_reg)
            self.mostrar_productos_reg_devolucion()
            QMessageBox.information(
                        self,
                        "Agregado",
                        f'El producto a sido agregado.'
                        )
        if self.id_venta_devolucion_bool == False :
                QMessageBox.warning(
                        self,
                        "Id venta",
                        f'Id venta incorrecto, no encontrado.'
                        )
        if self.id_empleado_devolucion_bool == False  :
                QMessageBox.warning(
                        self,
                        "Id empleado",
                        f'Id empleado incorrecto, no encontrado.'
                        )
        if self.id_producto_devolucion_bool == False:
                QMessageBox.warning(
                        self,
                        "Id producto",
                        f'Id producto incorrecto, no encontrado.'
                        )
        if self.id_cantidad_detalles_devolucion_reg=="":
            QMessageBox.warning(
                        self,
                        "Cantidad",
                        f'Ingrese una cantidad correcta.'
                        )
        if self.id_cantidad_detalles_devolucion_reg=="0":
            QMessageBox.warning(
                        self,
                        "Cantidad",
                        f'Ingrese una cantidad correcta.'
                        )

    @Slot()
    def mostrar_productos_reg_devolucion(self):
        resultados= self.articulo1.consulta_producto()
        #self.agregar_cantidad_prod_reg_venta(cantidad_llevar)

        self.ui.tabla_devolucion_reg_general_most.clear()
        self.ui.tabla_devolucion_reg_general_most.setRowCount(len(self.producto_devolucion))
        self.ui.tabla_devolucion_reg_general_most.setColumnCount(3)
        headers=["Id producto","Nombre","Cantidad"]
        self.ui.tabla_devolucion_reg_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        row=0
        indd=0
        print(self.productos_lista)
        for idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROVEE_fk in resultados :
            for idprod_lista_agregar in self.producto_devolucion:
                if int(idprod_lista_agregar) == idPROD:
                    
                    idPROD_widget= QTableWidgetItem(str(idPROD))
                    nombrePROD_widget= QTableWidgetItem(str(nombrePROD))
                    #cantidad_prod=self.producto1.__cantidad
                    cantidadLLEVAR_widget=QTableWidgetItem(str(self.cantidadedevolucion_lista[indd]))
                    
                    self.ui.tabla_devolucion_reg_general_most.setItem(row,0,idPROD_widget)
                    self.ui.tabla_devolucion_reg_general_most.setItem(row,1,nombrePROD_widget)
                    self.ui.tabla_devolucion_reg_general_most.setItem(row,2,cantidadLLEVAR_widget)
                    
                    encontrado=True
                    row+=1
                    indd+=1
               
    @Slot()
    def mostrar_productos_reg_pedido(self):
        resultados= self.articulo1.consulta_producto()
        #self.agregar_cantidad_prod_reg_venta(cantidad_llevar)

        self.ui.tabla_pedidos_reg_general_most.clear()
        self.ui.tabla_pedidos_reg_general_most.setRowCount(len(self.producto_pedido))
        self.ui.tabla_pedidos_reg_general_most.setColumnCount(3)
        headers=["Id producto","Nombre","Cantidad"]
        self.ui.tabla_pedidos_reg_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        row=0
        indd=0
        print(self.productos_lista)
        for idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROVEE_fk in resultados :
            for idprod_lista_agregar in self.producto_pedido:
                if int(idprod_lista_agregar) == idPROD:
                    
                    idPROD_widget= QTableWidgetItem(str(idPROD))
                    nombrePROD_widget= QTableWidgetItem(str(nombrePROD))
                    #cantidad_prod=self.producto1.__cantidad
                    cantidadLLEVAR_widget=QTableWidgetItem(str(self.cantidadespedido_lista[indd]))
                    
                    self.ui.tabla_pedidos_reg_general_most.setItem(row,0,idPROD_widget)
                    self.ui.tabla_pedidos_reg_general_most.setItem(row,1,nombrePROD_widget)
                    self.ui.tabla_pedidos_reg_general_most.setItem(row,2,cantidadLLEVAR_widget)
                    
                    encontrado=True
                    row+=1
                    indd+=1
               

    @Slot()
    def agregar_producto_a_gestor(self):
        try:
            if self.id_empleado_venta_bool==True and self.id_cliente_venta_bool==True and self.id_producto_venta_bool==True:
                self.producto1=Producto_venta(self.id_producto_cons,self.precio_prod)
                self.producto1.reg_cantidad(self.ui.cantidadproducto_venta_reg_spinBox.value())
                print(self.productos_list.productos)
                
                self.productos_lista.append(self.id_producto_cons)
                self.cantidades_lista.append(self.ui.cantidadproducto_venta_reg_spinBox.value())
                self.precios_lista.append(self.precio_prod)

                self.subtotal=self.ui.cantidadproducto_venta_reg_spinBox.value()*self.precio_prod
                self.ui.subtotal_vent_reg_lineEdit.setPlaceholderText(str(self.subtotal))
                self.iva=self.subtotal*0.16
                self.ui.iva_vent_reg_lineEdit.setPlaceholderText(str(self.iva))
                self.total+=self.subtotal+self.iva
                self.ui.total_vent_reg_lineEdit.setPlaceholderText(str(self.total))
                
                self.productos_list.agregar_final(self.producto1)
                self.mostrar_productos_reg_venta()
                QMessageBox.information(
                    self,
                    "Agregado",
                    f'Se a agregado el producto a la lista.'
                    )
            if self.id_empleado_venta_bool==False:
                QMessageBox.warning(
                        self,
                        "Id empleado",
                        f'Id empleado incorrecto, no encontrado.'
                        )
            if self.id_cliente_venta_bool==False:
                QMessageBox.warning(
                        self,
                        "Id cliente",
                        f'Id cliente incorrecto, no encontrado.'
                        )
            if self.id_producto_venta_bool==False:
                QMessageBox.warning(
                        self,
                        "Id producto",
                        f'Id producto incorrecto, no encontrado.'
                        )
        except:
            QMessageBox.warning(
                self,
                "Atención",
                "la venta no fue registrada, campos vacios en el formulario."
            )
                

    @Slot()
    def mostrar_productos_reg_venta(self):
        resultados= self.articulo1.consulta_producto()
        #self.agregar_cantidad_prod_reg_venta(cantidad_llevar)

        self.ui.tabla_general_most.clear()
        self.ui.tabla_general_most.setRowCount(len(self.productos_lista))
        self.ui.tabla_general_most.setColumnCount(3)
        headers=["Id producto","Nombre","Cantidad"]
        self.ui.tabla_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        row=0
        indd=0
        print(self.productos_lista)
        for idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROVEE_fk in resultados :
            for idprod_lista_agregar in self.productos_lista:
                if int(idprod_lista_agregar) == idPROD:
                    
                    idPROD_widget= QTableWidgetItem(str(idPROD))
                    nombrePROD_widget= QTableWidgetItem(str(nombrePROD))
                    #cantidad_prod=self.producto1.__cantidad
                    cantidadLLEVAR_widget=QTableWidgetItem(str(self.cantidades_lista[indd]))
                    
                    self.ui.tabla_general_most.setItem(row,0,idPROD_widget)
                    self.ui.tabla_general_most.setItem(row,1,nombrePROD_widget)
                    self.ui.tabla_general_most.setItem(row,2,cantidadLLEVAR_widget)
                    
                    encontrado=True
                    row+=1
                    indd+=1
               

    @Slot()
    def consultar_producto_venta(self):
        
        self.id_producto_cons=self.ui.idproducto_venta_reg_lineEdit.text()
        self.cantidad_llevar_reg_venta=self.ui.cantidadproducto_venta_reg_spinBox.value()
        resultados= self.articulo1.consulta_producto()
        print(self.cantidad_llevar_reg_venta)
        self.ui.tabla_general_most.clear()
        self.ui.tabla_general_most.setRowCount(1)
        self.ui.tabla_general_most.setColumnCount(2)
        headers=["Id producto","Nombre"]
        self.ui.tabla_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        
        print(self.productos_lista)
        for idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROVEE_fk in resultados :

            if int(self.id_producto_cons) == idPROD:
                #print(idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROVEE_fk)
                cantidad_update_venta=cantidad-self.cantidad_llevar_reg_venta
                idPROD_widget= QTableWidgetItem(str(idPROD))
                nombrePROD_widget= QTableWidgetItem(str(nombrePROD))
                    
                self.precio_prod=precioVenta
                self.ui.pago_venta_reg_lineEdit.setPlaceholderText(str(precioVenta))

                self.ui.tabla_general_most.setItem(0,0,idPROD_widget)
                self.ui.tabla_general_most.setItem(0,1,nombrePROD_widget)
                encontrado=True
                self.id_producto_venta_bool=True
       
        if not encontrado:
            self.id_producto_venta_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El producto"{self.id_producto_cons}"no fue encontrado'
            )
        
    
    @Slot()
    def consultar_cliente_venta(self):
        id_cliente_cons=self.ui.idcliente_venta_reg_lineEdit.text()
        resultados= self.articulo1.consulta_cliente()

        self.ui.tabla_general_most.clear()
        self.ui.tabla_general_most.setRowCount(1)
        self.ui.tabla_general_most.setColumnCount(3)
        headers=["Id cliente","Nombre","Puntos"]
        self.ui.tabla_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        for idCLIENT,nombreCLIENT,direccionCLIENT,puntos in resultados :
            if int(id_cliente_cons) == idCLIENT:
                #print(idCLIENT,nombreCLIENT,direccionCLIENT,puntos)
                
                idCLIENT_widget= QTableWidgetItem(str(idCLIENT))
                nombreCLIENT_widget= QTableWidgetItem(str(nombreCLIENT))
                puntos_widget= QTableWidgetItem(str(puntos))

                self.ui.tabla_general_most.setItem(0,0,idCLIENT_widget)
                self.ui.tabla_general_most.setItem(0,1,nombreCLIENT_widget)
                self.ui.tabla_general_most.setItem(0,2,puntos_widget)
                encontrado=True
                self.id_cliente_venta_bool=True
        if not encontrado:
            self.id_cliente_venta_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El cliente"{id_cliente_cons}"no fue encontrado'
            )
        
    @Slot()
    def actulizar_id_venta_reg(self):
        resultados= self.articulo1.consulta_ult_id_venta()
        new_str=str(resultados)
        self.id_venta_new_reg=""
        for inc in new_str:
            if ord(inc)!=44 and ord(inc)!= 40 and ord(inc)!=41 and ord(inc)!= 91 and ord(inc)!=93:
                self.id_venta_new_reg+=inc
        self.id_venta_new_reg_venta=len(resultados)+1
        if  self.id_venta_new_reg.lower() =="none":
            self.articulo1.reiniciar_id_venta()
            self.id_venta_new_reg=1
        else:
            self.id_venta_new_reg=str(int(self.id_venta_new_reg)+1)
        self.ui.idventa_vent_reg_lineEdit.setPlaceholderText(str(self.id_venta_new_reg))
    
    @Slot()
    def actulizar_id_empleado_reg(self):
        resultados= self.articulo1.consulta_ult_id_empleado()
        new_str=str(resultados)
        self.id_empleado_new_reg=""
        for inc in new_str:
            if ord(inc)!=44 and ord(inc)!= 40 and ord(inc)!=41 and ord(inc)!= 91 and ord(inc)!=93:
                self.id_empleado_new_reg+=inc
        if  self.id_empleado_new_reg.lower() =="none":
            self.articulo1.reiniciar_id_empleado()
            self.id_empleado_new_reg=str(1)
        else:
            self.id_empleado_new_reg=str(int(self.id_empleado_new_reg)+1)
        self.ui.idempleado_reg_lineEdit.setPlaceholderText(self.id_empleado_new_reg)
    
    @Slot()
    def actulizar_id_cliente_reg(self):
        resultados= self.articulo1.consulta_ult_id_cliente()
        new_str=str(resultados)
        self.id_cliente_new_reg=""
        for inc in new_str:
            if ord(inc)!=44 and ord(inc)!= 40 and ord(inc)!=41 and ord(inc)!= 91 and ord(inc)!=93:
                self.id_cliente_new_reg+=inc
        if  self.id_cliente_new_reg.lower() =="none":
            self.articulo1.reiniciar_id_clientes()
            self.id_cliente_new_reg=str(1)
        else:
            self.id_cliente_new_reg=str(int(self.id_cliente_new_reg)+1)
        self.ui.idcliente_reg_lineEdit.setPlaceholderText(self.id_cliente_new_reg)
    
    @Slot()
    def actulizar_id_proveedor_reg(self):
        resultados= self.articulo1.consulta_ult_id_proveedor()
        new_str=str(resultados)
        self.id_proveedor_new_reg=""
        for inc in new_str:
            if ord(inc)!=44 and ord(inc)!= 40 and ord(inc)!=41 and ord(inc)!= 91 and ord(inc)!=93:
                self.id_proveedor_new_reg+=inc
        if  self.id_proveedor_new_reg.lower() =="none":
            self.articulo1.reiniciar_id_proveedores()
            self.id_proveedor_new_reg=str(1)
        else:
            self.id_proveedor_new_reg=str(int(self.id_proveedor_new_reg)+1)
        self.ui.idproveedor_reg_lineEdit_2.setPlaceholderText(self.id_proveedor_new_reg)
    
    @Slot()
    def actulizar_id_producto_reg(self):
        
        resultados= self.articulo1.consulta_ult_id_producto()
        
        new_str=str(resultados)
        self.id_producto_new_reg=""
        for inc in new_str:
            if ord(inc)!=44 and ord(inc)!= 40 and ord(inc)!=41 and ord(inc)!= 91 and ord(inc)!=93:
                self.id_producto_new_reg+=inc
        if  self.id_producto_new_reg.lower() =="none":
            self.articulo1.reiniciar_id_producto()
            self.id_producto_new_reg=str(1)
        else:
            self.id_producto_new_reg=str(int(self.id_producto_new_reg)+1)
        self.ui.idproducto_reg_lineEdit.setPlaceholderText(self.id_producto_new_reg)
        

    @Slot()
    def actulizar_id_pedido_reg(self):
        try:
            resultados= self.articulo1.consulta_ult_id_pedido()
            new_str=str(resultados)
            self.id_pedido_new_reg=""
            for inc in new_str:
                if ord(inc)!=44 and ord(inc)!= 40 and ord(inc)!=41 and ord(inc)!= 91 and ord(inc)!=93:
                    self.id_pedido_new_reg+=inc
            if  self.id_pedido_new_reg.lower() =="none":
                self.articulo1.reiniciar_id_pedidos()
                self.id_pedido_new_reg=str(1)
            else:
                self.id_pedido_new_reg=str(int(self.id_pedido_new_reg)+1)
            self.ui.idpedido_compras_reg_lineEdit.setPlaceholderText(self.id_pedido_new_reg)
        except:
            print("eror: no actualizado id pedido")

    @Slot()
    def actulizar_id_devolucion_reg(self):
        
        resultados= self.articulo1.consulta_ult_id_devolucion()
        new_str=str(resultados)
        self.id_devolucion_new_reg=""
        for inc in new_str:
            if ord(inc)!=44 and ord(inc)!= 40 and ord(inc)!=41 and ord(inc)!= 91 and ord(inc)!=93:
                self.id_devolucion_new_reg+=inc
        if  self.id_devolucion_new_reg.lower() =="none":
            self.articulo1.reiniciar_id_devolucion()
            self.id_devolucion_new_reg=str(1)
        else:
            self.id_devolucion_new_reg=str(int(self.id_devolucion_new_reg)+1)
        self.ui.id_devolucion_detalledevolucion_reg_lineEdit.setPlaceholderText(self.id_devolucion_new_reg)
        

    @Slot()
    def consultar_empleado_mod(self):
        
        id_empleado_mod=self.ui.id_empleado_mod_lineEdit.text()
        resultados= self.articulo1.consulta_empleado()

        self.ui.tabla_empleado_mod_general_most.clear()
        self.ui.tabla_empleado_mod_general_most.setRowCount(1)
        self.ui.tabla_empleado_mod_general_most.setColumnCount(4)
        headers=["Id empleado","Nombre","Telefono","Status"]#**********
        self.ui.tabla_empleado_mod_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        for idEMP,nombreEMP,telEMP,status in resultados :
            if int(id_empleado_mod) == idEMP:
                #print(idEMP,nombreEMP,telEMP,status)
                
                idEMP_widget= QTableWidgetItem(str(idEMP))
                nombreEMP_widget= QTableWidgetItem(str(nombreEMP))
                telEMPMP_widget= QTableWidgetItem(str(telEMP))
                statusMP_widget= QTableWidgetItem(str(status))

                self.ui.tabla_empleado_mod_general_most.setItem(0,0,idEMP_widget)
                self.ui.tabla_empleado_mod_general_most.setItem(0,1,nombreEMP_widget)
                self.ui.tabla_empleado_mod_general_most.setItem(0,2,telEMPMP_widget)
                self.ui.tabla_empleado_mod_general_most.setItem(0,3,statusMP_widget)
                encontrado=True
                self.id_empleado_bool=True
        if not encontrado:
            self.id_empleado_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El empleado"{id_empleado_mod}"no fue encontrado'
            )

    @Slot()
    def consultar_cliente_mod(self):
        
        id_cliente_mod=self.ui.id_cliente_mod_lineEdit.text()
        resultados= self.articulo1.consulta_cliente()

        self.ui.tabla_cliente_mod_general_most.clear()
        self.ui.tabla_cliente_mod_general_most.setRowCount(1)
        self.ui.tabla_cliente_mod_general_most.setColumnCount(4)
        headers=["Id cliente","Nombre","Dirección","Puntos"]
        self.ui.tabla_cliente_mod_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        for idCLIENT,nombreCLIENT,direccionCLIENT,puntos in resultados :
            if int(id_cliente_mod) == idCLIENT:
                #print(idEMP,nombreEMP,telEMP,status)
                
                idCLIENT_widget= QTableWidgetItem(str(idCLIENT))
                nombreCLIENT_widget= QTableWidgetItem(str(nombreCLIENT))
                direccionCLIENT_widget= QTableWidgetItem(str(direccionCLIENT))
                puntos_widget= QTableWidgetItem(str(puntos))

                self.ui.tabla_cliente_mod_general_most.setItem(0,0,idCLIENT_widget)
                self.ui.tabla_cliente_mod_general_most.setItem(0,1,nombreCLIENT_widget)
                self.ui.tabla_cliente_mod_general_most.setItem(0,2,direccionCLIENT_widget)
                self.ui.tabla_cliente_mod_general_most.setItem(0,3,puntos_widget)
                encontrado=True
                self.id_cliente_bool=True
        if not encontrado:
            self.id_cliente_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El cliente"{id_cliente_mod}"no fue encontrado'
            )
            
    @Slot()
    def consultar_proveedor_reg_producto(self):
        
        id_proveedor_reg_prod=self.ui.idprovee_producto_reg_lineEdit.text()
        resultados= self.articulo1.consulta_proveedor()

        self.ui.tabla_producto_reg_general_most.clear()
        self.ui.tabla_producto_reg_general_most.setRowCount(1)
        self.ui.tabla_producto_reg_general_most.setColumnCount(4)
        headers=["Id proveedor","Nombre","Telefono","Celular"]
        self.ui.tabla_producto_reg_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        for idPROV,nombrePROV,telPROV,celPROV in resultados :
            if int(id_proveedor_reg_prod) == idPROV:
                #print(idEMP,nombreEMP,telEMP,status)
                
                idPROV_widget= QTableWidgetItem(str(idPROV))
                nombrePROV_widget= QTableWidgetItem(str(nombrePROV))
                telPROV_widget= QTableWidgetItem(str(telPROV))
                celPROV_widget= QTableWidgetItem(str(celPROV))

                self.ui.tabla_producto_reg_general_most.setItem(0,0,idPROV_widget)
                self.ui.tabla_producto_reg_general_most.setItem(0,1,nombrePROV_widget)
                self.ui.tabla_producto_reg_general_most.setItem(0,2,telPROV_widget)
                self.ui.tabla_producto_reg_general_most.setItem(0,3,celPROV_widget)
                encontrado=True
                self.id_proveedor_prod_bool=True
        if not encontrado:
            self.id_proveedor_prod_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El proveedor"{id_proveedor_reg_prod}"no fue encontrado'
            )

    @Slot()
    def consultar_proveedor_mod(self):
        
        id_proveedor_mod=self.ui.id_proveedor_mod_lineEdit.text()
        resultados= self.articulo1.consulta_proveedor()

        self.ui.tabla_proveedor_mod_general_most.clear()
        self.ui.tabla_proveedor_mod_general_most.setRowCount(1)
        self.ui.tabla_proveedor_mod_general_most.setColumnCount(4)
        headers=["Id proveedor","Nombre","Telefono","Celular"]
        self.ui.tabla_proveedor_mod_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        for idPROV,nombrePROV,telPROV,celPROV in resultados :
            if int(id_proveedor_mod) == idPROV:
                #print(idEMP,nombreEMP,telEMP,status)
                
                idPROV_widget= QTableWidgetItem(str(idPROV))
                nombrePROV_widget= QTableWidgetItem(str(nombrePROV))
                telPROV_widget= QTableWidgetItem(str(telPROV))
                celPROV_widget= QTableWidgetItem(str(celPROV))

                self.ui.tabla_proveedor_mod_general_most.setItem(0,0,idPROV_widget)
                self.ui.tabla_proveedor_mod_general_most.setItem(0,1,nombrePROV_widget)
                self.ui.tabla_proveedor_mod_general_most.setItem(0,2,telPROV_widget)
                self.ui.tabla_proveedor_mod_general_most.setItem(0,3,celPROV_widget)
                encontrado=True
                self.id_proveedor_bool=True
        if not encontrado:
            self.id_proveedor_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El proveedor"{id_proveedor_mod}"no fue encontrado'
            )
    @Slot()
    def consultar_proveedor_pedidos_reg(self):
        
        id_proveedor_mod=self.ui.idproveedor_compras_reg_lineEdit.text()
        id_proveedor_mod=int(id_proveedor_mod)
        resultados= self.articulo1.consulta_proveedor()
        resultados2=self.articulo1.consulta_producto_proveedor_pedido(id_proveedor_mod)
        self.ui.tabla_pedidos_reg_general_most.clear()
        self.ui.tabla_pedidos_reg_general_most.setRowCount(len(resultados2))
        self.ui.tabla_pedidos_reg_general_most.setColumnCount(8)
        headers=["Id proveedor","Nombre","Telefono","Celular","Producto","Precio compra","Precio venta","Cantidad"]
        self.ui.tabla_pedidos_reg_general_most.setHorizontalHeaderLabels(headers)
        row=0
        #print(resultados)
        encontrado=False
        for idPROV,nombrePROV,telPROV,celPROV in resultados :
            if int(id_proveedor_mod) == idPROV:
                #print(idEMP,nombreEMP,telEMP,status)
                
                idPROV_widget= QTableWidgetItem(str(idPROV))
                nombrePROV_widget= QTableWidgetItem(str(nombrePROV))
                telPROV_widget= QTableWidgetItem(str(telPROV))
                celPROV_widget= QTableWidgetItem(str(celPROV))

                self.ui.tabla_pedidos_reg_general_most.setItem(0,0,idPROV_widget)
                self.ui.tabla_pedidos_reg_general_most.setItem(0,1,nombrePROV_widget)
                self.ui.tabla_pedidos_reg_general_most.setItem(0,2,telPROV_widget)
                self.ui.tabla_pedidos_reg_general_most.setItem(0,3,celPROV_widget)
                encontrado=True
                self.id_proveedor_pedidos_bool=True
            for idPROD,nombrePROD,precioc,preciov,cantidad,idPROV in resultados2:
                        if int(id_proveedor_mod) == idPROV:
                            idPROD_FKwidget= QTableWidgetItem(str(idPROD))
                            nombrePROD_widget= QTableWidgetItem(str(nombrePROD))
                            precioc_widget= QTableWidgetItem(str(precioc))
                            preciov_widget= QTableWidgetItem(str(preciov))
                            cantidad_widget= QTableWidgetItem(str(cantidad))

                            #self.ui.tabla_venta_cons.setItem(row,4,idVENTA_FKwidget)
                            self.ui.tabla_pedidos_reg_general_most.setItem(row,4,idPROD_FKwidget)
                            self.ui.tabla_pedidos_reg_general_most.setItem(row,5,nombrePROD_widget)
                            self.ui.tabla_pedidos_reg_general_most.setItem(row,6,precioc_widget)
                            self.ui.tabla_pedidos_reg_general_most.setItem(row,7,preciov_widget)
                            self.ui.tabla_pedidos_reg_general_most.setItem(row,8,cantidad_widget)
                            row+=1
        if not encontrado:
            self.id_proveedor_pedidos_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El proveedor"{id_proveedor_mod}"no fue encontrado'
            )

    @Slot()
    def consultar_proveedor_producto_mod(self):
        
        id_proveedor_mod=self.ui.idprovee_producto_mod_lineEdit.text()
        resultados= self.articulo1.consulta_proveedor()

        self.ui.tabla_producto_mod_general_most.clear()
        self.ui.tabla_producto_mod_general_most.setRowCount(1)
        self.ui.tabla_producto_mod_general_most.setColumnCount(4)
        headers=["Id proveedor","Nombre","Telefono","Celular"]
        self.ui.tabla_producto_mod_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        for idPROV,nombrePROV,telPROV,celPROV in resultados :
            if int(id_proveedor_mod) == idPROV:
                #print(idEMP,nombreEMP,telEMP,status)
                
                idPROV_widget= QTableWidgetItem(str(idPROV))
                nombrePROV_widget= QTableWidgetItem(str(nombrePROV))
                telPROV_widget= QTableWidgetItem(str(telPROV))
                celPROV_widget= QTableWidgetItem(str(celPROV))

                self.ui.tabla_producto_mod_general_most.setItem(0,0,idPROV_widget)
                self.ui.tabla_producto_mod_general_most.setItem(0,1,nombrePROV_widget)
                self.ui.tabla_producto_mod_general_most.setItem(0,2,telPROV_widget)
                self.ui.tabla_producto_mod_general_most.setItem(0,3,celPROV_widget)
                encontrado=True
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'El proveedor"{id_proveedor_mod}"no fue encontrado'
            )

    @Slot()
    def consultar_producto_mod(self): 
        id_producto_mod=self.ui.id_product_mod_lineEdit.text()
        resultados= self.articulo1.consulta_producto()

        self.ui.tabla_producto_mod_general_most.clear()
        self.ui.tabla_producto_mod_general_most.setRowCount(1)
        self.ui.tabla_producto_mod_general_most.setColumnCount(6)
        headers=["Id producto","Nombre","Precio compra","Precio venta","Cantidad","Id proveedor"]
        self.ui.tabla_producto_mod_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        
        for idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROVEE_fk in resultados :
        
            if int(id_producto_mod) == idPROD:
                #print(idEMP,nombreEMP,telEMP,status)
                
                idPROD_widget= QTableWidgetItem(str(idPROD))
                nombrePROD_widget= QTableWidgetItem(str(nombrePROD))
                precioCompra_widget= QTableWidgetItem(str(precioCompra))
                precioVenta_widget= QTableWidgetItem(str(precioVenta))
                cantidad_widget= QTableWidgetItem(str(cantidad))
                idPROV_fk_widget= QTableWidgetItem(str(idPROVEE_fk))

                self.ui.tabla_producto_mod_general_most.setItem(0,0,idPROD_widget)
                self.ui.tabla_producto_mod_general_most.setItem(0,1,nombrePROD_widget)
                self.ui.tabla_producto_mod_general_most.setItem(0,2,precioCompra_widget)
                self.ui.tabla_producto_mod_general_most.setItem(0,3,precioVenta_widget)
                self.ui.tabla_producto_mod_general_most.setItem(0,4,cantidad_widget)
                self.ui.tabla_producto_mod_general_most.setItem(0,5,idPROV_fk_widget)
                encontrado=True
                self.id_producto_bool=True
        if not encontrado:
            self.id_producto_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El producto"{id_producto_mod}"no fue encontrado'
            )

    @Slot()
    def consultar_producto_pedidos_reg(self): 
        id_producto_mod=self.ui.id_producto_pedido_detalle_reg_lineEdit.text()
        resultados= self.articulo1.consulta_producto()

        self.ui.tabla_pedidos_reg_general_most.clear()
        self.ui.tabla_pedidos_reg_general_most.setRowCount(1)
        self.ui.tabla_pedidos_reg_general_most.setColumnCount(6)
        headers=["Id producto","Nombre","Precio compra","Precio venta","Cantidad","Id proveedor"]
        self.ui.tabla_pedidos_reg_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        
        for idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROVEE_fk in resultados :
        
            if int(id_producto_mod) == idPROD:
                #print(idEMP,nombreEMP,telEMP,status)
                
                idPROD_widget= QTableWidgetItem(str(idPROD))
                nombrePROD_widget= QTableWidgetItem(str(nombrePROD))
                precioCompra_widget= QTableWidgetItem(str(precioCompra))
                precioVenta_widget= QTableWidgetItem(str(precioVenta))
                cantidad_widget= QTableWidgetItem(str(cantidad))
                idPROV_fk_widget= QTableWidgetItem(str(idPROVEE_fk))

                self.ui.tabla_pedidos_reg_general_most.setItem(0,0,idPROD_widget)
                self.ui.tabla_pedidos_reg_general_most.setItem(0,1,nombrePROD_widget)
                self.ui.tabla_pedidos_reg_general_most.setItem(0,2,precioCompra_widget)
                self.ui.tabla_pedidos_reg_general_most.setItem(0,3,precioVenta_widget)
                self.ui.tabla_pedidos_reg_general_most.setItem(0,4,cantidad_widget)
                self.ui.tabla_pedidos_reg_general_most.setItem(0,5,idPROV_fk_widget)
                encontrado=True
                self.id_producto_pedidos_bool=True
        if not encontrado:
            self.id_producto_pedidos_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El producto"{id_producto_mod}"no fue encontrado'
            )

    @Slot()
    def consultar_producto_devolucion_reg(self):
        
        id_producto_cons=self.ui.id_producto_detalledevolucion_reg_lineEdit.text()
        resultados= self.articulo1.consulta_producto()

        self.ui.tabla_devolucion_reg_general_most.clear()
        self.ui.tabla_devolucion_reg_general_most.setRowCount(1)
        self.ui.tabla_devolucion_reg_general_most.setColumnCount(6)
        headers=["Id producto","Nombre","Precio Compra","Precio Venta","Cantidad","Id Proveedor"]
        self.ui.tabla_devolucion_reg_general_most.setHorizontalHeaderLabels(headers)
        
        encontrado=False
        for idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROVEE_fk in resultados :
            if int(id_producto_cons) == idPROD:
                
                idPROD_widget= QTableWidgetItem(str(idPROD))
                nombrePROD_widget= QTableWidgetItem(str(nombrePROD))
                precioCompra_widget= QTableWidgetItem(str(precioCompra))
                precioVenta_widget= QTableWidgetItem(str(precioVenta))
                cantidad_widget= QTableWidgetItem(str(cantidad))
                idPROVEE_fk_widget= QTableWidgetItem(str(idPROVEE_fk))

                self.ui.tabla_devolucion_reg_general_most.setItem(0,0,idPROD_widget)
                self.ui.tabla_devolucion_reg_general_most.setItem(0,1,nombrePROD_widget)
                self.ui.tabla_devolucion_reg_general_most.setItem(0,2,precioCompra_widget)
                self.ui.tabla_devolucion_reg_general_most.setItem(0,3,precioVenta_widget)
                self.ui.tabla_devolucion_reg_general_most.setItem(0,4,cantidad_widget)
                self.ui.tabla_devolucion_reg_general_most.setItem(0,5,idPROVEE_fk_widget)
                encontrado=True
                self.id_producto_devolucion_bool=True
        if not encontrado:
            self.id_producto_devolucion_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El producto"{id_producto_cons}"no fue encontrado'
            )

    @Slot()
    def consultar_venta_devolucion_reg(self):
        
        id_venta_cons=self.ui.codigoventa_devolucion_reg_lineEdit.text()
        resultados= self.articulo1.consulta_venta()
        resultados2=self.articulo1.consulta_venta_detalle(id_venta_cons)
            
        self.ui.tabla_devolucion_reg_general_most.clear()
        self.ui.tabla_devolucion_reg_general_most.setRowCount(len(resultados2))
        self.ui.tabla_devolucion_reg_general_most.setColumnCount(7)
     
        headers=["Id venta","Fecha","Id empleado","Id cliente","Id producto","Precio","Cantidad"]
        self.ui.tabla_devolucion_reg_general_most.setHorizontalHeaderLabels(headers)
        
        
        encontrado=False
        for idVENTA,fechaVENTA,idEMP_fk,idCLIENT_FK in resultados :
        
            if int(id_venta_cons) == idVENTA:
                
                
                idVENTA_widget= QTableWidgetItem(str(idVENTA))
                fechaVENTA_widget= QTableWidgetItem(str(fechaVENTA))
                idEMP_fk_widget= QTableWidgetItem(str(idEMP_fk))
                idCLIENT_FK_widget= QTableWidgetItem(str(idCLIENT_FK))
                

                self.ui.tabla_devolucion_reg_general_most.setItem(0,0,idVENTA_widget)
                self.ui.tabla_devolucion_reg_general_most.setItem(0,1,fechaVENTA_widget)
                self.ui.tabla_devolucion_reg_general_most.setItem(0,2,idEMP_fk_widget)
                self.ui.tabla_devolucion_reg_general_most.setItem(0,3,idCLIENT_FK_widget)
                row=0
                encontrado=True
                self.id_venta_devolucion_bool=True
                for idVENTA_FK,idPROD_FK,precioPROD,cantidadPROD in resultados2:
                        if int(id_venta_cons) == idVENTA_FK:
                            print(idVENTA_FK,idPROD_FK,precioPROD,cantidadPROD)
                            idVENTA_FKwidget= QTableWidgetItem(str(idVENTA_FK))
                            idPROD_FK_widget= QTableWidgetItem(str(idPROD_FK))
                            precioPROD_widget= QTableWidgetItem(str(precioPROD))
                            cantidadPROD_widget= QTableWidgetItem(str(cantidadPROD))

                            #self.ui.tabla_venta_cons.setItem(row,4,idVENTA_FKwidget)
                            self.ui.tabla_devolucion_reg_general_most.setItem(row,4,idPROD_FK_widget)
                            self.ui.tabla_devolucion_reg_general_most.setItem(row,5,precioPROD_widget)
                            self.ui.tabla_devolucion_reg_general_most.setItem(row,6,cantidadPROD_widget)
                            row+=1
        if not encontrado:
            self.id_venta_devolucion_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'La venta"{id_venta_cons}"no fue encontrada'
            )
    
    @Slot()
    def consultar_empleado_devolucion_reg(self):
        
        id_empleado_cons=self.ui.codigoempleado_devolucion_reg_lineEdit.text()
        resultados= self.articulo1.consulta_empleado()

        self.ui.tabla_devolucion_reg_general_most.clear()
        self.ui.tabla_devolucion_reg_general_most.setRowCount(1)
        self.ui.tabla_devolucion_reg_general_most.setColumnCount(4)
        headers=["Id empleado","Nombre","Telefono","Status"]
        self.ui.tabla_devolucion_reg_general_most.setHorizontalHeaderLabels(headers)
        
        encontrado=False
        for idEMP,nombreEMP,telEMP,status in resultados :
            if int(id_empleado_cons) == idEMP:
                
                idEMP_widget= QTableWidgetItem(str(idEMP))
                nombreEMP_widget= QTableWidgetItem(str(nombreEMP))
                telEMP_widget= QTableWidgetItem(str(telEMP))
                status_widget= QTableWidgetItem(str(status))

                self.ui.tabla_devolucion_reg_general_most.setItem(0,0,idEMP_widget)
                self.ui.tabla_devolucion_reg_general_most.setItem(0,1,nombreEMP_widget)
                self.ui.tabla_devolucion_reg_general_most.setItem(0,2,telEMP_widget)
                self.ui.tabla_devolucion_reg_general_most.setItem(0,3,status_widget)
                encontrado=True
                self.id_empleado_devolucion_bool=True
        if not encontrado:
            self.id_empleado_devolucion_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El empleado"{id_empleado_cons}"no fue encontrado'
            )

    @Slot()
    def consultar_empleado_venta(self):
        
        resultados= self.articulo1.consulta_venta()
        self.actulizar_id_venta_reg()
        id_empleado_cons=self.ui.idempleado_venta_reg_lineEdit.text()
        resultados= self.articulo1.consulta_empleado()

        self.ui.tabla_general_most.clear()
        self.ui.tabla_general_most.setRowCount(1)
        self.ui.tabla_general_most.setColumnCount(2)
        headers=["Id empleado","Nombre"]
        self.ui.tabla_general_most.setHorizontalHeaderLabels(headers)
        
        #print(resultados)
        encontrado=False
        for idEMP,nombreEMP,telEMP,status in resultados :
            if int(id_empleado_cons) == idEMP:
                #print(idEMP,nombreEMP,telEMP,status)
                
                idEMP_widget= QTableWidgetItem(str(idEMP))
                nombreEMP_widget= QTableWidgetItem(str(nombreEMP))

                self.ui.tabla_general_most.setItem(0,0,idEMP_widget)
                self.ui.tabla_general_most.setItem(0,1,nombreEMP_widget)
                
                encontrado=True
                self.id_empleado_venta_bool=True
        if not encontrado:
            self.id_empleado_venta_bool=False
            QMessageBox.warning(
                self,
                "Atencion",
                f'El empleado"{id_empleado_cons}"no fue encontrado'
            )

    @Slot()
    def registrar_pedido(self):
        #try:
            self.id_cantidad_detalles_pedido_reg=self.ui.cantidad_compras_reg_lineEdit.text()
            if  self.id_proveedor_pedidos_bool==True and self.id_producto_pedidos_bool==True and self.id_cantidad_detalles_pedido_reg !="" and self.id_cantidad_detalles_pedido_reg !="0":
                id_prove_detalles_pedido_reg=self.ui.idproveedor_compras_reg_lineEdit.text()
                self.articulo1.alta_pedido(id_prove_detalles_pedido_reg)

                self.id_producto_detalles_pedido_reg=self.ui.id_producto_pedido_detalle_reg_lineEdit.text()
                
                cons=0
                for indd in self.producto_pedido:
                    self.articulo1.alta_pedido_detalles(self.id_pedido_new_reg,indd,self.cantidadespedido_lista[cons])
                    self.articulo1.sumar_cantidad_prod(self.cantidadespedido_lista[cons],indd)
                    cons+=1
                QMessageBox.information(
                    self,
                    "Registro",
                    f'El pedido"{self.id_pedido_new_reg}"a sido registrado'
                    )
                self.actulizar_id_pedido_reg()
            if  self.id_proveedor_pedidos_bool== False:
                QMessageBox.warning(
                        self,
                        "Id proveedor",
                        f'Id proveedor incorrecto, no encontrado.'
                        )
            if self.id_producto_pedidos_bool==False:
                QMessageBox.warning(
                        self,
                        "Id producto",
                        f'Id producto incorrecto, no encontrado.'
                        )
            if self.id_cantidad_detalles_pedido_reg == "0":
                QMessageBox.warning(
                            self,
                            "Cantidad",
                            f'Ingrese una cantidad correcta.'
                            )
            if self.id_cantidad_detalles_pedido_reg == "":
                QMessageBox.warning(
                            self,
                            "Cantidad",
                            f'Ingrese una cantidad correcta.'
                            )
    """ 
        except mysql.connector.errors.DatabaseError:
            QMessageBox.warning(
                self,
                "Sin datos",
                f'El pedido no a sido registrado, campos vacios en formulario.'
                )
        """
    @Slot()
    def registrar_empleado(self):
        #try:
            nombre_empleado_reg = self.ui.nombre_empleado_reg_lineEdit.text()
            telefono_empleado_reg= self.ui.telefono_empleado_reg_lineEdit_2.text()
            status_empleadp_reg=self.ui.status_empleado_reg_spinBox.value()
            telefonos=self.articulo1.consultar_tel_empleado_reg(telefono_empleado_reg)
            
            if nombre_empleado_reg!=""and telefono_empleado_reg!="" and status_empleadp_reg!="" and len(telefonos)==0:
                self.articulo1.alta_empleado(nombre_empleado_reg,telefono_empleado_reg,status_empleadp_reg)
                QMessageBox.information(
                    self,
                    "Registro",
                    f'El empleado"{self.id_empleado_new_reg}"a sido registrado'
                    )
                self.actulizar_id_empleado_reg()
            if len(telefonos)!=0:
                QMessageBox.warning(
                    self,
                    "Telefono duplicado",
                    f'Los empleados no pueden tener un telefono igual.'
                )
            if nombre_empleado_reg==""and telefono_empleado_reg=="" and status_empleadp_reg=="":
                QMessageBox.warning(
                    self,
                    "Sin datos",
                    f'El empleado no a sido registrado, campos vacios en formulario.'
                )
                self.actulizar_id_empleado_reg()
    """
        except mysql.connector.errors.DatabaseError:
            QMessageBox.warning(
                self,
                "Sin datos",
                f'El empleado no a sido registrado, campos vacios en formulario.'
                )
        """
    @Slot()
    def registrar_cliente(self):
        try:
            nombre_cliente_reg=self.ui.nombre_cliente_reg_lineEdit.text()
            direccion_cliente_reg=self.ui.direccion_cliente_reg_lineEdit.text()
            puntos_cliente_reg=self.ui.puntos_cliente_reg_lineEdit.text()
            self.articulo1.alta_cliente(nombre_cliente_reg,direccion_cliente_reg,puntos_cliente_reg)
            QMessageBox.information(
                self,
                "Registro",
                f'El cliente"{self.id_cliente_new_reg}"a sido registrado'
                )
            self.actulizar_id_cliente_reg()
        except mysql.connector.errors.DatabaseError:
            QMessageBox.warning(
                self,
                "Sin datos",
                f'El cliente no a sido registrado, campos vacios en formulario.'
                )
    @Slot()
    def registrar_proveedor(self):
        #try:
            nombre_proveedor_reg=self.ui.nombre_proveedor_reg_lineEdit.text()
            telefono_proveedor_reg=self.ui.telefono_proveedor_reg_lineEdit.text()
            celular_proveedor_reg=self.ui.celular_proveedor_reg_lineEdit.text()
            nombres=self.articulo1.consultar_nombre_proveedor_reg(nombre_proveedor_reg)
            telefonos=self.articulo1.consultar_tel_proveedor_reg(telefono_proveedor_reg)
            celulares=self.articulo1.consultar_cel_proveedor_reg(celular_proveedor_reg)
            
            
            if nombre_proveedor_reg!="" and telefono_proveedor_reg!="" and celular_proveedor_reg!="" and len(nombres)==0 and len(telefonos)==0 and len(celulares)==0:
                self.articulo1.alta_proveedor(nombre_proveedor_reg,telefono_proveedor_reg,celular_proveedor_reg)
                QMessageBox.information(
                    self,
                    "Registro",
                    f'El proveedor"{self.id_proveedor_new_reg}"a sido registrado'
                    )
                self.actulizar_id_proveedor_reg()
            if len(nombres)!=0:
                QMessageBox.warning(
                    self,
                    "Nombre duplicado",
                    f'Los proveedores no pueden tener nombres iguales.'
                )
            if len(telefonos)!=0:
                QMessageBox.warning(
                    self,
                    "Telefono duplicado",
                    f'Los proveedores no pueden tener un telefono igual.'
                )
            if len(celulares)!=0:
                QMessageBox.warning(
                    self,
                    "Celular duplicado",
                    f'Los proveedores no pueden tener un celular igual.'
                )
            if nombre_proveedor_reg=="" and telefono_proveedor_reg=="" and celular_proveedor_reg=="":
                QMessageBox.warning(
                    self,
                    "Sin datos",
                    f'El proveedor no a sido registrado, campos vacios en formulario.'
                    )
    """except mysql.connector.errors.DatabaseError:
             QMessageBox.warning(
                self,
                "Sin datos",
                f'El cliente no a sido registrado, campos vacios en formulario.'
                )
        """
    @Slot()
    def registrar_producto(self):
        try:

            cantidad_producto_reg=self.ui.cantidad_producto_reg_lineEdit.text()
            nombre_producto_reg=self.ui.nombre_producto_reg_lineEdit.text()
            nombres=self.articulo1.consultar_nombre_producto_reg(nombre_producto_reg)
            if self.id_proveedor_prod_bool==True and cantidad_producto_reg!="0" and cantidad_producto_reg!="" and len(nombres)==0:
                
                preciocompra_producto_reg=self.ui.preciocomp_producto_reg_lineEdit.text()
                precioventa_producto_reg=self.ui.preciovent_producto_reg_lineEdit.text()
                
                idproveedor_producto_reg=self.ui.idprovee_producto_reg_lineEdit.text()
                self.articulo1.alta_producto(nombre_producto_reg,preciocompra_producto_reg,precioventa_producto_reg,cantidad_producto_reg,idproveedor_producto_reg)
                
                QMessageBox.information(
                    self,
                    "Registro",
                    f'El producto"{self.id_producto_new_reg}"a sido registrado'
                    )
                self.actulizar_id_producto_reg()
            if cantidad_producto_reg=="":
                QMessageBox.information(
                        self,
                        "Cantidad",
                        f'Ingrese una cantidad correcta.'
                        )
            if cantidad_producto_reg=="0":
                QMessageBox.information(
                        self,
                        "Cantidad",
                        f'Ingrese una cantidad correcta.'
                        )
            if self.id_proveedor_prod_bool==False:
                QMessageBox.warning(
                        self,
                        "Id proveedor",
                        f'Id proveedor incorrecto, no encontrado.'
                        )
            if len(nombres)!=0:
                QMessageBox.warning(
                        self,
                        "Nombre duplicado",
                        f'Los productos no pueden tener nombres iguales.'
                        )
        except mysql.connector.errors.DatabaseError:
             QMessageBox.warning(
                self,
                "Sin datos",
                f'El producto no a sido registrado, campos vacios en formulario.'
                )
    @Slot()
    def registrar_venta(self):
        #try:
            if self.id_empleado_venta_bool==True and self.id_cliente_venta_bool==True and self.id_producto_venta_bool==True and len(self.productos_lista) !=0:
                #Venta
                #fecha_venta_reg=self.ui.fecha_venta_reg_dateEdit_2.text()
                idempleado_venta_reg=self.ui.idempleado_venta_reg_lineEdit.text()
                idcliente_venta_reg=self.ui.idcliente_venta_reg_lineEdit.text()
                self.articulo1.alta_venta(idempleado_venta_reg,idcliente_venta_reg)
                #Detalle venta
                idproducto_venta_reg=self.ui.idproducto_venta_reg_lineEdit.text()
                cantidadproducto_venta_reg=self.ui.cantidadproducto_venta_reg_spinBox.value()
                #self.articulo1.alta_venta_detalle(self.id_venta_new_reg_venta,idproducto_venta_reg,self.precio_prod,cantidadproducto_venta_reg)
                indd=0
                for indice in self.productos_lista:
                    self.articulo1.alta_venta_detalle(self.id_venta_new_reg,indice,self.precios_lista[indd],self.cantidades_lista[indd])
                    
                    indice=int(indice)
                    self.articulo1.restar_cantidad_prod(self.cantidades_lista[indd],indice)   
                    indd+=1
                QMessageBox.information(
                    self,
                    "Registro",
                    f'La venta"{self.id_venta_new_reg}"a sido registrada'
                    )
                self.actulizar_id_venta_reg() 
                
            if self.id_empleado_venta_bool==False:
                QMessageBox.warning(
                        self,
                        "Id empleado",
                        f'Id empleado incorrecto, no encontrado.'
                        )
            if self.id_cliente_venta_bool==False:
                QMessageBox.warning(
                        self,
                        "Id cliente",
                        f'Id cliente incorrecto, no encontrado.'
                        )
            if self.id_producto_venta_bool==False:
                QMessageBox.warning(
                        self,
                        "Id producto",
                        f'Id producto incorrecto, no encontrado.'
                        )
            if len(self.productos_lista)==0:
                QMessageBox.warning(
                        self,
                        "Productos",
                        f'No hay productos agregados a la lista.'
                        )
            
            """except mysql.connector.errors.DatabaseError:
                QMessageBox.warning(
                    self,
                    "Sin datos",
                    f'La venta no a sido registrada, campos vacios en formulario.'
                    )
            """   


    @Slot()
    def coencide_devolucion(self):
        idproducto_dev_reg=self.ui.id_producto_detalledevolucion_reg_lineEdit.text()
        detalle_ventas=self.articulo1.consulta_venta_detalle(idproducto_dev_reg)
        print(detalle_ventas)
        idventa_devolucion_reg=self.ui.codigoventa_devolucion_reg_lineEdit.text() 
        retornar=False
        for id_detalle,idVENTA_FK,idPROD_FK,precioPROD,cantidadPROD in detalle_ventas:
            if  idventa_devolucion_reg == idVENTA_FK: 
                self.coencide_ventadev_detalleventa=True
            if idproducto_dev_reg ==idPROD_FK:
                self.coencide_productodev_detalleventa=True
            if self.coencide_productodev_detalleventa==False and self.coencide_ventadev_detalleventa==True:
                QMessageBox.warning(
                    self,
                    "Id producto",
                    f'Id producto incorrecto, no coencide con la venta.'
                    )
                retornar=False
            if self.coencide_productodev_detalleventa==True and self.coencide_ventadev_detalleventa==False:
                QMessageBox.warning(
                    self,
                    "Id venta",
                    f'Id venta incorrecto, no coencide con la venta.'
                    )
                retornar=False
            if self.coencide_productodev_detalleventa==True and self.coencide_ventadev_detalleventa==True:
                retornar==True
        return retornar
        """if self.coencide_productodev_detalleventa==False and self.coencide_ventadev_detalleventa==True:

                    QMessageBox.warning(
                        self,
                        "Id producto",
                        f'Id producto incorrecto, no coencide con la venta.'
                        )
            """
    @Slot()
    def registrar_devolucion(self):
        try:
            print(len(self.cantidadedevolucion_lista))
            if self.id_venta_devolucion_bool == True and self.id_empleado_devolucion_bool == True  and self.id_producto_devolucion_bool == True and len(self.cantidadedevolucion_lista) != 0 :#and self.coencide_productodev_detalleventa==True and self.coencide_ventadev_detalleventa==True:
                idventa_devolucion_reg=self.ui.codigoventa_devolucion_reg_lineEdit.text()
                idempleado_devolucion_reg=self.ui.codigoempleado_devolucion_reg_lineEdit.text()
                
                detalle_ventas=self.articulo1.consulta_venta_detalle(self.id_producto_detalles_devolucion_reg)
                self.articulo1.alta_devolucion(idempleado_devolucion_reg,idventa_devolucion_reg)
                
                id_producto_detalle_devolucion=self.ui.id_producto_detalledevolucion_reg_lineEdit.text()
                cantidad_detalle_devolucion=self.ui.cantidad_producto_detalledevolucion_reg_lineEdit.text()
                cons=0
                self.actulizar_id_devolucion_reg()
                for indd in self.producto_devolucion:
                    self.id_devolucion_new_reg=str(int(self.id_devolucion_new_reg)-1)
                    
                    self.articulo1.alta_detalles_devolucion(self.id_devolucion_new_reg,indd,self.cantidadedevolucion_lista[cons])
                    self.articulo1.sumar_cantidad_prod(self.cantidadedevolucion_lista[cons],indd)
                    cons+=1  
                QMessageBox.information(
                    self,
                    "Registro",
                    f'La devolución"{self.id_devolucion_new_reg}"a sido registrada'
                    )
                self.actulizar_id_devolucion_reg()
            if self.id_venta_devolucion_bool == False :
                QMessageBox.warning(
                        self,
                        "Id venta",
                        f'Id venta incorrecto, no encontrado.'
                        )
            if self.id_empleado_devolucion_bool == False  :
                QMessageBox.warning(
                        self,
                        "Id empleado",
                        f'Id empleado incorrecto, no encontrado.'
                        )
            if self.id_producto_devolucion_bool == False:
                QMessageBox.warning(
                        self,
                        "Id producto",
                        f'Id producto incorrecto, no encontrado.'
                        )
            if len(self.cantidadedevolucion_lista)==0:
                QMessageBox.warning(
                        self,
                        "Productos",
                        f'No hay productos agregados a la lista.'
                        )
            
        except mysql.connector.errors.DatabaseError:
                QMessageBox.warning(
                    self,
                    "Sin datos",
                    f'La devolucion no a sido registrada, campos vacios en formulario.'
                    )
            
    
        
    @Slot()
    def registrar_compras(self):
        print("true")
    @Slot()
    def modificar_empleado(self):
        try:
            id_empleado_mod=self.ui.id_empleado_mod_lineEdit.text()
            nombre_empleado_mod = self.ui.nombre_empleado_mod_lineEdit.text()
            telefono_empleado_mod= self.ui.telefono_empleado_mod_lineEdit.text()
            status_empleadp_mod=self.ui.status_empleado_mod_spinBox.value()
            telefonos=self.articulo1.consultar_tel_empleado_reg(telefono_empleado_mod)
            if self.id_empleado_bool==True:
                if len(telefonos)!=0:
                    QMessageBox.warning(
                        self,
                        "Telefono duplicado",
                        f'Los empleados no pueden tener un telefono igual.'
                    )
                if nombre_empleado_mod != "":
                    self.articulo1.modificar_empleado_nombre(nombre_empleado_mod,id_empleado_mod)
                    self.consultar_empleado_mod()
                    QMessageBox.information(
                        self,
                        "Registro",
                        f'La modificación del empleado"{id_empleado_mod}"a sido registrada'
                        )
                print(len(telefonos))
                if telefono_empleado_mod !="":
                    if len(telefonos)==0:
                        self.articulo1.modificar_empleado_telefono(telefono_empleado_mod,id_empleado_mod)
                        self.consultar_empleado_mod()
                        QMessageBox.information(
                            self,
                            "Registro",
                            f'La modificación del empleado"{id_empleado_mod}"a sido registrada'
                            )
                if status_empleadp_mod !="":
                    self.articulo1.modificar_empleado_status(status_empleadp_mod,id_empleado_mod)
                    self.consultar_empleado_mod()
                    #self.articulo1.alta_empleado(id_empleado_mod,nombre_empleado_mod,telefono_empleado_mod,status_empleadp_mod)
                    QMessageBox.information(
                        self,
                        "Registro",
                        f'La modificación del empleado"{id_empleado_mod}"a sido registrada'
                        )
                
            else:
                    QMessageBox.warning(
                        self,
                        "Id empleado",
                        f'El empleado no a sido modificado, id empleado incorrecto.'
                        )
        except:
            QMessageBox.warning(
                self,
                "Sin datos",
                f'El empleado no a sido modificado, campos vacios en formulario.'
                )

    @Slot()
    def modificar_cliente(self):
        try:
            id_cliente_mod=self.ui.id_cliente_mod_lineEdit.text()
            nombre_cliente_mod=self.ui.nombre_cliente_mod_lineEdit.text()
            direccion_cliente_mod=self.ui.direccion_cliente_mod_lineEdit.text()
            puntos_cliente_mod=self.ui.puntos_cliente_mod_lineEdit.text()
            if self.id_cliente_bool==True:
                
                if nombre_cliente_mod != "":
                    self.articulo1.modificar_cliente_nombre(nombre_cliente_mod,id_cliente_mod)
                    self.consultar_cliente_mod()
                if direccion_cliente_mod !="":
                    self.articulo1.modificar_cliente_direccion(direccion_cliente_mod,id_cliente_mod)
                    self.consultar_cliente_mod()
                if puntos_cliente_mod !="":
                    self.articulo1.modificar_cliente_puntos(puntos_cliente_mod,id_cliente_mod,)
                    self.consultar_cliente_mod()
                    #self.articulo1.alta_empleado(id_empleado_mod,nombre_empleado_mod,telefono_empleado_mod,status_empleadp_mod)
                if id_cliente_mod !="" and nombre_cliente_mod != "" or direccion_cliente_mod != "" or puntos_cliente_mod != "":
                    #self.ui.id_cliente_mod_lineEdit.clear()
                    QMessageBox.information(
                        self,
                        "Registro",
                        f'La modificación del cliente"{id_cliente_mod}"a sido registrada'
                        )
                else:
                    QMessageBox.warning(
                        self,
                        "Sin datos",
                        f'El cliente no a sido modificado, campos vacios en formulario.'
                        )
            else:
                    QMessageBox.warning(
                        self,
                        "Id cliente",
                        f'El cliente no a sido modificado, id cliente incorrecto.'
                        )
        except:
            QMessageBox.warning(
                self,
                "Sin datos",
                f'El cliente no a sido modificado, campos vacios en formulario.'
                )
    @Slot()
    def modificar_proveedor(self):
        try:
            id_proveedor_mod=self.ui.id_proveedor_mod_lineEdit.text()
            nombre_proveedor_mod=self.ui.nombre_proveedor_mod_lineEdit.text()
            telefono_proveedor_mod=self.ui.telefono_proveedor_mod_lineEdit.text()
            celular_proveedor_mod=self.ui.celular_proveedor_mod_lineEdit.text()
            nombres=self.articulo1.consultar_nombre_proveedor_reg(nombre_proveedor_mod)
            telefonos=self.articulo1.consultar_tel_proveedor_reg(telefono_proveedor_mod)
            celulares=self.articulo1.consultar_cel_proveedor_reg(celular_proveedor_mod)
            
            if self.id_proveedor_bool==True:
                if nombre_proveedor_mod != "" and len(nombres)==0:
                    self.articulo1.modificar_proveedor_nombre(nombre_proveedor_mod,id_proveedor_mod)
                    self.consultar_proveedor_mod()
                if telefono_proveedor_mod !="" and len(telefonos)==0:
                    self.articulo1.modificar_proveedor_telefono(telefono_proveedor_mod,id_proveedor_mod)
                    self.consultar_proveedor_mod()
                if celular_proveedor_mod !="" and len(celulares)==0:
                    self.articulo1.modificar_proveedor_celular(celular_proveedor_mod,id_proveedor_mod,)
                    self.consultar_proveedor_mod()
                if id_proveedor_mod!="" and (nombre_proveedor_mod != "" and len(nombres)==0 ) or (telefono_proveedor_mod !="" and len(telefonos)==0) or (celular_proveedor_mod !="") and len(celulares)==0:
                    QMessageBox.information(
                            self,
                            "Registro",
                            f'La modificación del proveedor"{id_proveedor_mod}"a sido registrada'
                            )
                if id_proveedor_mod!="" and (nombre_proveedor_mod != "" and len(nombres)!=0 ):
                    QMessageBox.warning(
                        self,
                        "Nombre duplicado",
                        f'Los proveedores no pueden tener el mismo nombre.'
                        )
                if id_proveedor_mod!="" and (telefono_proveedor_mod != "" and len(telefonos)!=0 ):
                    QMessageBox.warning(
                        self,
                        "Telefono duplicado",
                        f'Los proveedores no pueden tener el mismo telefono.'
                        )
                if id_proveedor_mod!="" and (celular_proveedor_mod != "" and len(celulares)!=0 ):
                    QMessageBox.warning(
                        self,
                        "Celular duplicado",
                        f'Los proveedores no pueden tener el mismo celular.'
                        )
                
            else:
                    QMessageBox.warning(
                        self,
                        "Id proveedor",
                        f'El proveedor no a sido modificado, id proveedor incorrecto.'
                        )
        except:
            QMessageBox.warning(
                self,
                "Sin datos",
                f'El proveedor no a sido modificado, campos vacios en formulario.'
                )
    @Slot()
    def modificar_producto(self):
        try:
            id_producto_mod=self.ui.id_product_mod_lineEdit.text()
            nombre_producto_mod=self.ui.nombre_producto_mod_lineEdit.text()
            preciocompra_produto_mod=self.ui.preciocomp_producto_mod_lineEdit.text()
            precioventa_producto_mod=self.ui.preciovent_producto_mod_lineEdit.text()
            idproveedor_producto_mod=self.ui.idprovee_producto_mod_lineEdit.text()
            cantidad_producto_mod=self.ui.cantidad_producto_mod_lineEdit.text()
            nombres=self.articulo1.consultar_nombre_producto_reg(nombre_producto_mod)
            if self.id_producto_bool==True:
                if nombre_producto_mod != "" and len(nombres)!=0:
                    QMessageBox.warning(
                        self,
                        "Nombre duplicado",
                        f'Los productos no pueden tener el mismo nombre.'
                        )
                if nombre_producto_mod != "" and len(nombres)==0:
                    self.articulo1.modificar_producto_nombre(nombre_producto_mod,id_producto_mod)
                    self.consultar_producto_mod()
                if preciocompra_produto_mod !="":
                    self.articulo1.modificar_producto_preciocompra(preciocompra_produto_mod,id_producto_mod)
                    self.consultar_producto_mod()
                if precioventa_producto_mod !="":
                    self.articulo1.modificar_producto_precioventa(precioventa_producto_mod,id_producto_mod,)
                    self.consultar_producto_mod()
                if idproveedor_producto_mod !="":
                    self.articulo1.modificar_producto_idproveedor(idproveedor_producto_mod,id_producto_mod,)
                    self.consultar_producto_mod()
                if cantidad_producto_mod !="":
                    self.articulo1.modificar_producto_cantidad(cantidad_producto_mod,id_producto_mod,)
                    self.consultar_producto_mod()
                if id_producto_mod !="" and  len(nombres)==0 and nombre_producto_mod != "" or preciocompra_produto_mod !="" or precioventa_producto_mod !="" or idproveedor_producto_mod !="" or cantidad_producto_mod !="" :
                    QMessageBox.information(
                        self,
                        "Registro",
                        f'La modificación del producto"{id_producto_mod}"a sido registrada'
                        )
        
            else:
                    QMessageBox.warning(
                        self,
                        "Id producto",
                        f'El producto no a sido modificado, id producto incorrecto.'
                        )
        except:
             QMessageBox.warning(
                self,
                "Sin datos",
                f'El producto no a sido modificado, campos vacios en formulario.'
                )
    
    @Slot()
    def consultar_empleado(self):
        
        id_empleado_cons=self.ui.id_empleado_cons_lineEdit.text()
        resultados= self.articulo1.consulta_empleado()

        self.ui.tabla_empleado_cons.clear()
        self.ui.tabla_empleado_cons.setRowCount(1)
        self.ui.tabla_empleado_cons.setColumnCount(4)
        headers=["Id empleado","Nombre","Telefono","Status"]
        self.ui.tabla_empleado_cons.setHorizontalHeaderLabels(headers)
        
        try:

            encontrado=False
            for idEMP,nombreEMP,telEMP,status in resultados :
                if int(id_empleado_cons) == idEMP:
                    
                    idEMP_widget= QTableWidgetItem(str(idEMP))
                    nombreEMP_widget= QTableWidgetItem(str(nombreEMP))
                    telEMP_widget= QTableWidgetItem(str(telEMP))
                    status_widget= QTableWidgetItem(str(status))

                    self.ui.tabla_empleado_cons.setItem(0,0,idEMP_widget)
                    self.ui.tabla_empleado_cons.setItem(0,1,nombreEMP_widget)
                    self.ui.tabla_empleado_cons.setItem(0,2,telEMP_widget)
                    self.ui.tabla_empleado_cons.setItem(0,3,status_widget)
                    encontrado=True
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atencion",
                    f'El empleado"{id_empleado_cons}"no fue encontrado'
                )
        except:
            QMessageBox.warning(
                    self,
                    "Atencion",
                    f'El empleado no fue encontrada,no ingreso un id a buscar.'
                )
    @Slot()
    def mostrar_empleado(self):
        
        resultados= self.articulo1.consulta_empleado()

        self.ui.tabla_empleado_most.clear()
        self.ui.tabla_empleado_most.setRowCount(len(resultados))
        self.ui.tabla_empleado_most.setColumnCount(4)
        headers=["Id empleado","Nombre","Telefono","Status"]
        self.ui.tabla_empleado_most.setHorizontalHeaderLabels(headers)
        row=0
        
        
        for idEMP,nombreEMP,telEMP,status in resultados :
                
            idEMP_widget= QTableWidgetItem(str(idEMP))
            nombreEMP_widget= QTableWidgetItem(str(nombreEMP))
            telEMP_widget= QTableWidgetItem(str(telEMP))
            status_widget= QTableWidgetItem(str(status))

            self.ui.tabla_empleado_most.setItem(row,0,idEMP_widget)
            self.ui.tabla_empleado_most.setItem(row,1,nombreEMP_widget)
            self.ui.tabla_empleado_most.setItem(row,2,telEMP_widget)
            self.ui.tabla_empleado_most.setItem(row,3,status_widget)  
            row+=1 

    @Slot()
    def consultar_cliente(self):
        
        id_cliente_cons=self.ui.id_cliente_cons_lineEdit.text()
        resultados= self.articulo1.consulta_cliente()

        self.ui.tabla_cliente_cons.clear()
        self.ui.tabla_cliente_cons.setRowCount(1)
        self.ui.tabla_cliente_cons.setColumnCount(4)
        headers=["Id cliente","Nombre","Direccion","Puntos"]
        self.ui.tabla_cliente_cons.setHorizontalHeaderLabels(headers)
        
        try:
            encontrado=False
            for idCLIENT,nombreCLIENT,direccionCLIENT,puntos in resultados :
                if int(id_cliente_cons) == idCLIENT:
                    
                    idCLIENT_widget= QTableWidgetItem(str(idCLIENT))
                    nombreCLIENT_widget= QTableWidgetItem(str(nombreCLIENT))
                    direccionCLIENT_widget= QTableWidgetItem(str(direccionCLIENT))
                    puntos_widget= QTableWidgetItem(str(puntos))

                    self.ui.tabla_cliente_cons.setItem(0,0,idCLIENT_widget)
                    self.ui.tabla_cliente_cons.setItem(0,1,nombreCLIENT_widget)
                    self.ui.tabla_cliente_cons.setItem(0,2,direccionCLIENT_widget)
                    self.ui.tabla_cliente_cons.setItem(0,3,puntos_widget)
                    encontrado=True
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atencion",
                    f'El cliente"{id_cliente_cons}"no fue encontrado'
                )
        except:
            QMessageBox.warning(
                    self,
                    "Atencion",
                    f'El cliente no fue encontrada,no ingreso un id a buscar.'
                )
                
    @Slot()
    def mostrar_cliente(self):
        
        resultados= self.articulo1.consulta_cliente()

        self.ui.tabla_cliente_most.clear()
        self.ui.tabla_cliente_most.setRowCount(len(resultados))
        self.ui.tabla_cliente_most.setColumnCount(4)
        headers=["Id cliente","Nombre","Direccion","Puntos"]
        self.ui.tabla_cliente_most.setHorizontalHeaderLabels(headers)
        row=0
      
        for idCLIENT,nombreCLIENT,direccionCLIENT,puntos in resultados :
            
            idCLIENT_widget= QTableWidgetItem(str(idCLIENT))
            nombreCLIENT_widget= QTableWidgetItem(str(nombreCLIENT))
            direccionCLIENT_widget= QTableWidgetItem(str(direccionCLIENT))
            puntos_widget= QTableWidgetItem(str(puntos))

            self.ui.tabla_cliente_most.setItem(row,0,idCLIENT_widget)
            self.ui.tabla_cliente_most.setItem(row,1,nombreCLIENT_widget)
            self.ui.tabla_cliente_most.setItem(row,2,direccionCLIENT_widget)
            self.ui.tabla_cliente_most.setItem(row,3,puntos_widget)  
            row+=1   
                
    @Slot()
    def consultar_proveedor(self):
        
        id_proveedor_cons=self.ui.id_proveedor_cons_lineEdit.text()
        resultados= self.articulo1.consulta_proveedor()

        self.ui.tabla_proveedor_cons.clear()
        self.ui.tabla_proveedor_cons.setRowCount(1)
        self.ui.tabla_proveedor_cons.setColumnCount(4)
        headers=["Id proveedor","Nombre","Telefono","Celular"]
        self.ui.tabla_proveedor_cons.setHorizontalHeaderLabels(headers)
        try:
            encontrado=False
            for idPROV,nombrePROV,telPROV,celPROV in resultados :
                if int(id_proveedor_cons) == idPROV:
                
                    idPROV_widget= QTableWidgetItem(str(idPROV))
                    nombrePROV_widget= QTableWidgetItem(str(nombrePROV))
                    telPROV_widget= QTableWidgetItem(str(telPROV))
                    celPROV_widget= QTableWidgetItem(str(celPROV))

                    self.ui.tabla_proveedor_cons.setItem(0,0,idPROV_widget)
                    self.ui.tabla_proveedor_cons.setItem(0,1,nombrePROV_widget)
                    self.ui.tabla_proveedor_cons.setItem(0,2,telPROV_widget)
                    self.ui.tabla_proveedor_cons.setItem(0,3,celPROV_widget)
                    encontrado=True
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atencion",
                    f'El Proveedor"{id_proveedor_cons}"no fue encontrado'
                )
        except:
            QMessageBox.warning(
                    self,
                    "Atencion",
                    f'El proveedor no fue encontrada,no ingreso un id a buscar.'
                )
    @Slot()
    def mostrar_proveedor(self):
        
        resultados= self.articulo1.consulta_proveedor()

        self.ui.tabla_proveedor_most.clear()
        self.ui.tabla_proveedor_most.setRowCount(len(resultados))
        self.ui.tabla_proveedor_most.setColumnCount(4)
        headers=["Id proveedor","Nombre","Telefono","Celular"]
        self.ui.tabla_proveedor_most.setHorizontalHeaderLabels(headers)
        row=0
        
        for idPROV,nombrePROV,telPROV,celPROV in resultados :
             
            idPROV_widget= QTableWidgetItem(str(idPROV))
            nombrePROV_widget= QTableWidgetItem(str(nombrePROV))
            telPROV_widget= QTableWidgetItem(str(telPROV))
            celPROV_widget= QTableWidgetItem(str(celPROV))

            self.ui.tabla_proveedor_most.setItem(row,0,idPROV_widget)
            self.ui.tabla_proveedor_most.setItem(row,1,nombrePROV_widget)
            self.ui.tabla_proveedor_most.setItem(row,2,telPROV_widget)
            self.ui.tabla_proveedor_most.setItem(row,3,celPROV_widget)  
            row+=1   

    @Slot()
    def consultar_producto(self):
        
        id_producto_cons=self.ui.id_producto_cons_lineEdit.text()
        resultados= self.articulo1.consulta_producto()

        self.ui.tabla_producto_cons.clear()
        self.ui.tabla_producto_cons.setRowCount(1)
        self.ui.tabla_producto_cons.setColumnCount(6)
        headers=["Id producto","Nombre","Precio Compra","Precio Venta","Cantidad","Id Proveedor"]
        self.ui.tabla_producto_cons.setHorizontalHeaderLabels(headers)
        
        try:
            encontrado=False
            for idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROVEE_fk in resultados :
                if int(id_producto_cons) == idPROD:
                
                    idPROD_widget= QTableWidgetItem(str(idPROD))
                    nombrePROD_widget= QTableWidgetItem(str(nombrePROD))
                    precioCompra_widget= QTableWidgetItem(str(precioCompra))
                    precioVenta_widget= QTableWidgetItem(str(precioVenta))
                    cantidad_widget= QTableWidgetItem(str(cantidad))
                    idPROVEE_fk_widget= QTableWidgetItem(str(idPROVEE_fk))

                    self.ui.tabla_producto_cons.setItem(0,0,idPROD_widget)
                    self.ui.tabla_producto_cons.setItem(0,1,nombrePROD_widget)
                    self.ui.tabla_producto_cons.setItem(0,2,precioCompra_widget)
                    self.ui.tabla_producto_cons.setItem(0,3,precioVenta_widget)
                    self.ui.tabla_producto_cons.setItem(0,4,cantidad_widget)
                    self.ui.tabla_producto_cons.setItem(0,5,idPROVEE_fk_widget)
                    encontrado=True
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atencion",
                    f'El producto"{id_producto_cons}"no fue encontrado'
                )
        except:
            QMessageBox.warning(
                    self,
                    "Atencion",
                    f'El producto no fue encontrada,no ingreso un id a buscar.'
                )

    @Slot()
    def mostrar_producto(self):
        
        resultados= self.articulo1.consulta_producto()

        self.ui.tabla_producto_most.clear()
        self.ui.tabla_producto_most.setRowCount(len(resultados))
        self.ui.tabla_producto_most.setColumnCount(6)
        headers=["Id producto","Nombre","Precio Compra","Precio Venta","Cantidad","Id Proveedor"]
        self.ui.tabla_producto_most.setHorizontalHeaderLabels(headers)
        row=0
        
        for idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROVEE_fk in resultados :
                
            idPROD_widget= QTableWidgetItem(str(idPROD))
            nombrePROD_widget= QTableWidgetItem(str(nombrePROD))
            precioCompra_widget= QTableWidgetItem(str(precioCompra))
            precioVenta_widget= QTableWidgetItem(str(precioVenta))
            cantidad_widget= QTableWidgetItem(str(cantidad))
            idPROVEE_fk_widget= QTableWidgetItem(str(idPROVEE_fk))

            self.ui.tabla_producto_most.setItem(row,0,idPROD_widget)
            self.ui.tabla_producto_most.setItem(row,1,nombrePROD_widget)
            self.ui.tabla_producto_most.setItem(row,2,precioCompra_widget)
            self.ui.tabla_producto_most.setItem(row,3,precioVenta_widget)
            self.ui.tabla_producto_most.setItem(row,4,cantidad_widget)
            self.ui.tabla_producto_most.setItem(row,5,idPROVEE_fk_widget)  
            row+=1  

    @Slot()
    def consultar_venta(self):
        #try:
            id_venta_cons=self.ui.id_venta_cons_lineEdit.text()
            resultados= self.articulo1.consulta_venta()
            id_venta_cons=int(id_venta_cons)
            resultados2=self.articulo1.consulta_venta_detalle(id_venta_cons)
            self.ui.tabla_venta_cons.clear()
            self.ui.tabla_venta_cons.setRowCount(len(resultados2))
            self.ui.tabla_venta_cons.setColumnCount(7)

            headers=["Id venta","Fecha","Id empleado","Id cliente","Id producto","Precio","Cantidad"]
            self.ui.tabla_venta_cons.setHorizontalHeaderLabels(headers)
            
            encontrado=False
            for idVENTA,fechaVENTA,idEMP_fk,idCLIENT_FK in resultados :
                if int(id_venta_cons) == idVENTA:
                    print(idVENTA,fechaVENTA,idEMP_fk,idCLIENT_FK)
                    
                    idVENTA_widget= QTableWidgetItem(str(idVENTA))
                    fechaVENTA_widget= QTableWidgetItem(str(fechaVENTA))
                    idEMP_fk_widget= QTableWidgetItem(str(idEMP_fk))
                    idCLIENT_FK_widget= QTableWidgetItem(str(idCLIENT_FK))

                    self.ui.tabla_venta_cons.setItem(0,0,idVENTA_widget)
                    self.ui.tabla_venta_cons.setItem(0,1,fechaVENTA_widget)
                    self.ui.tabla_venta_cons.setItem(0,2,idEMP_fk_widget)
                    self.ui.tabla_venta_cons.setItem(0,3,idCLIENT_FK_widget)
                    encontrado=True
                    row=0
                    for idVENTA_FK,idPROD_FK,precioPROD,cantidadPROD in resultados2:
                        if int(id_venta_cons) == idVENTA_FK:
                            print(idVENTA_FK,idPROD_FK,precioPROD,cantidadPROD)
                            idVENTA_FKwidget= QTableWidgetItem(str(idVENTA_FK))
                            idPROD_FK_widget= QTableWidgetItem(str(idPROD_FK))
                            precioPROD_widget= QTableWidgetItem(str(precioPROD))
                            cantidadPROD_widget= QTableWidgetItem(str(cantidadPROD))

                            #self.ui.tabla_venta_cons.setItem(row,4,idVENTA_FKwidget)
                            self.ui.tabla_venta_cons.setItem(row,4,idPROD_FK_widget)
                            self.ui.tabla_venta_cons.setItem(row,5,precioPROD_widget)
                            self.ui.tabla_venta_cons.setItem(row,6,cantidadPROD_widget)
                            row+=1
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atencion",
                    f'La venta"{id_venta_cons}"no fue encontrada'
                )
                
            """except:
                QMessageBox.warning(
                        self,
                        "Atencion",
                        f'La venta no fue encontrada,no ingreso un id a buscar.'
                    )
            """
               
    @Slot()
    def consultar_pedido(self):
        
        id_pedido_cons=self.ui.id_compras_cons_lineEdit.text()
        resultados= self.articulo1.consulta_pedidos()

        self.ui.tabla_compras_cons.clear()
        self.ui.tabla_compras_cons.setRowCount(1)
        self.ui.tabla_compras_cons.setColumnCount(3)
        headers=["idPEDIDOS","fechaPEDIDOS","id_PROV_fk"]
        self.ui.tabla_compras_cons.setHorizontalHeaderLabels(headers)
        try:
            print(resultados)
            encontrado=False
            for idPEDIDOS,fechaPEDIDOS,id_PROV_fk in resultados :
                if int(id_pedido_cons) == idPEDIDOS:
                    print(idPEDIDOS,fechaPEDIDOS,id_PROV_fk)
                    
                    idPEDIDOS_widget= QTableWidgetItem(str(idPEDIDOS))
                    fechaPEDIDOS_widget= QTableWidgetItem(str(fechaPEDIDOS))
                    id_PROV_fk_widget= QTableWidgetItem(str(id_PROV_fk))

                    self.ui.tabla_compras_cons.setItem(0,0,idPEDIDOS_widget)
                    self.ui.tabla_compras_cons.setItem(0,1,fechaPEDIDOS_widget)
                    self.ui.tabla_compras_cons.setItem(0,2,id_PROV_fk_widget)
                    
                    encontrado=True
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atencion",
                    f'La compra"{id_pedido_cons}"no fue encontrada'
                )
        except:
            QMessageBox.warning(
                    self,
                    "Atencion",
                    f'El pedido no fue encontrada,no ingreso un id a buscar.'
                )

    @Slot()
    def consultar_devolucion(self):
        
        id_devolucion_cons=self.ui.id_devolucion_cons_lineEdit.text()
        resultados= self.articulo1.consulta_devolucion()

        self.ui.tabla_devolucion_cons.clear()
        self.ui.tabla_devolucion_cons.setRowCount(1)
        self.ui.tabla_devolucion_cons.setColumnCount(4)
        headers=["idDEV","fechaDEV","idEMP_fk","idVENTA_fk"]
        self.ui.tabla_devolucion_cons.setHorizontalHeaderLabels(headers)
        try:
            print(resultados)
            encontrado=False
            for idDEV,fechaDEV,idEMP_fk,idVENTA_fk in resultados :
                if int(id_devolucion_cons) == idDEV:
                    print(idDEV,fechaDEV,idEMP_fk,idVENTA_fk)
                    
                    idDEV_widget= QTableWidgetItem(str(idDEV))
                    fechaDEV_widget= QTableWidgetItem(str(fechaDEV))
                    idEMP_fk_widget= QTableWidgetItem(str(idEMP_fk))
                    idVENTA_fk_widget= QTableWidgetItem(str(idVENTA_fk))
                    

                    self.ui.tabla_devolucion_cons.setItem(0,0,idDEV_widget)
                    self.ui.tabla_devolucion_cons.setItem(0,1,fechaDEV_widget)
                    self.ui.tabla_devolucion_cons.setItem(0,2,idEMP_fk_widget)
                    self.ui.tabla_devolucion_cons.setItem(0,3,idVENTA_fk_widget)
                    
                    encontrado=True
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atencion",
                    f'La devolucion"{id_devolucion_cons}"no fue encontrada'
                )
        except:
            QMessageBox.warning(
                    self,
                    "Atencion",
                    f'La devolución no fue encontrada,no ingreso un id a buscar.'
                )