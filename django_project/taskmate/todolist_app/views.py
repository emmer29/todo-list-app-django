from django.shortcuts import render
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm

# Create your views here.
def todolist(request):
    all_tasks = TaskList.objects.all
    
    return render(request,'todolist.html', {'all_tasks':all_tasks})


def contact (request):
    context = {
        'contact_text':"Welcome contact page.",
    }
    return render(request,'contact.html', context)


def about (request):
    context = {
        'about_text':"Welcome about page.",
    }
    return render(request,'about.html', context)


