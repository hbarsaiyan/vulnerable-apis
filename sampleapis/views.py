import json

from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['GET'])
def echo(request):
    print("request")
    print(request)
    print("reqData")
    print(request.data)
    #response_data = {}
    #response_data['result'] = 'error'
    #response_data['message'] = 'Some error message'
    to_json = {
        "key1": "value1",
        "key2": "value2"
    }    
    return HttpResponse(json.dumps(request.data), status=200)

