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
│     ├── init.py
│     ├── settings.py
│     ├── urls.py
│     ├── wsgi.py
│     └── asgi.py
│
├── mapper/
│    ├── init.py
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

</details>
```

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


