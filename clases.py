import datetime

# ENTIDADES

class Tienda:
    def __init__(self, nombre, direccion, ciudad):
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad

class Ciudad:
    def __init__(self, nombre, codigo_postal):
        self.nombre = nombre
        self.codigo_postal = codigo_postal

class Cliente:
    def __init__(self, id_cliente, nombre, direccion, telefono, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

class Pedido:
    def __init__(self, id_pedido, fecha, cliente, lista_productos):
        self.id_pedido = id_pedido
        self.fecha = fecha
        self.cliente = cliente
        self.lista_productos = lista_productos

class OrdenCompra:
    def __init__(self, id_orden, fecha, proveedor, productos, estado):
        self.id_orden = id_orden
        self.fecha = fecha
        self.proveedor = proveedor
        self.productos = productos
        self.estado = estado

class Proveedor:
    def __init__(self, id_proveedor, nombre, direccion, telefono, email):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

class Factura:
    def __init__(self, id_factura, fecha, orden_compra, total):
        self.id_factura = id_factura
        self.fecha = fecha
        self.orden_compra = orden_compra
        self.total = total

class Pago:
    def __init__(self, id_pago, fecha, monto, metodo_pago):
        self.id_pago = id_pago
        self.fecha = fecha
        self.monto = monto
        self.metodo_pago = metodo_pago

class Venta:
    def __init__(self, id_venta, fecha, cliente, productos, total):
        self.id_venta = id_venta
        self.fecha = fecha
        self.cliente = cliente
        self.productos = productos
        self.total = total


# CRUD 


clientes = []
proveedores = []
pedidos = []
ordenes = []
facturas = []
pagos = []
ventas = []
ciudades = []


# MENÚ PRINCIPAL


def menu():
    while True:
        print("\n--- TIENDA ---")
        print("1. Gestionar Clientes")
        print("2. Gestionar Proveedores")
        print("3. Gestionar Pedidos")
        print("4. Gestionar Órdenes de Compra")
        print("5. Gestionar Facturas")
        print("6. Gestionar Pagos")
        print("7. Gestionar Ventas")
        print("8. Gestionar Ciudades")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crud_clientes()
        elif opcion == "2":
            crud_proveedores()
        elif opcion == "3":
            crud_pedidos()
        elif opcion == "4":
            crud_ordenes()
        elif opcion == "5":
            crud_facturas()
        elif opcion == "6":
            crud_pagos()
        elif opcion == "7":
            crud_ventas()
        elif opcion == "8":
            crud_ciudades()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


# CRUD CLIENTES 


def crud_clientes():
    while True:
        print("\n--- CRUD Clientes ---")
        print("1. Crear Cliente")
        print("2. Ver Clientes")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("0. Volver al menú principal")

        op = input("Seleccione una opción: ")

        if op == "1":
            id_cliente = len(clientes) + 1
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            cliente = Cliente(id_cliente, nombre, direccion, telefono, email)
            clientes.append(cliente)
            print("Cliente agregado con éxito.")

        elif op == "2":
            print("\nLista de Clientes:")
            for c in clientes:
                print(f"{c.id_cliente} - {c.nombre} ({c.email})")

        elif op == "3":
            id_cliente = int(input("ID del cliente a actualizar: "))
            for c in clientes:
                if c.id_cliente == id_cliente:
                    c.nombre = input("Nuevo nombre: ")
                    c.direccion = input("Nueva dirección: ")
                    c.telefono = input("Nuevo teléfono: ")
                    c.email = input("Nuevo email: ")
                    print("Cliente actualizado.")
                    break
            else:
                print("Cliente no encontrado.")

        elif op == "4":
            id_cliente = int(input("ID del cliente a eliminar: "))
            for c in clientes:
                if c.id_cliente == id_cliente:
                    clientes.remove(c)
                    print("Cliente eliminado.")
                    break
            else:
                print("Cliente no encontrado.")

        elif op == "0":
            break
        else:
            print("Opción inválida.")
            

# CRUD PROVEEDORES


def crud_proveedores():
    while True:
        print("\n--- CRUD Proveedores ---")
        print("1. Crear Proveedor")
        print("2. Ver Proveedores")
        print("3. Actualizar Proveedor")
        print("4. Eliminar Proveedor")
        print("0. Volver al menú principal")

        op = input("Seleccione una opción: ")

        if op == "1":
            id_proveedor = len(proveedores) + 1
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            proveedor = Proveedor(id_proveedor, nombre, direccion, telefono, email)
            proveedores.append(proveedor)
            print("Proveedor agregado con éxito.")

        elif op == "2":
            print("\nLista de Proveedores:")
            for p in proveedores:
                print(f"{p.id_proveedor} - {p.nombre} ({p.email})")

        elif op == "3":
            id_proveedor = int(input("ID del proveedor a actualizar: "))
            for p in proveedores:
                if p.id_proveedor == id_proveedor:
                    p.nombre = input("Nuevo nombre: ")
                    p.direccion = input("Nueva dirección: ")
                    p.telefono = input("Nuevo teléfono: ")
                    p.email = input("Nuevo email: ")
                    print("Proveedor actualizado.")
                    break
            else:
                print("Proveedor no encontrado.")

        elif op == "4":
            id_proveedor = int(input("ID del proveedor a eliminar: "))
            for p in proveedores:
                if p.id_proveedor == id_proveedor:
                    proveedores.remove(p)
                    print("Proveedor eliminado.")
                    break
            else:
                print("Proveedor no encontrado.")

        elif op == "0":
            break
        else:
            print("Opción inválida.")


# CRUD PEDIDOS


def crud_pedidos():
    while True:
        print("\n--- CRUD Pedidos ---")
        print("1. Crear Pedido")
        print("2. Ver Pedidos")
        print("3. Actualizar Pedido")
        print("4. Eliminar Pedido")
        print("0. Volver al menú principal")

        op = input("Seleccione una opción: ")

        if op == "1":
            id_pedido = len(pedidos) + 1
            fecha = datetime.datetime.now()
            if not clientes:
                print("Debe crear un cliente primero.")
                continue
            print("Seleccione Cliente:")
            for c in clientes:
                print(f"{c.id_cliente} - {c.nombre}")
            id_cliente = int(input("ID cliente: "))
            cliente = next((c for c in clientes if c.id_cliente == id_cliente), None)
            if not cliente:
                print("Cliente no encontrado.")
                continue
            productos = input("Lista de productos (separados por coma): ").split(",")
            pedido = Pedido(id_pedido, fecha, cliente, productos)
            pedidos.append(pedido)
            print("Pedido creado con éxito.")

        elif op == "2":
            print("\nLista de Pedidos:")
            for p in pedidos:
                print(f"{p.id_pedido} - {p.cliente.nombre} - {p.fecha} - {p.lista_productos}")

        elif op == "3":
            id_pedido = int(input("ID del pedido a actualizar: "))
            for p in pedidos:
                if p.id_pedido == id_pedido:
                    productos = input("Nuevos productos (separados por coma): ").split(",")
                    p.lista_productos = productos
                    print("Pedido actualizado.")
                    break
            else:
                print("Pedido no encontrado.")

        elif op == "4":
            id_pedido = int(input("ID del pedido a eliminar: "))
            for p in pedidos:
                if p.id_pedido == id_pedido:
                    pedidos.remove(p)
                    print("Pedido eliminado.")
                    break
            else:
                print("Pedido no encontrado.")

        elif op == "0":
            break
        else:
            print("Opción inválida.")



# CRUD ORDENES DE COMPRA


def crud_ordenes():
    while True:
        print("\n--- CRUD Órdenes de Compra ---")
        print("1. Crear Orden")
        print("2. Ver Órdenes")
        print("3. Actualizar Orden")
        print("4. Eliminar Orden")
        print("0. Volver al menú principal")

        op = input("Seleccione una opción: ")

        if op == "1":
            id_orden = len(ordenes) + 1
            fecha = datetime.datetime.now()
            if not proveedores:
                print("Debe crear un proveedor primero.")
                continue
            print("Seleccione Proveedor:")
            for pr in proveedores:
                print(f"{pr.id_proveedor} - {pr.nombre}")
            id_proveedor = int(input("ID proveedor: "))
            proveedor = next((pr for pr in proveedores if pr.id_proveedor == id_proveedor), None)
            if not proveedor:
                print("Proveedor no encontrado.")
                continue
            productos = input("Productos (separados por coma): ").split(",")
            estado = input("Estado: ")
            orden = OrdenCompra(id_orden, fecha, proveedor, productos, estado)
            ordenes.append(orden)
            print("Orden creada con éxito.")

        elif op == "2":
            print("\nLista de Órdenes de Compra:")
            for o in ordenes:
                print(f"{o.id_orden} - {o.proveedor.nombre} - {o.estado} - {o.productos}")

        elif op == "3":
            id_orden = int(input("ID de la orden a actualizar: "))
            for o in ordenes:
                if o.id_orden == id_orden:
                    o.productos = input("Nuevos productos (separados por coma): ").split(",")
                    o.estado = input("Nuevo estado: ")
                    print("Orden actualizada.")
                    break
            else:
                print("Orden no encontrada.")

        elif op == "4":
            id_orden = int(input("ID de la orden a eliminar: "))
            for o in ordenes:
                if o.id_orden == id_orden:
                    ordenes.remove(o)
                    print("Orden eliminada.")
                    break
            else:
                print("Orden no encontrada.")

        elif op == "0":
            break
        else:
            print("Opción inválida.")



# CRUD FACTURAS


def crud_facturas():
    while True:
        print("\n--- CRUD Facturas ---")
        print("1. Crear Factura")
        print("2. Ver Facturas")
        print("3. Actualizar Factura")
        print("4. Eliminar Factura")
        print("0. Volver al menú principal")

        op = input("Seleccione una opción: ")

        if op == "1":
            id_factura = len(facturas) + 1
            fecha = datetime.datetime.now()
            if not ordenes:
                print("Debe crear una orden primero.")
                continue
            print("Seleccione Orden:")
            for o in ordenes:
                print(f"{o.id_orden} - {o.proveedor.nombre}")
            id_orden = int(input("ID orden: "))
            orden = next((o for o in ordenes if o.id_orden == id_orden), None)
            if not orden:
                print("Orden no encontrada.")
                continue
            total = float(input("Total: "))
            factura = Factura(id_factura, fecha, orden, total)
            facturas.append(factura)
            print("Factura creada con éxito.")

        elif op == "2":
            print("\nLista de Facturas:")
            for f in facturas:
                print(f"{f.id_factura} - Orden {f.orden_compra.id_orden} - Total: {f.total}")

        elif op == "3":
            id_factura = int(input("ID de la factura a actualizar: "))
            for f in facturas:
                if f.id_factura == id_factura:
                    f.total = float(input("Nuevo total: "))
                    print("Factura actualizada.")
                    break
            else:
                print("Factura no encontrada.")

        elif op == "4":
            id_factura = int(input("ID de la factura a eliminar: "))
            for f in facturas:
                if f.id_factura == id_factura:
                    facturas.remove(f)
                    print("Factura eliminada.")
                    break
            else:
                print("Factura no encontrada.")

        elif op == "0":
            break
        else:
            print("Opción inválida.")



# CRUD PAGOS


def crud_pagos():
    while True:
        print("\n--- CRUD Pagos ---")
        print("1. Crear Pago")
        print("2. Ver Pagos")
        print("3. Actualizar Pago")
        print("4. Eliminar Pago")
        print("0. Volver al menú principal")

        op = input("Seleccione una opción: ")

        if op == "1":
            id_pago = len(pagos) + 1
            fecha = datetime.datetime.now()
            monto = float(input("Monto: "))
            metodo = input("Método de pago: ")
            pago = Pago(id_pago, fecha, monto, metodo)
            pagos.append(pago)
            print("Pago creado con éxito.")

        elif op == "2":
            print("\nLista de Pagos:")
            for p in pagos:
                print(f"{p.id_pago} - {p.monto} - {p.metodo_pago} - {p.fecha}")

        elif op == "3":
            id_pago = int(input("ID del pago a actualizar: "))
            for p in pagos:
                if p.id_pago == id_pago:
                    p.monto = float(input("Nuevo monto: "))
                    p.metodo_pago = input("Nuevo método de pago: ")
                    print("Pago actualizado.")
                    break
            else:
                print("Pago no encontrado.")

        elif op == "4":
            id_pago = int(input("ID del pago a eliminar: "))
            for p in pagos:
                if p.id_pago == id_pago:
                    pagos.remove(p)
                    print("Pago eliminado.")
                    break
            else:
                print("Pago no encontrado.")

        elif op == "0":
            break
        else:
            print("Opción inválida.")


# CRUD VENTAS


def crud_ventas():
    while True:
        print("\n--- CRUD Ventas ---")
        print("1. Crear Venta")
        print("2. Ver Ventas")
        print("3. Actualizar Venta")
        print("4. Eliminar Venta")
        print("0. Volver al menú principal")

        op = input("Seleccione una opción: ")

        if op == "1":
            id_venta = len(ventas) + 1
            fecha = datetime.datetime.now()
            if not clientes:
                print("Debe crear un cliente primero.")
                continue
            print("Seleccione Cliente:")
            for c in clientes:
                print(f"{c.id_cliente} - {c.nombre}")
            id_cliente = int(input("ID cliente: "))
            cliente = next((c for c in clientes if c.id_cliente == id_cliente), None)
            if not cliente:
                print("Cliente no encontrado.")
                continue
            productos = input("Productos (separados por coma): ").split(",")
            total = float(input("Total: "))
            venta = Venta(id_venta, fecha, cliente, productos, total)
            ventas.append(venta)
            print("Venta creada con éxito.")

        elif op == "2":
            print("\nLista de Ventas:")
            for v in ventas:
                print(f"{v.id_venta} - {v.cliente.nombre} - {v.total} - {v.fecha}")

        elif op == "3":
            id_venta = int(input("ID de la venta a actualizar: "))
            for v in ventas:
                if v.id_venta == id_venta:
                    v.productos = input("Nuevos productos (separados por coma): ").split(",")
                    v.total = float(input("Nuevo total: "))
                    print("Venta actualizada.")
                    break
            else:
                print("Venta no encontrada.")

        elif op == "4":
            id_venta = int(input("ID de la venta a eliminar: "))
            for v in ventas:
                if v.id_venta == id_venta:
                    ventas.remove(v)
                    print("Venta eliminada.")
                    break
            else:
                print("Venta no encontrada.")

        elif op == "0":
            break
        else:
            print("Opción inválida.")


# CRUD CIUDADES


def crud_ciudades():
    while True:
        print("\n--- CRUD Ciudades ---")
        print("1. Crear Ciudad")
        print("2. Ver Ciudades")
        print("3. Actualizar Ciudad")
        print("4. Eliminar Ciudad")
        print("0. Volver al menú principal")

        op = input("Seleccione una opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            codigo_postal = input("Código Postal: ")
            ciudad = Ciudad(nombre, codigo_postal)
            ciudades.append(ciudad)
            print("Ciudad creada con éxito.")

        elif op == "2":
            print("\nLista de Ciudades:")
            for i, c in enumerate(ciudades, start=1):
                print(f"{i} - {c.nombre} - CP: {c.codigo_postal}")

        elif op == "3":
            id_ciudad = int(input("ID de la ciudad a actualizar: "))
            if 0 < id_ciudad <= len(ciudades):
                ciudades[id_ciudad - 1].nombre = input("Nuevo nombre: ")
                ciudades[id_ciudad - 1].codigo_postal = input("Nuevo código postal: ")
                print("Ciudad actualizada.")
            else:
                print("Ciudad no encontrada.")

        elif op == "4":
            id_ciudad = int(input("ID de la ciudad a eliminar: "))
            if 0 < id_ciudad <= len(ciudades):
                ciudades.pop(id_ciudad - 1)
                print("Ciudad eliminada.")
            else:
                print("Ciudad no encontrada.")

        elif op == "0":
            break
        else:
            print("Opción inválida.")


menu()



