from django.shortcuts import render

# Create your views here.
from news.models import NewsPost
from news.serializer import NewsPostSerializer
from rest_framework import viewsets
#from rest_framework.response import Response
#from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser


class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer

'''
@csrf_exempt
def _list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = NewsPost.objects.all()
        serializer = NewsPostSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
'''

'''
def index(request):
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')
'''
