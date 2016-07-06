import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from welcome.serializers import UserSerializer, GroupSerializer


from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())

class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited
	"""
	queryset=User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset=Group.objects.all()
	serializer_class=GroupSerializer

