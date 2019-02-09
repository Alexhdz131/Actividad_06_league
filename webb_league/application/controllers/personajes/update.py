import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre): 
        personajes = config.model_personajes.select_nombre(nombre) # Selecciona el registro que coincida con nombre del campeon
        return config.render.update(personajes) # Envia el registro y renderiza update.html
    
    def POST(self, nombre):
        formulario = web.input() # almacena los datos del formulario web
        nombre = formulario['nombre'] # almacena el nombre del campeon
        tipo_habilidad = formulario['tipo_habilidad'] # almacena el tipo de habilidad
        preciot = formulario['preciot'] #almacena el precio de tienda
        region  = formulario['region'] #almacena  la region
        rol = formulario['rol'] #almacena el rol
        sexo = formulario['sexo'] #almacena el sexo
        config.model_personajes.update_personajes(nombre, tipo_habilidad,preciot,region,rol,sexo) # actuliza los valores
        raise web.seeother('/') # redirecciona al index
