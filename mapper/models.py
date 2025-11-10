# Models

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
