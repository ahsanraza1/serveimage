from django.shortcuts import render
from .models import Account
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# Create your views here.




@api_view( ['GET'])
@permission_classes( [IsAuthenticated])
def show_users ( request ):
    if request.method == 'GET':
        if request.user.is_admin:
            users = Account.objects.all()
            serialized_users = UserSerializers( users, many=True)
            return JsonResponse( {'users':serialized_users.data}, safe=False)
        else:
            return Response( { 'error': 'Access Denied' }, status = status.HTTP_403_FORBIDDEN)

@api_view( ['POST'])
def register ( request ):
    # if request.method == 'GET':
    #     if request.user.is_admin:
    #         users = Account.objects.all()
    #         serialized_users = UserSerializers( users, many=True)
    #         return JsonResponse( {'users':serialized_users.data}, safe=False)
    #     else:
    #         return Response( { 'error': 'Access Denied' }, status = status.HTTP_403_FORBIDDEN)

    if request.method == 'POST':
        deserializer = UserSerializers( data = request.data )
        if deserializer.is_valid():
            deserializer.save()
            return Response( deserializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response( { 'error': deserializer.errors }, status = status.HTTP_205_RESET_CONTENT)