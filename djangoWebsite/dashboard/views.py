# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib import auth

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {})

