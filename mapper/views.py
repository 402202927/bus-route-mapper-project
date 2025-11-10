import os
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .models import BusStop, BusRoute, Trip
from .serializers import BusStopSerializer, BusRouteSerializer, TripSerializer

class BusStopViewSet(viewsets.ModelViewSet):
    queryset = BusStop.objects.all()
    serializer_class = BusStopSerializer

class BusRouteViewSet(viewsets.ModelViewSet):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

def index(request):
    return render(request, "mapper/index.html", context={})

APP_DIR = os.path.dirname(__file__)
CONFIG_JSON_PATH = os.path.join(APP_DIR, "config_data.json")

def load_config():
    if not os.path.exists(CONFIG_JSON_PATH):
        return {}
    try:
        with open(CONFIG_JSON_PATH, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return {}

def save_config(data):
    if not isinstance(data, dict):
        raise ValueError("Config data must be a JSON object.")
    os.makedirs(os.path.dirname(CONFIG_JSON_PATH), exist_ok=True)
    with open(CONFIG_JSON_PATH, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=4, ensure_ascii=False)

def configure_page(request):
    return render(request, "mapper/configure.html")

@method_decorator(csrf_exempt, name="dispatch")
def api_config(request):
    if request.method == "GET":
        data = load_config()
        return JsonResponse(data, safe=False)
    if request.method == "POST":
        try:
            payload = json.loads(request.body.decode("utf-8"))
        except Exception:
            return HttpResponseBadRequest("Invalid JSON payload.")
        try:
            save_config(payload)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
        return JsonResponse({"status": "ok", "message": "Configuration saved successfully."})
    return JsonResponse({"error": "Method not allowed."}, status=405)
