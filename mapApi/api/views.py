from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def mapimage(request, param1, param2, param3):
    zoom = str(param1)
    lat = str(param2)
    lng = str(param3)
    mapurl = 'http://180.179.210.246/osm_tiles/'+zoom+'/'+lat+'/'+lng+'.png' 
    r = requests.get(mapurl)
    return HttpResponse(r.content, content_type="image/png")


