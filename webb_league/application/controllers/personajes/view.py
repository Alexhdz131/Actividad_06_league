import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, nombre):  
        model_personajes = config.model_personajes.select_nombre(nombre) # Selecciona el registro que coincida con nombre del campeon 
        return config.render.view(personajes) # Envia el registro y renderiza view.html
