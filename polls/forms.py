from django import forms
from polls.models import Simulation, boundaryConditions

class MyForm(forms.ModelForm):

    class Meta:
        model = Simulation
        fields = "__all__"
        
class boundaryConditionsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        choices_pgroups = kwargs.pop("choices_pgroups")
        choices_bctypes = kwargs.pop("choices_bctypes")
        super(boundaryConditionsForm, self).__init__(*args, **kwargs)
        self.fields["physicalGroup"] = forms.ChoiceField(choices=choices_pgroups)
        self.fields["boundaryType"] = forms.ChoiceField(choices=choices_bctypes)

    class Meta:
        model = boundaryConditions
        fields = "__all__"
        
class baseformset(forms.BaseModelFormSet):
    pass
