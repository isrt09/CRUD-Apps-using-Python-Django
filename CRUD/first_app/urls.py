from django.urls import path
from. import views

app_name = 'first_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('student_form/', views.student_form, name='student_form'),
]
