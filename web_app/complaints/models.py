from django.db import models



class Report(models.Model):
    
    image_path = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    GRAFFITI = models.IntegerField()
    FADED_SIGNAGE = models.IntegerField()
    POTHOLES = models.IntegerField()
    GARBAGE = models.IntegerField()
    CONSTRUCTION_ROAD = models.IntegerField()
    BROKEN_SIGNAGE = models.IntegerField()
    BAD_STREETLIGHT = models.IntegerField()
    BAD_BILLBOARD = models.IntegerField()
    SAND_ON_ROAD = models.IntegerField()
    CLUTTER_SIDEWALK = models.IntegerField()
    UNKEPT_FACADE = models.IntegerField()
    resolved = models.CharField(max_length=100, null=True)
    total_detections = models.IntegerField()
    issued = models.DateTimeField(auto_now_add=True),
    

    def __str__(self):
        return self.image_path



