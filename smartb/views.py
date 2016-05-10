from django.shortcuts import render
from django.shortcuts import render_to_response
from smartb.db_layer import db_layer
from django.http import HttpResponse
import json

# Create your views here.

def home(request):
    return render_to_response("home.html")

def loaddata(request):
    restroom_id = request.GET.get("restroom_id","")
    if restroom_id:
        db = db_layer("iot_data")
        data = db.get_data({"tag":"real_time_data"})[0]
        data = data["data"]
        if str(data.get("restroom_id")) == restroom_id:
            data=json.dumps(data)
            print data
            return HttpResponse(data)
    return HttpResponse("")


def load_html(request):
    page_name = request.GET.get("name","")
    return render_to_response(page_name+".html")