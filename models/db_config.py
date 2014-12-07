# Archivo de configuración para los modelos. 
Inscripcion.tipo_asistencia.requires = IS_IN_SET(('Profesional +32 años',
                                                  'Joven Profesional hasta 32 años',
                                                  'Acompañante'))

Inscripcion.area_inscripcion.requires = IS_IN_SET(('Área I: Contabilidad',
                                                   'Área II: Administración',
                                                   'Área III: Economía'))

# Plugins CKEditor
from plugin_ckeditor import CKEditor
import os

ckeditor = CKEditor(db)
ckeditor.define_tables()

Noticia.cuerpo.widget=ckeditor.widget

def get_username(user):
    return SPAN(user.last_name, ', ', user.first_name)