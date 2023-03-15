from agencia.menu_admin import menuAdmin
from agencia.service.usuarios import buscarCedula, autenticarUsuario, crearUsuario
from agencia.menu_resevas import menuCancelarReservar, menuReservar, menuVerReservar


from os import system

def menuGenerico(msj):
    system("cls")
    print("****************************")
    print(f"********{msj}********")
    print("****************************")

def menuUser():
    cedula = -2
    while(cedula != -1): 
        menuGenerico("BIENVENIDO A VIAJES-AGENCIA.COM")
        
        cedula = input("ingrese su numero de cedula: ")
        if(buscarCedula(cedula)):
            pwd = input("ingrese su contraseña: ")
            usuario = autenticarUsuario(cedula, pwd)
            if(usuario):
                if(usuario['esAdmin']):
                   menuAdmin(usuario) 
                else:
                    menuUsuarios(usuario)
            else:
                print("+ Contraseña incorrecta")
                input("presione enter para continuar")
        else: 
            print("+ No estas registrado, se le pedirán unos datos para su registro")
            input("presione enter para continuar")
            menuCrearUsuario(cedula)

def menuCrearUsuario(cedula):
    menuGenerico("REGISTRO")
    nombre = input("ingrese su nombre: ")
    pwd = input("ingrese su constraseña: ")
    crearUsuario(nombre, cedula, pwd)
    print("Usuario Creado")
    print("------------------------")

def menuUsuarios(usario):
    opcion = -1
    while( opcion != 0): 
        menuGenerico("Este es el menu de usuario")
        print(f"USUARIO:::::::::: {usario['nombre']}")
        print(f"CEDULA:::::::::: {usario['cedula']}")
        print("0 -> Salir")
        print("1 -> Resevar")
        print("2 -> Ver Mis Reservas")
        print("3 -> Cancelar mis Reservas")
        opcion = int(input("Ingese su opción -> "))
        if(opcion == 1):
            menuReservar(usario)
            input("presione enter para continuar")
        elif(opcion == 2): 
            menuVerReservar(usario)
            input("presione enter para continuar")
        elif(opcion == 3):
            menuCancelarReservar(usario)
            input("presione enter para continuar")


