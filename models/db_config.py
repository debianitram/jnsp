crud.settings.create_captcha = auth.settings.captcha
# Archivo de configuración para los modelos.
Inscripcion.tipo_asistencia.requires = IS_IN_SET(('Profesional +32 años',
                                                  'Joven Profesional hasta 32 años',
                                                  'Acompañante',
                                                  'Observador'))

Inscripcion.area_inscripcion.requires = IS_IN_SET(('Área I: Contabilidad Gubernamental',
                                                   'Área II: Administración de los Organismos Públicos',
                                                   'Área III: Economía del Sector Público'))

# Plugins CKEditor
from plugin_ckeditor import CKEditor
import os

ckeditor = CKEditor(db)
ckeditor.define_tables()

Noticia.cuerpo.widget=ckeditor.widget

def get_username(user):
    return SPAN(user.last_name, ', ', user.first_name)

def hide_record(table, record):
    db[table](record).update_record(is_active=False)
    db.commit()
