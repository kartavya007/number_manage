from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import requests
from . import fetch_n
def get(request):
    if request.method == 'GET':
        url = request.GET.get('url')
        return JsonResponse(fetch_n.fetch(url))
    return HttpResponse("<form method='get'> <input type='text' name='url'> </form>")