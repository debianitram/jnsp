# -*- coding: utf-8 -*-

import os, time
# Config timezone
if not 'ART' in time.tzname:
    os.environ.update(TZ='America/Argentina/Catamarca')
    time.tzset()


db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])

response.generic_patterns = ['*'] if request.is_local else []


from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

# Customize table auth_user
auth.settings.extra_fields['auth_user'] = [
    Field('documento', unique=True, label='Nro Documento', comment=SPAN('sin puntos', _class='label label-info')),
    Field('institucion', label='Universidad/Institución'),
    Field('provincia'),
    Field('residencia', length=150, label='Domicilio'),
    Field('codigo_postal'),
    Field('telefono'),
    Field('modalidad', 'list:string', default='Asistente', writable=False, readable=False)
    ]
## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False, migrate=True)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True


### Definición de tablas.
Trabajo = db.define_table('trabajo',
            Field('titulo', length=50, label='Título', requires=IS_NOT_EMPTY()),
            Field('archivo', 'upload', label='Seleccionar un archivo'),
            Field('descripcion', 'text', label='Descripción'),
            auth.signature,
            format='Título: %(titulo)s, Autor: %(created_by)s')

Evaluacion = db.define_table('evaluacion',
            Field('evaluador_id', db.auth_user, default=auth.user_id),
            Field('trabajo_id', Trabajo),
            Field('puntaje', 'integer', default=0),
            auth.signature,
            format='ID Trab: %(trabajo_id)s - Puntos: %(puntaje)s')

Comprobante = db.define_table('comprobante',
            Field('archivo', 'upload'),
            auth.signature)

# S_IVA: Consumidor final, exento, Monotributista, Responsable Inscripto
SituacionIVA = db.define_table('situacion_iva',
            Field('nombre', length=100, requires=[IS_UPPER(), IS_NOT_EMPTY()]),
            auth.signature,
            format='%(nombre)s')

Catering = db.define_table('catering',
            Field('nombre', length=100, requires=[IS_UPPER(), IS_NOT_EMPTY()]),
            auth.signature,
            format='%(nombre)s')

Usuario_info = db.define_table('usuario_info',
            Field('usuario_id', db.auth_user, default=auth.user_id),
            Field('factura_razonsocial', length=150, label='Razón Social'),
            Field('factura_cuit', length=20, label='CUIT'),
            Field('factura_domicilio', length=150, label='Domicilio'),
            Field('factura_iva', SituacionIVA),
            Field('fecha_arribo', 'date', label='Fecha de arribo'),
            Field('acompaniante', 'integer', label='Cantidad de acompañantes'),
            Field('catering', Catering),
            Field('observacion', 'text'))

Pagina = db.define_table('pagina',
            Field('nombre'),
            Field('descripcion'),
            auth.signature,
            format='%(nombre)s')

Noticia = db.define_table('noticia',
            Field('pagina_id', Pagina),
            Field('titulo', length=140, requires=IS_NOT_EMPTY(), unique=True),
            Field('cuerpo', 'text'),
            Field('publicado', 'boolean', default=False),
            auth.signature,
            format='Título: %(titulo)s')