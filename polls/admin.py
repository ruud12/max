from django.contrib import admin
from polls.models import Simulation, boundaryConditions

# Register your models here.
admin.site.register(Simulation)
admin.site.register(boundaryConditions)
