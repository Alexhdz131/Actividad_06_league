import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        personajes = config.model_personajes.select_personajes().list() # Selecciona todos los registros de los personajes
        return config.render.index(personajes) # Envia todos los registros y renderiza index.html
