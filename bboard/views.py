from django.http import HttpResponse
from django.template import loader

from .models import Bb

def index(request):
    template = loader.get_template('bboard/index.html') # загружаем шаблон функцией get_template из модуля  django.template.loader. в качестве параметра указываем путь к файлу шаблона
    bbs = Bb.objects.order_by('-published')
    context = {'bbs':bbs}
    return HttpResponse(template.render(context, request)) #, content_type='text/plain; charset=utf-8'
