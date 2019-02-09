import web
'''
Parametros de configuracion para conectarse a una base de datos
MySQL o MariaDB
'''
db = web.database(
    dbn='mysql', # motor de base de datos
    host='localhost', # ruta del servidor
    db='league_bot', # nombre de la base de datos
    user='ahp', # usuario dela base de datos
    pw='ahp.2019', # password del usuario
    port = 3308 # puerto de mariadb
    )