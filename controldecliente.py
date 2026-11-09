import json
import fpdf
import os
usuarios = {}
datos = []
try:
    with open('usuario.json', 'r') as archivo:
        datos = json.load(archivo)

except (FileNotFoundError, json.JSONDecodeError, AttributeError):
    usuarios = {}

def menu():
    

    while True:
        print('CONTROL DE CLIENTES')
        print('1. Registrar clientes')
        print('2. Mostrar clientes')
        print('3. Buscar clientes')
        print('4. Eliminar clientes')
        print('5. Hacer factura')
        print('6. Salir')

        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            registrar_clientes()  
        elif opcion == '2':
            mostrar_clientes()
        elif opcion == '3':
            buscar_clientes()
        elif opcion == '4':
            eliminar_clientes()
        elif opcion == '5':
            factura()
        elif opcion == '6':
            salir()
            break
        else:
            print('Opcion invalida, intente de nuevo\n')




def registrar_clientes():
    usuarios = {}
    print('REGISTRAR CLIENTES')
    nombre = input('Ingrese nombre de cliente: ').strip()
    if nombre in [usuario['nombre'] for usuario in datos]:
        print('El cliente ya existe')
        return
    elif nombre == '':
        print('El nombre no puede estar vacio')
        return
    else:
        usuarios['nombre'] = nombre
    

    telefono = input('Ingrese numero telefono: ').strip()
    if telefono in [usuario['telefono'] for usuario in datos]:
        print('El cliente ya existe')
        return
    elif telefono == '':
        print('El telefono no puede estar vacio')
        return
    else:
        usuarios['telefono'] = telefono

    correo = input('Ingrese correo electronico: ').strip()
    if correo in [usuario['correo'] for usuario in datos]:
        print('El cliente ya existe')
        return
    elif correo == '':
        print('El correo no puede estar vacio')
        return
    else:
        usuarios['correo'] = correo
    usuarios['compras_realizadas'] = 0
    datos.append(usuarios)
    with open('usuario.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print('Cliente registrado con exito\n')

def mostrar_clientes():
    print('CLIENTES REGISTRADOS')
    if datos:
        for clientes in datos:
            print('-' * 50)
            print(f'Nombre: {clientes["nombre"]}')
            print(f'Telefono: {clientes["telefono"]}')
            print(f'Correo: {clientes["correo"]}\n')
    else:
        print('No hay clientes registrados\n')

def buscar_clientes():
    print('BUSCAR CLIENTES POR NOMBRE')
    nombre = input('Ingrese nombre de cliente: ').strip()
    for clientes in datos:
        if clientes['nombre'] == nombre:
            print('-' * 50)
            print(f'Nombre: {clientes["nombre"]}')
            print(f'Telefono: {clientes["telefono"]}')
            print(f'Correo: {clientes["correo"]}\n')
            print('-' * 50)
            print()
        else:
            print('Cliente no encontrado\n')

def eliminar_clientes():
    print('ELIMINAR CLIENTES POR NOMBRE')
    nombre = input('Ingrese nombre de cliente a eliminar: ')
    if nombre not in [clientes['nombre'] for clientes in datos]:
        print('Cliente no encontrado\n')
    else:
        for clientes in datos:
            if clientes['nombre'] == nombre:
                datos.remove(clientes)
                print(f'Cliente {nombre} eliminado con exito')
                return
    with open('usuario.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def factura():
    print('HACER FACTURA')
    nombre = input('Ingrese nombre de cliente: ')
    if nombre not in [clientes['nombre'] for clientes in datos]:
        print('Cliente no encontrado\n')
    else:
        for clientes in datos:
            if clientes['nombre'] == nombre:
                decision = input('Desea agregar una compra? (si/no): ')
                if decision.lower().strip() == 'si':
                   clientes['compras_realizadas'] += 1
                   producto = input('Ingrese nombre del producto que adquirio: ')
                   precio = input("Cual es el precio del producto? ")
                   print('Factura en formato PDF generada con exito\n')
                   pdf = fpdf.FPDF()
                   pdf.add_page()
                   pdf.set_font("Arial", size=12)
                   pdf.cell(200, 10, txt=f'Factura para {clientes["nombre"]}', ln=True)
                   pdf.cell(200, 10, txt=f'Telefono: {clientes["telefono"]}', ln=True)
                   pdf.cell(200, 10, txt=f'Correo: {clientes["correo"]}', ln=True)
                   pdf.cell(200, 10, txt=f'Total de compras realizadas por el usuario desde que se registro: {clientes["compras_realizadas"]}', ln=True)
                   pdf.cell(200, 10, txt=f'Producto adquirido: {producto} con el precio de: {precio}', ln=True)

                   pdf.output("factura.pdf")
                   os.startfile(os.path.abspath("factura.pdf"))
                
                else:
                    print('Factura no generada\n')
          

def salir():
    print('Saliendo del programa...')

menu()

with open('usuario.json', 'w') as archivo:
    json.dump(datos, archivo, indent=4)








