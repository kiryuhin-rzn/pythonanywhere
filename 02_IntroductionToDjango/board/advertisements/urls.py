from django.urls import path
from .import views


urlpatterns = [
    path("", views.advertisements_list, name='advertisements_list'),
    path('advertisements/', views.advertisements_detail, name='advertisements_list'),
    path('advertisements/data-scientist/', views.advertisements_data_scientist, name='advertisements_data_scientist'),
    path('advertisements/java-job/', views.advertisements_java_job, name='advertisements_java_job'),
    path('advertisements/python-job/', views.advertisements_python_job, name='advertisements_python_job'),
    path('advertisements/test-job/', views.advertisements_test_job, name='advertisements_test_job'),
    path('advertisements/web-job/', views.advertisements_web_job, name='advertisements_web_job'),
]