from os import system
from agencia.service.reservas import listarReservas, eliminarReserva, crearReserva, listarReservasHabiles

def menuGenerico(msj):
    system("cls")
    print("****************************")
    print(f"********{msj}********")
    print("****************************")

def enumerarReservas(reservas):
    print("---------------------")
    for i in range(len(reservas)):
        print(f"<- {i+1} ->")
        print(f"ID: {reservas[i]['idReserva']}")
        print(f"Fecha: {reservas[i]['fecha']}")
        print(f"Tipo: {reservas[i]['tipo']}")
        print(f"Lugar: {reservas[i]['lugar']}")
        print(f"Titulo: {reservas[i]['titulo']}")
        print(f"Descripcion: {reservas[i]['descripcion']}")
        print("---------------------")
def enumerarPlan(reservas):
    print("---------------------")
    for i in range(len(reservas)):
        print(f"<- {i+1} ->")
        print(f"ID: {reservas[i]['idPlan']}")
        print(f"Fecha: {reservas[i]['fecha']}")
        print(f"Tipo: {reservas[i]['tipo']}")
        print(f"Lugar: {reservas[i]['lugar']}")
        print(f"Titulo: {reservas[i]['titulo']}")
        print(f"Descripcion: {reservas[i]['descripcion']}")
        print("---------------------")

def menuReservar(usuario):
    menuGenerico("Relizar Reserva")
    reservas = listarReservasHabiles()
    enumerarPlan(reservas)
    id = input("ingrese el ID a reservar..")
    crearReserva(usuario['cedula'], id)

 
def menuVerReservar(usuario):
    menuGenerico("Ver Reservas")
    reservas = listarReservas(usuario['cedula'])
    if len(reservas) == 0:
        print("+ No tienes Reservas")
        return
    enumerarReservas(reservas)
 
def menuCancelarReservar(usuario):
    menuGenerico("Cancelar Reservas")
    reservas = listarReservas(usuario['cedula'])
    if len(reservas) == 0:
        print("+ No tienes Reservas")
        return
    enumerarReservas(reservas)
    id = input("ingrese el ID a cancelar..")
    eliminarReserva(id, usuario['cedula'])


    

