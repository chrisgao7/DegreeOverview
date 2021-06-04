from django.contrib import admin
from django.http.request import validate_host
from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', include('user.urls')),
    path('course/', include('course.urls')),

    path('showPerformance', views.showPerformance, name='showPerformance'),
    path('showPerformance/performance', views.performance, name='performance'),
    path('analysis', views.analysis, name='analysis'),
    path('analysis/analysisResult',
         views.analysisResult, name='analysisResult'),


    path('back', views.back, name='back')
]
