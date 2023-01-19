from produto import Producto_venta

class Gestor_Producto:
    def __init__(self):
        self.__productos = []

    @property
    def productos(self):
        return self.__productos

    def agregar_inicio(self,producto:Producto_venta):
        self.__productos.insert(0,producto)

    def agregar_final(self,producto:Producto_venta):
        self.__productos.append(producto)

    def mostrar(self):
        for producto in self.__productos:
            print(producto)
            
    def editar_cantidad_producto(self,idprod):
        for productoid in self.__productos:
            if productoid==idprod:
                print("simon")
            else:
                print("nel")

    def __str__(self):
        return "".join(
            str(producto) + '\n' for producto in self.__productos
        )
    def __len__(self):
        return len(self.__productos)
    
    def __iter__(self):
        self.cont=0
        return self

    def __next__(self):
        if self.cont < len(self.__productos):
            producto =self.__productos[self.cont]
            self.cont+=1
            return producto
        else:
            raise StopIteration

    
         
            #archivo.write(str(self))
#p= Particula(1,2,1,3,4,5,6,7,8,9)
#p1= Particula(20,69,59,41,55,66,99,80,52,63)
#p2= Particula(2,69,50,200,55,66,100,80,52,63)
#particulas=Particulas()
#particulas.agregar_inicio(p2)
#particulas.mostrar()
#particulas.agregar_final(p)
#particulas.mostrar()
##particulas.agregar_inicio(p1)
#particulas.mostrar()