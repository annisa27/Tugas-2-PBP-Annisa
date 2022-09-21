from django.db import models

# Create your models here.
class BarangMyWatchlist(models.Model):
    watched = models.TextField()
    title = models.CharField(max_length=200)
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()
