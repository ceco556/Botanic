from django.db import models

# Create your models here.

class Plant(models.Model):
  name = models.CharField(max_length=50)
  plant_type = models.CharField(max_length=50)
  img = models.ImageField(null=True, blank=True, upload_to='images/')
  description = models.CharField(max_length=150, null=True, blank=True)

  def __str__(self) -> str:
    return self.name
  
  def print_plant_type(self):
    return self.plant_type

