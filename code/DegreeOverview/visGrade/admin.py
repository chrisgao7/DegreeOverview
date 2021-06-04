from django.contrib import admin
from .models import *
# Register your models here.


class GradeReportManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['student', 'assessment', 'Marks']
    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['student']
    # 添加过滤器
    list_filter = ['assessment']
    # 添加搜索框[模糊查询]
    search_fields = ['assessment']
    # 添加可在列表页编辑的字段 与list_display_links不能为同一个 互斥
    list_editable = ['Marks']


class Student_CourseManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['student', 'course', 'Semester']
    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['student']
    # 添加过滤器
    list_filter = ['student']
    # 添加搜索框[模糊查询]
    search_fields = ['student']
    # 添加可在列表页编辑的字段 与list_display_links不能为同一个 互斥
    list_editable = ['course']


admin.site.register(GradeReport, GradeReportManager)
admin.site.register(Student_Course, Student_CourseManager)
