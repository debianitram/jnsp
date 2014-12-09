@auth.requires_login()
def novedades():
    page_novedades = db(Pagina.nombre == 'novedades').select(Pagina.id).first().id
    query = Noticia.pagina_id == page_novedades
    
    if 'new' in request.args:
        Noticia.pagina_id.default = page_novedades
        Noticia.pagina_id.readable = Noticia.pagina_id.writable = False
        
    if 'view' in request.args:
        Noticia.cuerpo.represent = lambda r, v: XML(v)
        
    fields = [Noticia.titulo, Noticia.created_on]
    
    formgrid = SQLFORM.grid(query,
                            csv=False,
                            fields=fields,
                            user_signature=True)
    
    return dict(formgrid=formgrid)


def lista_inscriptos():
    # Definir los campos para los inscriptos a la jornada
    return dict()


def contact_mails():
    # Ver mensajes del formulario de contacto.
    # Responder mensajes desde el correo de la jornada.
    return dict()
