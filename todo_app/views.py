from django.shortcuts import redirect, render
from .models import TodoList
# Create your views here.
def index(request):
    todolist = TodoList.objects.all()
    if request.method == 'POST':
        result = TodoList(
            title = request.POST['title']
        )
        result.save()
        return redirect('/')
    return render(request, 'index.html', {'todolist' : todolist})


def delete_view(request, pk):
    todolist = TodoList.objects.get(id=pk)
    todolist.delete()
    return redirect('/')