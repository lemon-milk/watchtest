from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    allTodoItems = TodoItem.objects.all()
    return render(request,'todo.html',
        {'all_items': allTodoItems})

def addTodo(request):
    #create a new todo object
    #save
    #redirect to '/todo/'
    newItem = TodoItem(content = request.POST['content'])
    newItem.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    #delete todo item
    #save
    #redirect
    oldItem = TodoItem.objects.get(id=todo_id)
    oldItem.delete()
    return HttpResponseRedirect('/todo/')