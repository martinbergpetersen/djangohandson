import datetime

from django.http import HttpResponse, Http404


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" \
        % (offset, dt)
    return HttpResponse(html)


def hello(request):
    return HttpResponse("hello world")


def my_home_page_view(request):
    return HttpResponse('Home page')


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is %s.</body></html>" % now
    return HttpResponse(html)
