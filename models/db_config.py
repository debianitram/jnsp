# Archivo de configuración para los modelos. 

db.auth_user.documento.requires = [IS_INT_IN_RANGE(10000, 9999999999), 
                                   IS_NOT_IN_DB(db, db.auth_user.documento)]
db.auth_user.institucion.requires = IS_NOT_EMPTY()
db.auth_user.provincia.requires = IS_NOT_EMPTY()
db.auth_user.modalidad.requires = IS_IN_SET(('Asistente', 'Expositor', 'Autor'))