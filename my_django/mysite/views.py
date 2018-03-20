import datetime

from django.http import HttpResponse


def hello(request):
    return HttpResponse("hello world")


def my_home_page_view(request):
    return HttpResponse('Home page')


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is %s.</body></html>" % now
    return HttpResponse(html)
