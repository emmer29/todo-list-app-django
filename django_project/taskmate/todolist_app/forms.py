from django import forms
from todolist_app.models import TaskList

#create class
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']
        