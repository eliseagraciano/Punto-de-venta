class Producto_venta:
    def __init__(self,id=0,precio_venta=0):
        self.__id=id
        
        self.__precio_venta=precio_venta
        
    def reg_cantidad(self,cantidad):
        self.__cantidad=cantidad

    def __str__(self):
        return(
            'Id: '+ str(self.__id) + '\n' +
            'Cantidad producto: '+ str(self.__cantidad) + '\n' +
            'Precio venta: '+ str(self.__precio_venta) + '\n' 
        )
    @property
    def id(self):
        return self.__id
    @property
    def cantidad(self):
        return self.__cantidad
    @property
    def precio_venta(self):
        return self.__precio_venta
   

    def to_dic(self):
        return{
            'id':self.__id,
            'cantidad':self.__cantidad,
            'precio venta':self.__precio_venta
        }
            
        
    
