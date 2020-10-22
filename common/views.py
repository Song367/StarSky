from django.shortcuts import render
from django.http import JsonResponse
from common.models import planet
def index(request):

    return render(request,'index.html')

def earth(request):
    return  render(request, '地球.html')

#八大行星
def planets(request):
    return render(request,'太阳系.html')

#发送数据
def planetdata(request):
    if request.method=='GET':
        data=planet.objects.values()
        data=list(data)

        return JsonResponse({'data':data})