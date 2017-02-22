from django.db import models

# Create your models here.
class Simulation(models.Model):
    
    CHOICES = (
        ("a", "a"),
        ("a", "b"),
        ("a", "c"),
    )
    
    mesh = models.FileField(verbose_name="mesh", upload_to="meshes")
    
    equationTypes = (
        ("displacement", "Displacement"),
        ("heat", "Heat"),
        ("flow", "Flow")
    )
    equationType = models.CharField(verbose_name="equationType",
                                    choices=equationTypes,
                                    max_length=100)
    
    analysisTypes = (
        ("static", "Static"),
        ("staticNonlinear", "Static non-linear"),
        ("transient", "Transient")
    )
    analysisType = models.CharField(verbose_name="analysisType",
                                    choices=analysisTypes,
                                    max_length=100)
    
    # all kind of analysis settings below:
    # would be nice if this could be generated based on Hybrida itself?!
    analysisTolerance = models.CharField(verbose_name="analysisTolerance",
                                         max_length=20)
    
    analysisMaxIter = models.CharField(verbose_name="analysisMaxIter",
                                         max_length=20)
    
    analysisReactions = models.CharField(verbose_name="analysisReactions",
                                         max_length=20)

    analysisTMax = models.CharField(verbose_name="analysisTMax",
                                         max_length=20)
    
    analysisDT = models.CharField(verbose_name="analysisDT",
                                  max_length=20)
    
    analysisAlpha = models.CharField(verbose_name="analysisAlpha",
                                     max_length=20)
    
    # boolean flags to set parts of the simulation
    timeFlag = models.BooleanField()
    optimizationFlag = models.BooleanField()
    printToScreen = models.BooleanField()
    printToParaview = models.BooleanField()

    def __str__(self):
        return str(self.id)


class BoundaryConditions(models.Model):

    physicalGroup = models.CharField(verbose_name="physicalgroup",
                                     max_length=100)
    
    bcType = models.CharField(verbose_name="bcType",
                              max_length=100)

    simulation = models.ForeignKey(Simulation, verbose_name="relatedSimulation")
    
class OptimizationModel(models.Model):
    
    choices_objective = (
            ("compliance", "Compliance"),
            ("compliance", "Compliance")
        )

    objectiveFunction = models.CharField(verbose_name="objectiveFunction",
                                         choices=choices_objective,
                                         max_length=100)
    
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
