import json

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Task


# Create your views here.

def index(request):
    print("Index Called", request, request.method)
    if request.method == 'GET':
        # return HttpResponse("This is working")
        return render(request, 'index.html')


# To create a task in DB
@csrf_exempt
@require_http_methods(["GET", "POST", "DELETE"])
def create_task(request):
    # TODO: Later make it dynamic based on session
    user = 1
    if request.method == 'GET':
        tasks = Task.objects.filter(user_id=1).values()
        print("fetched", tasks)
        return JsonResponse(list(tasks), safe=False)

    if request.method == 'POST':
        print("Creating Task ")
        print("Request Method: {}, \n request: {}".format(request.method, request))
        print("Body: {}".format(request.body))
        print("task: {}".format(request.POST.get("task")))
        body = request.body
        task = json.loads(body)
        title = task.get('title')
        duedate = task.get('duedate')
        duedate = duedate.replace('/', '-')
        category_id = task.get("category")

        print("Task from JSON:", task)

        # ORM, create Task object and save it to db
        taskobj = Task(task_text=title, user_id=1, due_date=duedate)
        taskobj.save()  # Convert object call into Query and will send to db

        return JsonResponse({'msg': 'Task Saved'})


@csrf_exempt
@require_http_methods(['POST'])
def task_status(request):
    data = json.loads(request.body)
    task_id = data['id']
    status = data['finstatus']
    Task.objects.filter(id=task_id).update(isfin=status)
    return JsonResponse({'msg': 'Updated'})