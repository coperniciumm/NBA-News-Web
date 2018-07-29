from django.shortcuts import render

# Create your views here.
from news.models import NewsPost
from news.serializer import NewsPostSerializer
from rest_framework import viewsets
#from rest_framework.response import Response
#from rest_framework import status
from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser

@api_view(['GET'])
def _list(request):
    """
    List all code news.
    """
    if request.method == 'GET':
        news = NewsPost.objects.all()
        serializer = NewsPostSerializer(news, many=True)
        return JsonResponse(serializer.data, safe=False)

def index(request):
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')

