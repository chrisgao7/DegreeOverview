from django.contrib import admin
from .models import Course, CILO, Assessment
# Register your models here.


class CourseManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['CourseID', 'CourseName', 'Code', 'Type', 'Program']
    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['CourseName']
    # 添加过滤器
    list_filter = ['CourseName']
    # 添加搜索框[模糊查询]
    search_fields = ['CourseName']
    # 添加可在列表页编辑的字段 与list_display_links不能为同一个 互斥
    list_editable = ['Code', 'Type', 'Program']


class CILOManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['CILOID', 'CILOName',
                    'Description', 'PreCILO', 'AcademicYear']
    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['CILOName']
    # 添加过滤器
    list_filter = ['CILOName']
    # 添加搜索框[模糊查询]
    search_fields = ['CILOName']


class AssessmentManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['AssessmentID', 'MethodName',
                    'Percentage', 'CILOIDs', 'AcademicYear']
    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['AssessmentID']
    # 添加过滤器
    list_filter = ['MethodName']
    # 添加搜索框[模糊查询]
    search_fields = ['MethodName']
    # 添加可在列表页编辑的字段 与list_display_links不能为同一个 互斥
    list_editable = ['Percentage']


admin.site.register(Course, CourseManager)
admin.site.register(CILO, CILOManager)
admin.site.register(Assessment, AssessmentManager)
