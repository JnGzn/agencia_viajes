from agencia.dictionary.dic_reservas import listaReservas, listaPlanes



def listarReservasHabiles():
    temp_list = []
    for d in listaPlanes:
        if d['cupos'] > 0:
            temp_list.append(d)
    return temp_list

def listarReservas(cedula):
    temp_list = []
    for reserva in listaReservas:
        if(reserva['idUsuario'] == cedula and reserva['estado']):
            plan = next(item for item in listaPlanes if item["idPlan"] == reserva['idPlan'])
            temp_list.append(dict(plan, **reserva))
    return temp_list  

def eliminarReserva(id, cedula):
    esEliminado = False
    for reserva in listaReservas:
        if(reserva['idReserva'] == id and reserva['idUsuario'] == cedula):
            reserva['estado'] = False
            esEliminado = True
    if esEliminado: 
        print(" + Se ha borrado su reserva")
    else:
        print(" + No se pudo borrar, revisar el ID ingresado")

def crearReserva(cedula, idPlan):
    esEncontrado = False
    for reserva in listaPlanes:
        if(reserva['idPlan'] == idPlan):
            reserva['cupos'] = reserva['cupos'] -1
            esEncontrado = True

    if esEncontrado:
        listaReservas.append(  {'idReserva': 'R'+str(len(listaReservas)),'idUsuario': cedula, 'idPlan': idPlan, 'estado': True},)
        print(" + Se ha realizado su reserva")
    else:
        print(" + No se pudo agregar, revisar el ID ingresado")

def listarTodasReservas(): 
    temp_list = []
    for reserva in listaReservas:
        plan = next(item for item in listaPlanes if item["idPlan"] == reserva['idPlan'])
        temp_list.append(dict(plan, **reserva))
    return temp_list  

def listarTodosPlanes(): 
    return listaPlanes

def crearPlan(plan):
    plan['idPlan'] = 'R'+str(len(listaPlanes))
    listaPlanes.append(plan)

def modificarPlan(planEdit):
    idx = -1
    for i in range(len(listaPlanes)):

        if(listaPlanes[i]['idPlan'] == planEdit['idPlan']):
            idx =i
            
            
    if idx != -1: 
        listaPlanes[idx] = planEdit
        print(" + Se ha modificado el plan")
    else:
        print(" + No se pudo modificar, revisar el ID ingresado")