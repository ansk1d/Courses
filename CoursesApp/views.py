
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *



def addcourse(request):
    if request.method == 'POST':
        courses= Course.objects.create(
            course_name = request.POST['course_name'],
            description = request.POST['description']
        )
        courses.save()
    return redirect("/")


def showcourse(request):
    shcourse = Course.objects.all()
    context ={
        'courses':shcourse
    }
    return render(request, 'index.html',context)

def delcourse(request,_id):
    course=Course.objects.get(id=_id)
    context={
        'delcourse':course
    }
    return render(request, 'destroy.html',context)

def delete(request,_id):
    course=Course.objects.get(id=_id)
    course.delete()
    return redirect('/')