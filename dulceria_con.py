import mysql.connector

class Articulos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="Elisea90", 
                                              database="dulceria")
        return conexion
    def restar_cantidad_prod(self,cantidad,idpro):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE producto SET cantidad=cantidad-%s WHERE idPROD=%s"
        cursor.execute(sql,(cantidad,idpro))
        cone.commit()
        cone.close()

    def sumar_cantidad_prod(self,cantidad,idpro):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE producto SET cantidad=cantidad+%s WHERE idPROD=%s"
        cursor.execute(sql,(cantidad,idpro))
        cone.commit()
        cone.close()

    def alta_pedido(self, id_prove_detalles_pedido_reg):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into pedidos(idPROV_fk) values (%s)"
        cursor.execute(sql,(id_prove_detalles_pedido_reg,))
        cone.commit()
        cone.close()

    def alta_pedido_detalles(self, id_pedido_detalles_pedido_reg,id_producto_detalles_pedido_reg,id_cantidad_detalles_pedido_reg):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into detalle_pedidos(idPEDIDO_fk,idPROD_fk,cantidadPROD) values (%s,%s,%s)"
        cursor.execute(sql,(id_pedido_detalles_pedido_reg,id_producto_detalles_pedido_reg,id_cantidad_detalles_pedido_reg))
        cone.commit()
        cone.close()

    def alta_empleado(self, nombre,telefono,status):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into empleado(nombreEMP,telEMP,status) values (%s,%s,%s)"
        cursor.execute(sql,(nombre,telefono,status))
        cone.commit()
        cone.close()

    def consultar_tel_empleado_reg(self,telf):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select telEMP from empleado where telEMP=%s"
        cursor.execute(sql,(telf,))
        return cursor.fetchall()
        cone.close()

    def consultar_tel_proveedor_reg(self,telf):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select telPROV from proveedores where telPROV=%s"
        cursor.execute(sql,(telf,))
        return cursor.fetchall()
        cone.close() 

    def consultar_nombre_proveedor_reg(self,nombre):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nombrePROV from proveedores where nombrePROV=%s"
        cursor.execute(sql,(nombre,))
        return cursor.fetchall()
        cone.close()

    def consultar_cel_proveedor_reg(self,cel):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select celPROV from proveedores where celPROV=%s"
        cursor.execute(sql,(cel,))
        return cursor.fetchall()
        cone.close()

    def consultar_nombre_producto_reg(self,nombre):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nombrePROD from producto where nombrePROD=%s"
        cursor.execute(sql,(nombre,))
        return cursor.fetchall()
        cone.close()

    def alta_cliente(self, nombre,direccion,puntos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into clientes(nombreCLIENT,direccionCLIENT,puntos) values (%s,%s,%s)"
        cursor.execute(sql,(nombre,direccion,puntos))
        cone.commit()
        cone.close()

    def alta_proveedor(self, nombre,telefono,celular):
        datos=(nombre,telefono,celular)
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into proveedores(nombrePROV,telPROV,celPROV) values (%s,%s,%s)"
        cursor.execute(sql,(nombre,telefono,celular))
        cone.commit()
        cone.close()
    
    def alta_producto(self, nombre,preciocompra,precioventa,cantidad,idproveedor):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into producto(nombrePROD,precioCompra,precioVenta,cantidad,idPROD_fk) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql,(nombre,preciocompra,precioventa,cantidad,idproveedor))
        cone.commit()
        cone.close()

    def alta_venta(self,idempleado,idcliente):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into venta(idEMP_fk,idCLIENT_FK) values (%s,%s)"
        cursor.execute(sql,(idempleado,idcliente))
        cone.commit()
        cone.close()

    def alta_venta_detalle(self,idventa_venta_reg,idproducto_venta_reg,precio_prod,cantidadproducto_venta_reg):
        
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into detalle_venta(idVENTA_FK,idPROD_FK,precioPROD,cantidadPROD) values (%s,%s,%s,%s)"
        cursor.execute(sql,(idventa_venta_reg,idproducto_venta_reg,precio_prod,cantidadproducto_venta_reg))
        cone.commit()
        cone.close()
       

    def alta_devolucion(self,idempleado_devolucion_reg,idventa_devolucion_reg):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into devolucion(idEMP_fk,idVENTA_fk) values (%s,%s)"
        cursor.execute(sql,(idempleado_devolucion_reg,idventa_devolucion_reg))
        cone.commit()
        cone.close()

    def alta_detalles_devolucion(self,id_devolcuion_detalle_reg,id_producto_detalle_devolucion,cantidad_detalle_devolucion):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into detalle_devolucion(idDEV_fk,idPROD_fk,cantidadPROD) values (%s,%s,%s)"
        cursor.execute(sql,(id_devolcuion_detalle_reg,id_producto_detalle_devolucion,cantidad_detalle_devolucion))
        cone.commit()
        cone.close()

    def modificar_empleado_nombre(self,nombre,idempleado):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE empleado SET nombreEMP=%s WHERE idEMP =%s"
        cursor.execute(sql,(nombre,idempleado))
        cone.commit()
        cone.close()
    
    def modificar_empleado_telefono(self,telefono,idempleado):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE empleado SET telEMP=%s WHERE idEMP =%s"
        cursor.execute(sql,(telefono,idempleado))
        cone.commit()
        cone.close()

    def modificar_empleado_status(self,status,idempleado):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE empleado SET status=%s WHERE idEMP =%s"
        cursor.execute(sql,(status,idempleado))
        cone.commit()
        cone.close()


    def modificar_cliente_nombre(self,nombre,idcliente):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE clientes SET nombreCLIENT=%s WHERE idCLIENT =%s"
        cursor.execute(sql,(nombre,idcliente))
        cone.commit()
        cone.close()
    
    def modificar_cliente_direccion(self,direccio,idcliente):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE clientes SET direccionCLIENT=%s WHERE idCLIENT =%s"
        cursor.execute(sql,(direccio,idcliente))
        cone.commit()
        cone.close()

    def modificar_cliente_puntos(self,puntos,idcliente):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE clientes SET puntos=%s WHERE idCLIENT =%s"
        cursor.execute(sql,(puntos,idcliente))
        cone.commit()
        cone.close()

    def modificar_proveedor_nombre(self,nombre,idproveedor):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE proveedores SET nombrePROV=%s WHERE idPROV =%s"
        cursor.execute(sql,(nombre,idproveedor))
        cone.commit()
        cone.close()
    
    def modificar_proveedor_telefono(self,telefono,idproveedor):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE proveedores SET telPROV=%s WHERE idPROV =%s"
        cursor.execute(sql,(telefono,idproveedor))
        cone.commit()
        cone.close()

    def modificar_proveedor_celular(self,celular,idproveedor):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE proveedores SET celPROV=%s WHERE idPROV =%s"
        cursor.execute(sql,(celular,idproveedor))
        cone.commit()
        cone.close()

    def modificar_producto_nombre(self,nombre,idproducto):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE producto SET nombrePROD=%s WHERE idPROD =%s"
        cursor.execute(sql,(nombre,idproducto))
        cone.commit()
        cone.close()
    #ql="UPDATE customers SET address = %s WHERE address = %s"
    def modificar_producto_preciocompra(self,preciocompra,idproducto):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE producto SET precioCompra=%s WHERE idPROD =%s"
        cursor.execute(sql,(preciocompra,idproducto))
        cone.commit()
        cone.close()
    
    def modificar_producto_precioventa(self,precioventa,idproducto):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE producto SET precioVenta=%s WHERE idPROD =%s"
        cursor.execute(sql,(precioventa,idproducto))
        cone.commit()
        cone.close()
    
    def modificar_producto_cantidad(self,cantidad,idproducto):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE producto SET cantidad=%s WHERE idPROD =%s"
        cursor.execute(sql,(cantidad,idproducto))
        cone.commit()
        cone.close()

    def modificar_producto_idproveedor(self,idproveedor,idproducto):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="UPDATE producto SET idPROD_fk=%s WHERE idPROD =%s"
        cursor.execute(sql,(idproveedor,idproducto))
        cone.commit()
        cone.close()
    
    def consulta_empleado(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT idEMP,nombreEMP,telEMP,status FROM empleado "
        cursor.execute(sql)
        
        return cursor.fetchall()
        cone.close()
    
    def consulta_cliente(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT idCLIENT,nombreCLIENT,direccionCLIENT,puntos FROM clientes "
        cursor.execute(sql)
        
        return cursor.fetchall()
        cone.close()
    
    def consulta_proveedor(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT idPROV,nombrePROV,telPROV,celPROV FROM proveedores "
        cursor.execute(sql)
        
        return cursor.fetchall()
        cone.close()
    
    def consulta_producto(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROD_fk FROM producto "
        cursor.execute(sql)
        
        return cursor.fetchall()
        cone.close()  
    
    def consulta_pedidos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT idPEDIDOS,fechaPEDIDOS,idPROV_fk FROM pedidos "
        cursor.execute(sql)
        return cursor.fetchall()
        cone.close()  
    
    def consulta_venta(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT idVENTA,fechaVENTA,idEMP_fk,idCLIENT_FK FROM venta "
        cursor.execute(sql)
        return cursor.fetchall()
        cone.close()  

    def consulta_venta_detalle(self,idventa):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT idVENTA_FK,idPROD_FK,precioPROD,cantidadPROD FROM detalle_venta where idVENTA_FK= %s"
        cursor.execute(sql,(idventa,))
        return cursor.fetchall()
        cone.close()  

    def consulta_producto_proveedor_pedido(self,idproveedor):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT idPROD,nombrePROD,precioCompra,precioVenta,cantidad,idPROD_fk FROM producto where idPROD_fk= %s"
        cursor.execute(sql,(idproveedor,))
        return cursor.fetchall()
        cone.close() 

    def consulta_devolucion(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT idDEV,fechaDEV,idEMP_fk,idVENTA_fk FROM devolucion "
        cursor.execute(sql)
            
        return cursor.fetchall()
        cone.close() 

    def consulta_producto_nombre(self, idproducto):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nombrePROD,precioCompra,precioVenta, cantidad from producto where idPROD=%s"
        cursor.execute(sql, (idproducto))
        cone.close()
        return cursor.fetchall()
    
    def consulta_producto_preciocompra(self, idproducto):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select precioCompra from producto where idEMP=%s"
        cursor.execute(sql, (idproducto))
        cone.close()
        return cursor.fetchall()
    
    def consulta_producto_precioventa(self, idproducto):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select precioVenta from producto where idEMP=%s"
        cursor.execute(sql, (idproducto))
        cone.close()
        return cursor.fetchall()
        
    def consulta_producto_cantidad(self, idproducto):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select cantidad from producto where idEMP=%s"
        cursor.execute(sql, (idproducto))
        cone.close()
        return cursor.fetchall()
    
    def consulta_producto_proveedor(self, idproducto):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select idPROD_fk from producto where idEMP=%s"
        cursor.execute(sql, (idproducto))
        cone.close()
        return cursor.fetchall()

    
        #return cursor.fetchall()
    def consulta_ult_id_empleado(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select MAX(idEMP) AS idEMP FROM empleado"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        return cursor.fetchall()
        cone.close()
    
    def consulta_ult_id_pedido(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select MAX(idPEDIDOS) AS idPEDIDOS FROM pedidos"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        return cursor.fetchall()
        cone.close()
    
    def consulta_ult_id_venta(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select MAX(idVENTA) AS idVENTA FROM venta"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        return cursor.fetchall()
        cone.close()

    def consulta_ult_id_cliente(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select MAX(idCLIENT) AS idCLIENT FROM clientes"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        return cursor.fetchall()
        cone.close()
    
    def consulta_ult_id_proveedor(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select MAX(idPROV) AS idPROV FROM proveedores"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        return cursor.fetchall()
        cone.close()
        
    def consulta_ult_id_producto(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select MAX(idPROD) AS idPROD FROM producto"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        return cursor.fetchall()
        cone.close()

    def consulta_ult_id_devolucion(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select MAX(idDEV) AS idDEV FROM devolucion"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        return cursor.fetchall()
        cone.close()
        
    def reiniciar_id_venta(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="ALTER TABLE venta AUTO_INCREMENT = 1"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        cone.close()

    def reiniciar_id_empleado(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="ALTER TABLE empleado AUTO_INCREMENT = 1"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        cone.close()

    def reiniciar_id_clientes(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="ALTER TABLE clientes AUTO_INCREMENT = 1"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        cone.close()
    
    def reiniciar_id_proveedores(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="ALTER TABLE proveedores AUTO_INCREMENT = 1"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        cone.close()

    def reiniciar_id_producto(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="ALTER TABLE producto AUTO_INCREMENT = 1"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        cone.close()
    
    def reiniciar_id_devolucion(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="ALTER TABLE devolucion AUTO_INCREMENT = 1"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        cone.close()

    def reiniciar_id_pedidos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="ALTER TABLE pedidos AUTO_INCREMENT = 1"
        cursor.execute(sql)
        #print(cursor.execute(sql,))
        cone.close()

    
        

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()