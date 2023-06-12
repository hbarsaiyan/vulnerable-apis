import json

from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def echo(request):
    return HttpResponse(json.dumps(request.data), status=200)
