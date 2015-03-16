# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

from applications.config_jnsp.modules import config

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = ''
response.title = 'Jornadas'
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Martín Miranda <debianitram @ gmail . com'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = config.analitycs_id


response.menu = [
    (SPAN(I(_class='icon-home icon-white'), STRONG(' Inicio')), 
     False,
     URL('default', 'index'),
     []),
    (SPAN(I(_class='icon-certificate icon-white'), STRONG(' Reglamento & Temario')),
     False,
     URL('pages', 'reglamento_temario')),
    (SPAN(I(_class='icon-calendar icon-white'), STRONG(' Programa')),
     False,
     URL('pages', 'programa')),
    (SPAN(I(_class='icon-tags icon-white'), STRONG(' Presentar Trabajos')),
     False,
     URL('default', 'form_trabajo')),
    (SPAN(I(_class='icon-pencil icon-white'), STRONG(' Inscripción', _style='color:lightcoral')),
     False,
     URL('default', 'form_inscripcion')),
]

if auth.user:
    _ = (SPAN(I(_class='icon-wrench icon-white'), STRONG(' Admin')),
         False,
         URL(),
         [(SPAN(I(_class='icon-pencil'), STRONG(' Redactar')),
            False,
            URL(c='administracion', f='novedades', user_signature=True)),
          (SPAN(I(_class='icon-user'), STRONG(' Inscriptos')), 
            False,
            URL(c='administracion', f='list_inscriptos', user_signature=True)),
          (SPAN(I(_class='icon-tags'), STRONG(' Trabajos')), 
            False,
            URL(c='administracion', f='list_trabajos', user_signature=True))])
    response.menu.append(_)



response.submenu = [
    (SPAN(I(_class='icon-briefcase'), STRONG(' Hospedajes')), 
     False,
     URL('pages', 'puntos_interes'),
     []),
    (SPAN(I(_class='icon-glass'), STRONG(' Restaurant')),
     False,
     URL('pages', 'puntos_interes')),
    (SPAN(I(_class='icon-camera'), STRONG(' Puntos de Interes')),
     False,
     URL('pages', 'puntos_interes')),
    (SPAN(I(_class='icon-info-sign'), STRONG(' FAQ')),
     False,
     URL('pages', 'faq')),  
]