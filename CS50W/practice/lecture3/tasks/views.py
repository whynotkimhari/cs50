from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

tasks = ['foo', 'bar', 'baz']
# Create your views here.
def index(request):
    if "task" not in request.session:
        request.session['task'] = []
    return render(request, 'tasks/index.html', {
        "tasks": request.session['task']
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['task'] += [task]
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/add.html', {
                "form": form
            })    
    return render(request, 'tasks/add.html', {
        "form": NewTaskForm()
    })

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "new task")
    priority = forms.IntegerField(label = "priority", min_value=1, max_value=10)