from agencia.dictionary.dic_usuarios import listaUsuarios

def buscarCedula(cedula):
    for usuario in listaUsuarios:
        if(usuario['cedula'] == cedula):
            return True
    return False

def autenticarUsuario(documento, pwd):
    for usuario in listaUsuarios:
        if(usuario['cedula'] == documento and usuario['password']==pwd): 
            return usuario

def crearUsuario(nombre, cedula, contrasena):
    listaUsuarios.append({'nombre': nombre, 'cedula': cedula, 'password': contrasena, 'esAdmin': False})

def listarUsuarios():
    return listaUsuarios