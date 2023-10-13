from django.db import models

# Create your models here.
class Objectives(models.Model):
    name = models.CharField(max_length=90, default='')
    description = models.CharField(max_length=400, default='')
    description_ar = models.CharField(max_length=400, default='')
    def __str__(self):
        return self.name
    
class Requirements(models.Model):
    name = models.CharField(max_length=90, default='')
    description = models.CharField(max_length=400, default='')
    description_ar = models.CharField(max_length=400, default='')
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200, default='')
    name_ar = models.CharField(max_length=200, default='')
    price = models.CharField(max_length=200, default='')
    price_ar = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    description_ar = models.TextField(default='')
    type = models.CharField(max_length=60, default='')
    type_ar = models.CharField(max_length=60, default='')
    duration = models.CharField(default='', max_length=50)
    duration_ar = models.CharField(default='', max_length=50)
    age = models.IntegerField(default=0)
    level = models.CharField(max_length=50, default='')
    level_ar = models.CharField(max_length=50, default='')
    period = models.CharField(max_length=200, default='')
    period_ar = models.CharField(max_length=200, default='')
    tutor = models.CharField(max_length=50, default='')
    tutor_ar = models.CharField(max_length=50, default='')
    objectives = models.ManyToManyField(Objectives, related_name='course')
    requirements = models.ManyToManyField(Requirements, related_name='Requirements')
    image = models.ImageField(upload_to='uploaded-images/gallery')
    after = models.TextField(default='')
    after_ar = models.TextField(default='')
    def __str__(self):
        return self.name
    
class Home(models.Model):
    frist = models.TextField(blank=True)
    frist_ar = models.TextField(blank=True)
    second = models.TextField(blank=True)
    second_ar = models.TextField(blank=True)