from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import views
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from rest_framework.response import Response
from .models import Post, Category, Comment, Like, User
from .serializers import UserSerializer, LoginSerializer


@api_view(['POST'])
def register(request):

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        if request.data.get('is_staff'):
            # permission = [permissions.IsAdminUser]
            user = User.objects.create_superuser(request.data.get('login'),
                                                 request.data.get('password'),
                                                 **serializer.validated_data)
        else:
            serializer.save()

        return redirect('/usof/api/users/')

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):

    def post(self, request):
        # serializer = LoginSerializer(data=request.data,
        #                              context={'request': request})
        # if serializer.is_valid():
        #     user = serializer.validated_data['user']
        #     login(request, user)
        #     return Response(None, status=status.HTTP_202_ACCEPTED)
        serialize = LoginSerializer(data=request.data)

        if serialize.is_valid():
            user = authenticate(login=request.data.get('login'),
                                email=request.data.get('email'),
                                password=request.data.get('password'))

            if user is not None:
                login(request, user)
                return redirect('/usof/api/users/')
            else:
                return Response('User does not exist', status=status.HTTP_400_BAD_REQUEST)

        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
