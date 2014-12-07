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
    (SPAN(I(_class='icon-leaf icon-white'), STRONG(' Sedes')),
     False,
     URL('pages', 'institucional')),
    (SPAN(I(_class='icon-certificate icon-white'), STRONG(' Reglamento & Temario')),
     False,
     URL('pages', 'reglamento_temario')),
    (SPAN(I(_class='icon-calendar icon-white'), STRONG(' Programa')),
     False,
     URL('pages', 'programa')),
    # (SPAN(I(_class='icon-globe'), STRONG(' Blog')),
    #  False,
    #  URL('blog', 'index')),
    (SPAN(I(_class='icon-briefcase icon-white'), STRONG(' Puntos de Interes')),
     False,
     URL('pages', 'puntos_interes')),
]
