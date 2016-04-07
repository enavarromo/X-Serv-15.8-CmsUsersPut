# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt

def pickPage(request, pageID):
    if request.user.is_authenticated():
        respuesta = 'Hola! ' + request.user.username\
                    + ' <a href="/logout">Logout</a> '
    else:
        respuesta = 'Hola desconocido, desea hacer \
                     <a href="/login">Login</a> ?'
    try:
        print(pageID)
        pagina = Pages.objects.get(name=pageID)
        respuesta += '<br><br>La pagina "' + pagina.name\
                    + '" dice: ' + pagina.page + '<br><br>'\
                    +'<form method="GET" action="/home/">'\
                    +'<br><input type="submit" value="Home">'\
                    +'</form>'
    except:
        respuesta += '<br><br><p1> No se encontro esa pagina </p1>'\
                    +'<form method="GET" action="/home/">'\
                    +'<br><br><input type="submit" value="Home">'\
                    +'</form>'
    return HttpResponse(respuesta)
    

@csrf_exempt
def homePage(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            respuesta = 'Hola! ' + request.user.username\
                + ' <a href="/logout">Logout</a>'\
                + '<br><p>Desea Crear/Editar alguna pagina?</p>'\
                + '<form method="GET" action="/mod/">'\
                + '<input type="submit" value="Edicion">'\
                + '</form>'
                
        else:
            respuesta = 'Hola desconocido, desea hacer \
                    <a href="/login">Login</a> ?'\
                    '<br>Solo los usuarios logeados pueden\
                     editar contenidos<br>'
        libro = Pages.objects.all()
        respuesta+='<br>Paginas almacenadas actualmente:<ol>'
        for pagina in libro:
            respuesta += '<li><a href="' + pagina.name + '">'\
                        + pagina.name + '</a>'
        respuesta += '</ol>'
    elif request.method == 'PUT':
        if request.user.is_authenticated():
            try:
                info = request.body
                pagina = info.split(':')[0]
                texto = info.split(':')[1]
                pagina=pagina.replace('+',' ')
                texto=texto.replace('+',' ')
                p = Pages(name=pagina,\
                          page=texto)
                p.save()
                respuesta = 'Todo Ok!'
            except:
                respuesta = 'Nada Ok... El formato debe ser... Título:\
                             texto. En el cuerpo del PUT'
        else:
            respuesta = 'Para crear Páginas debe logearse...'
    return HttpResponse(respuesta)
    
    
@csrf_exempt    
def createPage(request):
    print(request.method)
    if request.method == 'POST':
        print (request.body)
        body = request.body
        info=body.split('&')
        pagina = info[0].split('=')[1]
        texto = info[1].split('=')[1]
        pagina=pagina.replace('+',' ')
        texto=texto.replace('+',' ')
        pageAux = Pages(name=pagina, page=texto)
        pageAux.save()
        respuesta = 'Pagina Almecenada adecuadamente, continuemos!'\
                    + '<meta http-equiv="Refresh" content="2;\
                    url=http://127.0.0.1:8000/mod/">'
    else:
        respuesta = 'Página no permitida, redirigiendo...'\
                    + '<meta http-equiv="Refresh" content="3;\
                    url=http://127.0.0.1:8000/">'

    return HttpResponse(respuesta)
    

def managePages(request):
    respuesta = '<h3>Edición de Páginas</h3>'\
                +'<form method="POST" action="/createPage/">'\
                +'Título Página: <input type="text" name="pagina"><br>'\
                +'Texto: <input type="text"name="texto"><br>'\
                +'<input type="submit" value="Subir">'\
                +'</form>'\
                +'<form method="GET" action="/home/">'\
                +'<input type="submit" value="Home">'\
                +'</form>'
    return HttpResponse(respuesta)

def redirectHome(request):
    respuesta = '<meta http-equiv="Refresh" content="0;\
                 url=http://127.0.0.1:8000/">'
    return HttpResponse(respuesta)




#  Useful code:
"""
Modificaqr existente: listar toda la BD en vista 'mod/' con enlaces que incluyan el id de la opcion seleccionada. en url redireccionar con (d) para capturar el identificador. En nuevo def en views trabajar con la BD en cuestion tipo:
pagina = Pages.objects.get(id=pageID)
Primero) nuevo formulario y ver como sobreescribir en la BD
evolucion) mostrar texto editable...
"""

"""
Modificar primary key de BD
"""
    
    
    
    
 
