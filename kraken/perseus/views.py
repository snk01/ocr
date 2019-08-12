from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


from PIL import Image
import pytesseract
import requests
import random
import string
import os
import json

def index(request):
    return HttpResponse("Hello, world. You're at the perseus index.")

@csrf_exempt
def ocr(request):
    if(request.method != 'POST'):
        return HttpResponseNotAllowed("Method Invalid")
    json_data = json.loads(request.body)
    url = json_data['url']
    image_response = requests.get(url)
    content_type = image_response.headers['Content-Type']
    extension = ("jpg" in content_type and "jpg") or ("jpeg" in content_type and  "jpeg") or ("png" in content_type and "png") or "unknown"
    if(extension == 'unknown'):
        return HttpResponseBadRequest('Unknown File Type')    
    filename = 'test'+ '.' +extension
    with open(filename,"wb") as f:
        f.write(image_response.content)
    return HttpResponse(pytesseract.image_to_string(Image.open(filename)))

