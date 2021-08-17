from django import forms
from .models import officeDetail
'''
from .models import ModelName
class ModelNameForm(forms.ModelForm):
    class Meta:
        model = ModelName
        fields = '__all__'
'''
class officeDetailForm(forms.ModelForm):
    class Meta:
        model = officeDetail
        fields = '__all__'