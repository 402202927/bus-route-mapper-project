# Bus Route Mapper Project

A complete academic prototype for interactive bus route mapping using Django 5.2, Leaflet 0.32.0, and Python 3.13.9.  
This project allows visualization of bus stops, routes, and timetables for Golden Arrow bus services.

---

## Contents

1. [Folder Structure](#folder-structure)  
2. [File Contents](#file-contents)  
   - [Root Files](#root-files)  
   - [Config Folder](#config-folder)  
   - [Mapper App](#mapper-app)  
   - [Docs Folder](#docs-folder)  
3. [User Manual](#user-manual)  
   - [INTRODUCTION](#introduction)  
   - [USER](#user)  
   - [SETUP](#setup)  
   - [TROUBLESHOOT](#troubleshoot)  
4. [Index](#index)

---

## Folder Structure
```
bus-route-mapper-project/
│
├── config/
│     ├── __init__.py
│     ├── settings.py
│     ├── urls.py
│     ├── wsgi.py
│     └── asgi.py
│
├── mapper/
│    ├── __init__.py
│    ├── admin.py
│    ├── apps.py
│    ├── models.py
│    ├── serializers.py
│    ├── views.py
│    ├── urls.py
│    ├── tests.py
│    ├── config_data.json
│    ├── templates/
│    │    └── mapper/
│    │          ├── base.html
│    │          ├── index.html
│    │          └── configure.html
│    └── static/
│           └── mapper/
│                ├── css/
│                │    └── style.css
│                ├── js/
│                │    └── map.js
│                └── img/
│                      └── icons/
│                            └── bus-stop.png
│
├── data/
│    ├── raw/
│    ├── processed/
│    └── imports.log
│
├── docs/
│    └── PresentationSlides.pptx
│
├── config_options.py
├── apply_config.py
├── manage.py
├── requirements.txt
├── .env.example
├── README_FULL.md
└── .gitignore
```

---

## File Contents

### Root Files

<details>
<summary>README_FULL.md (this file)</summary>
   
```
# (This file — read-only)
Contains project documentation, file structure, user manual, and instructions.
```

</details>
<details>
<summary>requirements.txt</summary>
   
```
# Python 3.13.9
Django==5.2
django-leaflet==0.32.0
djangorestframework==3.20.0
```

</details>
<details>
<summary>.gitignore</summary>
   
```
__pycache__/
*.pyc
*.pyo
*.pyd
.env
*.sqlite3
*.log
/media/
staticfiles/
```

</details>
<details> 
<summary>.env.example</summary>
   
```
DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

</details>
<details>
<summary>manage.py</summary>
   
```
#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and in your PYTHONPATH."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
```

</details>
<details>
<summary>config_options.py</summary>

```
# Project-wide default configuration
PROJECT_NAME = "Bus Route Mapper"
AUTHOR = "Grant Graham Cloete"
DEBUG = True
DEFAULT_TIMEZONE = "Africa/Johannesburg"
DEFAULT_MAP_CENTER = [-33.9249, 18.4241]
DEFAULT_MAP_ZOOM = 12
MAP_TILE_PROVIDER = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
DATA_RAW_PATH = "data/raw"
DATA_PROCESSED_PATH = "data/processed"
OSM_GEOJSON_FILENAME = "osm_bus_stops.geojson"
TIMETABLE_DIR = "golden_arrow_timetables"
IMPORT_LOG_FILE = "data/imports.log"
VERBOSE_LOGGING = True
```

</details>
<details>
<summary>apply_config.py</summary>

```
#!/usr/bin/env python3
"""
apply_config.py
────────────────
Synchronizes the project based on config_options.py
"""

import argparse
from config_options import PROJECT_NAME

def main():
    parser = argparse.ArgumentParser(description="Apply project configuration.")
    parser.add_argument("--skip-osm", action="store_true")
    parser.add_argument("--skip-timetables", action="store_true")
    args = parser.parse_args()

    print(f"Applying configuration for {PROJECT_NAME}")

    if not args.skip_osm:
        print("Importing OSM data... (simulate)")
    if not args.skip_timetables:
        print("Importing timetables... (simulate)")

    print("Configuration applied successfully.")

if __name__ == "__main__":
    main()

```
</details>


### Config Folder

<details>
<summary>config/__init__.py</summary>

```
# Empty init for Django config package
```

</details>
<details>
<summary>config/settings.py</summary>

```
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'replace-this-with-env-var'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mapper',
    'rest_framework',
    'leaflet',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'mapper' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]},
    }
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'mapper' / 'static']
```

</details>
<details>
<summary>config/urls.py</summary>

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mapper.urls')),
]
```

</details>
<details>
<summary>config/wsgi.py</summary>

```
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
```

</details>
<details>
<summary>config/asgi.py</summary>

```
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
```

</details>


### Mapper App

<details>
<summary>mapper/config_data.json</summary>

```
{
    "PROJECT_NAME": "Bus Route Mapper",
    "AUTHOR": "Grant Graham Cloete",
    "DEBUG": true,
    "DEFAULT_TIMEZONE": "Africa/Johannesburg",
    "DEFAULT_MAP_CENTER": [-33.9249, 18.4241],
    "DEFAULT_MAP_ZOOM": 12,
    "MAP_TILE_PROVIDER": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    "DATA_RAW_PATH": "data/raw",
    "DATA_PROCESSED_PATH": "data/processed",
    "OSM_GEOJSON_FILENAME": "osm_bus_stops.geojson",
    "TIMETABLE_DIR": "golden_arrow_timetables",
    "IMPORT_LOG_FILE": "data/imports.log",
    "VERBOSE_LOGGING": true
}
```
</details>
<details>
<summary>mapper/admin.py</summary>

```
from django.contrib import admin
from .models import BusStop, BusRoute, Trip

@admin.register(BusStop)
class BusStopAdmin(admin.ModelAdmin):
    list_display = ('stop_id', 'name', 'latitude', 'longitude')
    search_fields = ('name', 'stop_id')

@admin.register(BusRoute)
class BusRouteAdmin(admin.ModelAdmin):
    list_display = ('route_id', 'name')
    search_fields = ('name', 'route_id')
    filter_horizontal = ('stops',)

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_id', 'route', 'departure_time', 'arrival_time')
    list_filter = ('route',)

```

</details>
<details>
<summary>mapper/apps.py</summary>

```
from django.apps import AppConfig

class MapperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mapper'
    verbose_name = "Bus Route Mapper"

```

</details>
<details> 
<summary>mapper/views.py</summary>

```
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
```
</details>
<details>
<summary>mapper/urls.py</summary>

```
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'busstops', views.BusStopViewSet)
router.register(r'busroutes', views.BusRouteViewSet)
router.register(r'trips', views.TripViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('admin/configure.html', views.configure_page, name='configure_page'),
    path('api/config/', views.api_config, name='api_config'),
]
```
</details>
<details>
<summary>mapper/templates/mapper/configure.html</summary>

```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Configure - Bus Route Mapper</title>
<style>
body{font-family:Arial,Helvetica,sans-serif;margin:24px}
label{display:block;margin-top:10px;font-weight:600}
input,textarea,select{width:100%;padding:8px;box-sizing:border-box;margin-top:6px}
textarea{min-height:110px;font-family:monospace}
.actions{margin-top:16px}
button{padding:10px 14px}
.msg{margin-top:8px;color:green}
.error{margin-top:8px;color:red}
</style>
</head>
<body>
<h1>Project Configuration</h1>
<p>Edit project configuration. Saved to mapper/config_data.json</p>

<form id="cfg-form">
<label>Raw JSON
<textarea id="rawjson"></textarea>
</label>
<div class="actions">
<button id="btn-save" type="submit">Save Configuration</button>
<button id="btn-refresh" type="button">Reload</button>
</div>
<div id="status" class="msg"></div>
<div id="error" class="error"></div>
</form>

<script>
async function loadConfig(){
document.getElementById('status').textContent='Loading...';
document.getElementById('error').textContent='';
try{
const resp=await fetch('/api/config/');
const data=await resp.json();
document.getElementById('rawjson').value=JSON.stringify(data,null,4);
document.getElementById('status').textContent='Configuration loaded.';
}catch(err){
document.getElementById('error').textContent=err.toString();
document.getElementById('status').textContent='';
}}
async function saveConfig(e){
e.preventDefault();
document.getElementById('status').textContent='Saving...';
document.getElementById('error').textContent='';
try{
const parsed=JSON.parse(document.getElementById('rawjson').value);
const resp=await fetch('/api/config/',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(parsed)});
const result=await resp.json();
if(!resp.ok) throw new Error(result.message||'Save failed');
document.getElementById('status').textContent=result.message||'Saved successfully.';
}catch(err){document.getElementById('error').textContent=err.toString();document.getElementById('status').textContent='';}}
document.getElementById('cfg-form').addEventListener('submit',saveConfig);
document.getElementById('btn-refresh').addEventListener('click',loadConfig);
loadConfig();
</script>
</body>
</html>
```

</details>
<details>
<summary>mapper/static/mapper/css/style.css</summary>

```
body { font-family: Arial, Helvetica, sans-serif; }
#map { height: 600px; width: 100%; }
```

</details>
<details>
<summary>mapper/static/mapper/js/map.js</summary>

```
var map = L.map('map').setView([-33.9249, 18.4241], 12);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);
```

</details>
<details>
<summary>mapper/models.py</summary>

```
from django.db import models

class BusStop(models.Model):
    stop_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class BusRoute(models.Model):
    route_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    stops = models.ManyToManyField(BusStop, related_name='routes')

    def __str__(self):
        return self.name

class Trip(models.Model):
    trip_id = models.CharField(max_length=50, unique=True)
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE, related_name='trips')
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    def __str__(self):
        return f"{self.route.name} - {self.trip_id}"

```
</details>
<details>
<summary>mapper/serializers.py</summary>

```
from rest_framework import serializers
from .models import BusStop, BusRoute, Trip

class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        fields = '__all__'

class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusRoute
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

```
</details>
<details>
<summary>mapper/templates/mapper/base.html</summary>

```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{% block title %}Bus Route Mapper{% endblock %}</title>
<link rel="stylesheet" href="{% static 'mapper/css/style.css' %}">
</head>
<body>
<header>
<h1>{% block header %}Bus Route Mapper{% endblock %}</h1>
</header>
<main>{% block content %}{% endblock %}</main>
<footer>{% block footer %}© Grant Graham Cloete{% endblock %}</footer>
</body>
</html>

```
</details>
<details>
<summary>mapper/templates/mapper/index.html</summary>

```
{% extends "mapper/base.html" %}

{% block title %}Bus Map{% endblock %}
{% block content %}
<div id="map" style="width:100%;height:600px;"></div>
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script src="{% static 'mapper/js/map.js' %}"></script>
{% endblock %}

```
</details>

### Docs Folder

<details>
<summary>docs/PresentationSlides.pptx</summary>

```
Binary PowerPoint file (presentation for stakeholders):
- Explains project purpose, architecture, and usage
- Screenshots of bus map interface
- Example workflows for end users
- Maintainer overview for setup and configuration
```
</details>

---

## User Manual


### INTRODUCTION

The Bus Route Mapper Project is a Django web application that visualizes bus stops, routes, and timetable information for Golden Arrow buses.
It is an academic prototype, suitable for demonstrating data visualization and geospatial analysis.


### USER

**Using the mapper as a user:**

1. Navigate to the web app index page (/) after starting the Django server:
   
   ```
   python manage.py runserver
   ```
   Open: http://127.0.0.1:8000/

2. View the map:

   - Bus stops are shown as icons.
   - Click a stop to see its name, routes served, and next trips.

3. Filter or search:

   - Use any built-in filtering or search fields to locate stops or routes.

4. Interaction:

   - Pan, zoom, or click icons to explore route relationships.
   - Leaflet allows standard map gestures.

Note: End users do not edit configurations; they only interact with the map.
   

### SETUP

**Maintainer configuration instructions:**

1. Environment setup:

   - Python 3.13.9
   - Install dependencies:

   ```
   pip install -r requirements.txt
   ```   

2. Configuration:

   - Use /admin/configure.html to update config_data.json.
   - apply_config.py and config_options.py can be updated manually or via scripts; web UI is independent.

3. Common configuration errors:

   - Incorrect JSON syntax in config_data.json → use web UI or JSON validator.
   - Invalid paths for OSM or timetable data → verify DATA_RAW_PATH and TIMETABLE_DIR.\
   - Missing Leaflet tiles → check MAP_TILE_PROVIDER URL.

4. Database:

   ```
   python manage.py migrate
   ```

5. Starting server:

   ```
   python manage.py runserver
   ```

### TROUBLESHOOT

**Common issues & fixes:**

1. Server won’t start
   
   - Check DEBUG=True and Python/Django versions.
   - Verify dependencies installed from requirements.txt.

2. Map not loading tiles

   - Check internet access.
   - Ensure MAP_TILE_PROVIDER URL is correct in config_data.json.

3. Bus stops missing

   - Re-run apply_config.py to refresh OSM/timetable data.

4. Configuration changes not applied

   - Confirm /admin/configure.html saved correctly.
   - Ensure JSON valid (no trailing commas, correct brackets).

5. Permissions errors

   - Ensure read/write permissions for data/, mapper/config_data.json.

---

## Index


**Web pages**

```
/                             ==>       Map interface
/admin/configure.html         ==>       Configuration UI
```

**API**

```
/api/busstops/             
/api/busroutes/
/api/trips/
/api/config/                   ==>      GET/POST configuration
```

**Python scripts**

```
apply_config.py                ==>      Applies config options to project (read/write)
config_options.py              ==>      Default project settings
```

**Data**

```
mapper/config_data.json        ==>      JSON storage for configuration UI
data/raw/                      ==>      Original imported OSM and timetable files
data/processed/                ==>      Processed GeoJSON and timetable data
data/imports.log               ==>      Logs of import operations
```

**Docs**

```
docs/PresentationSlides.pptx   ==>      Stakeholder presentation
```

**Configuration**

```
config_options.py              ==>      Default Python configuration (editable)
apply_config.py                ==>      Script to apply configuration
/admin/configure.html          ==>      Web interface for updating mapper/config_data.json
                                        (independent of Python config)
```

**Project structure**

```
config/                        ==>      Django settings, URLs, WSGI/ASGI
mapper/                        ==>      Main Django app (models, views, templates, static files)
requirements.txt               ==>      Dependencies
.env.example                   ==>      Example environment variables
.gitignore                     ==>      Ignored files
manage.py                      ==>      Django management script
```
---   
