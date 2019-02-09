import web # importa la libreria web.py
import application.models.model_personajes as model_personajes # importa el modelo_personajes


render = web.template.render('application/views/personajes/', base='master') # configura la ubicacion de las vistas