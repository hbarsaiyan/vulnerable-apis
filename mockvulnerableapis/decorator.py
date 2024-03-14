from functools import wraps
from django.http import HttpResponse

def authentication_token_required(view_function):
    @wraps(view_function)
    def wrap(request, *args, **kwargs):
        # exempt these paths from auth check
        bypass_paths = ['/login']
        if any(path in request.path for path in bypass_paths):
            return view_function(request, *args, **kwargs)
        if 'HTTP_ACCESS_TOKEN' not in request.META:
            return HttpResponse('Unauthorized', status=401)
        return view_function(request, *args, **kwargs)
    return wrap