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
