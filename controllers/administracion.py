@auth.requires_membership('administrador')
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


@auth.requires_membership('administrador')
def list_inscriptos():
    # Definir los campos para los inscriptos a la jornada
    fields = [Inscripcion.apellido,
             Inscripcion.nombre,
             Inscripcion.matricula,
             Inscripcion.consejo_origen,
             Inscripcion.profesion,
             Inscripcion.dni,
             Inscripcion.tipo_asistencia,
             Inscripcion.fecha_nacimiento,
             Inscripcion.telefono,
             Inscripcion.area_inscripcion,
             Inscripcion.transporte,
             Inscripcion.info_adicional
             ]
    
    query = Inscripcion.is_active == True

    grid = SQLFORM.grid(query,
                        fields=fields,
                        maxtextlength=50,
                        editable=False,
                        selectable=False,
                        paginate=100,
                        csv=True,
                        ondelete=hide_record,
                        user_signature=True
                        )

    return dict(grid=grid)


def contact_mails():
    # Ver mensajes del formulario de contacto.
    # Responder mensajes desde el correo de la jornada.
    return dict()

@auth.requires_membership('administrador')
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


@auth.requires_membership('administrador')
def list_trabajos():

    grid = SQLFORM.grid(Trabajo,
                        maxtextlength=50,
                        editable=False,
                        create=False,
                        selectable=False,
                        paginate=100,
                        csv=True,
                        ondelete=hide_record,
                        user_signature=True
                        )

    return dict(grid=grid)
