def institucional():
    response.view = 'pages/institucional.html'
    return dict()


def reglamento_temario():
    response.view = 'pages/reglamento_temario.html'
    q = Pagina.nombre == 'reglamento'
    reglamento = db(q).select(Noticia.ALL,
                         join=Noticia.on(Noticia.pagina_id == Pagina.id),
                         orderby=Noticia.id)

    q_ = Pagina.nombre == 'temario'
    temario = db(q_).select(Noticia.ALL,
                            join=Noticia.on(Noticia.pagina_id == Pagina.id),
                            orderby=Noticia.id)

    q__ = Pagina.nombre == 'normas'
    normas = db(q__).select(Noticia.ALL,
                            join=Noticia.on(Noticia.pagina_id == Pagina.id),
                            orderby=Noticia.id)
    
    return dict(reglamento=reglamento, temario=temario, normas=normas)


def programa():
    response.view = 'pages/programa.html'
    return dict()


def faq():
    q = Pagina.nombre == 'faq'
    faq = db(q).select(Noticia.ALL,
                         join=Noticia.on(Noticia.pagina_id == Pagina.id),
                         orderby=Noticia.id)
    return dict(faq=faq)


def puntos_interes():
    response.view = 'pages/puntos_interes.html'
    
    query = (Hoteles.id > 0) & (Hoteles.is_active == True)
    hoteles = db(query).select(orderby=Hoteles.nombre)
    
    return dict(hoteles=hoteles)
