# -*- coding: utf-8 -*-

from applications.config_jnsp.modules import config
import os, time
# Config timezone
if not 'ART' in time.tzname:
    os.environ.update(TZ='America/Argentina/Catamarca')
    time.tzset()


db = DAL(config.connect_to_db, pool_size=1, check_reserved=['all'])

response.generic_patterns = ['*'] if request.is_local else []


from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

# Customize table auth_user
## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False, migrate=True)

# Recaptcha

from gluon.tools import Recaptcha
auth.settings.captcha = Recaptcha(request, 
                                  config.captcha_public_key,
                                  config.captcha_private_key,
                                  use_ssl=True,
                                  error_message='inválido',
                                  label='Verificar:',
                                  options="theme:'white', lang:'es'")


## configure email
mail = auth.settings.mailer
mail.settings.server = config.mail_server
mail.settings.sender = config.mail_sender 
mail.settings.login = config.mail_login

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
auth.settings.actions_disabled = ('register', 'request_reset_password')
auth.settings.create_user_groups = False

auth.messages.reset_password = 'Haz clic en el link http://' + \
    request.env.http_host + \
    URL(r=request,c='default',f='user',args=['reset_password']) + \
    '/%(key)s para restablecer tu contraseña'


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

Profesion = db.define_table('profesion', Field('nombre'), format='%(nombre)s')
Transporte = db.define_table('transporte', Field('nombre'), format='%(nombre)s')


Inscripcion = db.define_table('inscripcion',
            Field('apellido', length=100),
            Field('nombre', length=100),
            Field('matricula', length=50),
            Field('consejo_origen', length=100),
            Field('profesion', 'reference profesion'),
            Field('dni', length=25),
            Field('tipo_asistencia', 'list:string'),
            Field('email'),
            Field('fecha_nacimiento', 'date'),
            Field('telefono'),
            Field('area_inscripcion', 'list:string'),
            Field('transporte', 'reference transporte'),
            Field('info_adicional', 'text'))

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
