productos=[]
class registro:
    def __init__(self,name,codigo,cant_p,valorU,valor_t):
        self.name=name
        self.codigo=codigo
        self.cant_p=cant_p
        self.valorU=valorU
        self.valor_t=valor_t

    def listar(self):
        print("------------Registro------------")
        print("nombre del producto: ", self.name)
        print("codigo de producto: ", self.codigo)
        print("cantidad de productos: ", self.cant_p)
        print("valor por unidad: ", self.valorU)
        print("valor total: ", self.valor_t)
        
    def editar(self,cant_p,valorU,valor_t):
        self.cant_p=cant_p
        self.valorU=valorU
        self.valor_t=valor_t
    
        
def registrar():
    print("-------------REGISTRO-----------")
    name=str(input("nombre del producto: "))
    codigo=int(input("codigo del producto: "))
    cant_p=int(input("cantidad de productos: "))
    valorU=int(input("valor unidad: "))
    valor_t=cant_p*valorU
    print("valor total: ",valor_t)
    objeto=registro(name,codigo,cant_p,valorU,valor_t)
    productos.append(objeto)
        
def mostrar():
    if productos:
        print("---------lista de productos--------")
        for i in productos:
            i.listar()
    else:
        print("lista vacia")

def buscar():
    buscar=int(input("codigo del producto a buscar: "))
    for i in productos:
        buscar==i.codigo
        i.listar()
        
def modificar():
    buscar=int(input("codigo del producto a buscar: "))
    for i in productos:
        if i.codigo==buscar:
            cant_p=int(input("cantidad de productos: "))
            valorU=int(input("valor unidad: "))
            valor_t=cant_p*valorU
            print("valores modificados")
            print("valor total: ",valor_t)
            i.editar(cant_p,valorU,valor_t)
            
def eliminar():
    buscar=int(input("codigo del producto a buscar: "))
    for i in productos:
        if buscar == i.codigo:
            productos.remove(i)
            print("producto eliminado correctamente")
             
def menu():
    seguir="si"
    while seguir=="si":
        print("----------------menu--------------")
        print("------1 registro de productos----")
        print("------2 mostrar productos-------")
        print("------3 buscar productos--------")
        print("------4 modificar productos-----")
        print("------5 eliminar productos-------")
        print("--------------6 salir -------------")
        opcion=int(input("digite un numero del menu: "))
        while opcion>7 or opcion < 1:
            print("error numero no valido")
            opcion=int(input("digite un numero del menu: "))
                    
        if opcion == 1:
            registrar()
        elif opcion ==2:
            mostrar()
        elif opcion==3:
            buscar()
        elif opcion ==4:
            modificar()
        elif opcion==5:
            eliminar()
        else:
            exit()
        
menu()