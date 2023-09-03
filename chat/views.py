from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from user.models import User
from rest_framework.decorators import api_view
from django.shortcuts import render
import json

@api_view(['GET'])
def getAllMessageByReceiverId(request, receiver_id):
    messages = User.objects.filter(receiver_id=receiver_id).order_by('id')[0:1]
    serialized_data = serialize("json", messages)
    return JsonResponse(json.loads(serialized_data), safe=False)

@api_view(['POST'])
def sendMessage(request):
    data = json.loads(request.body.decode('utf-8'))
    new_message = User.objects.create(receiver_id=data['receiver_id'], sender_id=data['sender_id'], message=data['message'])
    # return HttpResponse(new_message)
    return JsonResponse(new_message, safe=False)

@api_view(['GET'])
def showChat(request):
    return render(request, 'chat.html')