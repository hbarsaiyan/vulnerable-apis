from functools import wraps
from django.http import HttpResponse

def authorization_check(view_function):
    @wraps(view_function)
    def wrap(request, *args, **kwargs):
        if any(key in request.META for key in ['HTTP_AUTHORIZATION', 'HTTP_ACCESS_TOKEN', 'HTTP_X_AKTO_REMOVE_AUTH']):
            return view_function(request, *args, **kwargs)
        else:
            return HttpResponse('Unauthorized', status=401)
    return wrap