from django.contrib import admin
from polls.models import Simulation, BoundaryConditions, Materials

# Register your models here.
admin.site.register(Simulation)
admin.site.register(BoundaryConditions)
admin.site.register(Materials)
