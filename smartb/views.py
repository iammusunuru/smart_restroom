from django.shortcuts import render
from django.shortcuts import render_to_response
from smartb import db_layer
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render_to_response("index.html")


def loaddata(request):
    wash_id = request.GET.get("wash_id","")
    if wash_id:
        db = db_layer("iot_data")
        data = db.get_data({"tag":"real_time_data"})[0]
        print data
    return HttpResponse("sucess")

