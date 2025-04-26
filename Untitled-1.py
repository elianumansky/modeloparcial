class Cliente:
    def __init__(self, nombre, dni, email):
        self.nombre = nombre
        self.dni = dni
        self.email = email

    def __agregar_cliente():
        nombre_cliente = input('Ingrese nombre: ').capitalize()
        while True:
            try:
                dni = int(input('Ingrese DNI: '))
                break
            except ValueError:
                print('Ingrese un número válido')
        while True:
            email = input('Ingrese email: ')
            if '@' in email and '.' in email:
                break
            else:
                print('Ingrese un email existente')
        nuevo_cliente = Cliente(nombre_cliente, dni, email)
        clientes[dni] = nuevo_cliente
        print('Cliente agregado')

    def __eliminar_cliente():
        while True:
            try:
                cliente_eliminar = int(input('Ingrese DNI del cliente a eliminar: '))
                break
            except ValueError:
                print('Ingrese un número válido')
        if cliente_eliminar in clientes:
            del clientes[cliente_eliminar]
            print('Cliente eliminado')
            return cliente_eliminar
        else:
            print('Cliente inexistente')

    # Métodos públicos que sirven de interfaz
    def agregar_cliente():
        Cliente.__agregar_cliente()

    def eliminar_cliente():
        Cliente.__eliminar_cliente()


class Pedido:
    def __init__(self, numero, dni, libro):
        self.numero = numero
        self.dni = dni
        self.libro = libro

    def __agregar_pedido():
        while True:
            try:
                numero = int(input('Ingrese número de pedido: '))
                break
            except ValueError:
                print('Número inválido')
        while True:
            try:
                dni = int(input('Ingrese DNI del cliente: '))
                if dni in clientes:
                    email_clientes.add(clientes[dni].email)
                    break
                else:
                    print('Cliente inexistente')
            except ValueError:
                print('Ingrese un número válido')
        titulo = input('Ingrese título: ')
        while True:
            try:
                cantidad = int(input('Ingrese cantidad: '))
                if cantidad > 0:
                    break
                else:
                    print('La cantidad debe ser mayor a 0')
            except ValueError:
                print('La cantidad debe ser un número entero')
        libro = (titulo, cantidad)
        nuevo_pedido = Pedido(numero, dni, libro)
        pedidos.append(nuevo_pedido)
        print('Pedido agregado')
        if cantidad > 10:
            print('Pedido mayorista detectado')

    def __mostrar_listado_de_pedidos():
        for p in pedidos:
            print(f'Nro de pedido: {p.numero} Cliente: {p.dni} Libro: {p.libro[0]} Cantidad: {p.libro[1]}')

    # Métodos públicos
    def agregar_pedido():
        Pedido.__agregar_pedido()

    def mostrar_listado_de_pedidos():
        Pedido.__mostrar_listado_de_pedidos()


# Variables globales
clientes = {}
pedidos = []
email_clientes = set()

# Menú principal
opcion = ''
while opcion != '5':
    opcion = input(
        'Ingrese opción:\n'
        '1. Registrar nuevo cliente\n'
        '2. Eliminar cliente\n'
        '3. Registrar pedido\n'
        '4. Ver listado de pedidos\n'
        '5. Salir\n'
    )
    if opcion == '1':
        Cliente.agregar_cliente()
    elif opcion == '2':
        Cliente.eliminar_cliente()
    elif opcion == '3':
        Pedido.agregar_pedido()
    elif opcion == '4':
        Pedido.mostrar_listado_de_pedidos()
    elif opcion == '5':
        print('Hasta pronto!')
    else:
        print('Ingrese una opción válida')
