from django.db import models


class WalkingCountSurvey(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    total_count = models.IntegerField()
    time_0600 = models.IntegerField()
    time_0700 = models.IntegerField()

    # Add more fields for other time intervals

    def __str__(self):
        return f"{self.location} - {self.date}"


class BicycleCountSurvey(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    total_count = models.IntegerField()

    def __str__(self):
        return f"{self.location} - {self.date}"


class CarShareUsage(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    hours_booked = models.IntegerField()
    trip_distance = models.FloatField()  # Total distance of trips from that location

    def __str__(self):
        return f"{self.location} - {self.date}"
