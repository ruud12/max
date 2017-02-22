from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from polls import forms
from django.shortcuts import redirect
from django.forms import modelformset_factory
from polls.models import BoundaryConditions

#from hybrida.fem import Mesh, Step, Equation, Simulation, DisplacementType
#from hybrida.fem import Static, Thermomechanical, TransientThermal
#from hybrida.fem.materials import Heat, Elastic
#from hybrida.fem.conditions import Dirichlet, Neumann, NeumannDistributed
#from hybrida.fem.io import Output

import sys
import os
#import numpy as np


# Create your views here.

def index(request):

    # get list of physical groups and add to choices
#    mesh = Mesh("/Users/maxvanderkolk/Documents/PhD_local/ATCC Meetings/2017_01_30_5th_session/Hybrida_demo/input/mesh.msh")
    
#    choices = []
    
#    for key in mesh.pgroups.keys():
#        choices += [key]
    
#    choices = sorted(choices, key=str.lower)
#    choices = tuple(zip(choices, choices))
    choices_pgroups = (
            ('1', 'Edge 1'),
            ('2', 'Edge 2'),
            ('3', 'Surface'),
            ('4', 'Volume'),
    )
    
    choices_bctypes = (
            ("1", "Dirichlet"),
            ("2", "Neumann"),
            ("3", "Neumann distributed"),
    )

    boundaryConditionsFormSet = modelformset_factory(BoundaryConditions, form=forms.BoundaryConditionsForm, formset=forms.baseformset, extra=1)

    # doe iets met dit form
    if request.method == "POST":
        # form to select the mesh
        form = forms.MyForm(request.POST)
        
        # form set to add/remove and select multiple boundary conditions
        formset = BoundaryConditionsFormSet(request.POST, prefix="fs1", form_kwargs={"choices_pgroups":choices_pgroups, "choices_bctypes":choices_bctypes})
        
        # form to select a material
        materialsForm = forms.materialsForm(request.POST)
        optimizationForm = forms.OptimizationForm(request.POST)
        
        if form.is_valid() and formset.is_valid() and materialsForm.is_valid():

            simulation = form.save()
            pgroup = form.cleaned_data.get('My_field')
            
            for subform in formset:
                instance = subform.save(commit=False)
                instance.simulation = simulation
                instance.save()
            
    else:
        form = forms.MyForm()
        materialsForm = forms.materialsForm()
        formset = boundaryConditionsFormSet(prefix="fs1", form_kwargs={"choices_pgroups":choices_pgroups, "choices_bctypes":choices_bctypes})
        optimizationForm = forms.OptimizationForm()
        
    return render(request, 'polls/name.html', {"form": form,
                                               "formset": formset,
                                               "materialsForm": materialsForm,
                                               "optimizationForm": optimizationForm})
    
# def boundaryConditions(request, form):
#
#     # maak nog een form voor Dirichlet/Neumann
#     choices = (
#         ("Dirichlet", "Dirichlet"),
#         ("Neumann", "Neumann"),
#     )
#
#     return render(request, 'polls/boundaryConditions.html', {'form': form})

#
#def result(request, pgroup):
#    # analysis = [x[1] for x in forms.MyForm.fields.analyis.choices if x[0] == analysis]
#
#    mesh = Mesh("/Users/maxvanderkolk/Documents/PhD_local/ATCC Meetings/2017_01_30_5th_session/Hybrida_demo/input/mesh.msh")
#
#
#    # set material properties
#    heat = Heat(conductivity=1.,
#                specific_heat=1.,
#                density=1.)
#
#    # boundary conditions
#    dir_T1 = Neumann(pgroup, lambda x: (1., ))
#    dir_T2 = Dirichlet("bottom", lambda x: (0., ))
#
#    # define analysis step
#    step_T = Step(mesh=mesh,
#                  bcs=(dir_T1, dir_T2),
#                  analysis=Static(),
#                  equation=Equation.heat,
#                  materials=heat)
#
#    step_T.out = [Output("mesh", "all", '/Users/maxvanderkolk/Desktop/tets.vtu')]
#
#    # setup the simulation
#    sim = Simulation(steps=[step_T])
#
#    # solve simulation
#    sim.solve()
#
#    x = ", ".join([str(node[0]) for node in mesh.nodes])
#    y = ", ".join([str(node[1]) for node in mesh.nodes])
#    return render(request, 'polls/result.html', {'pgroup': pgroup, 'mesh': mesh, "x":x, "y":y})
