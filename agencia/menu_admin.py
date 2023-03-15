from os import system
from agencia.menu_resevas import enumerarPlan, enumerarReservas
from agencia.service.reservas import listarTodosPlanes, listarTodasReservas, crearPlan, modificarPlan
from agencia.service.usuarios import listarUsuarios

def menuGenerico(msj):
    system("cls")
    print("****************************")
    print(f"********{msj}********")
    print("****************************")

def menuAdmin(usario):
    opcion = -1
    while( opcion != 0): 
        menuGenerico("Este es el menu de ADMINs")
        print(f"USUARIO:::::::::: {usario['nombre']}")
        print(f"CEDULA:::::::::: {usario['cedula']}")
        print("0 -> Salir")
        print("1 -> Ver todos los Usuarios")
        print("2 -> Ver Todas las Resevas")
        print("3 -> Ver todos los Planes")
        print("4 -> Agregar un plan")
        print("5 -> Modificar un plan")
        opcion = int(input("Ingese su opción -> "))
        if(opcion == 1):
            enumerarUsuario(listarUsuarios())
            input("presione enter para continuar")
        elif(opcion == 2):
            enumerarReservas(listarTodasReservas())
            input("presione enter para continuar")
        elif(opcion == 3):
            enumerarPlan(listarTodosPlanes())
            input("presione enter para continuar")
        elif(opcion == 4):
            print("---------Agregar Plan------")
            crearPlan(formPlanes())
            input("presione enter para continuar")
        elif(opcion == 5):
            enumerarPlan(listarTodosPlanes())
            print("---------Editar Plan------")
            id = input("ingrese el ID a a modificar..")
            plan = formPlanes()
            plan['idPlan'] = id
            modificarPlan(plan)
            input("presione enter para continuar")

def enumerarUsuario(usuarios):
    print("---------------------")
    for i in range(len(usuarios)):
        print(f"<- {i+1} ->")
        print(f"Documento: {usuarios[i]['cedula']}")
        print(f"Nombre: {usuarios[i]['nombre']}")
        print(f"Es Admin: {usuarios[i]['esAdmin']}")
        print("---------------------")

def formPlanes():
    tipo = input("ingrese el tipo de plan: ")
    fecha = input("ingrese la fecha: ")
    titulo = input("ingrese el titulo: ")
    descripcion = input("ingrese la descripcion: ")
    lugar = input("ingrese el lugar: ")
    cupos = int(input("ingrese la cantidad de cupos: "))
    return {'tipo': tipo, 
            'fecha': fecha, 
            'titulo': titulo, 
            'descripcion': descripcion, 
            'lugar': lugar, 
            'cupos': cupos}
