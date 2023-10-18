from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from rest_framework.response import Response
from usof_api.user.models import User
from .serializers import LoginSerializer
from usof_api.user.serializers import UserSerializer


@api_view(['POST'])
def register(request):

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        if request.data.get('is_staff'):
            return Response(
                "You can't create admin via this registration form.",
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            serializer.save()

        return redirect('users')

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginView(request):
    serialize = LoginSerializer(data=request.data)
    serialize.is_valid(raise_exception=True)
    user = serialize.validated_data['user']
    login(request, user)
    return redirect('users')


@api_view(['GET', 'POST'])
def logoutView(request):
    logout(request)
    return redirect('users')