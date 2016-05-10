from django.shortcuts import render
from django.shortcuts import render_to_response
from smartb.db_layer import db_layer
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from smartb import mqtt_thread

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


"sends what ever got from the ui"
#TODO washroom id support
@csrf_exempt
def send_sensor(request):
    di = {}
    try:
        for key, value in request.POST.items():
            di[key] = value
        mqtt_thread.send_message(str(di))
        return HttpResponse("success")
    except:
        return HttpResponse("failed")


def get_active_washroom(request):
    db = db_layer("iot_data")
    data = db.get_data({"tag":"real_time_data"})[0]
    return HttpResponse(data["data"]["restroom_id"])


@csrf_exempt
def noti_config(request):
    try:
        restroom_id = request.POST.get("restroom_id","")
        type = request.POST.get("type","")
        telno = request.POST.get("telno","")
        db = db_layer("noti")
        db.set_data({"restroom_id":restroom_id, "type":type, "telno": telno})
        return HttpResponse("success")
    except:
        return HttpResponse("failed")

@csrf_exempt
def voice(request):
    msg = request.POST.get("msg","")
    mqtt_thread.send_voice(msg)
    return HttpResponse("success")