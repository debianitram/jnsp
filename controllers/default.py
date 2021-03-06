# -*- coding: utf-8 -*-


def index():
    if len(request.args):
        pagina = int(request.args(0))
    else:
        pagina = 0

    items = 10
    limitby = (pagina * items, (pagina + 1) * items + 1)

    qblog = Pagina.nombre == 'novedades'
    join = Noticia.on(Noticia.pagina_id == Pagina.id)

    total_noticias = db(qblog).select(Noticia.ALL, 
                                      join=join,
                                      orderby=~Noticia.modified_on,
                                      limitby=limitby).exclude(lambda r: r.publicado != False)

    return dict(noticias=total_noticias, pagina=pagina, items=items)


# @auth.requires_login()
def form_inscripcion():
    from modal_FieldsReference import modalFieldReference as modal

    modal_profesion = modal(Inscripcion.profesion,
                            btn_title='Agregar profesion',
                            btn_name='agregar',
                            modal_title='Nueva Profesión',
                            modal_key='inscripcion_profesion'
                            )

    modal_transporte = modal(Inscripcion.transporte,
                             btn_title='Agregar transporte',
                             btn_name='agregar',
                             modal_title='Nuevo Transporte',
                             modal_key='inscripcion_transporte')

    # Inscripcion.profesion.comment = modal_profesion.btn()
    # Inscripcion.transporte.comment = modal_transporte.btn()

    windows = {'profesion': modal_profesion.modal(),
               'transporte': modal_transporte.modal()}

    form = crud.create(Inscripcion)

    return dict(form=form, windows=windows)


def form_trabajo():
    form = SQLFORM(Trabajo)
    if form.accepts(request, session):
        session.jobid = form.vars.id
        redirect(URL('default', 'trabajo_ok'))

    elif form.errors:
        session.flash = 'Controle el formulario'
        
    return dict(form=form)


def trabajo_ok():
    job = Trabajo(session.jobid) or redirect(URL(c='default', f='index'))
    return dict(job=job)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
