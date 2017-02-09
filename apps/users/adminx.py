# -*- coding: utf-8 -*-
__author__ = 'jesse'
__date__ = '2017/2/9 23:08 '

import xadmin
from .models import EmailVerifyRecord
from .models import UserProfile


class UserProfileAdmin(object):
    list_display = ['username', 'gender', 'address', 'mobile']
    search_fields = ['username', 'gender', 'address', 'mobile']
    list_filter = ['username', 'gender', 'address', 'mobile']


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)