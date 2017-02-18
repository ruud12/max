from django import forms
from polls.models import Simulation, boundaryConditions

class MyForm(forms.ModelForm):

    class Meta:
        model = Simulation
        fields = "__all__"
        
class boundaryConditionsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop("choices")
        super(boundaryConditionsForm, self).__init__(*args, **kwargs)
        self.fields["physicalGroup"] = forms.ChoiceField(choices=choices)

    class Meta:
        model = boundaryConditions
        fields = "__all__"
        
class baseformset(forms.BaseModelFormSet):
    pass
