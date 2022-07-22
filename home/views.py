import email
import imp
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import View
import datetime
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import login,logout

# Create your views here.
class Base(View):
    views = {}

class HomeView(Base):
    def get(self,request):
        self.views
        self.views['sliders'] = Slider.objects.all() # get all slider and show
        return render(request,'index.html',self.views) # --> for render