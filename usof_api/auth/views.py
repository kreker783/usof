from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import login, get_user_model, authenticate
from django.shortcuts import redirect
from rest_framework.response import Response
from .serializers import LoginSerializer
from usof_api.user.serializers import UserSerializer
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.urls import reverse


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
            user.is_active = False
            user.set_password(request.data.get('password'))

            try:
                send_html_email(user)
            except:
                user.delete()
                return Response("Cannot send email, user isn't created", status=status.HTTP_400_BAD_REQUEST)

            user.save()

        return redirect('users')

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_html_email(user):
    mail_subject = "Account activation"

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = generate_token.make_token(user)
    site_url = "127.0.0.1:8000"
    activation_link = "http://{}{}".format(site_url, reverse('activate', kwargs={'uidb64': uid, 'token': token}))
    message = f"Hi, {user.login}. Please click on the link to confirm your registration:"
    html_message = render_to_string('account_activation_email.html', {'activation_link': activation_link})

    send_mail(
        mail_subject, message=message,
        recipient_list=[user.email], html_message=html_message,
        from_email="webmaster@localhost"
    )


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
@csrf_exempt
def loginView(request):
    serialize = LoginSerializer(data=request.data)
    serialize.is_valid(raise_exception=True)
    validated = serialize.validated_data

    user = authenticate(
        username=validated['login'],
        password=validated['password']
    )

    if user is not None:
        login(request, user)
        request.session['user'] = user.login
        return redirect('current_user')

    return Response(f"Your credentials are wrong!", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def logoutView(request):
    try:
        del request.session['user']
    except Exception:
        return redirect('current_user')
    return redirect('current_user')


@api_view(['GET'])
def get_current_user(request):
    try:
        user = request.session['user']
    except:
        user = "You aren't logged in"
    return Response(f"Current logged in user is: {user}")


@api_view(['POST'])
def password_reset(request):
    username = request.data.get('login')
    User = get_user_model()

    try:
        user = User.objects.get(login=username)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        return Response("User doesn't exist!", status=status.HTTP_400_BAD_REQUEST)

    mail_subject = "Password Reset"
    message = render_to_string(
        'password_reset_email.html', {
            'user': user,
            'site_url': "127.0.0.1:8000",
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        }
    )
    user_email = user.email
    email = EmailMessage(
        mail_subject, message, to=[user_email]
    )

    email.send()

    return redirect('users')


@api_view(['POST'])
def set_password(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and generate_token.check_token(user, token):
        user.set_password(request.data.get('new_password'))
        user.save()
        return Response("Now you have a new password!")
    else:
        return Response("Link is invalid")
