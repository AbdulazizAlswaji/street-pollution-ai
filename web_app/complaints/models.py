from django.db import models



class Report(models.Model):
    
    image_path = models.CharField(max_length=100, null=True)
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
    issued = models.DateTimeField(auto_now_add=True),

    def __str__(self):
        return self.image_path



