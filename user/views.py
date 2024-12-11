from django.shortcuts import render
from django.views import View
from user import models
from django.http import JsonResponse

# Create your views here.
class userIndex(View):
    def get(self, reuqest):
        ID = reuqest.GET['id']
        obj = models.User.objects.get(id=ID)

        return JsonResponse(obj)