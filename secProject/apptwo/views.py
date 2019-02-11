from django.shortcuts import render
from django.http import HttpResponse
from apptwo.models import Topic,web,Record


# Create your views here.
def index(req):
    web_list = Record.objects.order_by('date')
    date_dict = {'access':web_list}
    # return HttpResponse("My second App")
    return render(req,'sec.html',context=date_dict)