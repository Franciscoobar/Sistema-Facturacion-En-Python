class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio




class Factura: 
    def __init__(self):
        self.items = []

    def añadir(self, producto):
        self.items.append(producto)

    def total_con_iva(self):
        return sum(p.precio for p in self.items) * 1.21


factura = Factura()
factura.añadir(Producto("Teclado", 20))
factura.añadir(Producto("Mouse", 10))       


for item in factura.items:
    print(f"{item.nombre}: {item.precio}$")


print(f"Total con IVA: {factura.total_con_iva():.2f}$")    





