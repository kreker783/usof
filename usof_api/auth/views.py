from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import redirect
from rest_framework.response import Response
from .serializers import LoginSerializer
from usof_api.user.serializers import UserSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.core.mail import EmailMessage


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
            user = serializer.save()

            current_site = get_current_site(request)
            mail_subject = "Account activation"
            message = render_to_string(
                'account_activation_email.html', {
                    'user': user,
                    'site_url': "127.0.0.1:8000",
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': generate_token.make_token(user)
                }
            )
            user_email = serializer.validated_data['email']
            email = EmailMessage(
                mail_subject, message, to=[user_email]
            )

            email.send()

        return redirect('users')

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response("Your email is confirmed. Now you can login your account")
    else:
        return Response("Activation link is invalid")


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