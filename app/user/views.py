from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django import http
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSeriallizer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        name = data['name']
        email = data['email']

        send_mail(
            f'Welcome {name}',
            'Thank you for registeration',
            'test@email.com',
            [email]
        )
        serializer.save()


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSeriallizer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


def TestPageView(request):

    return render(request, "nucleus/components/stat_item.html", context={
        'value': '5269',
        'title': 'Units Sold',
        'subtitle': 'Avg. 351 per week',
        'label': '-12%',
    })
