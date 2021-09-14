productos = {"Jeans": {"Precio":20000, "Costo":120000}, 
"Camisa polo": {"Precio":99000, "Costo":50000}, 
"Vaqueros": {"Precio":220000, "Costo":125000}}

class CarritoCompras:
  #Atributos -> Caracteriza el carrito de compras
  usuario = ""            #<-
  listaCompras = {}
  total = 0
  costoProductos = {}     #<-
  cantidadArticulos = 0


  #Métodos -> ¿Qué puede hacer el carrito?
  def __init__(self, usuario, costoProductos):
    #Inicializar el objeto del carrito por cliente -> usuario, costoProductos
    self.usuario = usuario
    self.costoProductos = costoProductos  

    self.limpiar()

  def addArticulo(self, nombreArticulo, cantidad):
      
    compra = {
        "Cantidad": cantidad,
        "Precio Unitario": self.costoProductos[nombreArticulo]["Precio"]
    }

    compra["Subtotal"] = compra["Cantidad"]*compra["Precio Unitario"]

    if nombreArticulo in self.listaCompras:
      nuevaCantidad = compra["Cantidad"]+self.listaCompras[nombreArticulo]["Cantidad"]
      self.listaCompras[nombreArticulo] = {
          "Cantidad": nuevaCantidad,
          "Subtotal": nuevaCantidad*self.listaCompras[nombreArticulo]["Precio Unitario"],
          "Precio Unitario": self.costoProductos[nombreArticulo]["Precio"]
      }
    else:
      self.listaCompras[nombreArticulo] = compra  #Funciona si el artículo no existe en la lista
    
    #CALCULAR TOTAL DE COMPRAS 
    self.TOTAL()
  
  def removeArticulo(self, articulo):
    del self.listaCompras[articulo]
  
  def limpiar(self):
    #Reinicializar atributos
    self.listaCompras = {}
    self.total = 0
    self.cantidadArticulos = 0
  
  def TOTAL(self):
    total = 0
    for articulo in self.listaCompras:
      total += self.listaCompras[articulo]["Subtotal"]
    self.total = total
  
  def utilidades(self):
    pass


#DESARROLLO INTERACTIVO
carritoUsuario1 = CarritoCompras("lopez1", productos) #Se creó el carrito de 'lopez1'
while True:
  art = input("¿Qué artículo deseas comprar? ")
  cant = int(input("¿Qué cantidad deseas? "))

  carritoUsuario1.addArticulo(art, cant)

  print("El total acumulado es $" + str(carritoUsuario1.total))

  if input("¿Deseas eliminar un artículo? (s/n) ") == "s":
    carritoUsuario1.removeArticulo(input("¿Qué artículo quieres eliminar?"))

  if input("¿Deseas seguir comprando? (s/n) ") == "n":
    break

#Mostrar el total del carrito

