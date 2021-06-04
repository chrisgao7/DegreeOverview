from django.contrib import admin
from django.http.request import validate_host
from django.urls import path, include
from . import views

urlpatterns = [
    path('search/', views.Search, name='search'),

    # turn back to the main page based on different user type
    path('main/', views.TurnBackToMain, name='main_page'),

    # turn to different course info page based on different user type
    path('courseInfo/<int:id>/', views.TurnToCourseInfo, name='course_info'),
    path('cdCourseInfo/<int:id>/', views.cdCourseInfo, name='cd_course_info'),
    path('ncdCourseInfo/<int:id>/', views.ncdCourseInfo, name='ncd_course_info'),
    path('stuCourseInfo/<int:id>/', views.stuCourseInfo, name='stu_course_info'),

    # turn back to the search result
    path('searchHis/', views.TurnBackToSearchHis, name='search_his'),

    # the operation of edit course
    path('editcourse/<int:id>/', views.EditCourse, name='edit_course'),
    path('update_course/<int:id>/', views.UpdateCourse, name='update_course'),

    path('addcourse/', views.addCourse, name='add_course'),
    path('addciloassessment/<int:id>/', views.addCiloAssessment, name='add_ciloassessment'),
    path('finishCreate/<int:id>/', views.finishCreate, name='finish_create'),

    path('importCILO/<int:id>/', views.importCILO, name='importCILO'),
    path('importAssessment/<int:id>/', views.importAssessment, name='importAssessment'),
    # path('visualize', views.visualize, name='visualize'),

    path('editcilo/<int:id>/', views.EditCilo, name='edit_cilo'),
    path('turnfromeditcilo/<int:id>/', views.TurnFromEdit, name='edit_cilo'),
    path('deletecilo/<int:ciloid>/<int:courseid>/', views.DeleteCilo, name='deletecilo'),
    path('addcilo/<int:id>/', views.AddCILO, name='add_cilo'),

    path('editassessment/<int:id>/', views.EditAssessment, name='edit_assessment'),
    path('turnfromeditassessment/<int:id>/', views.TurnFromEdit, name='edit_assessment'),
    path('deleteassessment/<int:assessmentid>/<int:courseid>/', views.DeleteAssessment, name='deleteassessment'),
    path('addassessment/<int:id>/', views.AddAssessment, name='add_assessment'),

    path('visualize/', views.visualize, name='visualize')
]
