import json
from django.http import JsonResponse
from django.shortcuts import render

from .models import Goal

# Create your views here.

def form_submit(requst):
    if requst.method == 'POST':
        usergoal = requst.POST.get('goal')
        goal = Goal(goal=usergoal)
        goal.save()
        message = 'Goal Submitted'
        return JsonResponse({'message': message})
    return render(requst, 'app/form_submit.html')

def get_data(request):
    goals = Goal.objects.all()
    return JsonResponse({'goals': list(goals.values())})

def delete_goal(request, id):
    goal = Goal.objects.get(id=id)
    goal.delete()
    return JsonResponse({'message': 'Goal Deleted'})