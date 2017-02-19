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
                                    
    timeFlag = models.BooleanField()

    def __str__(self):
        return str(self.id)


class BoundaryConditions(models.Model):

    physicalGroup = models.CharField(verbose_name="physicalgroup",
                                     max_length=100)
    
    bcType = models.CharField(verbose_name="bcType",
                              max_length=100)

    simulation = models.ForeignKey(Simulation, verbose_name="relatedSimulation")
    
class Materials(models.Model):
    
    CHOICES = (
        ("Elastic", "Elastic"),
        ("Heat", "Heat"),
        ("Fluid", "Fluid"),
    )

    materialChoice = models.CharField(verbose_name="materialtypes",
                                      choices=CHOICES,
                                      max_length=100)
                                      
    conductivity = models.CharField(verbose_name="conductivity",
                                 max_length=20,
                                 null=True,
                                 blank=True
                                 )
                                 
    heatCapacity = models.CharField(verbose_name="heatCapacity",
                                 max_length=20,
                                 null=True,
                                 blank=True)

    poissonRatio = models.CharField(verbose_name="poissonRatio",
                                 max_length=20,
                                 null=True,
                                 blank=True)
    
    youngsModulus = models.CharField(verbose_name="youngsModulus",
                                 max_length=20,
                                 null=True,
                                 blank=True)
                                 
    density = models.CharField(verbose_name="density",
                                 max_length=20,
                                 null=True,
                                 blank=True)
                                 
    viscosity = models.CharField(verbose_name="Viscosity",
                                 max_length=20,
                                 null=True,
                                 blank=True)
