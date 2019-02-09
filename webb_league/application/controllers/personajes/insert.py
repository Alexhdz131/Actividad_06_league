import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre = formulario['nombre'] # almacena el nombre escrito en el input
        tipo_habilidad = formulario['tipo_habilidad'] # almacena el tipo de habilidad escrito en el input
        preciot = formulario['preciot'] # almacena el precio de tienda escrito en el input
        region = formulario['region'] # almacena la region escrito en el input
        rol = formulario['rol'] # almacena el rol del campeon  escrito en el input
        sexo= formulario['sexo'] # almacena el sexo escrito en el input
        config.model_personajes.insert_personajes(nombre, tipo_habilidad,preciot,region,rol,sexo,) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/') # redirecciona al index.html
