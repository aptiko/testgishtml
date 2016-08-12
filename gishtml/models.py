from django.contrib.gis.db import models


class Polygon(models.Model):
    mpoly = models.MultiPolygonField()
