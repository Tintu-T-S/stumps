from django.db import models

# Create your models here.
class imigration(models.Model):
    title = models.CharField(max_length=500)
    details = models.TextField()
    image = models.ImageField(upload_to='pics')

class team_staff(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=300)
    img = models.ImageField(upload_to='pics')

