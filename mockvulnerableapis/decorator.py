from functools import wraps
from django.http import HttpResponse

def authorization_check(view_function):
    @wraps(view_function)
    def wrap(request, *args, **kwargs):
        if ('HTTP_AUTHORIZATION' in request.META or 'HTTP_ACCESS_TOKEN' in request.META):
            return view_function(request, *args, **kwargs)
        else:
            return HttpResponse('Unauthorized', status=401)
    return wrap