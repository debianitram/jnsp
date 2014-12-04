def institucional():
    response.view = 'pages/institucional.html'
    return dict()


def reglamento_temario():
    response.view = 'pages/reglamento_temario.html'
    q = Pagina.nombre == 'reglamento'
    items = db(q).select(Noticia.ALL,
                         join=Noticia.on(Noticia.pagina_id == Pagina.id),
                         orderby=Noticia.id)
    return dict(items=items)


def programa():
    response.view = 'pages/programa.html'
    return dict()


def puntos_interes():
    response.view = 'pages/puntos_interes.html'
    return dict()