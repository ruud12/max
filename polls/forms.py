from django import forms
from polls.models import Simulation, BoundaryConditions, Materials, OptimizationModel

class MyForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(MyForm, self).__init__(*args, **kwargs)

        self.fields["timeFlag"] = forms.BooleanField()
        self.fields['timeFlag'].label = "Time dependent analysis"
        
        self.fields["optimizationFlag"] = forms.BooleanField()
        self.fields["optimizationFlag"].label = ""
        
        self.fields["printToScreen"] = forms.BooleanField()
        self.fields['printToScreen'].label = "Print to screen"
        
        self.fields["printToParaview"] = forms.BooleanField()
        self.fields['printToParaview'].label = "Print to Paraview"
        
        self.fields['analysisTolerance'] = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "Tolerance - this should show the default setting from hybrida"}))
        self.fields['analysisMaxIter'] = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "Max iterations - this should show the default setting from hybrida"}))
        self.fields['analysisReactions'] = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "Reactions - this should show the default setting from hybrida"}))
        self.fields['analysisTMax'] = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "End time (tmax) - this should show the default setting from hybrida"}))
        self.fields['analysisDT'] = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "Time step (dt) - this should show the default setting from hybrida"}))
        self.fields['analysisAlpha'] = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "Algorithm type (alpha) - this should show the default setting from hybrida"}))
        
    class Meta:
        model = Simulation
        fields = "__all__"
        
class BoundaryConditionsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        choices_pgroups = kwargs.pop("choices_pgroups")
        choices_bctypes = kwargs.pop("choices_bctypes")
        super(BoundaryConditionsForm, self).__init__(*args, **kwargs)
        self.fields["physicalGroup"] = forms.ChoiceField(choices=choices_pgroups)
        self.fields["boundaryType"] = forms.ChoiceField(choices=choices_bctypes)
        self.fields["xcoord"] = forms.CharField(max_length=10,
                                                widget=forms.TextInput(attrs={'placeholder': 'x'}))
        self.fields["ycoord"] = forms.CharField(max_length=10,
                                                widget=forms.TextInput(attrs={'placeholder': 'y'}))
        self.fields["zcoord"] = forms.CharField(max_length=10,
                                                widget=forms.TextInput(attrs={'placeholder': 'z'}))
        self.fields["time"] = forms.CharField(max_length=10,
                                              widget=forms.TextInput(attrs={'placeholder': 'Time'}))

    class Meta:
        model = BoundaryConditions
        fields = "__all__"
        
class OptimizationForm(forms.ModelForm):
    

    class Meta:
        model = OptimizationModel
        fields = "__all__"

class materialsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(materialsForm, self).__init__(*args, **kwargs)

        self.fields["youngsModulus"] = forms.CharField(max_length=20,
                                                widget=forms.TextInput(attrs={'placeholder': "Young's modulus"}))
        
        self.fields["density"] = forms.CharField(max_length=20,
                                                widget=forms.TextInput(attrs={'placeholder': "Density"}))

        self.fields["poissonRatio"] = forms.CharField(max_length=20,
                                                widget=forms.TextInput(attrs={'placeholder': "Poissons Ratio"}))
        
        self.fields["conductivity"] = forms.CharField(max_length=20,
                                                widget=forms.TextInput(attrs={'placeholder': "Conductivity"}))
        
        self.fields["heatCapacity"] = forms.CharField(max_length=20,
                                                widget=forms.TextInput(attrs={'placeholder': "Heat capacity"}))
                                                
        self.fields["viscosity"] = forms.CharField(max_length=20,
                                                widget=forms.TextInput(attrs={'placeholder': "Viscosity"}))

    class Meta:
        model = Materials
        fields = "__all__"
        
class baseformset(forms.BaseModelFormSet):
    pass
