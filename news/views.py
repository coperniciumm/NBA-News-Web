from django.shortcuts import render

# Create your views here.
from news.models import NewsPost
from news.serializer import NewsPostSerializer
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

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

