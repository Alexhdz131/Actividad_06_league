import web
        
urls = (
    '/', 'application.controllers.personajes.index.Index',
    '/insert', 'application.controllers.personajes.insert.Insert',
    '/update/(.*)', 'application.controllers.personajes.update.Update',
    '/delete/(.*)', 'application.controllers.personajes.delete.Delete',
    '/view/(.*)', 'application.controllers.personajes.view.View',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
