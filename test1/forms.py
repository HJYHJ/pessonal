from django import forms
from .models import otBoys,otBoysInfo

class otBoysForm(forms.ModelForm):
    class Meta:
        model = otBoys
        fields = ['name']
class otBoysInfoForm(forms.ModelForm):
    class Meta:
        model = otBoysInfo
        fields = '__all__'