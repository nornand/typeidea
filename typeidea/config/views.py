'''views of config'''
from django.http import HttpResponse

def links(request):
    '''返回链接'''
    return HttpResponse('links')
