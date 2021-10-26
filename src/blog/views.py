from django.shortcuts import render
from .models import Post
from django.utils import timezone

#
# Una View es un lugar donde ponemos la "lógica" de nuestra aplicación. Pedirá información 
# del modelo que has creado antes y se la pasará a la plantilla. Crearemos una plantilla en 
# el próximo capítulo. Las vistas son sólo métodos de Python que son un poco más complicados 
# que los que escribimos en el capítulo Introducción a Python.
#
# Las Vistas se colocan en el archivo views.py. Agregaremos nuestras views al archivo 
# blog/views.py.
#


def post_list(request):
    my_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    my_context = {
        'posts': my_posts,
    }

    return render(request, 'blog/post_list.html', my_context)