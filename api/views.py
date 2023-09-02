from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    return JsonResponse({ "message": "This is root api end point for chat" })