# -*- coding: utf-8 -*-
__author__ = 'jesse'
__date__ = '2017/2/11 20:42 '
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True) #设置为必填字段, 可以设置最大长度，最小长度
    password = forms.CharField(required=True,min_length=6)