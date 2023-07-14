from django.shortcuts import render
import json

from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import SampleData


@api_view(['POST'])
def add_sample_data(request):
    url = request.data["url"]
    data = request.data["data"]
    try:
        if SampleData.objects.filter(url=url).exists():
            SampleData.objects.update(data=json.dumps(data))
        else:
            SampleData.objects.create(url=url, data=json.dumps(data))

        return HttpResponse(json.dumps(request.data), status=200)
    except Exception as e:
        return HttpResponse("Error Inserting Sample Data".format(e), status=500)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'TRACE', 'TRACK', 'TestMethod'])
def fetch_sample_data(request):

    url = request.path
    print(url)
    try:
        sample_data = SampleData.objects.get(url=url)
        print("sample_data_url")
        print(sample_data.url)
        sample_data = json.loads(sample_data.data)
        resp = sample_data["responsePayload"]
        status_code = sample_data["statusCode"]
        headers = sample_data["responseHeaders"]

        api_resp = HttpResponse(json.dumps(resp), status=status_code)

        for key, value in headers.items():
            api_resp[key] = value

        return api_resp
    except Exception as e:
        return HttpResponse("Error Executing Request".format(e), status=500)
