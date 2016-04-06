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
        pagina = Pages.objects.get(id=pageID)
        respuesta += '<br><br>La pagina "' + pagina.name\
                    + '" dice: ' + pagina.page
    except:
        respuesta += '<br><br><br>No se encontro esa pagina'
    return HttpResponse(respuesta)
    

@csrf_exempt
def homePage(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            respuesta = 'Hola! ' + request.user.username\
                + ' <a href="/logout">Logout</a>'\
                + '<br><p>Desea Editar/Crear alguna pagina?</p>'\
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
            respuesta += '<li><a href="' + str(pagina.id) + '">'\
                        + pagina.name + '</a>'
        respuesta += '</ol>'
    elif request.method == 'PUT':
        if request.user.is_authenticated():
            try:
                info = request.body
                p = Pages(name=info.split(':')[0],\
                          page=info.split(':')[1])
                p.save()
                respuesta = 'Todo Ok!'
            except:
                respuesta = 'Nada Ok... El formato debe ser... Titulo:\
                             texto. En el cuerpo del PUT'
        else:
            respuesta = 'Para crear Paginas debe logearse...'
    return HttpResponse(respuesta)
    
    
@csrf_exempt    
def createPage(request):

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
                    + '<meta http-equiv="Refresh" content="3;\
                    url=http://127.0.0.1:8000/mod/">'
    else:
        respuesta = 'Pagina no permitida, redirigiendo...'\
                    + '<meta http-equiv="Refresh" content="3;\
                    url=http://127.0.0.1:8000/">'

    return HttpResponse(respuesta)
    

def managePages(request):
    respuesta = '<h3>Creacion de Paginas</h3>'\
                +'<form method="POST" action="/createPage/">'\
                +'Titulo Pagina: <input type="text" name="pagina"><br>'\
                +'Texto: <input type="text"name="texto"><br>'\
                +'<input type="submit" value="Crear">'\
                +'</form>'
    return HttpResponse(respuesta)
    

def redirectHome(request):
    respuesta = '<meta http-equiv="Refresh" content="0;\
                 url=http://127.0.0.1:8000/">'
    return HttpResponse(respuesta)



    
 