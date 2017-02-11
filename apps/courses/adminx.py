# -*- coding: utf-8 -*-
__author__ = 'jesse'
__date__ = '2017/2/10 0:29 '

from .models import Course,Lesson,Video,CourseResource
import xadmin


class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','click_nums']
    search_fields = ['name','desc','detail','degree']
    list_filter = ['name','desc','detail','learn_times','students','fav_nums']


class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course__name','name']


class VideoAdmin(object):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson__name','name']


class CourseResourceAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course__name','name']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
