from django.contrib import admin
from .models import Account, Student, CourseDesigner, NonCourseDesigner
# Register your models here.


class AccountManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['username', 'password']
    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['username']
    # 添加过滤器
    list_filter = ['username']
    # 添加搜索框[模糊查询]
    search_fields = ['username']
    # 添加可在列表页编辑的字段 与list_display_links不能为同一个 互斥
    list_editable = ['password']


class StudentManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['fullname', 'programme', 'enrollmentYear']
    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['fullname']
    # 添加过滤器
    list_filter = ['programme']
    # 添加搜索框[模糊查询]
    search_fields = ['fullname']
    # 添加可在列表页编辑的字段 与list_display_links不能为同一个 互斥
    list_editable = ['programme']


class CourseDesignerManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['fullname', 'programme']
    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['fullname']
    # 添加过滤器
    list_filter = ['programme']
    # 添加搜索框[模糊查询]
    search_fields = ['fullname']
    # 添加可在列表页编辑的字段 与list_display_links不能为同一个 互斥
    list_editable = ['programme']


class NonCourseDesignerManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['fullname', 'programme']
    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['fullname']
    # 添加过滤器
    list_filter = ['programme']
    # 添加搜索框[模糊查询]
    search_fields = ['fullname']
    # 添加可在列表页编辑的字段 与list_display_links不能为同一个 互斥
    list_editable = ['programme']


admin.site.register(Account, AccountManager)
admin.site.register(Student, StudentManager)
admin.site.register(CourseDesigner, CourseDesignerManager)
admin.site.register(NonCourseDesigner, NonCourseDesignerManager)
