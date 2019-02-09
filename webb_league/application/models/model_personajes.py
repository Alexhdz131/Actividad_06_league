import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla personajes
'''
def select_personajes():
    try:
        return db.select('personajes') # Selecciona todos los registros de la tabla personajes
    except Exception as e:
        print "Model select_personajes Error {}".format(e.args)
        print "Model select_personajes Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''
def select_nombre(nombre):
    try:
        return db.select('personajes',where='nombre=$nombre', vars=locals())[0] # selecciona el primer registro que coincida con el nombre del campeon
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando los campos que estan por defecto.
'''
def insert_personajes(nombre, tipo_habilidad,preciot,region,rol,sexo):
    try:
        return db.insert('personajes', nombre=nombre,tipo_habilidad=tipo_habilidad,preciot=preciot,region=region,rol=rol,sexo=sexo) # inserta un registro en personjes
    except Exception as e:
        print "Model insert_personajes Error {}".format(e.args)
        print "Model insert_personajes Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_personajes(nombre):
    try:
        return db.delete('personajes', where='nombre=$nombre',vars=locals()) # borra un registro de personajes
    except Exception as e:
        print "Model delete_personajes Error {}".format(e.args)
        print "Model delete_personajes Message {}".format(e.message)
        return None

'''
Metodo para actualizar 
'''
def update_personajes(nombre,tipo_habilidad,preciot,region,rol,sexo): # actualiza los campos de personajes que coincidan con el nombre
    try:
        return db.update('personajes', 
            tipo_habilidad=tipo_habilidad,
            preciot=preciot,
            region=region,
            rol=rol,
            sexo=sexo,

            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_personajes Error {}".format(e.args)
        print "Model update_personajes Message {}".format(e.message)
        return None
