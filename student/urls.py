from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('room/<str:pk>/', views.room, name="room"),
    path('student_display/',views.student_display, name='student_display'),
]
