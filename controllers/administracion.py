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


@auth.requires_login()
def list_inscriptos():
    # Definir los campos para los inscriptos a la jornada
    fields = [Inscripcion.apellido,
             Inscripcion.nombre,
             Inscripcion.matricula,
             Inscripcion.email,
             Inscripcion.matricula]

    grid = SQLFORM.grid(Inscripcion,
                        fields=fields,
                        maxtextlength=50,
                        editable=False,
                        selectable=False,
                        csv=True,
                        deletable=False,
                        user_signature=True
                        )

    return dict(grid=grid)


def contact_mails():
    # Ver mensajes del formulario de contacto.
    # Responder mensajes desde el correo de la jornada.
    return dict()

@auth.requires_signature()
def edit_rt():
    # Edicion del reglamento y temario
    fields = ['titulo', 'cuerpo']
    Noticia.titulo.writable = False

    form = crud.update(Noticia,
                       request.args(0),
                       deletable=False,
                       next=URL(c='pages', f='reglamento_temario'),
                       message='Registro actualizado',
                       fields=fields)

    return dict(form=form)
