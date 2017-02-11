# -*- coding: utf-8 -*-
__author__ = 'jesse'
__date__ = '2017/2/9 23:08 '


import xadmin
from xadmin import views
from .models import EmailVerifyRecord
from .models import UserProfile
from django.utils.datastructures import OrderedDict


class BaseSetting(object):
    enable_themes = True
    use_bootswatch =True


class GlobalSettings(object):
    site_title = '慕学在线学习网'
    site_footer = '慕学在线'
    menu_style = 'accordion'

class UserProfileAdmin(object):
    list_display = ['username', 'gender', 'address', 'mobile']
    search_fields = ['username', 'gender', 'address', 'mobile']
    list_filter = ['username', 'gender', 'address', 'mobile']


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title','image','index','add_time']
    search_fields = ['title','index']
    list_filter = ['title','index']


xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)