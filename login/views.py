
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


from django.http import HttpResponse

from login.models import Author


import json

def index(request):
    # list = ['jackwu', 'xxxx', 'wawajiao']
    # person=author(name="jackwu",email="1683358846@qq.com")  
      p=Author.objects.all()
      return render(request, u"index.html", {'list': p})


def getuser(request):
    '''注册成功'''
    name=request.GET['name']
    email=request.GET['email']
    print (name,email)
    
    person=Author(name=name,email=email)
    person.save()

    p=Author.objects.all()
    return render(request, u"index.html", {'list': p})


def getjson(request):
    info={'name':'jackwu','email':'12121@4454'}
    s=json.dumps(info)
    return s