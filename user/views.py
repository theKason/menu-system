from django.shortcuts import render
from django.views import View
from models import User
from django.http import JsonResponse

# Create your views here.
class userIndex(View):
    def get(self, reuqest):
        ID = reuqest.GET['id']
        obj = User.objects.get(id=ID)

        return JsonResponse(obj)