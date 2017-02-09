# -*- coding: utf-8 -*-
__author__ = 'jesse'
__date__ = '2017/2/10 0:29 '

from .models import Course,Lesson,Video,CourseResource
import xadmin

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','click_nums']
    search_fields = ['name','desc','detail','degree']
    list_filter = ['name','desc','detail','learn_times','students','fav_nums']


xadmin.site.register(Course,CourseAdmin)