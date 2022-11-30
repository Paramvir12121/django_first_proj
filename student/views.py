from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
rooms=[
    {'id':1, 'name':"Project Discription", 'url_link':'proj.html'},
    {'id':2, 'name':"Add Students",'url_link':'http://127.0.0.1:8000/admin/student/student/add/'},
    {'id':3, 'name':"Display Students",'url_link':'student_display'}
]


def home(request):
    context={'rooms':rooms}
    return render(request, 'student/home.html',context)

def student_display(request):
    students = Student.objects.all()
    return render(request, 'student/student_display.html',students)


def room(request,pk):
    room = None
    for i in rooms: 
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    
    return render(request, 'student/room.html',context)