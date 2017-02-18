from django.db import models

# Create your models here.
class Simulation(models.Model):
    
    CHOICES = (
        ("a", "a"),
        ("a", "b"),
        ("a", "c"),
    )
    
    mesh = models.FileField(verbose_name="mesh", upload_to="meshes")
    analysisType = models.CharField(verbose_name="analysisType",
                                    choices=CHOICES,
                                    max_length=100)

    def __str__(self):
        return str(self.id)


class boundaryConditions(models.Model):

    physicalGroup = models.CharField(verbose_name="physicalgroup",
                                     max_length=100)
    
    bcType = models.CharField(verbose_name="bcType",
                              max_length=100)

    simulation = models.ForeignKey(Simulation, verbose_name="relatedSimulation")
