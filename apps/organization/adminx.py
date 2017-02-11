# -*- coding: utf-8 -*-
__author__ = 'jesse'
__date__ = '2017/2/10 21:33 '

from .models import CityDict,Teacher,CourseOrg
import xadmin


class CityDictAdmin(object):
    list_display = ['name','desc','add_time']
    search_fields = ['name','desc']
    list_filter = ['name','desc']


class CourseOrgAdmin(object):

    list_display = ['name', 'desc', 'click_nums','fav_nums','address','city', 'add_time']
    search_fields = ['name', 'desc','address','city', 'add_time']
    list_filter = ['name', 'desc','city__name']


class TeacherAdmin(object):
    list_display = ['name','org','work_years','work_company','work_position','click_nums','fav_nums','add_time']
    search_fields = ['name','org','work_years','work_company','work_position']
    list_filter = ['name','org__name']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)