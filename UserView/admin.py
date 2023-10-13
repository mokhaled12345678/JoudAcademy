from django.contrib import admin
from .models import Course, Objectives, Requirements, Home
# Register your models here.

admin.site.register(Course)
admin.site.register(Objectives)
admin.site.register(Requirements)
admin.site.register(Home)