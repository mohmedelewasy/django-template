from django.urls import path, include
from . import views
from . import api

app_name='job'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add_job', views.add_job, name = 'add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),
    path('api/list', api.job_list_api, name = 'job_list_api'),
    path('api/list/<str:slug>', api.job_detail_api, name = 'job_detail_api'),

    #class based view
    path('api/list_v2', api.JobListApi.as_view(), name = 'job_list_api_v2'),
]