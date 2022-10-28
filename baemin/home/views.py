from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop,Menu, Order,Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

def index(request):
        return render(request, 'home/index.html',{})
